"""
CONFIGURAÇÃO DO BANCO DE DADOS POSTGRESQL
==========================================

Centraliza as configurações de conexão PostgreSQL
"""

import os

# Configurações PostgreSQL
PG_CONFIG = {
    'host': os.getenv('PG_HOST', 'localhost'),
    'port': int(os.getenv('PG_PORT', 5432)),
    'database': os.getenv('PG_DATABASE', 'financas'),
    'user': os.getenv('PG_USER', 'postgres'),
    'password': os.getenv('PG_PASSWORD', '123456')  # ⚠️ USAR VARIÁVEL DE AMBIENTE EM PRODUÇÃO
}

def get_connection_string():
    """Retorna string de conexão PostgreSQL"""
    return (
        f"host={PG_CONFIG['host']} "
        f"port={PG_CONFIG['port']} "
        f"dbname={PG_CONFIG['database']} "
        f"user={PG_CONFIG['user']} "
        f"password={PG_CONFIG['password']}"
    )
