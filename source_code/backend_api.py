"""
BACKEND API - FRAMEWORK DSB
==========================
API Backend simplificada com funções Flask para comunicação frontend ↔ backend
Versão refatorada: Classes → Funções simples para melhor performance e manutenibilidade
"""

# =============================================================================
# IMPORTS E DEPENDÊNCIAS
# =============================================================================

from flask import Flask, request, jsonify
import logging
import sys
import os
from datetime import datetime
import data_manager
from data_manager import consultar_bd, get_view, inserir_dados, atualizar_dados, excluir_dados

# Importa debugger personalizado
from debugger import flow_marker, error_catcher, unexpected_error_catcher, _inicializar_log

# =============================================================================
# FUNÇÃO PARA CONFIGURAR ENDPOINTS EM QUALQUER INSTÂNCIA FLASK
# =============================================================================

def configurar_endpoints(app):
    """
    Configura todos os endpoints da API em uma instância Flask fornecida
    
    @param {Flask} app - Instância Flask onde os endpoints serão registrados
    """
    
    # Configuração de logging
    logger = logging.getLogger(__name__)
    
    @app.route('/health', methods=['GET'])
    def health_check():
        """
        Endpoint de health check - verifica se API está funcionando
        
        @return {dict} - Status da API e informações básicas
        """
        return jsonify({
            "status": "ok", 
            "app": "Framework DSB API",
            "message": "API Backend funcionando",
            "timestamp": datetime.now().isoformat()
        })

    @app.route('/processar_extratos_pdf', methods=['POST'])
    def processar_extratos_pdf():
        """
        Endpoint para processar extratos PDF e extrair despesas
        
        Executa o processo completo:
        1. Validação de arquivos e banco de dados
        2. Extração de dados dos PDFs
        3. Classificação das despesas
        4. Salvamento no banco de dados
        
        @return {dict} - Resultado do processamento com status e mensagem
        """
        flow_marker("INÍCIO endpoint /processar_extratos_pdf")
        _inicializar_log()  # Limpa o log anterior
        
        try:
            # Adiciona o caminho do extratorDePDF ao sys.path para imports
            extrator_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'extratorDePDF')
            flow_marker(f"Caminho calculado: {extrator_path}")
            flow_marker(f"Arquivo existe? {os.path.exists(os.path.join(extrator_path, 'orquestrador_validacao.py'))}")
            
            if extrator_path not in sys.path:
                sys.path.append(extrator_path)
            
            # Verifica se os módulos existem antes de importar
            orquestrador_validacao_path = os.path.join(extrator_path, 'orquestrador_validacao.py')
            orquestrador_extracao_path = os.path.join(extrator_path, 'orquestrador_extracao.py')
            
            if not os.path.exists(orquestrador_validacao_path):
                flow_marker(f"Arquivo não encontrado: {orquestrador_validacao_path}")
                return jsonify({
                    "sucesso": False,
                    "erro": f"Módulo orquestrador_validacao não encontrado em {orquestrador_validacao_path}",
                    "etapa": "validacao_modulo"
                }), 500
            
            if not os.path.exists(orquestrador_extracao_path):
                flow_marker(f"Arquivo não encontrado: {orquestrador_extracao_path}")
                return jsonify({
                    "sucesso": False,
                    "erro": f"Módulo orquestrador_extracao não encontrado em {orquestrador_extracao_path}",
                    "etapa": "validacao_modulo"
                }), 500
            
            # Imports do sistema de extração
            from orquestrador_validacao import executar_validacao_completa
            from orquestrador_extracao import processar_e_salvar_extratos
            
            flow_marker("Iniciando validação completa dos arquivos PDF")
            
            # FASE 1: Validação completa
            sucesso_validacao, dados_validados = executar_validacao_completa()
            
            if not sucesso_validacao:
                flow_marker(f"Validação falhou: {dados_validados}")
                return jsonify({
                    "sucesso": False,
                    "erro": dados_validados,
                    "etapa": "validacao"
                }), 400
            
            flow_marker(f"Validação bem-sucedida. Dados validados: {dados_validados}")
            
            # FASE 2: Processamento e salvamento
            flow_marker("Iniciando extração e salvamento dos extratos")
            sucesso_extracao, mensagem_extracao = processar_e_salvar_extratos(dados_validados)
            
            if sucesso_extracao:
                flow_marker(f"Processo concluído com sucesso: {mensagem_extracao}")
                return jsonify({
                    "sucesso": True,
                    "mensagem": mensagem_extracao,
                    "dados_processados": dados_validados
                })
            else:
                flow_marker(f"Erro na extração: {mensagem_extracao}")
                return jsonify({
                    "sucesso": False,
                    "erro": mensagem_extracao,
                    "etapa": "extracao"
                }), 500
                
        except ImportError as e:
            error_msg = f"Erro ao importar módulos de extração: {str(e)}"
            error_catcher(error_msg, e)
            return jsonify({
                "sucesso": False,
                "erro": error_msg,
                "etapa": "import"
            }), 500
            
        except Exception as e:
            error_msg = f"Erro inesperado durante processamento: {str(e)}"
            flow_marker(error_msg)
            return jsonify({
                "sucesso": False,
                "erro": error_msg,
                "etapa": "processamento"
            }), 500

    @app.route('/consultar_dados_db', methods=['POST'])
    def consultar_dados_db():
        """
        Endpoint para consultar dados de views prontas para popular formulários
        
        REGRA IMPORTANTE: Este endpoint deve ser usado APENAS com views prontas
        que foram criadas especificamente para uso em determinados formulários.
        
        NÃO usar consultas diretas em tabelas - sempre usar views dedicadas.
        
        @param {string} view - Nome da view pronta (ex: vw_grupos, vw_lancamentos)
        @param {string} database_path - Caminho do banco de dados
        @param {string} database_name - Nome do arquivo do banco
        @param {string} database_host - Host do banco (se remoto)
        @return {dict} - Dicionário de dados para popular formulário
        """
        flow_marker("INÍCIO endpoint /consultar_dados_db")
        
        try:
            # Validação de request usando função auxiliar
            dados_request, erro = _validar_request_json()
            if erro:
                return erro
            
            flow_marker("Dados recebidos no endpoint", dados_request)
            
            # Valida se view foi fornecida
            nome_view = dados_request.get('view', '')
            if not nome_view:
                return jsonify({
                    "dados": [],
                    "mensagem": "Nome da view não fornecido"
                }), 400
            
            # Valida campos solicitados
            campos_solicitados = dados_request.get('campos', ['Todos'])
            if not campos_solicitados or campos_solicitados == []:
                return jsonify({
                    "dados": [],
                    "mensagem": "Nenhum campo informado"
                }), 400
            
            flow_marker(f"Consultando view: {nome_view} com campos: {campos_solicitados}")
            
            # Processa configurações
            path_name = _processar_db_path_name(dados_request)
            
            # Extrai filtros da requisição
            filtros = dados_request.get('filtros', '')
            
            # Executa consulta na view usando função direta
            resultado = consultar_bd(nome_view, campos_solicitados, database_path=path_name.get('database_path'), database_name=path_name.get('database_name'), filtros=filtros)
            
            # Prepara resposta padronizada
            resposta = {
                "dados": resultado if resultado else [],
                "mensagem": "sucesso"
            }
            
            flow_marker(f"Consulta executada - View: {nome_view}, Registros: {len(resultado) if resultado else 0}")
            
            # Rastreamento do envio da resposta
            flow_marker(f"✅ ENVIANDO RESPOSTA AO FRONTEND: {len(resultado) if resultado else 0} registros")
            flow_marker(f"📤 ESTRUTURA DA RESPOSTA: {resposta}")
            
            return jsonify(resposta)
            
        except Exception as e:
            return _erro_padronizado("/consultar_dados_db", e)

    @app.route('/update_data_db', methods=['POST'])
    def update_data_db():
        """
        Endpoint para atualizar dados existentes
        
        @param {dict} dados_para_update - Dados para atualização contendo:
            - tabela: nome da tabela
            - campos: lista de campos  
            - dados_a_atualizar: dados atuais do registro
            - dados_form_out: novos dados para atualização
            - database_path: caminho do banco
            - database_name: nome do banco
        @return {dict} - Resultado da operação de atualização
        """
        flow_marker("INÍCIO endpoint /update_data_db")
        
        try:
            # Validação de request usando função auxiliar
            dados_request, erro = _validar_request_json()
            if erro:
                return erro
            
            flow_marker("Dados recebidos no endpoint", dados_request)
            
            # Valida se tabela_alvo foi fornecida
            tabela = dados_request.get('tabela_alvo', '')
            if not tabela:
                return jsonify({
                    "dados": [],
                    "mensagem": "Nome da tabela_alvo não fornecido"
                }), 400
            
            flow_marker(f"Atualizando tabela: {tabela}")
            
            # Processa configurações
            path_name = _processar_db_path_name(dados_request)
            
            # Extrai parâmetros adicionais do payload
            tabela_alvo = dados_request.get('tabela_alvo')
            campos_obrigatorios = dados_request.get('campos_obrigatorios')
            
            # Executa operação de update usando função direta
            dados_a_atualizar = dados_request.get('dados', {})
            resultado = atualizar_dados(tabela, dados_a_atualizar, path_name.get('database_path'), path_name.get('database_name'), tabela_alvo, campos_obrigatorios)
            
            flow_marker(f"Update executado - Tabela: {tabela}")
            flow_marker("🔍 RESULTADO da função atualizar_dados", resultado)
            
            # ===============================================================
            # ESTRATÉGIA DE SINCRONIZAÇÃO INTELIGENTE (UPDATE):
            # Após atualização bem-sucedida, consultamos novamente a view para
            # retornar o array completo atualizado e ordenado.
            # Isso evita "tremor" na interface e mantém navegação fluida,
            # especialmente quando campos ordenados são alterados.
            # ===============================================================
            
            if resultado.get('sucesso'):
                flow_marker('🔄 Consultando dados atualizados após update')
                
                # Consulta dados atualizados com parâmetros corretos
                consulta_atualizada = consultar_bd(f"{tabela_alvo}_view", ['Todos'], database_path=path_name.get('database_path'), database_name=path_name.get('database_name'))
                
                flow_marker('📊 Dados atualizados consultados', {
                    'view': f"{tabela_alvo}_view",
                    'total_registros': len(consulta_atualizada.get('dados', [])) if consulta_atualizada and consulta_atualizada.get('dados') else 0
                })
                
                # Resposta enriquecida com dados atualizados
                resultado_final = {
                    "sucesso": True,
                    "mensagem": resultado.get('mensagem', 'Registro atualizado com sucesso'),
                    "dados_atualizados": consulta_atualizada.get('dados', []) if consulta_atualizada else [],
                    "total_registros": len(consulta_atualizada.get('dados', [])) if consulta_atualizada and consulta_atualizada.get('dados') else 0
                }
                
                flow_marker('✅ Resposta completa com dados atualizados (UPDATE)', {
                    'total_registros': resultado_final['total_registros']
                })
                
                return jsonify(resultado_final)
            
            return jsonify(resultado)
            
        except Exception as e:
            return _erro_padronizado("/update_data_db", e)

    @app.route('/incluir_reg_novo_db', methods=['POST'])
    def incluir_reg_novo_db():
        """
        Endpoint para incluir novos registros
        
        @param {dict} dados_novo_registro - Dados do novo registro
        @return {dict} - Resultado da operação de inclusão
        """
        try:
            flow_marker('🔄 INÍCIO endpoint /incluir_reg_novo_db')
            
            dados_request = request.get_json()
            flow_marker('📋 Dados recebidos no endpoint', dados_request)
            
            # Extrai parâmetros da requisição
            tabela_alvo = dados_request.get('tabela_alvo')
            dados_form_in = dados_request.get('dados', {})
            database_path = dados_request.get('database_path')
            database_name = dados_request.get('database_name')
            campos_obrigatorios = dados_request.get('campos_obrigatorios', [])
            
            # Constrói caminho completo do banco
            database_file = os.path.join(database_path, database_name)
            
            flow_marker('🔧 Parâmetros extraídos', {
                'tabela_alvo': tabela_alvo,
                'database_file': database_file,
                'campos_para_inserir': list(dados_form_in.keys())
            })
            
            # Chama data_manager para inserir dados
            resultado = data_manager.inserir_dados(
                tabela=tabela_alvo,
                dados_form_in=dados_form_in,
                database_path=database_path,
                database_name=database_name,
                tabela_alvo=tabela_alvo,
                campos_obrigatorios=campos_obrigatorios
            )
            
            flow_marker('📤 Resultado da inserção', resultado)
            
            if resultado.get('sucesso'):
                # ===============================================================
                # ESTRATÉGIA DE SINCRONIZAÇÃO INTELIGENTE:
                # Após inserção bem-sucedida, consultamos novamente a view para
                # retornar o array completo atualizado e ordenado.
                # Isso evita "tremor" na interface e mantém navegação fluida,
                # pois o frontend substitui dadosDisponiveis e recalcula reg_num
                # automaticamente através de find() da nova PK.
                # ===============================================================
                
                flow_marker('🔄 Consultando dados atualizados após inserção')
                
                # Consulta dados atualizados com parâmetros corretos
                consulta_atualizada = consultar_bd(f"{tabela_alvo}_view", ['Todos'], database_path=database_path, database_name=database_name)
            
                flow_marker('📊 Dados atualizados consultados', {
                    'view': f"{tabela_alvo}_view",
                    'total_registros': len(consulta_atualizada.get('dados', [])) if consulta_atualizada and consulta_atualizada.get('dados') else 0
                })
                
                resposta = {
                    "sucesso": True,
                    "mensagem": resultado.get('mensagem', 'Registro inserido com sucesso'),
                    "dados_atualizados": consulta_atualizada.get('dados', []) if consulta_atualizada else [],
                    "total_registros": len(consulta_atualizada.get('dados', [])) if consulta_atualizada and consulta_atualizada.get('dados') else 0
                }
                flow_marker('✅ Resposta completa com dados atualizados', {
                    'total_registros': resposta['total_registros']
                })
                return jsonify(resposta)
            else:
                resposta = {
                    "sucesso": False,
                    "mensagem": resultado.get('mensagem', 'Erro na inserção')
                }
                flow_marker('❌ Resposta de erro', resposta)
                return jsonify(resposta), 400
            
        except Exception as e:
            logger.error(f"Erro em incluir_reg_novo_db: {e}")
            flow_marker('💥 Erro crítico no endpoint', str(e))
            return jsonify({"sucesso": False, "mensagem": f"Erro: {str(e)}"}), 500

    @app.route('/delete_reg', methods=['POST'])
    def delete_reg():
        """
        Endpoint para excluir registros existentes
        
        @param {dict} dados_para_delete - Dados para exclusão contendo:
            - tabela_alvo: nome da tabela
            - pk_para_excluir: chave primária do registro a excluir
            - database_path: caminho do banco
            - database_name: nome do banco
        @return {dict} - Resultado da operação de exclusão com dados atualizados
        """
        flow_marker('🔄 INÍCIO endpoint /delete_reg')
        
        try:
            # Validação de request usando função auxiliar
            dados_request, erro = _validar_request_json()
            if erro:
                return erro
            
            flow_marker('📋 Dados recebidos no endpoint', dados_request)
            
            # Valida se tabela_alvo foi fornecida
            tabela_alvo = dados_request.get('tabela_alvo', '')
            if not tabela_alvo:
                return jsonify({
                    "sucesso": False,
                    "mensagem": "Nome da tabela_alvo não fornecido"
                }), 400
            
            # Valida se pk_para_excluir foi fornecida
            pk_para_excluir = dados_request.get('pk_para_excluir')
            if not pk_para_excluir:
                return jsonify({
                    "sucesso": False,
                    "mensagem": "Chave primária para exclusão não fornecida"
                }), 400
            
            flow_marker(f'🗑️ Excluindo registro da tabela: {tabela_alvo}, PK: {pk_para_excluir}')
            
            # Processa configurações
            database_path = dados_request.get('database_path', '')
            database_name = dados_request.get('database_name', '')
            
            # Monta caminho completo do banco
            database_file = os.path.join(database_path, database_name)
            flow_marker('🔧 Parâmetros extraídos', {
                'tabela_alvo': tabela_alvo,
                'database_file': database_file,
                'pk_para_excluir': pk_para_excluir
            })
            
            # Executa operação de exclusão usando função direta
            resultado = excluir_dados(tabela_alvo, pk_para_excluir, database_path, database_name)
            
            flow_marker('📤 Resultado da exclusão', resultado)
            
            # ===============================================================
            # ESTRATÉGIA DE SINCRONIZAÇÃO INTELIGENTE (DELETE):
            # Após exclusão bem-sucedida, consultamos novamente a view para
            # retornar o array completo atualizado e ordenado.
            # Isso evita "tremor" na interface e mantém navegação fluida,
            # reposicionando automaticamente após remoção do registro.
            # ===============================================================
            
            if resultado.get('sucesso'):
                flow_marker('🔄 Consultando dados atualizados após exclusão')
                
                # Consulta dados atualizados com parâmetros corretos
                consulta_atualizada = consultar_bd(f"{tabela_alvo}_view", ['Todos'], database_path=database_path, database_name=database_name)
                
                flow_marker('📊 Dados atualizados consultados', {
                    'view': f"{tabela_alvo}_view",
                    'total_registros': len(consulta_atualizada.get('dados', [])) if consulta_atualizada and consulta_atualizada.get('dados') else 0
                })
                
                resposta = {
                    "sucesso": True,
                    "mensagem": resultado.get('mensagem', 'Registro excluído com sucesso'),
                    "dados_atualizados": consulta_atualizada.get('dados', []) if consulta_atualizada else [],
                    "total_registros": len(consulta_atualizada.get('dados', [])) if consulta_atualizada and consulta_atualizada.get('dados') else 0
                }
                flow_marker('✅ Resposta completa com dados atualizados (DELETE)', {
                    'total_registros': resposta['total_registros']
                })
                return jsonify(resposta)
            else:
                resposta = {
                    "sucesso": False,
                    "mensagem": resultado.get('mensagem', 'Erro na exclusão')
                }
                flow_marker('❌ Resposta de erro', resposta)
                return jsonify(resposta), 400
            
        except Exception as e:
            logger.error(f"Erro em delete_reg: {e}")
            flow_marker('💥 Erro crítico no endpoint', str(e))
            return jsonify({"sucesso": False, "mensagem": f"Erro: {str(e)}"}), 500

    # =============================================================================
    # ENDPOINTS PARA SERVIR FRONTEND (DESENVOLVIMENTO LOCAL)
    # =============================================================================
    # NOTA: Remover/comentar estas rotas para deploy em nuvem

    @app.route('/')
    def serve_index():
        """
        Serve o index.html na raiz - APENAS DESENVOLVIMENTO LOCAL
        """
        from flask import send_from_directory
        return send_from_directory(app.static_folder, 'index.html')

    @app.route('/framework_dsb/<path:filename>')
    def serve_framework_files(filename):
        """
        Serve arquivos do framework DSB
        """
        from flask import send_from_directory
        return send_from_directory('C:\\Applications_DSB\\framework_dsb', filename)

    @app.route('/<path:path>')
    def serve_static_files(path):
        """
        Serve arquivos estáticos (JS, CSS, etc.) - APENAS DESENVOLVIMENTO LOCAL
        """
        from flask import send_from_directory
        return send_from_directory(app.static_folder, path)

