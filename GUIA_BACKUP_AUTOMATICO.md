# 💾 GUIA DE BACKUP AUTOMÁTICO - FinCtl

## 🎯 **VISÃO GERAL**

Sistema de backup automático do banco de dados SQLite do FinCtl usando:
- ✅ **Backend:** Endpoints Flask para criar e baixar backups
- ✅ **Agendador:** cron-job.org (grátis, na nuvem)
- ✅ **Armazenamento:** PythonAnywhere (4 últimas cópias)

---

## 📋 **ENDPOINTS IMPLEMENTADOS**

### **1️⃣ Criar Backup (Automático/Manual)**

**URL:** `GET/POST /api/backup/create?token=SEU_TOKEN`

**Função:** Cria backup do banco de dados com timestamp

**Parâmetros:**
- `token` (obrigatório): Token de segurança

**Response:**
```json
{
    "success": true,
    "arquivo": "financas_backup_20251116_030000.db",
    "tamanho_kb": 94.5,
    "caminho": "/home/davidbit/backups/financas_backup_20251116_030000.db",
    "timestamp": "20251116_030000"
}
```

---

### **2️⃣ Listar Backups**

**URL:** `GET /api/backup/list`

**Função:** Lista todos os backups disponíveis

**Response:**
```json
{
    "success": true,
    "total": 4,
    "backups": [
        {
            "nome": "financas_backup_20251116_030000.db",
            "tamanho_kb": 94.5,
            "data_criacao": "2025-11-16T03:00:00",
            "timestamp": 1731726000
        }
    ]
}
```

---

### **3️⃣ Baixar Último Backup**

**URL:** `GET /api/backup/download/latest`

**Função:** Força download do backup mais recente

**Response:** Arquivo `.db` para download

---

### **4️⃣ Baixar Backup Específico**

**URL:** `GET /api/backup/download/<filename>`

**Função:** Baixa backup específico

**Exemplo:** `/api/backup/download/financas_backup_20251110_030000.db`

---

## 🔐 **CONFIGURAÇÃO DE SEGURANÇA**

### **Token de Backup:**

O token padrão é: `finctl_backup_2025_secure`

**Para maior segurança, configure variável de ambiente no PythonAnywhere:**

1. Acesse: Dashboard → Web → Environment variables
2. Adicione:
   - Nome: `BACKUP_TOKEN`
   - Valor: `sua_senha_super_secreta_aqui_123`

---

## 🚀 **CONFIGURAÇÃO DO CRON-JOB.ORG**

### **Passo 1 - Criar Conta (GRÁTIS)**

1. Acesse: https://cron-job.org
2. Clique em **Sign up**
3. Preencha e-mail e senha
4. Confirme e-mail

---

### **Passo 2 - Criar Cron Job**

1. Faça login em https://cron-job.org
2. Clique em **Create cronjob**

**Configurações:**

| Campo | Valor |
|-------|-------|
| **Title** | FinCtl - Backup Automático |
| **Address (URL)** | `https://davidbit.pythonanywhere.com/api/backup/create?token=finctl_backup_2025_secure` |
| **Schedule** | Every Sunday, 03:00 (UTC) |
| **Enabled** | ✅ Yes |
| **Save responses** | ✅ Yes (para ver logs) |

3. Clique em **Create**

---

### **Passo 3 - Testar Manualmente**

Antes de esperar o agendamento, teste:

1. Na lista de cron jobs, clique nos **3 pontinhos** ⋮
2. Selecione **Execute now**
3. Aguarde alguns segundos
4. Verifique **Execution history** (deve mostrar sucesso)

---

## 📊 **ESTRUTURA DE ARMAZENAMENTO**

```
PythonAnywhere
└── /home/davidbit/
    ├── FinCtl/
    │   └── data/
    │       └── financas.db  ← Banco em produção
    └── backups/
        ├── financas_backup_20251116_030000.db  ← Mais recente
        ├── financas_backup_20251109_030000.db
        ├── financas_backup_20251102_030000.db
        └── financas_backup_20251026_030000.db  ← Mais antigo (será deletado no próximo)
```

**Sistema mantém automaticamente as 4 últimas cópias (1 mês)**

---

## 🔄 **FLUXO AUTOMÁTICO**

