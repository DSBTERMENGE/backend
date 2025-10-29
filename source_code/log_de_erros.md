*****************************
SISTEMA DE LOG DE ERROS
SEÇÃO INICIADA EM 29/10/2025 às 15:14:22
*****************************

*****************************
SISTEMA DE LOG DE ERROS
SEÇÃO INICIADA EM 29/10/2025 às 15:14:22
*****************************

**[15:14:57]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[15:14:57]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[15:14:57]** 🔄 **FLOW:** Consultando view: rec_mensal_report com campos: ['Todos']

**[15:14:57]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[15:14:57]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 2}
```

**[15:14:57]** 🔄 **FLOW:** Consulta executada - View: rec_mensal_report, Registros: 4

**[15:14:57]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[15:14:57]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Idreceita': 2, 'Descrição': 'Aluguel Apto DC', '(R$)Valor': '1.375,00', 'Recebto': '25/10/2025', 'Observação': 'Dep. no SantanderNN'}, {'Idreceita': 1, 'Descrição': 'INSS', '(R$)Valor': '3.105.00', 'Recebto': '03/10/2025', 'Observação': 'Pensao do INSS'}], 'erro': None, 'sucesso': True, 'total_registros': 2}, 'mensagem': 'sucesso'}

**[15:14:57]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[15:14:57]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[15:14:57]** 🔄 **FLOW:** Consultando view: rec_mensal_report com campos: ['Todos']

**[15:14:57]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[15:14:57]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 2}
```

**[15:14:57]** 🔄 **FLOW:** Consulta executada - View: rec_mensal_report, Registros: 4

**[15:14:57]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[15:14:57]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Idreceita': 2, 'Descrição': 'Aluguel Apto DC', '(R$)Valor': '1.375,00', 'Recebto': '25/10/2025', 'Observação': 'Dep. no SantanderNN'}, {'Idreceita': 1, 'Descrição': 'INSS', '(R$)Valor': '3.105.00', 'Recebto': '03/10/2025', 'Observação': 'Pensao do INSS'}], 'erro': None, 'sucesso': True, 'total_registros': 2}, 'mensagem': 'sucesso'}

**[15:14:57]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[15:14:57]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM desp_mensal...

**[15:14:57]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[15:14:57]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[15:14:57]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[15:14:57]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM desp_mensal WHERE pagamento = "S"...

**[15:14:57]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[15:14:57]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[15:14:57]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[15:14:57]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM receitas_mensais...

**[15:14:57]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[15:14:57]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[15:14:57]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[15:14:57]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM desp_mensal...

**[15:14:57]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[15:14:57]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[15:14:58]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[15:14:58]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM receitas_mensais...

**[15:14:58]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[15:14:58]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[15:24:31]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[15:24:31]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[15:24:31]** 🔄 **FLOW:** Consultando view: rec_mensal_report com campos: ['Todos']

**[15:24:31]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[15:24:31]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 2}
```

**[15:24:31]** 🔄 **FLOW:** Consulta executada - View: rec_mensal_report, Registros: 4

**[15:24:31]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[15:24:31]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Idreceita': 2, 'Descrição': 'Aluguel Apto DC', '(R$)Valor': '1.375,00', 'Recebto': '25/10/2025', 'Observação': 'Dep. no SantanderNN'}, {'Idreceita': 1, 'Descrição': 'INSS', '(R$)Valor': '3.105.00', 'Recebto': '03/10/2025', 'Observação': 'Pensao do INSS'}], 'erro': None, 'sucesso': True, 'total_registros': 2}, 'mensagem': 'sucesso'}

**[15:34:34]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[15:34:35]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[15:34:35]** 🔄 **FLOW:** Consultando view: rec_mensal_report com campos: ['Todos']

**[15:34:35]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[15:34:35]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 2}
```

**[15:34:35]** 🔄 **FLOW:** Consulta executada - View: rec_mensal_report, Registros: 4