# =============================================================================
#                           VALIDAÇÕES
# =============================================================================

def _validar_request_json():
    """
    Valida se o request contém JSON válido
    
    @return {tuple} - (dados_request, erro_response) 
    """
    dados_request = request.get_json()

    if not dados_request:
        flow_marker("ERRO: Dados não fornecidos")
        erro = jsonify({
            "dados": [],
            "mensagem": "Dados não fornecidos"
        }), 400
        return None, erro
    
    # Retorna dados válidos sem erro
    return dados_request, None

# =============================================================================
#                         FUNÇÕES AUXILIARES
# =============================================================================

def _processar_db_path_name(dados_request):
    """
    Organiza os dados de configuração do database em um dicionário
    @param {dict} dados_request - Dados da requisição
    @return {dict} - Configurações do database processadas
    """
    return {
        'database_path': dados_request.get('database_path', ''),
        'database_name': dados_request.get('database_name', ''),
        'database_host': dados_request.get('database_host', '')
    }

def _erro_padronizado(endpoint_nome, erro):
    """
    Gera resposta de erro padronizada
    
    @param {string} endpoint_nome - Nome do endpoint
    @param {Exception} erro - Objeto de erro
    @return {tuple} - Response JSON e código HTTP
    """
    error_catcher(f"Erro no endpoint {endpoint_nome}", erro)
    return jsonify({
        "dados": [],
        "mensagem": f"Erro interno: {str(erro)}"
    }), 500

