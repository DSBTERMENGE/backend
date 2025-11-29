#!/usr/bin/env python3
"""
Script para testar backup PostgreSQL localmente
Usa mesma lógica do backend_api.py mas com diagnóstico detalhado
"""

import os
import subprocess
import gzip
from datetime import datetime

def testar_backup_postgresql():
    """
    Testa criação de backup PostgreSQL com diagnóstico completo
    """
    print("=" * 70)
    print("🔍 DIAGNÓSTICO DE BACKUP POSTGRESQL")
    print("=" * 70)
    
    # 1. Verificar se pg_dump está disponível
    print("\n1️⃣ Verificando pg_dump...")
    try:
        resultado = subprocess.run(['which', 'pg_dump'], capture_output=True, text=True)
        if resultado.returncode == 0:
            print(f"   ✅ pg_dump encontrado: {resultado.stdout.strip()}")
        else:
            print("   ❌ pg_dump NÃO encontrado!")
            print("   💡 Instale: sudo apt-get install postgresql-client")
            return False
    except Exception as e:
        print(f"   ❌ Erro ao verificar pg_dump: {e}")
        return False
    
    # 2. Configurações
    print("\n2️⃣ Configurações do backup...")
    database_name = os.getenv('PGDATABASE', 'financas')
    db_user = os.getenv('PGUSER', 'davidbit')
    db_host = os.getenv('PGHOST', 'localhost')
    db_port = os.getenv('PGPORT', '5432')
    
    print(f"   Database: {database_name}")
    print(f"   Usuário: {db_user}")
    print(f"   Host: {db_host}")
    print(f"   Porta: {db_port}")
    
    # 3. Criar diretório de teste
    print("\n3️⃣ Preparando diretório de teste...")
    backup_dir = os.path.join(os.getcwd(), 'test_backups')
    os.makedirs(backup_dir, exist_ok=True)
    print(f"   📁 Diretório: {backup_dir}")
    
    # 4. Criar backup
    print("\n4️⃣ Executando pg_dump...")
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_filename = f'test_backup_{timestamp}.sql'
    backup_path = os.path.join(backup_dir, backup_filename)
    
    cmd = f'pg_dump -U {db_user} -h {db_host} -p {db_port} -d {database_name} -f {backup_path}'
    print(f"   🔧 Comando: {cmd}")
    
    resultado = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    
    print(f"\n   📊 Return code: {resultado.returncode}")
    
    if resultado.stdout:
        print(f"   📤 stdout: {resultado.stdout[:300]}")
    
    if resultado.stderr:
        print(f"   ⚠️  stderr: {resultado.stderr[:300]}")
    
    # 5. Verificar se backup foi criado
    print("\n5️⃣ Verificando arquivo de backup...")
    if resultado.returncode == 0 and os.path.exists(backup_path):
        tamanho = os.path.getsize(backup_path) / 1024
        print(f"   ✅ Backup criado com sucesso!")
        print(f"   📦 Arquivo: {backup_filename}")
        print(f"   📏 Tamanho: {tamanho:.2f} KB")
        
        # 6. Comprimir
        print("\n6️⃣ Comprimindo backup...")
        try:
            with open(backup_path, 'rb') as f_in:
                with gzip.open(f'{backup_path}.gz', 'wb') as f_out:
                    f_out.writelines(f_in)
            
            os.remove(backup_path)
            backup_path_gz = f'{backup_path}.gz'
            tamanho_comprimido = os.path.getsize(backup_path_gz) / 1024
            
            print(f"   ✅ Compressão concluída!")
            print(f"   📦 Arquivo: {backup_filename}.gz")
            print(f"   📏 Tamanho comprimido: {tamanho_comprimido:.2f} KB")
            print(f"   💾 Economia: {((tamanho - tamanho_comprimido) / tamanho * 100):.1f}%")
            
            # 7. Verificar conteúdo
            print("\n7️⃣ Verificando conteúdo do backup...")
            with gzip.open(backup_path_gz, 'rt') as f:
                primeiras_linhas = [f.readline() for _ in range(10)]
                if any('CREATE TABLE' in linha or 'INSERT INTO' in linha for linha in primeiras_linhas):
                    print("   ✅ Backup contém comandos SQL válidos")
                    print("   📄 Primeiras linhas:")
                    for i, linha in enumerate(primeiras_linhas[:5], 1):
                        print(f"      {i}. {linha.strip()[:80]}")
                else:
                    print("   ⚠️  Backup pode estar vazio ou inválido")
            
            print("\n" + "=" * 70)
            print("✅ TESTE DE BACKUP CONCLUÍDO COM SUCESSO!")
            print("=" * 70)
            print(f"\n📁 Arquivo salvo em: {backup_path_gz}")
            print(f"🗑️  Para limpar: rm -rf {backup_dir}")
            return True
            
        except Exception as e:
            print(f"   ❌ Erro ao comprimir: {e}")
            return False
    else:
        print("   ❌ Backup NÃO foi criado!")
        print(f"   🔍 Arquivo esperado: {backup_path}")
        print(f"   🔍 Arquivo existe? {os.path.exists(backup_path)}")
        
        print("\n" + "=" * 70)
        print("❌ TESTE DE BACKUP FALHOU!")
        print("=" * 70)
        
        # Sugestões de diagnóstico
        print("\n💡 Possíveis causas:")
        print("   1. PostgreSQL não está rodando")
        print("   2. Credenciais incorretas")
        print("   3. Database não existe")
        print("   4. Sem permissão para acessar database")
        
        print("\n🔧 Teste manualmente:")
        print(f"   psql -U {db_user} -h {db_host} -p {db_port} -d {database_name} -c '\\dt'")
        
        return False

if __name__ == '__main__':
    testar_backup_postgresql()
