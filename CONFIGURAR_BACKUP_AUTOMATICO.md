# 🔄 CONFIGURAR BACKUP AUTOMÁTICO NO PYTHONANYWHERE

## ⚠️ PROBLEMA IDENTIFICADO

O backup automático não está funcionando no PythonAnywhere. Precisamos:

1. ✅ Testar manualmente se o endpoint de backup funciona
2. ✅ Configurar 2 tarefas agendadas (scheduled tasks)
3. ✅ Verificar permissões e variáveis de ambiente

---

## 📋 PASSO 1: TESTAR BACKUP MANUALMENTE

### No PythonAnywhere Bash Console:

```bash
# Testar se pg_dump está acessível
which pg_dump
# Saída esperada: /usr/bin/pg_dump

# Testar pg_dump manualmente
pg_dump -U davidbit -d financas -f /home/davidbit/test_backup.sql

# Verificar se funcionou
ls -lh /home/davidbit/test_backup.sql

# Se funcionou, remover teste
rm /home/davidbit/test_backup.sql
```

### Testar endpoint via curl:

```bash
curl -X GET "https://davidbit.pythonanywhere.com/api/backup/create?token=finctl_backup_2025_secure"
```

**Resposta esperada (sucesso):**
```json
{
  "success": true,
  "arquivo": "financas_backup_20251129_153045.sql.gz",
  "tamanho_original_kb": 245.67,
  "tamanho_comprimido_kb": 48.23,
  "caminho": "/home/davidbit/backups/financas_backup_20251129_153045.sql.gz",
  "timestamp": "20251129_153045",
  "tipo": "PostgreSQL dump (gzip)"
}
```

**Resposta se falhar:**
```json
{
  "success": false,
  "message": "pg_dump falhou (code 1): ...",
  "stderr": "...",
  "returncode": 1,
  "comando": "pg_dump -U davidbit -d financas -f ..."
}
```

---

## 📋 PASSO 2: VERIFICAR VARIÁVEIS DE AMBIENTE

**⚠️ CRÍTICO - Variáveis Obrigatórias para pg_dump:**

No PythonAnywhere, as seguintes variáveis **DEVEM** estar configuradas no WSGI file:

```python
# Editar: /var/www/davidbit_pythonanywhere_com_wsgi.py
import os

# PostgreSQL Configuration (OBRIGATÓRIO para pg_dump funcionar)
os.environ['PGUSER'] = 'davidbit'
os.environ['PGPASSWORD'] = 'SUA_SENHA_POSTGRESQL_AQUI'  # ⚠️ CRÍTICO!
os.environ['PGHOST'] = 'davidbit-12345.postgres.pythonanywhere-services.com'
os.environ['PGPORT'] = '12345'
os.environ['PGDATABASE'] = 'financas'

# Backup Token
os.environ['BACKUP_TOKEN'] = 'finctl_backup_2025_secure'
```

**🔍 Como Encontrar os Valores:**
1. Vá em PythonAnywhere → **Databases** → **PostgreSQL**
2. Clique em **"Connection Settings"**
3. Copie `Host`, `Port`, `Database name`, `Username`
4. `PGPASSWORD`: A senha que você definiu ao criar o banco PostgreSQL

**Verificar se está configurado (no bash):**
```bash
# Ver variáveis PostgreSQL (NÃO mostrará PGPASSWORD por segurança)
echo "PGUSER: $PGUSER"
echo "PGHOST: $PGHOST"
echo "PGPORT: $PGPORT"
echo "PGDATABASE: $PGDATABASE"
```

**Após adicionar no WSGI, RECARREGUE a webapp** no botão verde "Reload" no dashboard.
os.environ['PGUSER'] = 'davidbit'
os.environ['PGDATABASE'] = 'financas'
os.environ['PGHOST'] = 'davidbit-12345.postgres.pythonanywhere-services.com'
os.environ['PGPORT'] = '12345'
```

---

## 📋 PASSO 3: CONFIGURAR TAREFAS AGENDADAS

### Na interface do PythonAnywhere:

1. Acesse: **Tasks** (menu superior)
2. Clique em **"Create a new scheduled task"**

### ⏰ Tarefa 1 - Backup Manhã (06:00 UTC = 03:00 BRT)

**Comando:**
```bash
curl -X GET "https://davidbit.pythonanywhere.com/api/backup/create?token=finctl_backup_2025_secure"
```

**Horário:** `06:00` UTC  
**Frequência:** Daily (Diário)  
**Descrição:** Backup automático PostgreSQL (manhã)

### ⏰ Tarefa 2 - Backup Tarde (18:00 UTC = 15:00 BRT)

**Comando:**
```bash
curl -X GET "https://davidbit.pythonanywhere.com/api/backup/create?token=finctl_backup_2025_secure"
```

**Horário:** `18:00` UTC  
**Frequência:** Daily (Diário)  
**Descrição:** Backup automático PostgreSQL (tarde)

---

## 📋 PASSO 4: VERIFICAR DIRETÓRIO DE BACKUPS

```bash
# Criar diretório se não existir
mkdir -p /home/davidbit/backups

