#!/usr/bin/env python3
"""
Script de Backup Automático para FinCtl
Uso: python3 backup_automatico.py
Executado via PythonAnywhere Scheduled Tasks
"""

import os
import sys
import subprocess
from datetime import datetime

# Configuração
DB_PATH = "/home/DavidBit/Applications_DSB/FinCtl/data"
DB_NAME = "financas.db"
BACKUP_DIR = "/home/DavidBit/Applications_DSB/FinCtl/backups"
LOG_FILE = "/home/DavidBit/Applications_DSB/FinCtl/backups/backup.log"
MANTER_BACKUPS = 4  # Quantidade de backups a manter no servidor

def log(mensagem):
    """Registra mensagem no arquivo de log"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    linha = f"[{timestamp}] {mensagem}\n"
    
    # Criar diretório de logs se não existir
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(linha)
    
    print(linha.strip())

def limpar_backups_antigos(diretorio, manter=4):
    """Remove backups antigos, mantendo apenas os N mais recentes"""
    try:
        arquivos = [
            f for f in os.listdir(diretorio)
            if f.startswith('financas_backup_') and f.endswith('.db')
        ]
        
        if len(arquivos) <= manter:
            return
        
        # Ordenar por data de modificação (mais antigo primeiro)
        arquivos_completos = [
            (f, os.path.getmtime(os.path.join(diretorio, f)))
            for f in arquivos
        ]
        arquivos_completos.sort(key=lambda x: x[1])
        
        # Deletar os mais antigos
        quantidade_deletar = len(arquivos) - manter
        for arquivo, _ in arquivos_completos[:quantidade_deletar]:
            caminho = os.path.join(diretorio, arquivo)
            os.remove(caminho)
            log(f"  ♻️ Backup antigo removido: {arquivo}")
            
    except Exception as e:
        log(f"  ⚠️ Erro ao limpar backups antigos: {e}")

def criar_backup():
    """Executa o backup do banco de dados SQLite"""
    log("="*60)
    log("🚀 INICIANDO BACKUP AUTOMÁTICO")
    
    try:
        # Validar caminho do banco de dados
        db_completo = os.path.join(DB_PATH, DB_NAME)
        if not os.path.exists(db_completo):
            log(f"  ❌ ERRO: Banco de dados não encontrado: {db_completo}")
            return False
        
        tamanho_db = os.path.getsize(db_completo) / 1024  # KB
        log(f"  📊 Banco de dados: {DB_NAME} ({tamanho_db:.2f} KB)")
        
        # Criar diretório de backups
        os.makedirs(BACKUP_DIR, exist_ok=True)
        log(f"  📁 Diretório de backups: {BACKUP_DIR}")
        
        # Nome do arquivo de backup com timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_filename = f'financas_backup_{timestamp}.db'
        backup_path = os.path.join(BACKUP_DIR, backup_filename)
        
        # Criar backup usando SQLite .backup (método consistente)
        log(f"  ⏳ Criando backup: {backup_filename}")
        cmd = f'sqlite3 "{db_completo}" ".backup \'{backup_path}\'"'
        resultado = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        
        if resultado.returncode == 0 and os.path.exists(backup_path):
            tamanho_backup = os.path.getsize(backup_path) / 1024  # KB
            log(f"  ✅ Backup criado com sucesso!")
            log(f"  📦 Arquivo: {backup_filename}")
            log(f"  💾 Tamanho: {tamanho_backup:.2f} KB")
            
            # Limpar backups antigos
            log(f"  🧹 Limpando backups antigos (mantendo {MANTER_BACKUPS})...")
            limpar_backups_antigos(BACKUP_DIR, manter=MANTER_BACKUPS)
            
            # Listar backups existentes
            backups = [
                f for f in os.listdir(BACKUP_DIR)
                if f.startswith('financas_backup_') and f.endswith('.db')
            ]
            log(f"  📋 Total de backups no servidor: {len(backups)}")
            
            log("✨ BACKUP CONCLUÍDO COM SUCESSO")
            log("="*60)
            return True
            
        else:
            log(f"  ❌ ERRO ao criar backup")
            if resultado.stderr:
                log(f"  📝 Detalhes: {resultado.stderr}")
            log("="*60)
            return False
            
    except Exception as e:
        log(f"  ❌ EXCEÇÃO durante backup: {str(e)}")
        log("="*60)
        return False

if __name__ == '__main__':
    sucesso = criar_backup()
    sys.exit(0 if sucesso else 1)
