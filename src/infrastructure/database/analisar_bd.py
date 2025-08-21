import sqlite3

# Conecta ao banco financas.db
conn = sqlite3.connect('financas.db')
cursor = conn.cursor()

print("=== ESTRUTURA DO BANCO FINANCAS.DB ===")

# Lista tabelas
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tabelas = cursor.fetchall()
print(f"\n📋 TABELAS ENCONTRADAS ({len(tabelas)}):")
for tabela in tabelas:
    print(f"  - {tabela[0]}")

# Lista views
cursor.execute("SELECT name FROM sqlite_master WHERE type='view'")
views = cursor.fetchall()
print(f"\n👁️ VIEWS ENCONTRADAS ({len(views)}):")
for view in views:
    print(f"  - {view[0]}")

# Para cada tabela, mostra estrutura
print(f"\n🏗️ ESTRUTURA DAS TABELAS:")
for tabela in tabelas:
    nome_tabela = tabela[0]
    print(f"\n--- {nome_tabela.upper()} ---")
    
    cursor.execute(f"PRAGMA table_info({nome_tabela})")
    colunas = cursor.fetchall()
    
    for coluna in colunas:
        pk = " (PK)" if coluna[5] == 1 else ""
        print(f"  {coluna[1]} {coluna[2]}{pk}")
    
    # Conta registros
    cursor.execute(f"SELECT COUNT(*) FROM {nome_tabela}")
    total = cursor.fetchone()[0]
    print(f"  📊 Total de registros: {total}")

conn.close()
print("\n✅ Análise concluída!")
