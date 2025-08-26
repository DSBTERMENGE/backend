from datetime import datetime

def log_acompanhamento(mensagem):
    """Função simples para acompanhar o fluxo - como console.log"""
    try:
        horario = datetime.now().strftime("%H:%M:%S")
        with open(r"C:\Applications_DSB\framework_dsb\backend\acompanhamento.txt", "a", encoding="utf-8") as f:
            f.write(f"[{horario}] {mensagem}\n")
    except:
        pass  # Se der erro, ignora