**[15:34:35]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[15:34:35]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Idreceita': 2, 'Descrição': 'Aluguel Apto DC', '(R$)Valor': '1.375,00', 'Recebto': '25/10/2025', 'Observação': 'Dep. no SantanderNN'}, {'Idreceita': 1, 'Descrição': 'INSS', '(R$)Valor': '3.105.00', 'Recebto': '03/10/2025', 'Observação': 'Pensao do INSS'}], 'erro': None, 'sucesso': True, 'total_registros': 2}, 'mensagem': 'sucesso'}

**[15:35:52]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[15:35:52]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM desp_mensal...

**[15:35:52]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[15:35:52]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[15:36:09]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[15:36:09]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM desp_mensal WHERE pagamento = "S"...

**[15:36:09]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[15:36:09]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[15:36:09]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[15:36:09]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM receitas_mensais...

**[15:36:09]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[15:36:09]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[15:37:27]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[15:37:27]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM desp_mensal...

**[15:37:27]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[15:37:27]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[15:47:19]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[15:47:19]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM receitas_mensais...

**[15:47:19]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[15:47:19]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[15:57:53]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[15:57:53]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[15:57:53]** 🔄 **FLOW:** Consultando view: rec_mensal_report com campos: ['Todos']

**[15:57:53]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[15:57:53]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 2}
```

**[15:57:53]** 🔄 **FLOW:** Consulta executada - View: rec_mensal_report, Registros: 4

**[15:57:53]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[15:57:53]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Idreceita': 2, 'Descrição': 'Aluguel Apto DC', '(R$)Valor': '1.375,00', 'Recebto': '25/10/2025', 'Observação': 'Dep. no SantanderNN'}, {'Idreceita': 1, 'Descrição': 'INSS', '(R$)Valor': '3.105.00', 'Recebto': '03/10/2025', 'Observação': 'Pensao do INSS'}], 'erro': None, 'sucesso': True, 'total_registros': 2}, 'mensagem': 'sucesso'}

**[15:57:53]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[15:57:53]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[15:57:53]** 🔄 **FLOW:** Consultando view: rec_mensal_report com campos: ['Todos']

**[15:57:53]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[15:57:53]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 2}
```

**[15:57:53]** 🔄 **FLOW:** Consulta executada - View: rec_mensal_report, Registros: 4

**[15:57:53]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[15:57:53]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Idreceita': 2, 'Descrição': 'Aluguel Apto DC', '(R$)Valor': '1.375,00', 'Recebto': '25/10/2025', 'Observação': 'Dep. no SantanderNN'}, {'Idreceita': 1, 'Descrição': 'INSS', '(R$)Valor': '3.105.00', 'Recebto': '03/10/2025', 'Observação': 'Pensao do INSS'}], 'erro': None, 'sucesso': True, 'total_registros': 2}, 'mensagem': 'sucesso'}

**[15:57:54]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[15:57:54]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM desp_mensal...

**[15:57:54]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[15:57:54]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[15:57:54]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[15:57:54]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM desp_mensal WHERE pagamento = "S"...

**[15:57:54]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[15:57:54]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[15:57:54]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[15:57:54]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM receitas_mensais...

**[15:57:54]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[15:57:54]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[15:57:54]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[15:57:54]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM desp_mensal...

**[15:57:54]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[15:57:54]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[15:57:54]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[15:57:54]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM receitas_mensais...

**[15:57:54]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[15:57:54]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[15:58:55]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[15:58:55]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[15:58:55]** 🔄 **FLOW:** Consultando view: rec_mensal_report com campos: ['Todos']

**[15:58:55]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[15:58:55]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 2}
```

**[15:58:55]** 🔄 **FLOW:** Consulta executada - View: rec_mensal_report, Registros: 4

**[15:58:55]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[15:58:55]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Idreceita': 2, 'Descrição': 'Aluguel Apto DC', '(R$)Valor': '1.375,00', 'Recebto': '25/10/2025', 'Observação': 'Dep. no SantanderNN'}, {'Idreceita': 1, 'Descrição': 'INSS', '(R$)Valor': '3.105.00', 'Recebto': '03/10/2025', 'Observação': 'Pensao do INSS'}], 'erro': None, 'sucesso': True, 'total_registros': 2}, 'mensagem': 'sucesso'}

**[15:58:55]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[15:58:55]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[15:58:55]** 🔄 **FLOW:** Consultando view: rec_mensal_report com campos: ['Todos']

**[15:58:55]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[15:58:55]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 2}
```