```
┌─────────────────────────────────────┐
│  Domingo, 03:00 UTC (00:00 BRT)     │
│  cron-job.org acorda                │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│  HTTP GET Request                   │
│  /api/backup/create?token=...       │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│  Backend valida token               │
│  ✅ Token OK                        │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│  Executa: sqlite3 .backup           │
│  Cria: financas_backup_YYYYMMDD.db  │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│  Limpa backups antigos              │
│  Mantém apenas 4 últimos            │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│  Retorna JSON de sucesso            │
│  cron-job.org registra nos logs     │
└─────────────────────────────────────┘
```

---

## 📥 **COMO BAIXAR BACKUPS**

### **Opção 1 - Via Navegador (mais fácil):**

Acesse diretamente:
```
https://davidbit.pythonanywhere.com/api/backup/download/latest
```

Download automático do backup mais recente!

---

### **Opção 2 - Via cURL/PowerShell:**

```powershell
# PowerShell
Invoke-WebRequest -Uri "https://davidbit.pythonanywhere.com/api/backup/download/latest" -OutFile "backup_financas.db"
```

```bash
# Linux/Mac
curl -O https://davidbit.pythonanywhere.com/api/backup/download/latest
```

---

### **Opção 3 - Listar e escolher:**

1. Listar backups disponíveis:
```
https://davidbit.pythonanywhere.com/api/backup/list
```

2. Baixar específico:
```
https://davidbit.pythonanywhere.com/api/backup/download/financas_backup_20251110_030000.db
```

---

## 🛠️ **TROUBLESHOOTING**

### **Problema: Backup não está sendo criado**

**Verificar:**

1. **cron-job.org está executando?**
   - Acesse: https://cron-job.org → Execution history
   - Status deve ser: ✅ Success (200)

2. **Token está correto?**
   - Verifique URL no cron-job.org
   - Token deve ser: `finctl_backup_2025_secure`

3. **Endpoint está respondendo?**
   - Teste manual: abra URL no navegador
   - Deve retornar JSON de sucesso

---

### **Problema: Erro 401 (Não autorizado)**

**Causa:** Token inválido ou ausente

**Solução:**
- Verifique se URL tem `?token=finctl_backup_2025_secure`
- Se mudou token no servidor, atualize no cron-job.org

---

### **Problema: Erro 500 (Erro interno)**

**Causa:** Problema no servidor

**Solução:**
1. Acesse PythonAnywhere → Web → Error log
2. Verifique mensagem de erro
3. Possíveis causas:
   - Banco de dados em uso (raro)
   - Permissões de pasta
   - Espaço em disco cheio

---

## 📅 **FREQUÊNCIA RECOMENDADA**

| Tipo de Uso | Frequência | Manter |
|-------------|-----------|--------|
| **Pessoal** | Semanal (domingo) | 4 backups (1 mês) |
| **Produção leve** | 2x semana (dom, qua) | 8 backups (1 mês) |
| **Produção crítica** | Diário | 30 backups (1 mês) |

**Configuração atual:** Semanal, 4 backups

**Para mudar para diário:**
- cron-job.org: Schedule → Every day, 03:00
- Altere `manter=4` para `manter=30` no código

---

## 🔧 **MANUTENÇÃO**

### **Verificar Status (Mensal):**

1. Acesse: https://cron-job.org → Execution history
2. Confirme: últimos 4 domingos = ✅ Success
3. Teste download: `/api/backup/download/latest`

### **Restaurar Backup:**

1. Baixe backup desejado
2. No PythonAnywhere:
   ```bash
   # Backup do banco atual
   cp /home/davidbit/FinCtl/data/financas.db /home/davidbit/financas_before_restore.db
   
   # Restaurar backup
   cp /home/davidbit/backups/financas_backup_YYYYMMDD.db /home/davidbit/FinCtl/data/financas.db
   ```
3. Reload web app

---

## ✅ **CHECKLIST DE IMPLEMENTAÇÃO**

- [ ] Código do backend commitado
- [ ] Deploy no PythonAnywhere realizado
- [ ] Conta no cron-job.org criada
- [ ] Cron job configurado com URL correta
- [ ] Teste manual executado (Execute now)
- [ ] Primeiro backup criado com sucesso
- [ ] Download testado via navegador
- [ ] Documentação salva

---

## 📞 **SUPORTE**

**cron-job.org:**
- Docs: https://cron-job.org/en/documentation/
- Support: https://cron-job.org/en/support/

**PythonAnywhere:**
- Help: https://help.pythonanywhere.com/

---

**Sistema implementado e pronto para uso! 🎉**

**NFNSMA! 🫡**
