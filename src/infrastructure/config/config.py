# === config.py (VersÃ£o com correÃ§Ã£o definitiva de caminho de log) ===

# -*- coding: utf-8 -*-

from pathlib import Path

"""
Arquivo de ConfiguraÃ§Ã£o para o projeto FinCtlByDSB.
"""

# --- 1. IDENTIFICAÃ‡ÃƒO DE ARQUIVOS E INSTITUIÃ‡Ã•ES ---
LISTA_CARTOES = ['VISA', 'MASTERCARD']
LISTA_BANCOS = ['SANTANDER', 'NOMADE']


# --- 2. PARÃ‚METROS DE VALIDAÃ‡ÃƒO (FLUXO DE CARTÃ•ES) ---
PALAVRAS_EXCLUIR_CARTAO = [
    "SALDO ANTERIOR", "SALDO FATURA", "SALDO DESTA FATURA", "PAGAMENTO DE FATURA",
    "TOTAL DE PAGAMENTOS", "TOTAL DE CREDITOS", "TOTAL DE CRÃ‰DITOS", "TOTAL DESPESAS",
    "TOTAL DE DESPESAS", "VALOR TOTAL", "COTAÃ‡ÃƒO", "COTACAO", "COTAÃ‡ÃƒO DOLAR",
    "COTAÃ‡ÃƒO DO DOLAR", "PARCELA"
]
PALAVRAS_CHAVE_APROVACAO = {
    "SALDO_ANTERIOR": ["SALDO", "ANTERIOR"],
    "TOTAL_PAGAMENTOS": ["PAGAMENTO", "FATURA"],
    "TOTAL_FATURA": ["SALDO", "FATURA"]
}
TOLERANCIA_APROVACAO_PERCENTUAL = 1.0


# --- 3. PARÃ‚METROS DE VALIDAÃ‡ÃƒO (FLUXO DE BANCOS) ---
FILTRO_PAGAMENTO_CARTAO = "PGTO_CARTÃƒO"
FILTRO_SALDO = "SALDO"


# --- 4. PARÃ‚METROS DE FORMATAÃ‡ÃƒO DE TEXTO ---
ABREVIACOES = [
    ['RECEBIDO', 'REC'], ['RECEBIDA', 'REC'], ['ENVIADO', 'ENV'],
    ['ENVIADA', 'ENV'], ['PAGAMENTO', 'PGTO']
]


# --- 5. CONFIGURAÃ‡Ã•ES DE DIRETÃ“RIOS E ARQUIVOS ---
PROJECT_ROOT = Path(__file__).resolve().parent
CAMINHO_PASTA_EXTRATOS = PROJECT_ROOT.parent / "extratos"
CAMINHO_PASTA_DADOS = PROJECT_ROOT.parent / "base_de_dados"
CAMINHO_PASTA_LOGS = PROJECT_ROOT.parent / "logs"
CAMINHO_BANCO_DE_DADOS = PROJECT_ROOT / "financas.db"

# =====================================================================
# A CORREÃ‡ÃƒO ESTÃ AQUI.
# Esta linha agora usa a variÃ¡vel CAMINHO_PASTA_LOGS para garantir consistÃªncia.
CAMINHO_LOG_EXTRACAO = CAMINHO_PASTA_LOGS / "log_extracao.txt"
# =====================================================================

# --- 6. CONFIGURAÃ‡Ã•ES DE LOGGING ---
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s [%(levelname)s] - %(message)s"
LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
