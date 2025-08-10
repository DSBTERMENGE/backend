# === scripts/logger_setup.py (Sincronizado com seu config.py) ===

import logging
import sys
from logging.handlers import RotatingFileHandler
from infrastructure.config import config

def configurar_logging():
    """
    Configura os loggers usando as variáveis definidas no arquivo config.py.
    """
    # --- 1. CONFIGURAÇÃO DO LOGGER DE DIAGNÓSTICO (RAIZ) ---

    # Usa o formato e o formato de data definidos em config.py
    log_formatter = logging.Formatter(
        fmt=config.LOG_FORMAT,
        datefmt=config.LOG_DATE_FORMAT
    )

    # Constrói o caminho completo do arquivo de log usando a pasta definida em config.py
    log_file = config.CAMINHO_PASTA_LOGS / "app.log"

    # Garante que o diretório de log exista
    log_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Handler para rotacionar arquivos de log
    file_handler = RotatingFileHandler(
        log_file, maxBytes=5*1024*1024, backupCount=5, encoding='utf-8'
    )
    file_handler.setFormatter(log_formatter)
    
    # Handler para exibir logs de diagnóstico no console
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setFormatter(log_formatter)
    
    root_logger = logging.getLogger()
    # Usa o nível de log definido em config.py
    root_logger.setLevel(config.LOG_LEVEL)
    
    if not root_logger.handlers:
        root_logger.addHandler(file_handler)
        root_logger.addHandler(stdout_handler)

    # --- 2. CONFIGURAÇÃO DO LOGGER DE CONSOLE (PARA UI) ---
    # Este logger mantém um formato simples para não poluir a interface do usuário
    console_formatter = logging.Formatter('%(message)s')
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(console_formatter)
    console_handler.setLevel(config.LOG_LEVEL) 
    
    ui_logger = logging.getLogger('console_logger')
    ui_logger.setLevel(config.LOG_LEVEL)
    
    if not ui_logger.handlers:
        ui_logger.addHandler(console_handler)
    ui_logger.propagate = False