**[15:58:55]** 🔄 **FLOW:** Consulta executada - View: rec_mensal_report, Registros: 4

**[15:58:55]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[15:58:55]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Idreceita': 2, 'Descrição': 'Aluguel Apto DC', '(R$)Valor': '1.375,00', 'Recebto': '25/10/2025', 'Observação': 'Dep. no SantanderNN'}, {'Idreceita': 1, 'Descrição': 'INSS', '(R$)Valor': '3.105.00', 'Recebto': '03/10/2025', 'Observação': 'Pensao do INSS'}], 'erro': None, 'sucesso': True, 'total_registros': 2}, 'mensagem': 'sucesso'}

**[15:58:55]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[15:58:55]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM desp_mensal...

**[15:58:55]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[15:58:55]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[15:58:55]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[15:58:55]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM desp_mensal WHERE pagamento = "S"...

**[15:58:55]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[15:58:55]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[15:58:56]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[15:58:56]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM receitas_mensais...

**[15:58:56]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[15:58:56]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[15:58:56]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[15:58:56]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM desp_mensal...

**[15:58:56]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[15:58:56]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[15:58:56]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[15:58:56]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM receitas_mensais...

**[15:58:56]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[15:58:56]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[15:59:53]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[15:59:53]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[15:59:53]** 🔄 **FLOW:** Consultando view: rec_mensal_report com campos: ['Todos']

**[15:59:53]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[15:59:53]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 2}
```

**[15:59:53]** 🔄 **FLOW:** Consulta executada - View: rec_mensal_report, Registros: 4

**[15:59:53]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[15:59:53]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Idreceita': 2, 'Descrição': 'Aluguel Apto DC', '(R$)Valor': '1.375,00', 'Recebto': '25/10/2025', 'Observação': 'Dep. no SantanderNN'}, {'Idreceita': 1, 'Descrição': 'INSS', '(R$)Valor': '3.105.00', 'Recebto': '03/10/2025', 'Observação': 'Pensao do INSS'}], 'erro': None, 'sucesso': True, 'total_registros': 2}, 'mensagem': 'sucesso'}

**[15:59:54]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[15:59:54]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[15:59:54]** 🔄 **FLOW:** Consultando view: rec_mensal_report com campos: ['Todos']

**[15:59:54]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[15:59:54]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 2}
```

**[15:59:54]** 🔄 **FLOW:** Consulta executada - View: rec_mensal_report, Registros: 4

**[15:59:54]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[15:59:54]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Idreceita': 2, 'Descrição': 'Aluguel Apto DC', '(R$)Valor': '1.375,00', 'Recebto': '25/10/2025', 'Observação': 'Dep. no SantanderNN'}, {'Idreceita': 1, 'Descrição': 'INSS', '(R$)Valor': '3.105.00', 'Recebto': '03/10/2025', 'Observação': 'Pensao do INSS'}], 'erro': None, 'sucesso': True, 'total_registros': 2}, 'mensagem': 'sucesso'}

**[15:59:54]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[15:59:54]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM desp_mensal...

**[15:59:54]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[15:59:54]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[15:59:54]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[15:59:54]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM desp_mensal WHERE pagamento = "S"...

**[15:59:54]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[15:59:54]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[15:59:54]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[15:59:54]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM receitas_mensais...

**[15:59:54]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[15:59:54]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[15:59:54]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[15:59:54]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM desp_mensal...

**[15:59:54]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[15:59:54]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[15:59:54]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[15:59:54]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM receitas_mensais...

