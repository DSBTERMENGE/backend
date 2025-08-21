#!/usr/bin/env python3
"""
Inicializador Principal do Backend - Framework DSB
Arquivo genérico para iniciar qualquer aplicação do framework
"""

import sys
import os

# Adiciona o diretório src ao path para importações
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.infrastructure.database.backend_api import api_be
from src.infrastructure.database.data_manager import db_manager

def main():
    """
    Função principal para inicializar o servidor backend
    Pode ser usado para qualquer aplicação do framework
    """
    print("🚀 Iniciando Servidor Backend Framework DSB...")
    
    # ========== INSTANCIAÇÃO DA API BACKEND ==========
    
    # Instanciando a API backend genérica
    api_backend = api_be()
    
    # Configurações padrão (podem ser sobrescritas por variáveis de ambiente)
    api_backend.aplicacao = os.getenv("APP_NAME", "Framework_DSB")
    api_backend.versao = os.getenv("APP_VERSION", "1.0.0")
    api_backend.host = os.getenv("HOST", "localhost")
    api_backend.porta = int(os.getenv("PORT", "5000"))
    api_backend.debug = os.getenv("DEBUG", "True").lower() == "true"
    
    # Configurando banco de dados
    api_backend.database_path = os.getenv("DATABASE_PATH", "framework_dsb.db")
    
    print(f"✅ API Backend configurada:")
    print(f"   📱 Aplicação: {api_backend.aplicacao}")
    print(f"   📍 Host: {api_backend.host}:{api_backend.porta}")
    print(f"   💾 Database: {api_backend.database_path}")
    print(f"   🐛 Debug: {api_backend.debug}")
    
    # ========== CONFIGURAÇÃO DO BANCO DE DADOS ==========
    
    # Instanciando o gerenciador de banco
    db_instance = db_manager(api_backend.database_path)
    
    # Associando o db_manager à API
    api_backend.db_manager = db_instance
    
    print("✅ Gerenciador de banco associado à API")
    
    # ========== INICIALIZAÇÃO DO SERVIDOR ==========
    
    try:
        print("🌐 Iniciando servidor Flask...")
        print(f"🔗 Acesse: http://{api_backend.host}:{api_backend.porta}")
        print("⏹️ Pressione Ctrl+C para parar o servidor")
        print("-" * 50)
        
        api_backend.iniciar_servidor()
        
    except KeyboardInterrupt:
        print("\n⏹️ Servidor interrompido pelo usuário")
        
    except Exception as e:
        print(f"❌ Erro ao iniciar servidor: {e}")
        
    finally:
        print("🔒 Encerrando servidor backend")


if __name__ == "__main__":
    main()
