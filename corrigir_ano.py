import psycopg2

# Conecta no PostgreSQL
conn = psycopg2.connect(
    host='localhost',
    port=5432,
    database='financas',
    user='postgres',
    password='123456'
)

cursor = conn.cursor()

# Corrige ano
cursor.execute("UPDATE desp_mensal SET ano = 2025 WHERE ano = 20025;")
conn.commit()

print(f"✅ {cursor.rowcount} registros corrigidos!")

cursor.close()
conn.close()
