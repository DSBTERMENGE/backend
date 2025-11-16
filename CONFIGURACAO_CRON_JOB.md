# ⏰ CONFIGURAÇÃO RÁPIDA - CRON-JOB.ORG

## ✅ **VOCÊ JÁ SE CADASTROU!**

Agora falta apenas configurar o cron job para chamar seu backend automaticamente.

---

## 🚀 **PASSO A PASSO (5 minutos)**

### **1️⃣ Fazer Login**

1. Acesse: https://cron-job.org
2. Faça login com suas credenciais

---

### **2️⃣ Criar Novo Cron Job**

1. No painel principal, clique em: **"Create cronjob"**

---

### **3️⃣ Configurar o Cron Job**

Preencha os campos conforme abaixo:

#### **📋 CONFIGURAÇÕES ESSENCIAIS:**

| Campo | Valor |
|-------|-------|
| **Title** | `FinCtl - Backup Automático` |
| **Address (URL)** | `https://davidbit.pythonanywhere.com/api/backup/create?token=finctl_backup_2025_secure` |

#### **⏰ AGENDAMENTO:**

**Opção 1 - Semanal (Recomendado para começar):**
- Schedule type: **Every week**
- Day: **Sunday** (Domingo)
- Time: **03:00**
- Timezone: **UTC**

**Opção 2 - Diário (Para uso intenso):**
- Schedule type: **Every day**
- Time: **03:00**
- Timezone: **UTC**

#### **⚙️ OPÇÕES AVANÇADAS:**

| Campo | Valor |
|-------|-------|
| **Enabled** | ✅ **Yes** |
| **Save responses** | ✅ **Yes** (para ver logs) |
| **Notifications** | Email on failure (opcional) |

---

### **4️⃣ Salvar**

Clique em: **"Create"**

✅ Pronto! Cron job criado!

---

## 🧪 **TESTAR AGORA (Importante!)**

Não espere até domingo! Teste agora:

1. Na lista de cron jobs, encontre: **"FinCtl - Backup Automático"**
2. Clique nos **3 pontinhos** `⋮` no final da linha
3. Selecione: **"Execute now"**
4. Aguarde 5-10 segundos
5. Atualize a página

---

### **📊 Verificar Resultado:**

1. Clique no nome do cron job: **"FinCtl - Backup Automático"**
2. Vá em: **"Execution history"**
3. Deve mostrar:
   ```
   ✅ Success
   Status Code: 200
   Response: {"success": true, "arquivo": "financas_backup_20251116_HHMMSS.db", ...}
   ```

**Se aparecer isso = FUNCIONOU! 🎉**

---

## ❌ **TROUBLESHOOTING**

### **Erro 401 - Unauthorized:**

**Problema:** Token inválido

**Solução:**
- Verifique se URL tem exatamente: `?token=finctl_backup_2025_secure`
- Copie e cole novamente a URL completa

---

### **Erro 500 - Internal Server Error:**

**Problema:** Erro no backend

**Solução:**
1. Verifique se fez deploy no PythonAnywhere
2. Acesse PythonAnywhere → Web → Error log
3. Veja a mensagem de erro específica

---

### **Erro de Timeout:**

**Problema:** Backend não responde

**Solução:**
- Verifique se web app está rodando no PythonAnywhere
- Teste URL manualmente no navegador

---

## 📥 **VERIFICAR BACKUPS CRIADOS**

### **Via Navegador:**

Acesse:
```
https://davidbit.pythonanywhere.com/api/backup/list
```

Deve retornar JSON com lista de backups:
```json
{
  "success": true,
  "total": 1,
  "backups": [
    {
      "nome": "financas_backup_20251116_030000.db",
      "tamanho_kb": 94.5,
      "data_criacao": "2025-11-16T03:00:00"
    }
  ]
}
```

---

### **Baixar Backup:**

Acesse diretamente:
```
https://davidbit.pythonanywhere.com/api/backup/download/latest
```

Download automático! 📥

---

## 📅 **MONITORAMENTO**

### **Verificar Execuções (Recomendado Mensal):**

1. Login no cron-job.org
2. Click no cron job
3. Veja "Execution history"
4. Confirme que está rodando todo domingo ✅

---

### **Notificações por E-mail (Opcional):**

Para ser avisado se der erro:

1. Edite o cron job
2. Em "Notifications"
3. Marque: **"Send email on failure"**
4. Salvar

Você receberá e-mail apenas se falhar!

---

## 🎯 **PRÓXIMA EXECUÇÃO**

Após configurar, o próximo backup será:

**Domingo, 03:00 UTC (00:00 BRT)**

Ou seja, domingo de madrugada (horário de Brasília).

---

## 🔄 **MUDAR HORÁRIO**

Para alterar o horário:

1. Edite o cron job
2. Mude "Time" para o horário desejado (UTC)
3. **Lembre:** UTC tem 3h de diferença do BRT
   - 03:00 UTC = 00:00 BRT (meia-noite)
   - 06:00 UTC = 03:00 BRT (madrugada)
   - 12:00 UTC = 09:00 BRT (manhã)

---

## ✅ **CHECKLIST DE CONFIGURAÇÃO**

- [ ] Login no cron-job.org realizado
- [ ] Cron job criado com URL correta
- [ ] Teste manual executado ("Execute now")
- [ ] Execution history mostra "Success (200)"
- [ ] Backup listado em `/api/backup/list`
- [ ] Download testado via `/api/backup/download/latest`
- [ ] Agendamento configurado (domingo 03:00 UTC)

**Tudo OK? Sistema funcionando! 🎉**

---

## 📞 **SUPORTE**

**Dúvidas sobre cron-job.org:**
- Documentação: https://cron-job.org/en/documentation/
- FAQ: https://cron-job.org/en/faq/
- Support: https://cron-job.org/en/support/

---

**Sistema pronto! Backup automático configurado! 🚀**

**NFNSMA! 🫡**
