# 🔄 DIFERENÇAS: Backup SQLite vs PostgreSQL

## 📊 Comparação Técnica

| Aspecto | SQLite (FUNCIONAVA) | PostgreSQL (NÃO FUNCIONAVA) |
|---------|---------------------|------------------------------|
| **Complexidade** | ✅ Simples - arquivo local | ❌ Complexo - servidor remoto |
| **Autenticação** | ✅ Nenhuma necessária | ❌ Usuário + Senha obrigatórios |
| **Comando** | `shutil.copy2()` | `pg_dump` com parâmetros |
| **Dependências** | ✅ Nenhuma | ❌ PostgreSQL client tools |
| **Rede** | ✅ Local | ❌ Conexão TCP/IP |
| **Variáveis de Ambiente** | ✅ Nenhuma | ❌ 5 obrigatórias (PGUSER, PGPASSWORD, etc.) |
| **Compressão** | ❌ Opcional | ✅ Obrigatório (gzip) |

---

## 🐛 POR QUE NÃO FUNCIONAVA?

### **Código SQLite Original (funcionava):**
```python
# Simples - apenas copiar arquivo
import shutil
backup_path = f'backup_{timestamp}.db'
shutil.copy2('financas.db', backup_path)
# ✅ Funciona sempre - arquivo local
```

### **Código PostgreSQL Inicial (BUGADO):**
```python
# ❌ FALTAVA: host, port, senha!
cmd = f'pg_dump -U {db_user} -d {database_name} -f {backup_path}'
resultado = subprocess.run(cmd, shell=True, capture_output=True, text=True)
# ❌ FALHA: pg_dump precisa se conectar ao servidor PostgreSQL
# ❌ FALHA: Sem senha, conexão é recusada
# ❌ FALHA: Sem host/port, não sabe onde conectar
```

### **Código PostgreSQL Corrigido (funciona):**
```python
# ✅ COMPLETO: host, port, user, senha via ambiente
db_host = os.getenv('PGHOST', 'davidbit-12345.postgres.pythonanywhere-services.com')
db_port = os.getenv('PGPORT', '12345')
db_password = os.getenv('PGPASSWORD', '')

env = os.environ.copy()
if db_password:
    env['PGPASSWORD'] = db_password  # ✅ Senha via variável de ambiente

cmd = f'pg_dump -h {db_host} -p {db_port} -U {db_user} -d {database_name} -f {backup_path}'
resultado = subprocess.run(cmd, shell=True, capture_output=True, text=True, env=env)
# ✅ Funciona: pg_dump consegue se conectar ao servidor PostgreSQL
```

---

## 🔐 REQUISITOS ADICIONAIS PostgreSQL

### **1. Variáveis de Ambiente no WSGI:**
```python
# Arquivo: /var/www/davidbit_pythonanywhere_com_wsgi.py
import os

os.environ['PGUSER'] = 'davidbit'
os.environ['PGPASSWORD'] = 'sua_senha_postgresql'  # ⚠️ CRÍTICO!
os.environ['PGHOST'] = 'davidbit-12345.postgres.pythonanywhere-services.com'
os.environ['PGPORT'] = '12345'
os.environ['PGDATABASE'] = 'financas'
```

### **2. pg_dump Instalado:**
```bash
# Verificar se existe
which pg_dump
# Deve retornar: /usr/bin/pg_dump ou similar

# Se não existir, instalar PostgreSQL client
sudo apt-get install postgresql-client
```

### **3. Conexão de Rede:**
```bash
# Testar conexão manual
psql -h davidbit-12345.postgres.pythonanywhere-services.com \
     -p 12345 \
     -U davidbit \
     -d financas \
     -c "SELECT version();"
```

### **4. Diretório de Backups:**
```bash
# Criar diretório
mkdir -p /home/davidbit/backups
chmod 755 /home/davidbit/backups

# Verificar permissões
ls -ld /home/davidbit/backups
# Deve mostrar: drwxr-xr-x
```

---

## 📝 CHECKLIST DE MIGRAÇÃO

Para cada sistema que migrar de SQLite para PostgreSQL, verificar:

- [ ] Variáveis de ambiente configuradas no WSGI (5 variáveis)
- [ ] pg_dump instalado e acessível no PATH
- [ ] Conexão de rede com servidor PostgreSQL funcional
- [ ] PGPASSWORD configurado (senha correta)
- [ ] Diretório /home/davidbit/backups criado com permissões 755
- [ ] Comando pg_dump testado manualmente no bash
- [ ] Endpoint /api/backup/create testado via curl
- [ ] Scheduled tasks configuradas (2x por dia)
- [ ] Log de erros monitorado após primeira execução
- [ ] Backup .sql.gz verificado manualmente (download e descompressão)

---

## 🚀 PRÓXIMOS PASSOS

1. **Upload do backend_api.py corrigido** para PythonAnywhere
2. **Editar WSGI file** e adicionar as 5 variáveis de ambiente
3. **Recarregar webapp** no dashboard (botão verde "Reload")
4. **Testar manualmente** via curl:
   ```bash
   curl "https://davidbit.pythonanywhere.com/api/backup/create?token=finctl_backup_2025_secure"
   ```
5. **Verificar log de erros** (`log_de_erros.md`) para mensagens detalhadas
6. **Configurar scheduled tasks** (2x por dia: 06:00 e 18:00 UTC)
7. **Aguardar 24h** e verificar se backups foram criados:
   ```bash
   ls -lht /home/davidbit/backups/ | head -5
   ```

---

## 💡 LIÇÕES APRENDIDAS

1. **SQLite é simples, PostgreSQL é poderoso mas complexo**
   - SQLite: arquivo local, zero configuração
   - PostgreSQL: servidor remoto, autenticação obrigatória

2. **Backups PostgreSQL requerem credenciais completas**
   - Host, Port, User, Password, Database name
   - Sem PGPASSWORD, pg_dump falha com "authentication failed"

3. **Variáveis de ambiente são críticas**
   - Devem estar no WSGI file para Flask acessar
   - Bash console e Flask webapp têm ambientes separados

4. **Teste manual antes de automatizar**
   - Primeiro: pg_dump manual no bash
   - Depois: curl no endpoint
   - Por último: scheduled tasks

5. **Logs detalhados salvam tempo**
   - Com logs, identificamos problema em minutos
   - Sem logs, seria dias de tentativa e erro