**[15:59:54]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[15:59:54]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[16:00:50]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[16:00:50]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[16:00:50]** 🔄 **FLOW:** Consultando view: rec_mensal_report com campos: ['Todos']

**[16:00:50]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[16:00:50]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 2}
```

**[16:00:50]** 🔄 **FLOW:** Consulta executada - View: rec_mensal_report, Registros: 4

**[16:00:50]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[16:00:50]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Idreceita': 2, 'Descrição': 'Aluguel Apto DC', '(R$)Valor': '1.375,00', 'Recebto': '25/10/2025', 'Observação': 'Dep. no SantanderNN'}, {'Idreceita': 1, 'Descrição': 'INSS', '(R$)Valor': '3.105.00', 'Recebto': '03/10/2025', 'Observação': 'Pensao do INSS'}], 'erro': None, 'sucesso': True, 'total_registros': 2}, 'mensagem': 'sucesso'}

**[16:00:51]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[16:00:51]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[16:00:51]** 🔄 **FLOW:** Consultando view: rec_mensal_report com campos: ['Todos']

**[16:00:51]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[16:00:51]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 2}
```

**[16:00:51]** 🔄 **FLOW:** Consulta executada - View: rec_mensal_report, Registros: 4

**[16:00:51]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[16:00:51]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Idreceita': 2, 'Descrição': 'Aluguel Apto DC', '(R$)Valor': '1.375,00', 'Recebto': '25/10/2025', 'Observação': 'Dep. no SantanderNN'}, {'Idreceita': 1, 'Descrição': 'INSS', '(R$)Valor': '3.105.00', 'Recebto': '03/10/2025', 'Observação': 'Pensao do INSS'}], 'erro': None, 'sucesso': True, 'total_registros': 2}, 'mensagem': 'sucesso'}

**[16:00:51]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[16:00:51]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM desp_mensal...

**[16:00:51]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[16:00:51]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[16:00:51]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[16:00:51]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM desp_mensal WHERE pagamento = "S"...

**[16:00:51]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[16:00:51]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[16:00:51]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[16:00:51]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM receitas_mensais...

**[16:00:51]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[16:00:51]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[16:00:51]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[16:00:51]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM desp_mensal...

**[16:00:51]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[16:00:51]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[16:00:52]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[16:00:52]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM receitas_mensais...

**[16:00:52]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[16:00:52]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[16:37:56]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[16:37:56]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[16:37:56]** 🔄 **FLOW:** Consultando view: rec_mensal_report com campos: ['Todos']

**[16:37:56]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[16:37:56]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 2}
```

**[16:37:56]** 🔄 **FLOW:** Consulta executada - View: rec_mensal_report, Registros: 4

**[16:37:56]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[16:37:56]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Idreceita': 2, 'Descrição': 'Aluguel Apto DC', '(R$)Valor': '1.375,00', 'Recebto': '25/10/2025', 'Observação': 'Dep. no SantanderNN'}, {'Idreceita': 1, 'Descrição': 'INSS', '(R$)Valor': '3.105.00', 'Recebto': '03/10/2025', 'Observação': 'Pensao do INSS'}], 'erro': None, 'sucesso': True, 'total_registros': 2}, 'mensagem': 'sucesso'}

**[16:37:56]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[16:37:56]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[16:37:56]** 🔄 **FLOW:** Consultando view: rec_mensal_report com campos: ['Todos']

**[16:37:56]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[16:37:56]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 2}
```

**[16:37:56]** 🔄 **FLOW:** Consulta executada - View: rec_mensal_report, Registros: 4

**[16:37:56]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[16:37:56]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Idreceita': 2, 'Descrição': 'Aluguel Apto DC', '(R$)Valor': '1.375,00', 'Recebto': '25/10/2025', 'Observação': 'Dep. no SantanderNN'}, {'Idreceita': 1, 'Descrição': 'INSS', '(R$)Valor': '3.105.00', 'Recebto': '03/10/2025', 'Observação': 'Pensao do INSS'}], 'erro': None, 'sucesso': True, 'total_registros': 2}, 'mensagem': 'sucesso'}

