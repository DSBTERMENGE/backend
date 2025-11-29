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
        
        # Nome base do backup (database + "_backup")
        nome_db_backup = f"{database_name}_backup"
        
        # Garante que o diretório existe (cria só se não existir)
        try:
            os.makedirs(backup_dir, exist_ok=True)
        except Exception as e:
            mensagem = f"ERRO ao criar diretório de backup: {str(e)}"
            print(mensagem)
            registrar_log(os.getcwd(), mensagem)
            return False
        
        # Nome do arquivo com timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_filename = f'{nome_db_backup}_{timestamp}.sql'
        backup_path = os.path.join(backup_dir, backup_filename)
        
        # Log
        print(f"[{timestamp}] Iniciando backup...")
        print(f"Aplicação: {ACTIVE_APP}")
        print(f"Database: {database_name}")
        print(f"Host: {db_host}")
        print(f"Destino: {backup_path}")
        
        # Configurar ambiente para pg_dump (senha via variável)
        env = os.environ.copy()
        if db_password:
            env['PGPASSWORD'] = db_password
        
        # Executar pg_dump
        cmd = f'pg_dump -h {db_host} -p {db_port} -U {db_user} -d {database_name} -f {backup_path}'
        resultado = subprocess.run(cmd, shell=True, capture_output=True, text=True, env=env)
        
        if resultado.returncode != 0:
            print(f"ERRO no pg_dump: {resultado.stderr}")
            registrar_log(backup_dir, f"ERRO: pg_dump falhou - {resultado.stderr}")
            return False
        
        if not os.path.exists(backup_path):
            print("ERRO: Arquivo de backup não foi criado")
            registrar_log(backup_dir, "ERRO: Arquivo não criado")
            return False
        
        tamanho_original = os.path.getsize(backup_path) / 1024  # KB
        
        # Comprimir backup
        print("Comprimindo backup...")
        with open(backup_path, 'rb') as f_in:
            with gzip.open(f'{backup_path}.gz', 'wb') as f_out:
                f_out.writelines(f_in)
        
        os.remove(backup_path)  # Remove SQL não comprimido
        backup_path = f'{backup_path}.gz'
        backup_filename = f'{backup_filename}.gz'
        tamanho_comprimido = os.path.getsize(backup_path) / 1024  # KB
        
        # Limpar backups antigos
        limpar_backups_antigos(backup_dir, nome_db_backup, manter=4)
        
        # Log de sucesso
        mensagem = (
            f"SUCESSO: Backup criado\n"
            f"  Arquivo: {backup_filename}\n"
            f"  Tamanho original: {tamanho_original:.2f} KB\n"
            f"  Tamanho comprimido: {tamanho_comprimido:.2f} KB\n"
            f"  Compressão: {((1 - tamanho_comprimido/tamanho_original) * 100):.1f}%"
        )
        print(mensagem)
        registrar_log(backup_dir, mensagem)
        
        return True
        
    except Exception as e:
        mensagem = f"ERRO FATAL: {str(e)}"
        print(mensagem)
        # Tenta registrar no diretório de backup, se não conseguir, tenta no cwd
        try:
            registrar_log(backup_dir if 'backup_dir' in locals() else os.getcwd(), mensagem)
        except Exception as log_erro:
            print(f"ERRO ao registrar log: {str(log_erro)}")
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
            for arquivo, _ in backups[manter:]:
                caminho = os.path.join(backup_dir, arquivo)
                os.remove(caminho)
                print(f"Backup antigo removido: {arquivo}")
    except Exception as e:
        print(f"Erro ao limpar backups: {str(e)}")

def registrar_log(backup_dir, mensagem):
    """
    Registra mensagem no arquivo backup.log
    """
    try:
        log_path = os.path.join(backup_dir, 'backup.log')
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_existe = os.path.exists(log_path)
        with open(log_path, 'a', encoding='utf-8') as f:
            if not log_existe:
                f.write(f"[{timestamp}] criado backup log\n")
            f.write(f"[{timestamp}] {mensagem}\n")
    except Exception as e:
        print(f"Erro ao registrar log: {str(e)}")
    # Log explícito de início de execução
    try:
        registrar_log(backup_dir if 'backup_dir' in locals() else os.getcwd(), "Iniciado backup")
    except Exception as e:
        print(f"Erro ao registrar início do backup: {str(e)}")

if __name__ == '__main__':
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
