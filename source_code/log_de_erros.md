*****************************
SISTEMA DE LOG DE ERROS
SEÇÃO INICIADA EM 05/11/2025 às 09:29:05
*****************************

*****************************
SISTEMA DE LOG DE ERROS
SEÇÃO INICIADA EM 05/11/2025 às 09:29:05
*****************************

**[09:29:41]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[09:29:41]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[09:29:41]** 🔄 **FLOW:** Consultando view: desp_mensal_report com campos: ['Todos']

**[09:29:41]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[09:29:41]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 12}
```

**[09:29:41]** 🔄 **FLOW:** Consulta executada - View: desp_mensal_report, Registros: 4

**[09:29:41]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[09:29:41]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Descrição': 'Aluguel do Apto de Ipanema', '(R$)Valor': '3.125,00', 'Vencimento': '05/10/20025', 'Pago': 'S', 'Observação': 'Se pagar atrasado tem juros'}, {'Descrição': 'Caroline Buterine', '(R$)Valor': '250,00', 'Vencimento': '05/10/20025', 'Pago': 'S', 'Observação': 'Pgto mensal Clinica Buterine'}, {'Descrição': 'Conta de Gás - Naturgy', '(R$)Valor': '65,00', 'Vencimento': '10/10/2025', 'Pago': 'N', 'Observação': ''}, {'Descrição': 'Limpeza do apto', '(R$)Valor': '340,00', 'Vencimento': '25/10/2025', 'Pago': 'N', 'Observação': 'Incluso UBER estimado R$ 140,00'}, {'Descrição': 'Pagamento Cartão MASTERCARD', '(R$)Valor': '3.200,00', 'Vencimento': '26/10/2025', 'Pago': 'N', 'Observação': 'Vencimento em todo di 26 do mes'}, {'Descrição': 'Pagamento Cartão VISA', '(R$)Valor': '1.700,00', 'Vencimento': '16/10/2025', 'Pago': 'N', 'Observação': ''}, {'Descrição': 'Pagto Lucinha - INSS', '(R$)Valor': '800,00', 'Vencimento': '15/10/2025', 'Pago': 'S', 'Observação': 'Vl. mensal '}, {'Descrição': 'Pgto Conta de Luz Ap. Ipa', '(R$)Valor': '95,00', 'Vencimento': '08/10/2025', 'Pago': 'N', 'Observação': 'Conta Light'}, {'Descrição': 'Pgto Curso MBA', '(R$)Valor': '370,00', 'Vencimento': '10/10/2025', 'Pago': 'N', 'Observação': 'MBA Mercado de Capitais - UCB'}, {'Descrição': 'Pgto Lucinha - POLICON', '(R$)Valor': '228,00', 'Vencimento': '10/10/20025', 'Pago': 'N', 'Observação': '2 planos'}, {'Descrição': 'Pgto cta VIVO', '(R$)Valor': '331,00', 'Vencimento': '10/10/2025', 'Pago': 'N', 'Observação': ''}, {'Descrição': 'Prevent Senior', '(R$)Valor': '1.350,00', 'Vencimento': '30/10/2025', 'Pago': 'N', 'Observação': 'Plano Prevent'}], 'erro': None, 'sucesso': True, 'total_registros': 12}, 'mensagem': 'sucesso'}

**[09:29:42]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[09:29:42]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[09:29:42]** 🔄 **FLOW:** Consultando view: rec_mensal_report com campos: ['Todos']

**[09:29:42]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[09:29:42]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 2}
```

**[09:29:42]** 🔄 **FLOW:** Consulta executada - View: rec_mensal_report, Registros: 4

**[09:29:42]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[09:29:42]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Idreceita': 2, 'Descrição': 'Aluguel Apto DC', '(R$)Valor': '1.375,00', 'Recebto': '25/10/2025', 'Observação': 'Dep. no SantanderNN'}, {'Idreceita': 1, 'Descrição': 'INSS', '(R$)Valor': '3.125,00', 'Recebto': '03/10/2025', 'Observação': 'Pensao do INSS'}], 'erro': None, 'sucesso': True, 'total_registros': 2}, 'mensagem': 'sucesso'}

**[09:29:42]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[09:29:42]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(CAST(REPLACE(valor, ",", ".") AS REAL)) as total FROM desp_mensal...

**[09:29:42]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[09:29:42]** 🔄 **FLOW:** 📊 RESULTADO da query SQL: {'sucesso': True, 'dados': [{'total': 2488.375}], 'mensagem': 'Consulta executada com sucesso. 1 registro(s) encontrado(s).'}

**[09:29:42]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[09:29:42]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[09:29:42]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(CAST(REPLACE(valor, ",", ".") AS REAL)) as total FROM desp_mensal WHERE pagamento = "S"...

**[09:29:42]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[09:29:42]** 🔄 **FLOW:** 📊 RESULTADO da query SQL: {'sucesso': True, 'dados': [{'total': 1053.125}], 'mensagem': 'Consulta executada com sucesso. 1 registro(s) encontrado(s).'}

**[09:29:42]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[09:29:42]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[09:29:42]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(CAST(REPLACE(valor, ",", ".") AS REAL)) as total FROM receitas_mensais...

**[09:29:42]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[09:29:42]** 🔄 **FLOW:** 📊 RESULTADO da query SQL: {'sucesso': True, 'dados': [{'total': 4.5}], 'mensagem': 'Consulta executada com sucesso. 1 registro(s) encontrado(s).'}

**[09:29:42]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[09:29:42]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[09:29:42]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM desp_mensal...

**[09:29:42]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[09:29:42]** 🔄 **FLOW:** 📊 RESULTADO da query SQL: {'sucesso': True, 'dados': [{'total': 2488.375}], 'mensagem': 'Consulta executada com sucesso. 1 registro(s) encontrado(s).'}

**[09:29:42]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[09:29:43]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[09:29:43]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM receitas_mensais...

**[09:29:43]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[09:29:43]** 🔄 **FLOW:** 📊 RESULTADO da query SQL: {'sucesso': True, 'dados': [{'total': 4.5}], 'mensagem': 'Consulta executada com sucesso. 1 registro(s) encontrado(s).'}

**[09:29:43]** 🔄 **FLOW:** ✅ SQL executado com sucesso