**[16:37:57]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[16:37:57]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM desp_mensal...

**[16:37:57]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[16:37:57]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[16:37:57]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[16:37:57]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM desp_mensal WHERE pagamento = "S"...

**[16:37:57]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[16:37:57]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[16:37:57]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[16:37:57]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM receitas_mensais...

**[16:37:57]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[16:37:57]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[16:37:57]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[16:37:57]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM desp_mensal...

**[16:37:57]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[16:37:57]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[16:37:57]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[16:37:57]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM receitas_mensais...

**[16:37:57]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[16:37:57]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[16:38:31]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[16:38:31]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[16:38:31]** 🔄 **FLOW:** Consultando view: rec_mensal_report com campos: ['Todos']

**[16:38:31]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[16:38:31]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 2}
```

**[16:38:31]** 🔄 **FLOW:** Consulta executada - View: rec_mensal_report, Registros: 4

**[16:38:31]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[16:38:32]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Idreceita': 2, 'Descrição': 'Aluguel Apto DC', '(R$)Valor': '1.375,00', 'Recebto': '25/10/2025', 'Observação': 'Dep. no SantanderNN'}, {'Idreceita': 1, 'Descrição': 'INSS', '(R$)Valor': '3.105.00', 'Recebto': '03/10/2025', 'Observação': 'Pensao do INSS'}], 'erro': None, 'sucesso': True, 'total_registros': 2}, 'mensagem': 'sucesso'}

**[16:38:32]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[16:38:32]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[16:38:32]** 🔄 **FLOW:** Consultando view: rec_mensal_report com campos: ['Todos']

**[16:38:32]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[16:38:32]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 2}
```

**[16:38:32]** 🔄 **FLOW:** Consulta executada - View: rec_mensal_report, Registros: 4

**[16:38:32]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[16:38:32]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Idreceita': 2, 'Descrição': 'Aluguel Apto DC', '(R$)Valor': '1.375,00', 'Recebto': '25/10/2025', 'Observação': 'Dep. no SantanderNN'}, {'Idreceita': 1, 'Descrição': 'INSS', '(R$)Valor': '3.105.00', 'Recebto': '03/10/2025', 'Observação': 'Pensao do INSS'}], 'erro': None, 'sucesso': True, 'total_registros': 2}, 'mensagem': 'sucesso'}

**[16:38:32]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[16:38:32]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM desp_mensal...

**[16:38:32]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[16:38:32]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[16:38:32]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[16:38:32]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM desp_mensal WHERE pagamento = "S"...

**[16:38:32]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[16:38:32]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[16:38:32]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[16:38:32]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM receitas_mensais...

**[16:38:32]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[16:38:32]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[16:38:32]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[16:38:32]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM desp_mensal...

**[16:38:32]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[16:38:32]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[16:38:33]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[16:38:33]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM receitas_mensais...

**[16:38:33]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[16:38:33]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[18:45:14]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[18:45:14]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[18:45:14]** 🔄 **FLOW:** Consultando view: rec_mensal_report com campos: ['Todos']

**[18:45:14]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[18:45:14]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 2}
```

**[18:45:14]** 🔄 **FLOW:** Consulta executada - View: rec_mensal_report, Registros: 4

**[18:45:14]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[18:45:14]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Idreceita': 2, 'Descrição': 'Aluguel Apto DC', '(R$)Valor': '1.375,00', 'Recebto': '25/10/2025', 'Observação': 'Dep. no SantanderNN'}, {'Idreceita': 1, 'Descrição': 'INSS', '(R$)Valor': '3.105.00', 'Recebto': '03/10/2025', 'Observação': 'Pensao do INSS'}], 'erro': None, 'sucesso': True, 'total_registros': 2}, 'mensagem': 'sucesso'}

**[18:45:14]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[18:45:14]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[18:45:14]** 🔄 **FLOW:** Consultando view: rec_mensal_report com campos: ['Todos']

**[18:45:14]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[18:45:14]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 2}
```

