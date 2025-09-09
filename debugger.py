"""
DEBUGGER.PY - Framework DSB
===========================
Módulo de debug para backend Python - Equivalente ao Debugger.js
Funções padronizadas para logging e controle de fluxo
"""

import os
import sys
import traceback
from datetime import datetime


# Caminho do arquivo de log
LOG_FILE = os.path.join(os.path.dirname(__file__), 'log_de_erros.md')


def _inicializar_log():
    """
    Limpa o arquivo de log e adiciona cabeçalho com timestamp
    Chamada automaticamente na primeira execução
    """
    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    cabecalho = f"""# LOG DE ERROS DO BACKEND

**Sessão iniciada:** {timestamp}  
**Sistema:** Python Backend  
**Arquivo:** Framework DSB  

---

"""
    
    try:
        with open(LOG_FILE, 'w', encoding='utf-8') as f:
            f.write(cabecalho)
    except Exception as e:
        print(f"Erro ao inicializar log: {e}")


def _escrever_log(conteudo):
    """
    Escreve conteúdo no arquivo de log
    
    @param {str} conteudo - Conteúdo a ser escrito
    """
    timestamp = datetime.now().strftime("%H:%M:%S")
    linha = f"**[{timestamp}]** {conteudo}\n\n"
    
    try:
        with open(LOG_FILE, 'a', encoding='utf-8') as f:
            f.write(linha)
    except Exception as e:
        print(f"Erro ao escrever log: {e}")


def flow_marker(mensagem, dados=None):
    """
    Marca pontos importantes no fluxo de execução
    Equivalente ao flow_marker() do Debugger.js
    
    @param {str} mensagem - Mensagem descritiva
    @param {any} dados - Dados opcionais para logging
    """
    log_content = f"🔄 **FLOW:** {mensagem}"
    
    if dados is not None:
        log_content += f"  \n```\n{dados}\n```"
    
    _escrever_log(log_content)
    print(f"🔄 FLOW: {mensagem}")


def error_catcher(mensagem, erro=None):
    """
    Captura e registra erros tratados
    Equivalente ao error_catcher() do Debugger.js
    
    @param {str} mensagem - Mensagem descritiva do erro
    @param {Exception} erro - Objeto de erro (opcional)
    """
    log_content = f"❌ **ERRO:** {mensagem}"
    
    if erro is not None:
        log_content += f"  \n```\nTipo: {type(erro).__name__}\nMensagem: {str(erro)}\n```"
        
        # Adiciona stack trace se disponível
        if hasattr(erro, '__traceback__') and erro.__traceback__:
            tb_lines = traceback.format_tb(erro.__traceback__)
            log_content += f"  \n**Stack Trace:**\n```\n{''.join(tb_lines)}\n```"
    
    _escrever_log(log_content)
    print(f"❌ ERRO: {mensagem}")


def unexpected_error_catcher():
    """
    Configura captura de erros não manipulados
    Equivalente ao unexpected_error_catcher() do Debugger.js
    """
    def handle_exception(exc_type, exc_value, exc_traceback):
        if issubclass(exc_type, KeyboardInterrupt):
            # Permite Ctrl+C funcionar normalmente
            sys.__excepthook__(exc_type, exc_value, exc_traceback)
            return
        
        # Registra erro não manipulado
        tb_str = ''.join(traceback.format_exception(exc_type, exc_value, exc_traceback))
        
        log_content = f"💥 **ERRO NÃO MANIPULADO:**  \n```\n{tb_str}\n```"
        _escrever_log(log_content)
        
        print(f"💥 ERRO NÃO MANIPULADO: {exc_value}")
        print(tb_str)
    
    # Instala o handler de exceções
    sys.excepthook = handle_exception
    
    log_content = "🛡️ **Sistema de captura de erros ativado**"
    _escrever_log(log_content)
    print("🛡️ Sistema de captura de erros ativado")


# Inicializa o log automaticamente quando o módulo é importado
_inicializar_log()
