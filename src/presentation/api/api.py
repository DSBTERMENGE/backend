"""
API Genérica - Framework BackEnd_Teste
Fornece endpoints básicos de CRUD para qualquer projeto.
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import logging
import sys
import os

# Adiciona src ao path para imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

# Imports do framework
from infrastructure.database import data_manager
from infrastructure.config import config
from infrastructure.logging import logger_setup

# Configuração da aplicação Flask
app = Flask(__name__)
CORS(app, supports_credentials=True, methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'])

# Configuração de logging
logger_setup.configurar_logging()
logger = logging.getLogger(__name__)

# Configurações básicas
API_KEY = getattr(config, 'API_KEY', "framework-key-123")

def verificar_api_key():
    """Verificação básica de API key (personalizável por projeto)"""
    if request.method == 'OPTIONS':
        return True
    
    api_key = request.headers.get('x-api-key')
    return api_key == API_KEY

# === ENDPOINTS GENÉRICOS DO FRAMEWORK ===

@app.route("/", methods=["GET"])
def status():
    """Status da API"""
    if not verificar_api_key():
        return jsonify({"erro": "API key inválida"}), 403
    
    return jsonify({
        "status": "Framework BackEnd_Teste rodando",
        "versao": "1.0",
        "endpoints": [
            "GET / - Status da API",
            "GET /api/tables - Lista tabelas disponíveis", 
            "GET /api/<table> - Lista registros de uma tabela",
            "POST /api/<table> - Criar novo registro",
            "PUT /api/<table>/<id> - Atualizar registro",
            "DELETE /api/<table>/<id> - Deletar registro"
        ]
    })

@app.route("/api/tables", methods=["GET"])
def listar_tabelas():
    """Lista todas as tabelas disponíveis no banco"""
    if not verificar_api_key():
        return jsonify({"erro": "API key inválida"}), 403
    
    try:
        tabelas = data_manager.listar_tabelas()
        return jsonify({"tabelas": tabelas})
    except Exception as e:
        logger.error(f"Erro ao listar tabelas: {e}")
        return jsonify({"erro": "Erro interno do servidor"}), 500

@app.route("/api/<table>", methods=["GET"])
def listar_registros(table):
    """Lista todos os registros de uma tabela"""
    if not verificar_api_key():
        return jsonify({"erro": "API key inválida"}), 403
    
    try:
        registros = data_manager.obter_todos_registros(table)
        return jsonify({"dados": registros})
    except Exception as e:
        logger.error(f"Erro ao listar registros da tabela {table}: {e}")
        return jsonify({"erro": f"Erro ao acessar tabela {table}"}), 500

@app.route("/api/<table>", methods=["POST"]) 
def criar_registro(table):
    """Cria um novo registro na tabela"""
    if not verificar_api_key():
        return jsonify({"erro": "API key inválida"}), 403
    
    try:
        dados = request.get_json()
        if not dados:
            return jsonify({"erro": "Dados não fornecidos"}), 400
        
        id_criado = data_manager.criar_registro(table, dados)
        return jsonify({"mensagem": "Registro criado", "id": id_criado}), 201
    except Exception as e:
        logger.error(f"Erro ao criar registro na tabela {table}: {e}")
        return jsonify({"erro": "Erro ao criar registro"}), 500

@app.route("/api/<table>/<int:id>", methods=["PUT"])
def atualizar_registro(table, id):
    """Atualiza um registro existente"""
    if not verificar_api_key():
        return jsonify({"erro": "API key inválida"}), 403
    
    try:
        dados = request.get_json()
        if not dados:
            return jsonify({"erro": "Dados não fornecidos"}), 400
        
        sucesso = data_manager.atualizar_registro(table, id, dados)
        if sucesso:
            return jsonify({"mensagem": "Registro atualizado"})
        else:
            return jsonify({"erro": "Registro não encontrado"}), 404
    except Exception as e:
        logger.error(f"Erro ao atualizar registro {id} na tabela {table}: {e}")
        return jsonify({"erro": "Erro ao atualizar registro"}), 500

@app.route("/api/<table>/<int:id>", methods=["DELETE"])
def deletar_registro(table, id):
    """Deleta um registro"""
    if not verificar_api_key():
        return jsonify({"erro": "API key inválida"}), 403
    
    try:
        sucesso = data_manager.deletar_registro(table, id)
        if sucesso:
            return jsonify({"mensagem": "Registro deletado"})
        else:
            return jsonify({"erro": "Registro não encontrado"}), 404
    except Exception as e:
        logger.error(f"Erro ao deletar registro {id} na tabela {table}: {e}")
        return jsonify({"erro": "Erro ao deletar registro"}), 500

# === PONTO DE ENTRADA ===
if __name__ == '__main__':
    port = getattr(config, 'API_PORT', 5000)
    debug = getattr(config, 'DEBUG', True)
    
    print(f"Iniciando Framework BackEnd_Teste em http://127.0.0.1:{port}")
    print("Para usar a API, inclua o header: x-api-key: framework-key-123")
    
    app.run(debug=debug, port=port)
