"""
BACKEND API - FRAMEWORK DSB
==========================
API Backend simplificada com funções Flask para comunicação frontend ↔ backend
Versão refatorada: Classes → Funções simples para melhor performance e manutenibilidade
"""

# =============================================================================
# IMPORTS E DEPENDÊNCIAS
# =============================================================================

from flask import Flask, request, jsonify, send_from_directory, send_from_directory, send_from_directory
import logging
import sys
import os
from datetime import datetime
import data_manager
from data_manager import consultar_bd, get_view, inserir_dados, atualizar_dados, atualizar_dados_lote, excluir_dados

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
    
    @app.route('/')
    def index():
        """
        Serve o arquivo index.html na rota raiz
        """
        return send_from_directory(app.static_folder, 'index.html')
    
    @app.route('/framework_dsb/<path:filename>')
    def serve_framework(filename):
        """
        Serve arquivos do framework DSB
        """
        # Caminho absoluto para a pasta framework_dsb
        framework_base = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        return send_from_directory(framework_base, filename)
    
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
        Delega toda validação para o orquestrador de validação
        
        Executa o processo completo:
        1. Validação de arquivos e banco de dados (orquestrador)
        2. Extração de dados dos PDFs
        3. Classificação das despesas
        4. Salvamento no banco de dados
        
        @return {dict} - Resultado do processamento com status e mensagem
        """
        flow_marker("INÍCIO endpoint /processar_extratos_pdf")
        _inicializar_log()  # Limpa o log anterior
        
        try:
            # Adicionar o path do extrator ao sys.path
            extrator_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'extratorDePDF')
            if extrator_path not in sys.path:
                sys.path.append(extrator_path)
            
            # Imports diretos com path absoluto
            try:
                import sys
                import importlib.util
                
                # Carregar orquestrador_validacao
                spec_validacao = importlib.util.spec_from_file_location(
                    "orquestrador_validacao", 
                    os.path.join(extrator_path, "orquestrador_validacao.py")
                )
                orquestrador_validacao = importlib.util.module_from_spec(spec_validacao)
                spec_validacao.loader.exec_module(orquestrador_validacao)
                
                # Carregar orquestrador_extracao  
                spec_extracao = importlib.util.spec_from_file_location(
                    "orquestrador_extracao",
                    os.path.join(extrator_path, "orquestrador_extracao.py")
                )
                orquestrador_extracao = importlib.util.module_from_spec(spec_extracao)
                spec_extracao.loader.exec_module(orquestrador_extracao)
                
                # Extrair as funções necessárias
                executar_validacao_completa = orquestrador_validacao.executar_validacao_completa
                processar_e_salvar_extratos = orquestrador_extracao.processar_e_salvar_extratos
                
            except (ImportError, AttributeError, FileNotFoundError) as e:
                flow_marker(f"Erro ao importar módulos do extrator: {str(e)}")
                return jsonify({
                    "sucesso": False,
                    "msg": f"Módulo extrator não encontrado: {str(e)}"
                }), 500
            
            # FASE 1: Validação completa (orquestrador faz todas as verificações)
            sucesso_validacao, dados_validados = executar_validacao_completa()
            
            if not sucesso_validacao:
                flow_marker(f"Validação falhou: {dados_validados}")
                return jsonify({
                    "sucesso": False,
                    "msg": f"Erro na validação: {dados_validados}. Verifique o arquivo log_de_erros.md para detalhes."
                }), 400
            
            flow_marker(f"Validação bem-sucedida. Dados validados: {dados_validados}")
            
            # FASE 2: Processamento e salvamento
            flow_marker("Iniciando extração e salvamento dos extratos")
            sucesso_extracao, mensagem_extracao = processar_e_salvar_extratos(dados_validados)
            
            if sucesso_extracao:
                flow_marker(f"Processo concluído com sucesso: {mensagem_extracao}")
                return jsonify({
                    "sucesso": True,
                    "msg": "Extratos processados com sucesso! Consulte os formulários para visualizar os dados."
                })
            else:
                flow_marker(f"Erro na extração: {mensagem_extracao}")
                return jsonify({
                    "sucesso": False,
                    "msg": f"Erro no processamento: {mensagem_extracao}. Verifique o arquivo log_de_erros.md para detalhes."
                }), 500
                
        except ImportError as e:
            error_msg = f"Erro ao importar módulos de extração: {str(e)}"
            error_catcher(error_msg, e)
            return jsonify({
                "sucesso": False,
                "msg": "Erro nos módulos de extração. Verifique o arquivo log_de_erros.md para detalhes."
            }), 500
            
        except Exception as e:
            error_msg = f"Erro inesperado durante processamento: {str(e)}"
            error_catcher(error_msg, e)
            return jsonify({
                "sucesso": False,
                "msg": "Erro inesperado no processamento. Verifique o arquivo log_de_erros.md para detalhes."
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
            filtros = dados_request.get('filtros', '')
            
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
                
                # Consulta dados atualizados aplicando filtros (se houver)
                consulta_atualizada = consultar_bd(
                    f"{tabela_alvo}_view", 
                    ['Todos'], 
                    database_path=path_name.get('database_path'), 
                    database_name=path_name.get('database_name'),
                    filtros=filtros if filtros else None
                )
                
                flow_marker('📊 Dados atualizados consultados', {
                    'view': f"{tabela_alvo}_view",
                    'filtros_aplicados': filtros if filtros else 'Nenhum',
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

    @app.route('/atualizar_lote', methods=['POST'])
    def atualizar_lote():
        """
        Endpoint para atualizar múltiplos registros em lote (operação em massa)
        FUNÇÃO GENÉRICA: Pode ser usada para qualquer tabela do sistema
        
        Performance: 1 requisição HTTP + loop interno de UPDATEs + 1 COMMIT
        Muito mais rápido que N requisições individuais
        
        @param {dict} payload - Dados da requisição contendo:
            - tabela_alvo (str): Nome da tabela para UPDATE (ex: 'despesas', 'produtos')
            - dados_lote (list[dict]): Array de objetos com dados para atualizar
                                       Ex: [{'iddespesa': 1234, 'idgrupo': 3, 'idsubgrupo': 5}, ...]
            - pk_field (str): Nome do campo chave primária (ex: 'iddespesa', 'idproduto')
            - campos_permitidos (list): Lista de campos permitidos para atualização (segurança)
                                       Ex: ['idgrupo', 'idsubgrupo']
            - database_path (str): Caminho do banco (opcional, usa config padrão)
            - database_name (str): Nome do banco (opcional, usa config padrão)
        
        @return {dict} - Resultado com estatísticas:
                        {
                            "sucesso": True/False,
                            "total_processados": 1000,
                            "atualizados": 950,
                            "erros": 50,
                            "erros_detalhes": [{...}]
                        }
        
        @example Requisição:
            POST /atualizar_lote
            {
                "tabela_alvo": "despesas",
                "dados_lote": [
                    {"iddespesa": 1234, "idgrupo": 3, "idsubgrupo": 5},
                    {"iddespesa": 1235, "idgrupo": 2, "idsubgrupo": 8}
                ],
                "pk_field": "iddespesa",
                "campos_permitidos": ["idgrupo", "idsubgrupo"],
                "database_path": "C:/Apps/data",
                "database_name": "financas.db"
            }
        """
        flow_marker("INÍCIO endpoint /atualizar_lote")
        
        try:
            # Validação de request usando função auxiliar
            dados_request, erro = _validar_request_json()
            if erro:
                return erro
            
            flow_marker("Dados recebidos no endpoint /atualizar_lote", {
                "tabela_alvo": dados_request.get('tabela_alvo'),
                "total_registros": len(dados_request.get('dados_lote', [])),
                "pk_field": dados_request.get('pk_field')
            })
            
            # =================================================================
            # VALIDAÇÃO DE PARÂMETROS OBRIGATÓRIOS
            # =================================================================
            
            tabela_alvo = dados_request.get('tabela_alvo')
            if not tabela_alvo:
                flow_marker("❌ Erro: tabela_alvo não fornecida")
                return jsonify({
                    "sucesso": False,
                    "erro": "Parâmetro 'tabela_alvo' não fornecido"
                }), 400
            
            dados_lote = dados_request.get('dados_lote')
            if not dados_lote or not isinstance(dados_lote, list) or len(dados_lote) == 0:
                flow_marker("❌ Erro: dados_lote inválido")
                return jsonify({
                    "sucesso": False,
                    "erro": "Parâmetro 'dados_lote' deve ser um array não vazio"
                }), 400
            
            pk_field = dados_request.get('pk_field')
            if not pk_field:
                flow_marker("❌ Erro: pk_field não fornecido")
                return jsonify({
                    "sucesso": False,
                    "erro": "Parâmetro 'pk_field' não fornecido"
                }), 400
            
            # Parâmetros opcionais
            campos_permitidos = dados_request.get('campos_permitidos')  # Pode ser None
            
            # Processa configurações de banco de dados
            path_name = _processar_db_path_name(dados_request)
            database_path = path_name.get('database_path')
            database_name = path_name.get('database_name')
            
            flow_marker(f"Parâmetros validados - Tabela: {tabela_alvo}, PK: {pk_field}, Registros: {len(dados_lote)}")
            
            # =================================================================
            # EXECUTA ATUALIZAÇÃO EM LOTE
            # =================================================================
            
            resultado = atualizar_dados_lote(
                tabela_alvo=tabela_alvo,
                dados_lote=dados_lote,
                pk_field=pk_field,
                database_path=database_path,
                database_name=database_name,
                campos_permitidos=campos_permitidos
            )
            
            flow_marker("Atualização em lote concluída", {
                "sucesso": resultado.get('sucesso'),
                "total_processados": resultado.get('total_processados', 0),
                "atualizados": resultado.get('atualizados', 0),
                "erros": resultado.get('erros', 0)
            })
            
            # =================================================================
            # RETORNA RESULTADO
            # =================================================================
            
            if resultado.get('sucesso'):
                flow_marker("✅ Atualização em lote bem-sucedida")
                return jsonify(resultado), 200
            else:
                flow_marker("❌ Atualização em lote com erro")
                return jsonify(resultado), 500
            
        except Exception as e:
            flow_marker(f"❌ EXCEÇÃO no endpoint /atualizar_lote: {str(e)}")
            return _erro_padronizado("/atualizar_lote", e)

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
            filtros = dados_request.get('filtros', '')
            
            # Constrói caminho completo do banco
            database_file = os.path.join(database_path, database_name)
            
            flow_marker('🔧 Parâmetros extraídos', {
                'tabela_alvo': tabela_alvo,
                'database_file': database_file,
                'campos_para_inserir': list(dados_form_in.keys()),
                'filtros': filtros
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
                
                # Consulta dados atualizados aplicando filtros (se houver)
                consulta_atualizada = consultar_bd(
                    f"{tabela_alvo}_view", 
                    ['Todos'], 
                    database_path=database_path, 
                    database_name=database_name,
                    filtros=filtros if filtros else None
                )
            
                flow_marker('📊 Dados atualizados consultados', {
                    'view': f"{tabela_alvo}_view",
                    'filtros_aplicados': filtros if filtros else 'Nenhum',
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

    @app.route('/executar_sql', methods=['POST'])
    def executar_sql_endpoint():
        """
        Endpoint para executar SQL direto no banco de dados
        
        Permite envio de consultas SQL personalizadas do frontend.
        Retorna dados estruturados para SELECT ou resultado de operação para DDL/DML.
        
        @param {dict} request_data - Dados da requisição
        @param {str} request_data.sql - Comando SQL a executar
        @param {str} request_data.database_path - Caminho do banco
        @param {str} request_data.database_name - Nome do banco
        
        @return {dict} - Resultado estruturado:
        Para SELECT: {"sucesso": True, "dados": [{"campo": "valor"}], "mensagem": "..."}
        Para DDL/DML: {"sucesso": True, "registros_afetados": N, "mensagem": "..."}
        Para erro: {"sucesso": False, "erro": "..."}
        """
        flow_marker("INÍCIO endpoint /executar_sql")
        
        try:
            # Validação do request JSON
            dados_request, erro_response = _validar_request_json()
            if erro_response:
                return erro_response
            
            # Validação de campos obrigatórios
            sql = dados_request.get('sql', '').strip()
            if not sql:
                flow_marker('❌ SQL não fornecido')
                return jsonify({
                    "sucesso": False,
                    "erro": "SQL não fornecido"
                }), 400
            
            # Extração de parâmetros obrigatórios
            database_path = dados_request.get('database_path')
            database_name = dados_request.get('database_name')
            
            if not database_path:
                flow_marker('❌ database_path não fornecido')
                return jsonify({
                    "sucesso": False,
                    "erro": "database_path é obrigatório"
                }), 400
            
            if not database_name:
                flow_marker('❌ database_name não fornecido')
                return jsonify({
                    "sucesso": False,
                    "erro": "database_name é obrigatório"
                }), 400
            
            flow_marker(f"📝 SQL recebido: {sql[:100]}...")
            flow_marker(f"💾 Database: {database_name} em {database_path}")
            
            # Importa e executa a função do data_manager
            from data_manager import executar_sql
            resultado = executar_sql(sql, database_path, database_name)
            
            # Loga o resultado para diagnóstico
            flow_marker(f"📊 RESULTADO da query SQL: {resultado}")
            
            # Retorna resultado estruturado
            if resultado.get('sucesso'):
                flow_marker('✅ SQL executado com sucesso')
                return jsonify(resultado)
            else:
                flow_marker(f'❌ Erro na execução SQL: {resultado.get("erro")}')
                return jsonify(resultado), 400
                
        except Exception as e:
            logger.error(f"Erro em executar_sql_endpoint: {e}")
            flow_marker('💥 Erro crítico no endpoint executar_sql', str(e))
            return jsonify({
                "sucesso": False,
                "erro": f"Erro interno: {str(e)}"
            }), 500

   
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

