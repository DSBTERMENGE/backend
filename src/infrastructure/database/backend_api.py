"""
Backend API - Framework DSB
Classe api_be para comunicação entre frontend e backend
Instanciável para múltiplas aplicações
"""

from flask import Flask, request, jsonify
import logging
import sys
import os
from datetime import datetime
from .data_manager import db_manager, consultar_bd

# Importa funções de log
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from log_helper import log_acompanhamento

# La este mó = logging.getLogger(__name__)


class api_be:
    """
    API Backend para Framework DSB
    Classe instanciável para cada aplicação
    Gerencia comunicação frontend-backend via HTTP
    """
    
    def __init__(self, app_name: str = "framework_app", host: str = "localhost", port: int = 5000):
        """
        Inicializa a API Backend
        
        @param {string} app_name - Nome da aplicação
        @param {string} host - Host do servidor (padrão: localhost) 
        @param {int} port - Porta do servidor (padrão: 5000)
        """
        self.app_name = app_name
        self.host = host
        self.port = port
        # ORIGINAL (para deploy em nuvem): self.flask_app = Flask(app_name)
        # DESENVOLVIMENTO LOCAL (serve frontend + API em uma porta):
        self.flask_app = Flask(app_name, static_folder='C:\\Applications_DSB\\FinCtl', static_url_path='')
        
        # Configurações da aplicação
        self.database_config = {}
        self.routes_registered = False
        
        # Logger específico da aplicação
        self.log = logging.getLogger(f"{__name__}.{app_name}")
        
        # Registra rotas automaticamente
        self._register_routes()
        
        self.log.info(f"api_be inicializada para aplicação '{app_name}' em {host}:{port}")
    
    def _register_routes(self):
        """Registra todas as rotas da API"""
        if self.routes_registered:
            return
            
        @self.flask_app.route('/health', methods=['GET'])
        def health():
            """Endpoint de health check"""
            return jsonify({
                "status": "ok", 
                "app": self.app_name,
                "message": "API Backend funcionando"
            })
        
        @self.flask_app.route('/inserir', methods=['POST'])
        def inserir_dados():
            """Endpoint para inserir dados"""
            return self._processar_operacao('insert')
        
        @self.flask_app.route('/atualizar', methods=['POST'])
        def atualizar_dados():
            """Endpoint para atualizar dados"""
            return self._processar_operacao('update')
        
        @self.flask_app.route('/excluir', methods=['POST'])
        def excluir_dados():
            """Endpoint para excluir dados"""
            return self._processar_operacao('delete')
        
        @self.flask_app.route('/obter', methods=['POST'])
        def obter_dados():
            """Endpoint para obter dados de tabela"""
            return self._processar_consulta('table')
        
        @self.flask_app.route('/consultar_dados_db', methods=['POST'])
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
            log_acompanhamento("➡️ ENTRADA: Endpoint /consultar_dados_db")
            dados_request = request.get_json()
            log_acompanhamento(f"📨 DADOS RECEBIDOS: {dados_request}")
            resultado = self._processar_consulta_formulario()
            log_acompanhamento(f"⬅️ SAÍDA: Endpoint /consultar_dados_db - Resposta: {resultado}")
            return resultado
        
        @self.flask_app.route('/obter_view', methods=['POST'])
        def obter_view():
            """Endpoint para obter dados de view (legado - usar consultar_dados_db)"""
            return self._processar_consulta('view')
        
        # ========== ROTAS PARA SERVIR FRONTEND (DESENVOLVIMENTO LOCAL) ==========
        # REMOVER/COMENTAR estas rotas para deploy em nuvem
        
        @self.flask_app.route('/')
        def index():
            """Serve o index.html na raiz - APENAS DESENVOLVIMENTO LOCAL"""
            from flask import send_from_directory
            return send_from_directory('C:\\Applications_DSB\\FinCtl', 'index.html')
        
        @self.flask_app.route('/framework_dsb/<path:filename>')
        def serve_framework_files(filename):
            """Serve arquivos do framework DSB"""
            from flask import send_from_directory
            return send_from_directory('C:\\Applications_DSB\\framework_dsb', filename)
        
        @self.flask_app.route('/<path:path>')
        def static_files(path):
            """Serve arquivos estáticos (JS, CSS, etc.) - APENAS DESENVOLVIMENTO LOCAL"""
            from flask import send_from_directory
            return send_from_directory(self.flask_app.static_folder, path)
        
        # ========== FIM DAS ROTAS DE DESENVOLVIMENTO ==========
        
        self.routes_registered = True
        self.log.info("Rotas da API registradas com sucesso")
    
    def _processar_operacao(self, operacao: str):
        """
        Processa operações CRUD (insert, update, delete)
        
        @param {string} operacao - Tipo de operação (insert/update/delete)
        @return {dict} - Resultado da operação
        """
        try:
            # Recebe dados do frontend
            dados_request = request.get_json()
            
            if not dados_request:
                return jsonify({"erro": "Dados não fornecidos"}), 400
            
            # Valida estrutura do request
            if not self._validar_request_operacao(dados_request):
                return jsonify({"erro": "Estrutura de dados inválida"}), 400
            
            # Processa configurações de banco enviadas pelo frontend
            database_path = dados_request.get('database_path', '')
            database_name = dados_request.get('database_name', '')
            database_host = dados_request.get('database_host', '')
            
            # Determina o caminho final do banco
            if database_path:
                # Se caminho completo foi fornecido, usa diretamente
                caminho_banco_final = database_path
            elif database_name:
                # Se apenas nome foi fornecido, usa diretório padrão
                caminho_banco_final = database_name
            else:
                # Usa configuração padrão da classe
                caminho_banco_final = self.database_config.get('caminho', 'default.db')
            
            self.log.info(f"Banco configurado: {caminho_banco_final}")
            
            # Cria instância do db_manager com banco específico
            db = db_manager(
                tabela_principal=dados_request['tabela'],
                campos=dados_request.get('campos', []),
                consulta=dados_request.get('consulta'),
                database_path=database_path,
                database_name=database_name
            )
            
            # Configura database_config se fornecido
            if 'database_config' in dados_request:
                db.database_config = dados_request['database_config']
            else:
                db.database_config = self.database_config
            
            # Configura dados do formulário
            db.dados_form_in = dados_request.get('dados_form_in', {})
            db.dados_form_out = dados_request.get('dados_form_out', {})
            
            # Executa operação
            if operacao == 'insert':
                resultado = db.insert_data()
            elif operacao == 'update':
                resultado = db.update_data()
            elif operacao == 'delete':
                resultado = db.delete_data()
            else:
                return jsonify({"erro": f"Operação '{operacao}' não suportada"}), 400
            
            self.log.info(f"Operação '{operacao}' executada com sucesso para tabela '{dados_request['tabela']}'")
            return jsonify(resultado)
            
        except Exception as e:
            self.log.error(f"Erro na operação '{operacao}': {e}", exc_info=True)
            return jsonify({"erro": str(e)}), 500
    
    def _processar_consulta_formulario(self):
        """
        Processa consultas de views prontas para população de formulários
        
        IMPORTANTE: Este método trabalha apenas com views dedicadas criadas
        especificamente para uso em formulários específicos.
        
        ESTRUTURA DE RESPOSTA:
        - SUCESSO: {dados: [{...}], mensagem: "sucesso"}
        - ERRO: {dados: [null], mensagem: "Descrição do erro"}
        
        @return {dict} - Dicionário de dados organizados para formulário
        """
        try:
            log_acompanhamento("➡️ ENTRADA: Função _processar_consulta_formulario()")
            
            # Recebe dados do frontend
            dados_request = request.get_json()
            log_acompanhamento(f"📋 DADOS REQUEST: {dados_request}")
            
            if not dados_request:
                log_acompanhamento("❌ ERRO: Dados não fornecidos")
                return jsonify({
                    "dados": [],
                    "mensagem": "Dados não fornecidos"
                }), 400
            
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
            
            # Processa configurações de banco
            database_path = dados_request.get('database_path', '')
            database_name = dados_request.get('database_name', '')
            database_host = dados_request.get('database_host', '')
            
            self.log.info(f"Consultando view pronta: {nome_view} com campos: {campos_solicitados}")
            
            # ✅ VALIDAÇÃO DE CAMPOS CONTRA VIEW
            if campos_solicitados != ['Todos']:
                campos_validos = self._validar_campos_view(nome_view, campos_solicitados, database_path, database_name)
                if not campos_validos['valido']:
                    return jsonify({
                        "dados": [],
                        "mensagem": campos_validos['erro']
                    }), 400
            
            # Cria instância do db_manager
            db = db_manager(
                tabela_principal=nome_view,
                campos=campos_solicitados,
                database_path=database_path,
                database_name=database_name
            )
            
            # Executa consulta na view (sistema normal)
            resultado = db.get_view(nome_view)
            
            # TESTE 2: Consulta específica na view (campo único)
            try:
                log_acompanhamento(f"🔍 TESTE 2 - EXECUTANDO SQL: SELECT idgrupo FROM {nome_view}")
                resultado_teste2 = consultar_bd(nome_view, ['idgrupo'], database_path, database_name)
                log_acompanhamento(f"📊 TESTE 2 - REGISTROS OBTIDOS: {len(resultado_teste2) if resultado_teste2 else 0} registros")
                log_acompanhamento(f"� TESTE 2 - DADOS RETORNADOS: {resultado_teste2}")
            except Exception as e:
                log_acompanhamento(f"❌ TESTE 2 - ERRO: {e}")
            
            # TESTE 3: Consulta direta na tabela grupos
            try:
                log_acompanhamento(f"🔍 TESTE 3 - EXECUTANDO SQL: SELECT * FROM grupos")
                resultado_teste3 = consultar_bd('grupos', ['Todos'], database_path, database_name)
                log_acompanhamento(f"�📊 TESTE 3 - REGISTROS OBTIDOS: {len(resultado_teste3) if resultado_teste3 else 0} registros")
                log_acompanhamento(f"📋 TESTE 3 - DADOS RETORNADOS: {resultado_teste3}")
            except Exception as e:
                log_acompanhamento(f"❌ TESTE 3 - ERRO: {e}")
            
            # Prepara resposta padronizada
            resposta = {
                "dados": resultado if resultado else [],
                "mensagem": "sucesso"
            }
            
            log_acompanhamento("⬅️ SAÍDA: Função _processar_consulta_formulario()")
            self.log.info(f"Consulta executada com sucesso - View: {nome_view}, Registros: {len(resultado) if resultado else 0}")
            return jsonify(resposta)
            
        except Exception as e:
            self.log.error(f"Erro na consulta de dados para formulário: {e}", exc_info=True)
            return jsonify({
                "dados": [],
                "mensagem": f"Erro interno: {str(e)}"
            }), 500
    
    def _validar_campos_view(self, nome_view, campos_solicitados, database_path, database_name):
        """
        Valida se os campos solicitados existem na view
        
        @param {str} nome_view - Nome da view a validar
        @param {list} campos_solicitados - Lista de campos solicitados
        @param {str} database_path - Caminho do banco
        @param {str} database_name - Nome do banco
        @return {dict} - {valido: bool, erro: str}
        """
        try:
            import sqlite3
            
            # Determina caminho do banco
            if database_path:
                db_file = database_path + "/" + (database_name or "default.db")
            elif database_name:
                db_file = database_name
            else:
                db_file = "default.db"
            
            # Conecta e obtém estrutura da view
            with sqlite3.connect(db_file) as conn:
                cursor = conn.cursor()
                cursor.execute(f"PRAGMA table_info({nome_view})")
                campos_view = [row[1] for row in cursor.fetchall()]  # row[1] = nome do campo
            
            # Verifica campos inexistentes
            campos_inexistentes = [campo for campo in campos_solicitados if campo not in campos_view]
            
            if campos_inexistentes:
                return {
                    "valido": False,
                    "erro": f"Campo(s) inexistente(s): {', '.join(campos_inexistentes)}. Campos disponíveis na view {nome_view}: {', '.join(campos_view)}"
                }
            
            return {"valido": True, "erro": None}
            
        except Exception as e:
            return {
                "valido": False,
                "erro": f"Erro ao validar campos da view {nome_view}: {str(e)}"
            }
    
    def _processar_consulta(self, tipo: str):
        """
        Processa consultas (table/view)
        
        @param {string} tipo - Tipo de consulta (table/view)
        @return {dict} - Dados consultados
        """
        try:
            # Recebe dados do frontend
            dados_request = request.get_json()
            
            if not dados_request:
                return jsonify({"erro": "Dados não fornecidos"}), 400
            
            # Processa configurações de banco enviadas pelo frontend
            database_path = dados_request.get('database_path', '')
            database_name = dados_request.get('database_name', '')
            database_host = dados_request.get('database_host', '')
            
            # Determina o caminho final do banco
            if database_path:
                caminho_banco_final = database_path
            elif database_name:
                caminho_banco_final = database_name
            else:
                caminho_banco_final = self.database_config.get('caminho', 'default.db')
            
            self.log.info(f"Banco configurado para consulta: {caminho_banco_final}")
            
            # Cria instância do db_manager com banco específico
            db = db_manager(
                tabela_principal=dados_request.get('tabela', ''),
                campos=dados_request.get('campos', []),
                consulta=dados_request.get('consulta'),
                database_path=database_path,
                database_name=database_name
            )
            
            # Configura database_config
            if 'database_config' in dados_request:
                db.database_config = dados_request['database_config']
            else:
                db.database_config = self.database_config
            
            # Configura filtros
            db.dados_form_in = dados_request.get('filtros', {})
            
            # Executa consulta
            if tipo == 'view':
                nome_view = dados_request.get('nome_view', '')
                if not nome_view:
                    return jsonify({"erro": "Nome da view não fornecido"}), 400
                resultado = db.get_view(nome_view)
            else:
                # Consulta em tabela (implementar método se necessário)
                return jsonify({"erro": "Consulta em tabela não implementada ainda"}), 501
            
            self.log.info(f"Consulta '{tipo}' executada com sucesso")
            return jsonify({"dados": resultado})
            
        except Exception as e:
            self.log.error(f"Erro na consulta '{tipo}': {e}", exc_info=True)
            return jsonify({"erro": str(e)}), 500
    
    def _validar_request_operacao(self, dados: dict) -> bool:
        """
        Valida estrutura do request para operações CRUD
        
        @param {dict} dados - Dados do request
        @return {bool} - True se válido
        """
        campos_obrigatorios = ['tabela']
        
        for campo in campos_obrigatorios:
            if campo not in dados:
                self.log.warning(f"Campo obrigatório '{campo}' não encontrado no request")
                return False
        
        return True
    
    def configurar_database(self, database_config: dict):
        """
        Configura parâmetros do database para esta instância da API
        
        @param {dict} database_config - Configuração do database
        """
        self.database_config = database_config
        self.log.info(f"Database configurado: {database_config}")
    
    def iniciar_servidor(self, debug: bool = True):
        """
        Inicia o servidor Flask
        
        @param {bool} debug - Modo debug (padrão: True)
        """
        self.log.info(f"Iniciando servidor {self.app_name} em {self.host}:{self.port}")
        self.flask_app.run(host=self.host, port=self.port, debug=debug)
    
    def obter_app_flask(self):
        """
        Retorna a instância do Flask para configurações adicionais
        
        @return {Flask} - Instância do Flask
        """
        return self.flask_app


# =====================================
# FUNÇÕES UTILITÁRIAS
# =====================================

def criar_api_aplicacao(app_name: str, database_config: dict, port: int = 5000):
    """
    Função helper para criar API pré-configurada para uma aplicação
    
    @param {string} app_name - Nome da aplicação
    @param {dict} database_config - Configuração do database
    @param {int} port - Porta do servidor
    @return {api_be} - Instância configurada da API
    """
    api = api_be(app_name=app_name, port=port)
    api.configurar_database(database_config)
    return api


# Módulo backend_api carregado - Classe api_be disponível

if __name__ == "__main__":
    api_backend = api_be()
    api_backend.iniciar_servidor()