**[18:45:14]** 🔄 **FLOW:** Consulta executada - View: rec_mensal_report, Registros: 4

**[18:45:14]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[18:45:14]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Idreceita': 2, 'Descrição': 'Aluguel Apto DC', '(R$)Valor': '1.375,00', 'Recebto': '25/10/2025', 'Observação': 'Dep. no SantanderNN'}, {'Idreceita': 1, 'Descrição': 'INSS', '(R$)Valor': '3.105.00', 'Recebto': '03/10/2025', 'Observação': 'Pensao do INSS'}], 'erro': None, 'sucesso': True, 'total_registros': 2}, 'mensagem': 'sucesso'}

**[18:45:14]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[18:45:14]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM desp_mensal...

**[18:45:14]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[18:45:14]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[18:45:14]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[18:45:14]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM desp_mensal WHERE pagamento = "S"...

**[18:45:14]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[18:45:14]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[18:45:15]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[18:45:15]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM receitas_mensais...

**[18:45:15]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[18:45:15]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[18:45:15]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[18:45:15]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM desp_mensal...

**[18:45:15]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[18:45:15]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[18:45:15]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[18:45:15]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM receitas_mensais...

**[18:45:15]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[18:45:15]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[18:54:40]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[18:54:40]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[18:54:40]** 🔄 **FLOW:** Consultando view: rec_mensal_report com campos: ['Todos']

**[18:54:40]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[18:54:40]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 2}
```

**[18:54:40]** 🔄 **FLOW:** Consulta executada - View: rec_mensal_report, Registros: 4

**[18:54:40]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[18:54:40]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Idreceita': 2, 'Descrição': 'Aluguel Apto DC', '(R$)Valor': '1.375,00', 'Recebto': '25/10/2025', 'Observação': 'Dep. no SantanderNN'}, {'Idreceita': 1, 'Descrição': 'INSS', '(R$)Valor': '3.105.00', 'Recebto': '03/10/2025', 'Observação': 'Pensao do INSS'}], 'erro': None, 'sucesso': True, 'total_registros': 2}, 'mensagem': 'sucesso'}

**[18:54:40]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[18:54:40]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[18:54:40]** 🔄 **FLOW:** Consultando view: rec_mensal_report com campos: ['Todos']

**[18:54:40]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[18:54:40]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 2}
```

**[18:54:40]** 🔄 **FLOW:** Consulta executada - View: rec_mensal_report, Registros: 4

**[18:54:40]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[18:54:40]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Idreceita': 2, 'Descrição': 'Aluguel Apto DC', '(R$)Valor': '1.375,00', 'Recebto': '25/10/2025', 'Observação': 'Dep. no SantanderNN'}, {'Idreceita': 1, 'Descrição': 'INSS', '(R$)Valor': '3.105.00', 'Recebto': '03/10/2025', 'Observação': 'Pensao do INSS'}], 'erro': None, 'sucesso': True, 'total_registros': 2}, 'mensagem': 'sucesso'}

**[18:54:41]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[18:54:41]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM desp_mensal...

**[18:54:41]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[18:54:41]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[18:54:41]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[18:54:41]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM desp_mensal WHERE pagamento = "S"...

**[18:54:41]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[18:54:41]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[18:54:41]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[18:54:41]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM receitas_mensais...

**[18:54:41]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[18:54:41]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[18:54:41]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[18:54:41]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM desp_mensal...

**[18:54:41]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[18:54:41]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[18:54:41]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[18:54:41]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM receitas_mensais...

**[18:54:41]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[18:54:41]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[19:13:43]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[19:13:43]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[19:13:43]** 🔄 **FLOW:** Consultando view: desp_mensal_report com campos: ['Todos']

