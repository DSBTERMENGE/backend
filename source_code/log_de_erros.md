**[11:37:54]** === LOG TRUNCADO ===

**[11:37:54]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[11:37:54]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[11:37:54]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[11:37:54]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM receitas_mensais...

**[11:37:54]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[11:37:54]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[11:38:38]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[11:38:38]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[11:38:38]** 🔄 **FLOW:** Consultando view: rec_mensal_report com campos: ['Todos']

**[11:38:38]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[11:38:38]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 2}
```

**[11:38:38]** 🔄 **FLOW:** Consulta executada - View: rec_mensal_report, Registros: 4

**[11:38:38]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[11:38:38]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Idreceita': 2, 'Descrição': 'Aluguel Apto DC', '(R$)Valor': '1.375,00', 'Recebto': '25/10/2025', 'Observação': 'Dep. no SantanderNN'}, {'Idreceita': 1, 'Descrição': 'INSS', '(R$)Valor': '3.105.00', 'Recebto': '03/10/2025', 'Observação': 'Pensao do INSS'}], 'erro': None, 'sucesso': True, 'total_registros': 2}, 'mensagem': 'sucesso'}

**[11:38:38]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[11:38:38]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[11:38:38]** 🔄 **FLOW:** Consultando view: rec_mensal_report com campos: ['Todos']

**[11:38:38]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[11:38:38]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 2}
```

**[11:38:38]** 🔄 **FLOW:** Consulta executada - View: rec_mensal_report, Registros: 4

**[11:38:38]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[11:38:38]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Idreceita': 2, 'Descrição': 'Aluguel Apto DC', '(R$)Valor': '1.375,00', 'Recebto': '25/10/2025', 'Observação': 'Dep. no SantanderNN'}, {'Idreceita': 1, 'Descrição': 'INSS', '(R$)Valor': '3.105.00', 'Recebto': '03/10/2025', 'Observação': 'Pensao do INSS'}], 'erro': None, 'sucesso': True, 'total_registros': 2}, 'mensagem': 'sucesso'}

**[11:38:38]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[11:38:38]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM desp_mensal...

**[11:38:38]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[11:38:38]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[11:38:38]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[11:38:38]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM desp_mensal WHERE pagamento = "S"...

**[11:38:38]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[11:38:38]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[11:38:38]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[11:38:38]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM receitas_mensais...

**[11:38:38]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[11:38:38]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[11:38:39]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[11:38:39]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM desp_mensal...

**[11:38:39]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[11:38:39]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[11:38:39]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[11:38:39]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM receitas_mensais...

**[11:38:39]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[11:38:39]** 🔄 **FLOW:** ✅ SQL executado com sucesso

