#!/usr/bin/env python3
"""
SERVIDOR GENÉRICO FRAMEWORK DSB - INICIALIZAÇÃO UNIVERSAL
=========================================================

PROCESSOS DE INICIALIZAÇÃO PREVISTOS:
=====================================

1. DESENVOLVIMENTO (ATUAL):
   - Execução manual: python server_Applications_DSB.py [nome_app]
   - Usa configuração hardcoded do arquivo: server_Applications_DSB_config.json
   - Ideal para desenvolvimento de aplicação específica
   - Exemplo: python server_Applications_DSB.py finctl

2. PRODUÇÃO (FUTURO):
   - Inicialização automática de múltiplas aplicações simultaneamente
   - Gerenciamento de processos em background
   - Configuração dinâmica via banco de dados
   - Load balancing e failover automático

RESPONSABILIDADES:
==================
- Ler configurações de aplicações do server_Applications_DSB_config.json
- Criar servidor Flask dinamicamente para cada aplicação
- Servir arquivos estáticos e configurar endpoints CRUD
- Fornecer infraestrutura backend universal para todas as apps do Framework DSB

CONFIGURAÇÃO HARDCODED:
======================
CONFIGURAÇÃO HARDCODED:
======================
As configurações no JSON são apropriadas sendo hardcoded porque definem a
infraestrutura do servidor (portas, caminhos, etc.), não dados das aplicações.
Os dados dinâmicos vêm do frontend via configuração em main.js de cada app.
"""

import sys
import os
import json
from flask import Flask
from debugger import flow_marker, error_catcher, unexpected_error_catcher
from backend_api import configurar_endpoints

# =============================================================================
# FUNÇÕES DE CONFIGURAÇÃO
# =============================================================================

def obter_caminho_config():
    """
    Obtém o caminho para o arquivo de configuração das aplicações
    
    ⚠️  OBSERVAÇÃO IMPORTANTE:
    Este servidor tem uma peculiaridade não identificada onde só inicializa
    corretamente quando executado com cd e python no mesmo comando PowerShell:
    
    COMANDO CORRETO:
    cd "C:\Applications_DSB\framework_dsb\backend\source_code" ; python server_Applications_DSB.py
    
    Executar cd separadamente e depois python resulta em erro de inicialização.
    """
    # Arquivo agora fica na mesma pasta do código-fonte
    # ENDEREÇO: source_code/server_Applications_DSB_config.json
    # Mais organizado e auto-contido
    pasta_atual = os.path.dirname(__file__)
    return os.path.join(pasta_atual, 'server_Applications_DSB_config.json')

def ler_configuracao_apps():
    """Lê configurações das aplicações do arquivo JSON"""
    arquivo_config = obter_caminho_config()
    
    try:
        with open(arquivo_config, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"❌ Arquivo de configuração não encontrado: {arquivo_config}")
        print("📝 Crie o arquivo server_Applications_DSB_config.json na pasta Applications_DSB")
        return None
    except json.JSONDecodeError as e:
        print(f"❌ Erro no arquivo JSON: {e}")
        return None

def obter_apps_ativas(configuracoes):
    """Retorna apenas aplicações com status 'ativo'"""
    if not configuracoes or 'aplicacoes' not in configuracoes:
        return {}
    
    return {
        nome: dados 
        for nome, dados in configuracoes['aplicacoes'].items() 
        if dados.get('status', 'ativo') == 'ativo'
    }

def escolher_app_interativo(apps_disponiveis):
    """Permite seleção interativa da aplicação"""
    print("\n📱 APLICAÇÕES DISPONÍVEIS:")
    print("-" * 50)
    
    apps = list(apps_disponiveis.keys())
    for i, app in enumerate(apps, 1):
        config = apps_disponiveis[app]
        print(f"{i}. {app.upper()} - {config.get('description', app)}")
    
    print("-" * 50)
    
    try:
        escolha = int(input("Escolha uma aplicação (número): ")) - 1
        if 0 <= escolha < len(apps):
            return apps[escolha]
        else:
            print("❌ Escolha inválida!")
            return None
    except ValueError:
        print("❌ Digite um número válido!")
        return None

# =============================================================================
# CRIAÇÃO DO SERVIDOR FLASK
# =============================================================================

def criar_servidor_flask(app_name, config):
    """Cria e configura a instância Flask dinamicamente"""
    print(f"🏗️ Criando servidor Flask para: {app_name}")
    
    # Cria instância Flask com configurações da aplicação
    app = Flask(
        f"{app_name}_api",
        static_folder=config['static_folder'],
        static_url_path=''
    )
    
    # Importa e configura endpoints do backend_api
    from backend_api import configurar_endpoints
    configurar_endpoints(app)
    
    return app

# =============================================================================
# FUNÇÃO PRINCIPAL GENÉRICA
# =============================================================================

