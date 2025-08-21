import sqlite3
import os

# Define o caminho correto para o banco
db_path = os.path.join(os.path.dirname(__file__), 'financas.db')

# Conecta ao banco financas.db existente
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

print("=== CRIANDO VIEW GRUPOS_VIEW ===")
print(f"📁 Usando banco: {db_path}")

try:
    # Cria view grupos_view = tabela grupos ordenada por grupo
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
    
    # Commit das mudanças
    conn.commit()
    
    # Testa a view
    cursor.execute("SELECT * FROM grupos_view")
    grupos = cursor.fetchall()
    
    print(f"\n📋 CONTEÚDO DA VIEW GRUPOS_VIEW ({len(grupos)} registros):")
    for grupo in grupos:
        print(f"  {grupo[0]:2d} | {grupo[1]:15s} | {grupo[2]}")
    
    print("\n✅ View criada e testada com sucesso!")
    
except Exception as e:
    print(f"❌ Erro: {e}")
    
finally:
    conn.close()
    print("🔒 Conexão fechada.")
