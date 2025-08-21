import sqlite3
import os

# Define o caminho correto para o banco
db_path = os.path.join(os.path.dirname(__file__), 'financas.db')

# Conecta ao banco financas.db existente
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

print("=== CRIANDO TABELA GRUPOS E VIEW ===")
print(f"📁 Usando banco: {db_path}")

try:
    # Cria tabela grupos
    sql_tabela = """
    CREATE TABLE IF NOT EXISTS grupos (
        idgrupo INTEGER PRIMARY KEY AUTOINCREMENT,
        grupo TEXT NOT NULL UNIQUE,
        descricao TEXT NOT NULL
    )
    """
    
    cursor.execute(sql_tabela)
    print("✅ Tabela 'grupos' criada com sucesso!")
    
    # Cria view grupos_view
    sql_view = """
    CREATE VIEW IF NOT EXISTS grupos_view AS
    SELECT 
        idgrupo,
        grupo,
        descricao
    FROM grupos
    ORDER BY grupo
    """
    
    cursor.execute(sql_view)
    print("✅ View 'grupos_view' criada com sucesso!")
    
    # Verifica se já existem dados na tabela grupos
    cursor.execute("SELECT COUNT(*) FROM grupos")
    total_existente = cursor.fetchone()[0]
    
    if total_existente == 0:
        # Extrai grupos únicos da tabela classificacao existente
        cursor.execute("SELECT DISTINCT grupo FROM classificacao WHERE grupo IS NOT NULL AND grupo != ''")
        grupos_existentes = cursor.fetchall()
        
        print(f"📋 Encontrados {len(grupos_existentes)} grupos únicos na tabela classificacao:")
        
        # Prepara dados para inserção (grupo + descrição genérica)
        grupos_para_inserir = []
        for grupo_row in grupos_existentes:
            grupo = grupo_row[0]
            descricao = f"Grupo de classificação: {grupo}"
            grupos_para_inserir.append((grupo, descricao))
            print(f"  - {grupo}")
        
        # Insere os grupos extraídos
        if grupos_para_inserir:
            sql_insert = "INSERT INTO grupos (grupo, descricao) VALUES (?, ?)"
            cursor.executemany(sql_insert, grupos_para_inserir)
            print(f"✅ {len(grupos_para_inserir)} grupos extraídos e inseridos!")
        else:
            print("⚠️ Nenhum grupo válido encontrado na tabela classificacao")
    else:
        print(f"ℹ️ Tabela grupos já possui {total_existente} registros")
    
    # Commit das mudanças
    conn.commit()
    
    # Testa a view final
    cursor.execute("SELECT * FROM grupos_view")
    grupos = cursor.fetchall()
    
    print(f"\n📋 CONTEÚDO FINAL DA VIEW GRUPOS_VIEW ({len(grupos)} registros):")
    for grupo in grupos:
        print(f"  {grupo[0]:2d} | {grupo[1]:15s} | {grupo[2]}")
    
    print("\n✅ Estrutura criada e populada com sucesso!")
    
except Exception as e:
    print(f"❌ Erro: {e}")
    
finally:
    conn.close()
    print("🔒 Conexão fechada.")