# Verificar permissões
ls -ld /home/davidbit/backups

# Listar backups existentes
ls -lh /home/davidbit/backups/
```

---

## 📋 PASSO 5: VERIFICAR LOGS

Após configurar as tarefas agendadas, verificar se executam:

```bash
# Ver log de erros do backend
tail -f /home/davidbit/logs/backend_api.log

# Ou verificar o log padrão do Flask
tail -f /var/log/davidbit.pythonanywhere.com.error.log
```

---

## 🔍 DIAGNÓSTICO DE PROBLEMAS COMUNS

### Problema 1: "pg_dump: command not found"

**Causa:** PostgreSQL client tools não instalados  
**Solução:** No PythonAnywhere, pg_dump deve estar em `/usr/bin/pg_dump`

```bash
# Verificar
ls -l /usr/bin/pg_dump

# Se não existir, abrir ticket de suporte PythonAnywhere
```

### Problema 2: "FATAL: password authentication failed"

**Causa:** Credenciais PostgreSQL incorretas  
**Solução:** Criar arquivo `.pgpass` no home:

```bash
# Criar arquivo .pgpass
nano ~/.pgpass

# Adicionar linha (substituir valores reais):
davidbit-12345.postgres.pythonanywhere-services.com:12345:financas:davidbit:SUA_SENHA_AQUI

# Ajustar permissões (obrigatório)
chmod 600 ~/.pgpass
```

### Problema 3: "Token inválido"

**Causa:** Token não corresponde ao esperado  
**Solução:** Verificar variável de ambiente `BACKUP_TOKEN`:

```python
# No WSGI, adicionar:
os.environ['BACKUP_TOKEN'] = 'finctl_backup_2025_secure'
```

### Problema 4: "Permission denied" ao escrever backup

**Causa:** Sem permissão no diretório  
**Solução:**

```bash
# Garantir permissões
chmod 755 /home/davidbit/backups
```

---

## ✅ CHECKLIST FINAL

- [ ] `pg_dump` acessível (`which pg_dump`)
- [ ] Teste manual de pg_dump funcionou
- [ ] Endpoint `/api/backup/create` responde com sucesso
- [ ] Diretório `/home/davidbit/backups` existe com permissões corretas
- [ ] Variável `BACKUP_TOKEN` configurada
- [ ] Arquivo `.pgpass` criado (se necessário)
- [ ] Tarefa agendada 1 (06:00 UTC) configurada
- [ ] Tarefa agendada 2 (18:00 UTC) configurada
- [ ] Aguardar próxima execução e verificar em `/home/davidbit/backups/`

---

## 🎯 VERIFICAÇÃO DE SUCESSO

Após 24h, verificar:

```bash
# Deve ter 2 backups (um de cada horário)
ls -lh /home/davidbit/backups/

# Ver detalhes
ls -lht /home/davidbit/backups/ | head -5

# Testar restauração local
gunzip -c /home/davidbit/backups/financas_backup_XXXXXXXX_XXXXXX.sql.gz | head -20
```

---

## 📥 RESTAURAR BACKUP LOCALMENTE

Para diagnóstico de problemas em produção:

```bash
# No PythonAnywhere, baixar backup
# (na interface web: Files > /home/davidbit/backups/ > Download)

# No ambiente local Windows
# Descomprimir
gunzip financas_backup_20251129_153045.sql.gz

# Restaurar no PostgreSQL local
psql -U postgres -d financas_dev < financas_backup_20251129_153045.sql

# Ou criar database novo
createdb -U postgres financas_diagnostico
psql -U postgres -d financas_diagnostico < financas_backup_20251129_153045.sql
```

---

## 🚨 NOTAS IMPORTANTES

1. **Backups mantidos:** 4 mais recentes (8 por semana com 2x/dia)
2. **Compressão:** ~80% de redução (SQL → SQL.GZ)
3. **Tamanho esperado:** 
   - SQL descomprimido: ~200-500 KB
   - SQL.GZ comprimido: ~40-100 KB
4. **Retenção:** Automática (deleta backups antigos)
5. **Segurança:** Token obrigatório para criar backups

---

## 📞 SUPORTE

Se problemas persistirem:

1. Verificar logs em `/var/log/davidbit.pythonanywhere.com.error.log`
2. Testar manualmente `pg_dump` no bash console
3. Abrir ticket de suporte no PythonAnywhere se `pg_dump` não funcionar
4. Verificar se PostgreSQL database está acessível (`psql -U davidbit -d financas -c '\dt'`)