def main():
    """
    Função principal para inicializar servidor genérico Framework DSB
    
    PROCESSOS DE INICIALIZAÇÃO:
    ==========================
    
    1. DESENVOLVIMENTO (ATUAL): 
       - Comando: python server_Applications_DSB.py [nome_app]
       - Configuração: server_Applications_DSB_config.json (hardcoded)
       - Uso: Desenvolvimento de aplicação específica
       
       ⚠️  IMPORTANTE - COMANDO PARA INICIALIZAÇÃO:
       Por motivo não identificado, o servidor só inicializa corretamente 
       quando executado com cd e python no mesmo comando:
       
       COMANDO CORRETO (copie exatamente):
       cd "C:\Applications_DSB\framework_dsb\backend\source_code" ; python server_Applications_DSB.py
       
       NÃO FUNCIONA se executar cd separadamente e depois python!
       
    2. PRODUÇÃO (FUTURO):
       - Inicialização automática de múltiplas aplicações
       - Configuração dinâmica via banco de dados
       - Gerenciamento de processos em background
    
    Detecta aplicação automaticamente ou via argumento
    """
    print("🚀 Iniciando Servidor Backend Framework DSB Genérico...")
    print("📋 Processo: DESENVOLVIMENTO - Configuração via server_Applications_DSB_config.json")
    
    # Carrega configurações das aplicações
    configuracoes = ler_configuracao_apps()
    if not configuracoes:
        return
    
    # Determina qual aplicação usar
    app_name = None
    config = None
    
    # MODO 1: Argumento da linha de comando
    if len(sys.argv) > 1:
        app_name = sys.argv[1].lower()
        if app_name in configuracoes.get('aplicacoes', {}):
            config = configuracoes['aplicacoes'][app_name]
            print(f"🎯 Aplicação solicitada: {app_name}")
        else:
            print(f"❌ Aplicação '{app_name}' não encontrada no arquivo de configuração!")
            print(f"📋 Aplicações disponíveis: {list(configuracoes.get('aplicacoes', {}).keys())}")
            return
    
    # MODO 2: Detecção automática por status 'ativo'
    else:
        apps_ativas = obter_apps_ativas(configuracoes)
        
        if len(apps_ativas) == 1:
            # Uma aplicação ativa: inicia automaticamente
            app_name = list(apps_ativas.keys())[0]
            config = apps_ativas[app_name]
            print(f"🎯 Aplicação ativa detectada: {app_name}")
            
        elif len(apps_ativas) > 1:
            # Múltiplas aplicações ativas: menu interativo
            print(f"🔍 Encontradas {len(apps_ativas)} aplicações ativas")
            app_name = escolher_app_interativo(apps_ativas)
            if not app_name:
                return
            config = apps_ativas[app_name]
            
        else:
            # Nenhuma aplicação ativa
            print("❌ Nenhuma aplicação com status 'ativo' encontrada!")
            print("💡 Configure status='ativo' no arquivo de configuração ou")
            print("� Execute: python server_Applications_DSB.py <nome_da_app>")
            return
    
    # Exibe informações da aplicação
    print("\n" + "="*60)
    print(f"📱 APLICAÇÃO: {app_name.upper()}")
    print(f"� DESCRIÇÃO: {config.get('description', 'N/A')}")
    print(f"📁 PASTA ESTÁTICA: {config.get('static_folder', 'N/A')}")
    print(f"🗄️ DATABASE: {config.get('database_name', 'N/A')}")
    print(f"🌐 PORTA: {config.get('port', 5000)}")
    print(f"🔧 STATUS: {config.get('status', 'ativo')}")
    print("="*60)
    
    # Cria e inicia servidor Flask
    try:
        print("🏗️ Criando servidor Flask...")
        servidor = criar_servidor_flask(app_name, config)
        
        host = configuracoes.get('configuracoes_gerais', {}).get('host_desenvolvimento', 'localhost')
        port = config.get('port', 5000)
        debug = configuracoes.get('configuracoes_gerais', {}).get('debug_mode', True)
        
        print(f"🌐 Iniciando servidor em {host}:{port}...")
        print(f"🔗 Acesse: http://{host}:{port}")
        print("🛑 Pressione Ctrl+C para parar o servidor")
        print("=" * 60)
        print("✅ SERVIDOR ATIVO E FUNCIONANDO!")
        print("🔄 Aguardando requisições... (Ctrl+C para parar)")
        print("=" * 60)
        
        try:
            servidor.run(host=host, port=port, debug=debug)
        except Exception as server_error:
            error_catcher("Erro na linha servidor.run()", server_error)
            raise
        
    except KeyboardInterrupt:
        print("\n⏹️ Servidor interrompido pelo usuário")
        
    except Exception as e:
        print(f"❌ Erro ao iniciar servidor: {e}")
        
    finally:
        print("🔒 Encerrando servidor backend Framework DSB")


if __name__ == "__main__":
    main()
