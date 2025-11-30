"""
BACKUP AUTOMÁTICO - POSTGRESQL
================================
Script para backup automático do banco PostgreSQL no PythonAnywhere
Executado via Task agendada: python3.11 /home/DavidBit/Applications_DSB/framework_dsb/backend/source_code/backup_automatico.py

IMPORTANTE - MULTI-APLICAÇÃO:
Define a variável ACTIVE_APP para selecionar qual aplicação fazer backup:
    os.environ['ACTIVE_APP'] = 'finctl'   # ou 'invctl' ou 'game'

Variáveis compartilhadas (todas as apps):
    os.environ['PG_HOST'] = 'host.postgres.pythonanywhere-services.com'
    os.environ['PG_PORT'] = '12345'
    os.environ['PG_USER'] = 'seu_usuario'

Variáveis específicas por app (opcionais - tem defaults):
    FINCTL_DATABASE, FINCTL_BACKUP_DIR, FINCTL_PG_PASSWORD
    INVCTL_DATABASE, INVCTL_BACKUP_DIR, INVCTL_PG_PASSWORD
    GAME_DATABASE, GAME_BACKUP_DIR, GAME_PG_PASSWORD

Funcionalidades:
- Usa pg_dump para backup PostgreSQL
- Comprime backup (gzip)
- Mantém últimos 4 backups
- Gera log de execução
- Suporta múltiplas aplicações (finctl, invctl, game)
"""

import os
import subprocess
import gzip
from datetime import datetime
from db_config import PG_CONFIG, ACTIVE_APP
from debugger import flow_marker, error_catcher, _inicializar_log


def criar_backup():
    """
    Cria backup do banco PostgreSQL usando pg_dump
    """
    try:
        # Configurações do banco via PG_CONFIG (já considera ACTIVE_APP)
        database_name = PG_CONFIG['database']
        db_user = PG_CONFIG['user']
        db_password = PG_CONFIG['password']
        db_host = PG_CONFIG['host']
        db_port = PG_CONFIG['port']
        backup_dir = PG_CONFIG['backup_dir']
        
        flow_marker(f"Iniciando backup - App: {ACTIVE_APP}, DB: {database_name}, Host: {db_host}")
        
        # Nome base do backup (database + "_backup")
        nome_db_backup = f"{database_name}_backup"
        
        # Garante que o diretório existe (cria só se não existir)
        try:
            os.makedirs(backup_dir, exist_ok=True)
            flow_marker(f"Diretório verificado: {backup_dir}")
        except Exception as e:
            error_catcher(f"Erro ao criar diretório de backup: {backup_dir}", e)
            return False
        
        # Nome do arquivo com timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_filename = f'{nome_db_backup}_{timestamp}.sql'
        backup_path = os.path.join(backup_dir, backup_filename)
        
        # Configurar ambiente para pg_dump (senha via variável)
        env = os.environ.copy()
        if db_password:
            env['PGPASSWORD'] = db_password
        
        flow_marker(f"Executando pg_dump: {database_name} -> {backup_filename}")
        
        # Executar pg_dump
        cmd = ['pg_dump', '-h', db_host, '-p', str(db_port), '-U', db_user, '-d', database_name, '-f', backup_path]
        resultado = subprocess.run(cmd, capture_output=True, text=True, env=env)
        
        if resultado.returncode != 0:
            error_catcher(f"pg_dump falhou", Exception(resultado.stderr))
            return False
        
        if not os.path.exists(backup_path):
            error_catcher("Arquivo de backup não foi criado", Exception(f"Esperado em: {backup_path}"))
            return False
        
        tamanho_original = os.path.getsize(backup_path) / 1024  # KB
        flow_marker(f"pg_dump concluído - Arquivo: {tamanho_original:.2f} KB")
        
        # Comprimir backup
        flow_marker("Comprimindo backup...")
        with open(backup_path, 'rb') as f_in:
            with gzip.open(f'{backup_path}.gz', 'wb') as f_out:
                f_out.writelines(f_in)
        
        os.remove(backup_path)  # Remove SQL não comprimido
        backup_path = f'{backup_path}.gz'
        backup_filename = f'{backup_filename}.gz'
        tamanho_comprimido = os.path.getsize(backup_path) / 1024  # KB
        
        compressao_pct = ((1 - tamanho_comprimido/tamanho_original) * 100)
        flow_marker(f"Backup comprimido - {tamanho_comprimido:.2f} KB ({compressao_pct:.1f}% redução)")
        
        # Limpar backups antigos
        flow_marker("Limpando backups antigos...")
        limpar_backups_antigos(backup_dir, nome_db_backup, manter=4)
        
        flow_marker(f"Backup finalizado com sucesso - {backup_filename}")
        
        return True
        
    except Exception as e:
        error_catcher("Erro fatal no backup", e)
        return False

def limpar_backups_antigos(backup_dir, nome_db_backup, manter=4):
    """
    Remove backups antigos, mantendo apenas os N mais recentes
    
    @param backup_dir: Diretório onde estão os backups
    @param nome_db_backup: Prefixo dos arquivos de backup (ex: 'financas_backup', 'inventario_backup')
    @param manter: Quantidade de backups a manter (padrão: 4)
    """
    try:
        backups = []
        prefixo = f'{nome_db_backup}_'
        for arquivo in os.listdir(backup_dir):
            if arquivo.startswith(prefixo) and arquivo.endswith('.sql.gz'):
                caminho = os.path.join(backup_dir, arquivo)
                backups.append((arquivo, os.path.getmtime(caminho)))
        
        # Ordenar por data (mais recente primeiro)
        backups.sort(key=lambda x: x[1], reverse=True)
        
        # Deletar excedentes
        if len(backups) > manter:
            removidos = []
            for arquivo, _ in backups[manter:]:
                caminho = os.path.join(backup_dir, arquivo)
                os.remove(caminho)
                removidos.append(arquivo)
            flow_marker(f"Limpeza concluída - Removidos {len(removidos)} backups antigos, mantidos {manter}")
        else:
            flow_marker(f"Limpeza concluída - Total de {len(backups)} backups, nenhum removido")
    except Exception as e:
        error_catcher("Erro ao limpar backups antigos", e)

if __name__ == '__main__':
    # Inicializa o log (limpa arquivo anterior)
    _inicializar_log()
    
    print("="*60)
    print("BACKUP AUTOMÁTICO - POSTGRESQL")
    print(f"Aplicação: {ACTIVE_APP.upper()}")
    print("="*60)
    
    sucesso = criar_backup()
    
    print("="*60)
    print(f"Aplicação: {ACTIVE_APP.upper()}")
    print(f"Status final: {'✓ SUCESSO' if sucesso else '✗ FALHA'}")
    print("="*60)
    
    # Exit code para monitoramento do PythonAnywhere
    exit(0 if sucesso else 1)
