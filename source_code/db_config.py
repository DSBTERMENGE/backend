"""
CONFIGURAÇÃO DO BANCO DE DADOS POSTGRESQL
==========================================

Centraliza as configurações de conexão PostgreSQL
Suporta múltiplas aplicações com configurações independentes

APLICAÇÕES SUPORTADAS:
- finctl: Controle financeiro (em produção)
- invctl: Controle de inventário (em desenvolvimento)
- game: Sistema de games (planejado)
"""

import os

# ============================================================================
# CONFIGURAÇÕES COMPARTILHADAS (host, port, user)
# ============================================================================
PG_SHARED = {
    'host': os.getenv('PG_HOST', 'localhost'),
    'port': int(os.getenv('PG_PORT', 5432)),
    'user': os.getenv('PG_USER', 'postgres')
}

# ============================================================================
# CONFIGURAÇÕES POR APLICAÇÃO
# ============================================================================
APP_CONFIGS = {
    'finctl': {
        'database': os.getenv('FINCTL_DATABASE', 'financas'),
        'backup_dir': os.getenv('FINCTL_BACKUP_DIR', '/home/DavidBit/backups/finctl'),
        'password': os.getenv('FINCTL_PG_PASSWORD', os.getenv('PG_PASSWORD', '123456'))
    },
    'invctl': {
        'database': os.getenv('INVCTL_DATABASE', 'inventario'),
        'backup_dir': os.getenv('INVCTL_BACKUP_DIR', '/home/DavidBit/backups/invctl'),
        'password': os.getenv('INVCTL_PG_PASSWORD', os.getenv('PG_PASSWORD', '123456'))
    },
    'game': {
        'database': os.getenv('GAME_DATABASE', 'games'),
        'backup_dir': os.getenv('GAME_BACKUP_DIR', '/home/DavidBit/backups/game'),
        'password': os.getenv('GAME_PG_PASSWORD', os.getenv('PG_PASSWORD', '123456'))
    }
}

# ============================================================================
# CONFIGURAÇÃO ATIVA (selecionada por variável de ambiente)
# ============================================================================
ACTIVE_APP = os.getenv('ACTIVE_APP', 'finctl')  # Default: finctl

# Mescla configurações compartilhadas + específicas do app ativo
PG_CONFIG = {
    **PG_SHARED,
    **APP_CONFIGS.get(ACTIVE_APP, APP_CONFIGS['finctl'])
}

# ============================================================================
# FUNÇÕES
# ============================================================================

def get_config_for_app(app_name):
    """
    Retorna configuração completa para uma aplicação específica
    
    @param app_name: Nome da aplicação ('finctl', 'invctl', 'game')
    @return: Dict com configuração completa (host, port, user, database, backup_dir, password)
    
    Exemplo:
        config = get_config_for_app('finctl')
        # Retorna: {'host': '...', 'port': 5432, 'user': '...', 'database': 'financas', ...}
    """
    if app_name not in APP_CONFIGS:
        raise ValueError(f"Aplicação '{app_name}' não configurada. Apps válidos: {list(APP_CONFIGS.keys())}")
    
    return {
        **PG_SHARED,
        **APP_CONFIGS[app_name]
    }

def get_connection_string(database_name=None):
    """
    Retorna string de conexão PostgreSQL
    
    @param database_name: Nome do banco (opcional - usa do PG_CONFIG se não fornecido)
    @return: String de conexão PostgreSQL formatada
    
    IMPORTANTE: 
    - Se database_name não for fornecido, usa PG_CONFIG['database'] (app ativo)
    - Framework genérico - compatível com código legado que passa database_name
    """
    db_name = database_name or PG_CONFIG.get('database')
    
    if not db_name:
        raise ValueError("database_name é obrigatório - deve vir da aplicação ou estar em PG_CONFIG")
    
    return (
        f"host={PG_CONFIG['host']} "
        f"port={PG_CONFIG['port']} "
        f"dbname={db_name} "
        f"user={PG_CONFIG['user']} "
        f"password={PG_CONFIG['password']}"
    )
