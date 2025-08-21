"""
Backend API - Framework DSB
Classe api_be para comunicação entre frontend e backend
Instanciável para múltiplas aplicações
"""

from flask import Flask, request, jsonify
import logging
from data_manager import db_manager

# Logger para este módulo
log = logging.getLogger(__name__)


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
        self.flask_app = Flask(app_name)
        
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
        
        @self.flask_app.route('/obter_view', methods=['POST'])
        def obter_view():
            """Endpoint para obter dados de view"""
            return self._processar_consulta('view')
        
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


# Log de inicialização
log.info("Módulo backend_api carregado - Classe api_be disponível")

if __name__ == "__main__":
    api_backend = api_be()
    api_backend.iniciar_servidor()
