"""
CONFIGURAÇÃO DO BANCO DE DADOS POSTGRESQL
==========================================

Centraliza as configurações de conexão PostgreSQL
Framework genérico - nome do banco vem da aplicação
"""

import os

# Configurações PostgreSQL (SEM database hardcoded - vem da aplicação)
PG_CONFIG = {
    'host': os.getenv('PG_HOST', 'localhost'),
    'port': int(os.getenv('PG_PORT', 5432)),
    'user': os.getenv('PG_USER', 'postgres'),
    'password': os.getenv('PG_PASSWORD', '123456')  # ⚠️ USAR VARIÁVEL DE AMBIENTE EM PRODUÇÃO
}

def get_connection_string(database_name):
    """
    Retorna string de conexão PostgreSQL
    
    @param database_name: Nome do banco de dados (vem da aplicação via main.js)
    @return: String de conexão PostgreSQL formatada
    
    IMPORTANTE: Framework genérico não tem database hardcoded.
    O nome do banco vem da aplicação (ex: FinCtl define 'financas' no main.js)
    """
    if not database_name:
        raise ValueError("database_name é obrigatório - deve vir da aplicação")
    
    return (
        f"host={PG_CONFIG['host']} "
        f"port={PG_CONFIG['port']} "
        f"dbname={database_name} "
        f"user={PG_CONFIG['user']} "
        f"password={PG_CONFIG['password']}"
    )