**[19:13:43]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[19:13:43]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 12}
```

**[19:13:43]** 🔄 **FLOW:** Consulta executada - View: desp_mensal_report, Registros: 4

**[19:13:43]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[19:13:43]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Descrição': 'Aluguel do Apto de Ipanema', '(R$)Valor': '3.125,00', 'Vencimento': '05/10/20025', 'Pago': 'N', 'Observação': 'Se pagar atrasado tem juros'}, {'Descrição': 'Caroline Buterine', '(R$)Valor': '500,00', 'Vencimento': '05/10/20025', 'Pago': 'N', 'Observação': 'Pgto mensal Clinica Buterine'}, {'Descrição': 'Conta de Gás - Naturgy', '(R$)Valor': '65,00', 'Vencimento': '10/10/2025', 'Pago': 'N', 'Observação': ''}, {'Descrição': 'Limpeza do apto', '(R$)Valor': '340,00', 'Vencimento': '25/10/2025', 'Pago': 'N', 'Observação': 'Incluso UBER estimado R$ 140,00'}, {'Descrição': 'Pagamento Cartão MASTERCARD', '(R$)Valor': '3.200,00', 'Vencimento': '26/10/2025', 'Pago': 'N', 'Observação': 'Vencimento em todo di 26 do mes'}, {'Descrição': 'Pagamento Cartão VISA', '(R$)Valor': '1.700,00', 'Vencimento': '16/10/2025', 'Pago': 'N', 'Observação': ''}, {'Descrição': 'Pagto Lucinha - INSS', '(R$)Valor': '800,00', 'Vencimento': '15/10/2025', 'Pago': 'N', 'Observação': 'Vl. mensal '}, {'Descrição': 'Pgto Conta de Luz Ap. Ipa', '(R$)Valor': '95,00', 'Vencimento': '08/10/2025', 'Pago': 'N', 'Observação': 'Conta Light'}, {'Descrição': 'Pgto Curso MBA', '(R$)Valor': '370,00', 'Vencimento': '10/10/2025', 'Pago': 'N', 'Observação': 'MBA Mercado de Capitais - UCB'}, {'Descrição': 'Pgto Lucinha - POLICON', '(R$)Valor': '228,00', 'Vencimento': '10/10/20025', 'Pago': 'N', 'Observação': '2 planos'}, {'Descrição': 'Pgto cta VIVO', '(R$)Valor': '331,00', 'Vencimento': '10/10/2025', 'Pago': 'N', 'Observação': ''}, {'Descrição': 'Prevent Senior', '(R$)Valor': '1.350,00', 'Vencimento': '30/10/2025', 'Pago': 'N', 'Observação': 'Plano Prevent'}], 'erro': None, 'sucesso': True, 'total_registros': 12}, 'mensagem': 'sucesso'}

**[19:13:43]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[19:13:43]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[19:13:43]** 🔄 **FLOW:** Consultando view: rec_mensal_report com campos: ['Todos']

**[19:13:43]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[19:13:43]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 2}
```

**[19:13:43]** 🔄 **FLOW:** Consulta executada - View: rec_mensal_report, Registros: 4

**[19:13:43]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[19:13:43]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Idreceita': 2, 'Descrição': 'Aluguel Apto DC', '(R$)Valor': '1.375,00', 'Recebto': '25/10/2025', 'Observação': 'Dep. no SantanderNN'}, {'Idreceita': 1, 'Descrição': 'INSS', '(R$)Valor': '3.105.00', 'Recebto': '03/10/2025', 'Observação': 'Pensao do INSS'}], 'erro': None, 'sucesso': True, 'total_registros': 2}, 'mensagem': 'sucesso'}

**[19:13:43]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[19:13:43]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM desp_mensal...

**[19:13:43]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[19:13:43]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[19:13:43]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[19:13:43]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM desp_mensal WHERE pagamento = "S"...

**[19:13:43]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[19:13:43]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[19:13:44]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[19:13:44]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM receitas_mensais...

**[19:13:44]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[19:13:44]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[19:13:44]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[19:13:44]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM desp_mensal...

**[19:13:44]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[19:13:44]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[19:13:44]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[19:13:44]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM receitas_mensais...

**[19:13:44]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[19:13:44]** 🔄 **FLOW:** ✅ SQL executado com sucesso

