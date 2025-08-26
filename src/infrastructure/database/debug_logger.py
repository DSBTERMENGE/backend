import logging
import os
from datetime import datetime

def setup_debug_logger():
    """Configura logger para debug do backend"""
    
    # Cria diretório de logs se não existir
    log_dir = os.path.join(os.path.dirname(__file__), 'logs')
    os.makedirs(log_dir, exist_ok=True)
    
    # Nome do arquivo com data/hora
    log_filename = f"debug_backend_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    log_path = os.path.join(log_dir, log_filename)
    
    # Configuração do logger
    logger = logging.getLogger('debug_backend')
    logger.setLevel(logging.DEBUG)
    
    # Remove handlers existentes
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)
    
    # Handler para arquivo
    file_handler = logging.FileHandler(log_path, encoding='utf-8')
    file_formatter = logging.Formatter(
        '%(asctime)s | %(levelname)s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
    
    # Handler para console (terminal)
    console_handler = logging.StreamHandler()
    console_formatter = logging.Formatter(
        '🔍 %(asctime)s | %(message)s',
        datefmt='%H:%M:%S'
    )
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)
    
    logger.info("="*60)
    logger.info("🚀 DEBUG LOGGER INICIADO")
    logger.info(f"📄 Log salvo em: {log_path}")
    logger.info("="*60)
    
    return logger

# Instancia global do logger
debug_logger = setup_debug_logger()
