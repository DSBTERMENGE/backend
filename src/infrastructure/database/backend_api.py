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
from .data_manager import consultar_bd, get_view, inserir_dados, atualizar_dados, excluir_dados

# Importa debugger personalizado
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from debugger import flow_marker, error_catcher, unexpected_error_catcher

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
            
            # Executa consulta na view usando função direta
            resultado = consultar_bd(nome_view, campos_solicitados, database_path=path_name.get('database_path'), database_name=path_name.get('database_name'))
            
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
            
            # Valida se tabela foi fornecida
            tabela = dados_request.get('tabela', '')
            if not tabela:
                return jsonify({
                    "dados": [],
                    "mensagem": "Nome da tabela não fornecido"
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
            dados_request = request.get_json()
            
            # TODO: Implementar lógica de inclusão usando data_manager
            resultado = {"status": "em_desenvolvimento", "operacao": "incluir"}
            
            return jsonify(resultado)
            
        except Exception as e:
            logger.error(f"Erro em incluir_reg_novo_db: {e}")
            return jsonify({"erro": str(e)}), 500

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

