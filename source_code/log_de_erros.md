*****************************
SISTEMA DE LOG DE ERROS
SEÇÃO INICIADA EM 10/11/2025 às 20:15:38
*****************************

*****************************
SISTEMA DE LOG DE ERROS
SEÇÃO INICIADA EM 10/11/2025 às 20:15:38
*****************************

**[20:16:12]** 🔄 **FLOW:** INÍCIO endpoint /despesas_12m

**[20:16:12]** 🔄 **FLOW:** 📦 Dados recebidos: {'view_name': 'despesas_view', 'campo_Agrupamento': 'grupo', 'campo_Pivot': 'data_extrato', 'campo_valor': 'valor', 'numColunasPivot': 12, 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db'}

**[20:16:12]** 🔄 **FLOW:** 📊 Calculando tabela pivot:

**[20:16:12]** 🔄 **FLOW:**    - View: despesas_view

**[20:16:12]** 🔄 **FLOW:**    - Campo agrupamento: grupo

**[20:16:12]** 🔄 **FLOW:**    - Campo pivot: data_extrato

**[20:16:12]** 🔄 **FLOW:**    - Campo valor: valor

**[20:16:12]** 🔄 **FLOW:**    - Num colunas pivot: 12

**[20:16:13]** 🔄 **FLOW:** ✅ Tabela pivot calculada: 7 grupos × 3 colunas

**[20:16:13]** 🔄 **FLOW:** INÍCIO endpoint /despesas_12m

**[20:16:13]** 🔄 **FLOW:** 📦 Dados recebidos: {'view_name': 'despesas_view', 'campo_Agrupamento': 'grupo', 'campo_Pivot': 'data_extrato', 'campo_valor': 'valor', 'numColunasPivot': 12, 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db'}

**[20:16:13]** 🔄 **FLOW:** 📊 Calculando tabela pivot:

**[20:16:13]** 🔄 **FLOW:**    - View: despesas_view

**[20:16:13]** 🔄 **FLOW:**    - Campo agrupamento: grupo

**[20:16:13]** 🔄 **FLOW:**    - Campo pivot: data_extrato

**[20:16:13]** 🔄 **FLOW:**    - Campo valor: valor

**[20:16:13]** 🔄 **FLOW:**    - Num colunas pivot: 12

**[20:16:13]** 🔄 **FLOW:** ✅ Tabela pivot calculada: 7 grupos × 3 colunas

**[20:16:21]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[20:16:21]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[20:16:21]** 🔄 **FLOW:** Consultando view: desp_mensal_report com campos: ['Todos']

**[20:16:21]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[20:16:21]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 13}
```

**[20:16:21]** 🔄 **FLOW:** Consulta executada - View: desp_mensal_report, Registros: 4

**[20:16:21]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[20:16:21]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Descrição': 'Aluguel do Apto de Ipanema', '(R$)Valor': 3053.89, 'Vencimento': '05/11/2025', 'Pago': 'S', 'Observação': 'Se pagar atrasado tem juros'}, {'Descrição': 'Caroline Buterine', '(R$)Valor': 500, 'Vencimento': '05/11/2025', 'Pago': 'S', 'Observação': 'Pgto mensal Clinica Buterine'}, {'Descrição': 'Conta de Gás - Naturgy', '(R$)Valor': 69.2, 'Vencimento': '10/11/2025', 'Pago': 'S', 'Observação': ''}, {'Descrição': 'Limpeza do apto', '(R$)Valor': 315, 'Vencimento': '07/11/2025', 'Pago': 'S', 'Observação': 'Incluso UBER estimado R$ 140,00'}, {'Descrição': 'Pagamento Cartão MASTERCARD', '(R$)Valor': 3200, 'Vencimento': '26/11/2025', 'Pago': 'N', 'Observação': 'Vencimento em todo di 26 do mes'}, {'Descrição': 'Pagamento Cartão VISA', '(R$)Valor': 1700, 'Vencimento': '16/11/2025', 'Pago': 'N', 'Observação': ''}, {'Descrição': 'Pagto Lucinha - INSS', '(R$)Valor': 800, 'Vencimento': '15/11/2025', 'Pago': 'N', 'Observação': 'Vl. mensal '}, {'Descrição': 'Pgto Conta de Luz Ap. Ipa', '(R$)Valor': 95, 'Vencimento': '08/11/2025', 'Pago': 'N', 'Observação': 'Conta Light'}, {'Descrição': 'Pgto Curso MBA', '(R$)Valor': 370, 'Vencimento': '10/11/2025', 'Pago': 'N', 'Observação': 'MBA Mercado de Capitais - UCB'}, {'Descrição': 'Pgto Lucinha - POLICON', '(R$)Valor': 228, 'Vencimento': '07/11/20025', 'Pago': 'S', 'Observação': '2 planos'}, {'Descrição': 'Pgto cta VIVO', '(R$)Valor': 331, 'Vencimento': '10/11/2025', 'Pago': 'N', 'Observação': ''}, {'Descrição': 'Pilates Ipanema', '(R$)Valor': 380, 'Vencimento': '07/11/2025', 'Pago': 'S', 'Observação': 'Academia de Pilates'}, {'Descrição': 'Prevent Senior', '(R$)Valor': 1350, 'Vencimento': '30/11/2025', 'Pago': 'N', 'Observação': 'Plano Prevent'}], 'erro': None, 'sucesso': True, 'total_registros': 13}, 'mensagem': 'sucesso'}

**[20:16:21]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[20:16:21]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[20:16:21]** 🔄 **FLOW:** Consultando view: rec_mensal_report com campos: ['Todos']

**[20:16:21]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[20:16:21]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 2}
```

**[20:16:21]** 🔄 **FLOW:** Consulta executada - View: rec_mensal_report, Registros: 4

**[20:16:21]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[20:16:21]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Idreceita': 2, 'Descrição': 'Aluguel Apto DC', '(R$)Valor': 1375.0, 'Recebto': '25/10/2025', 'Observação': 'Dep. no SantanderNN'}, {'Idreceita': 1, 'Descrição': 'INSS', '(R$)Valor': 3125.0, 'Recebto': '03/10/2025', 'Observação': 'Pensao do INSS'}], 'erro': None, 'sucesso': True, 'total_registros': 2}, 'mensagem': 'sucesso'}

**[20:16:21]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[20:16:21]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM desp_mensal...

**[20:16:21]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[20:16:21]** 🔄 **FLOW:** 📊 RESULTADO da query SQL: {'sucesso': True, 'dados': [{'total': 12392.09}], 'mensagem': 'Consulta executada com sucesso. 1 registro(s) encontrado(s).'}

**[20:16:21]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[20:16:21]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[20:16:21]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM desp_mensal WHERE pagamento = "S"...

**[20:16:21]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[20:16:21]** 🔄 **FLOW:** 📊 RESULTADO da query SQL: {'sucesso': True, 'dados': [{'total': 4546.09}], 'mensagem': 'Consulta executada com sucesso. 1 registro(s) encontrado(s).'}

**[20:16:21]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[20:16:21]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[20:16:21]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM receitas_mensais...

**[20:16:21]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[20:16:21]** 🔄 **FLOW:** 📊 RESULTADO da query SQL: {'sucesso': True, 'dados': [{'total': 4500.0}], 'mensagem': 'Consulta executada com sucesso. 1 registro(s) encontrado(s).'}

**[20:16:21]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[20:16:22]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[20:16:22]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM desp_mensal...

**[20:16:22]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[20:16:22]** 🔄 **FLOW:** 📊 RESULTADO da query SQL: {'sucesso': True, 'dados': [{'total': 12392.09}], 'mensagem': 'Consulta executada com sucesso. 1 registro(s) encontrado(s).'}

**[20:16:22]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[20:16:22]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[20:16:22]** 🔄 **FLOW:** 📝 SQL recebido: SELECT SUM(valor) as total FROM receitas_mensais...

**[20:16:22]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[20:16:22]** 🔄 **FLOW:** 📊 RESULTADO da query SQL: {'sucesso': True, 'dados': [{'total': 4500.0}], 'mensagem': 'Consulta executada com sucesso. 1 registro(s) encontrado(s).'}

**[20:16:22]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[20:16:26]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[20:16:26]** 🔄 **FLOW:** 📝 SQL recebido: SELECT DISTINCT substr(data_extrato, -4, 4) AS ano FROM despesas WHERE data_extrato LIKE '%_%' ORDER...

**[20:16:26]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[20:16:26]** 🔄 **FLOW:** 📊 RESULTADO da query SQL: {'sucesso': True, 'dados': [{'ano': '2025'}], 'mensagem': 'Consulta executada com sucesso. 1 registro(s) encontrado(s).'}

**[20:16:26]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[20:16:30]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[20:16:30]** 🔄 **FLOW:** 📝 SQL recebido: SELECT DISTINCT substr(data_extrato, 1, instr(data_extrato, '_')-1) AS mes FROM despesas WHERE data_...

**[20:16:30]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[20:16:30]** 🔄 **FLOW:** 📊 RESULTADO da query SQL: {'sucesso': True, 'dados': [{'mes': 'FEV'}, {'mes': 'JAN'}, {'mes': 'MAR'}], 'mensagem': 'Consulta executada com sucesso. 3 registro(s) encontrado(s).'}

**[20:16:30]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[20:16:30]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[20:16:30]** 🔄 **FLOW:** 📝 SQL recebido: SELECT DISTINCT instituicao FROM despesas WHERE instituicao IS NOT NULL AND instituicao <> '' AND da...

**[20:16:30]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[20:16:30]** 🔄 **FLOW:** 📊 RESULTADO da query SQL: {'sucesso': True, 'dados': [{'instituicao': 'MASTERCARD'}, {'instituicao': 'SANTANDER'}, {'instituicao': 'VISA'}], 'mensagem': 'Consulta executada com sucesso. 3 registro(s) encontrado(s).'}

**[20:16:30]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[20:16:32]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[20:16:32]** 🔄 **FLOW:** 📝 SQL recebido: SELECT DISTINCT instituicao FROM despesas WHERE instituicao IS NOT NULL AND instituicao <> '' AND da...

**[20:16:32]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[20:16:32]** 🔄 **FLOW:** 📊 RESULTADO da query SQL: {'sucesso': True, 'dados': [{'instituicao': 'MASTERCARD'}, {'instituicao': 'SANTANDER'}, {'instituicao': 'VISA'}], 'mensagem': 'Consulta executada com sucesso. 3 registro(s) encontrado(s).'}

**[20:16:32]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[20:16:35]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[20:16:35]** 🔄 **FLOW:** 📝 SQL recebido: SELECT descricao AS 'Descrição', instituicao AS 'Instituição', valor AS '(R$)Valor' FROM despesas_vi...

**[20:16:35]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[20:16:35]** 🔄 **FLOW:** 📊 RESULTADO da query SQL: {'sucesso': True, 'dados': [{'Descrição': 'ZONA SUL FL 08', 'Instituição': 'MASTERCARD', '(R$)Valor': 145.73}, {'Descrição': 'RAIA432', 'Instituição': 'MASTERCARD', '(R$)Valor': 138.94}, {'Descrição': 'ZONA SUL FL 08', 'Instituição': 'MASTERCARD', '(R$)Valor': 130.06}, {'Descrição': 'TOKIO MARINE*VIAG06D06', 'Instituição': 'MASTERCARD', '(R$)Valor': 123.87}, {'Descrição': 'ZONA SUL FL 08', 'Instituição': 'MASTERCARD', '(R$)Valor': 121.4}, {'Descrição': 'CONCESSAO METROVIARIA', 'Instituição': 'MASTERCARD', '(R$)Valor': 100}, {'Descrição': 'ZONA SUL FL 08', 'Instituição': 'MASTERCARD', '(R$)Valor': 86.47}, {'Descrição': '28/02 RAIA432 UBER UBER *TRIP HELP U 03/03', 'Instituição': 'MASTERCARD', '(R$)Valor': 80.08}, {'Descrição': 'DROGARIA VENANCIO', 'Instituição': 'MASTERCARD', '(R$)Valor': 71.97}, {'Descrição': 'ZONA SUL FL 08', 'Instituição': 'MASTERCARD', '(R$)Valor': 71.89}, {'Descrição': '07/03 DROGARIAS UBER* TRIP PACHECO 02/03', 'Instituição': 'MASTERCARD', '(R$)Valor': 70.05}, {'Descrição': 'ZONA SUL FL 08', 'Instituição': 'MASTERCARD', '(R$)Valor': 63.37}, {'Descrição': 'UBER* TRIP', 'Instituição': 'MASTERCARD', '(R$)Valor': 62.9}, {'Descrição': 'ZONA SUL FL 08', 'Instituição': 'MASTERCARD', '(R$)Valor': 61.73}, {'Descrição': 'O CARANGUEJO', 'Instituição': 'MASTERCARD', '(R$)Valor': 61}, {'Descrição': 'ZONA SUL FL 08', 'Instituição': 'MASTERCARD', '(R$)Valor': 59.92}, {'Descrição': 'ZONA SUL FL 08', 'Instituição': 'MASTERCARD', '(R$)Valor': 58.27}, {'Descrição': 'ZONA SUL FL 08', 'Instituição': 'MASTERCARD', '(R$)Valor': 55.57}, {'Descrição': 'ZONA SUL FL 08', 'Instituição': 'MASTERCARD', '(R$)Valor': 53.55}, {'Descrição': 'ZONA SUL FL 08', 'Instituição': 'MASTERCARD', '(R$)Valor': 47.39}, {'Descrição': 'ZONA SUL FL 08', 'Instituição': 'MASTERCARD', '(R$)Valor': 45.43}, {'Descrição': 'MANECO GOURMET', 'Instituição': 'MASTERCARD', '(R$)Valor': 40.31}, {'Descrição': 'UBER UBER *TRIP HELP U', 'Instituição': 'MASTERCARD', '(R$)Valor': 33.93}, {'Descrição': 'ZONA SUL FL 08', 'Instituição': 'MASTERCARD', '(R$)Valor': 33.79}, {'Descrição': 'UBER UBER *TRIP HELP U', 'Instituição': 'MASTERCARD', '(R$)Valor': 31.95}, {'Descrição': 'REI DO MATE', 'Instituição': 'MASTERCARD', '(R$)Valor': 30.9}, {'Descrição': 'ZONA SUL FL 1008 PIZZ', 'Instituição': 'MASTERCARD', '(R$)Valor': 30.79}, {'Descrição': 'ZONA SUL FL 08', 'Instituição': 'MASTERCARD', '(R$)Valor': 29.97}, {'Descrição': 'UTILICASA', 'Instituição': 'MASTERCARD', '(R$)Valor': 27.98}, {'Descrição': 'ZONA SUL FL 08', 'Instituição': 'MASTERCARD', '(R$)Valor': 25.7}, {'Descrição': 'ZONA SUL FL 1008 PIZZ', 'Instituição': 'MASTERCARD', '(R$)Valor': 24.68}, {'Descrição': 'CAFE CARDIN', 'Instituição': 'MASTERCARD', '(R$)Valor': 24.64}, {'Descrição': 'CAFE CARDIN', 'Instituição': 'MASTERCARD', '(R$)Valor': 24.64}, {'Descrição': 'CAFE CARDIN', 'Instituição': 'MASTERCARD', '(R$)Valor': 24.64}, {'Descrição': 'ZONA SUL FL 08', 'Instituição': 'MASTERCARD', '(R$)Valor': 24.57}, {'Descrição': 'ZONA SUL FL 08', 'Instituição': 'MASTERCARD', '(R$)Valor': 24.37}, {'Descrição': 'ZONA SUL FL 1008 PIZZ', 'Instituição': 'MASTERCARD', '(R$)Valor': 24.32}, {'Descrição': 'ZONA SUL FL 08', 'Instituição': 'MASTERCARD', '(R$)Valor': 24.17}, {'Descrição': 'FEDREVON CAFETERIA', 'Instituição': 'MASTERCARD', '(R$)Valor': 22.5}, {'Descrição': 'FEDREVON CAFETERIA', 'Instituição': 'MASTERCARD', '(R$)Valor': 22.5}, {'Descrição': 'ZONA SUL FL 1008 PIZZ', 'Instituição': 'MASTERCARD', '(R$)Valor': 21.08}, {'Descrição': 'ZONA SUL FL 08', 'Instituição': 'MASTERCARD', '(R$)Valor': 20.9}, {'Descrição': 'ZONA SUL FL 08', 'Instituição': 'MASTERCARD', '(R$)Valor': 18.49}, {'Descrição': 'ZONA SUL FL 27', 'Instituição': 'MASTERCARD', '(R$)Valor': 17.98}, {'Descrição': 'ZONA SUL FL 1008 PIZZ', 'Instituição': 'MASTERCARD', '(R$)Valor': 17.13}, {'Descrição': 'TAPIOKINHA', 'Instituição': 'MASTERCARD', '(R$)Valor': 17}, {'Descrição': 'CASA VELHA', 'Instituição': 'MASTERCARD', '(R$)Valor': 16.99}, {'Descrição': 'ZONA SUL FL 1008 PIZZ', 'Instituição': 'MASTERCARD', '(R$)Valor': 16.41}, {'Descrição': 'FEDREVON CAFETERIA', 'Instituição': 'MASTERCARD', '(R$)Valor': 15}, {'Descrição': 'ZONA SUL FL 1008 PIZZ', 'Instituição': 'MASTERCARD', '(R$)Valor': 14.97}, {'Descrição': 'ZONA SUL FL 1008 PIZZ', 'Instituição': 'MASTERCARD', '(R$)Valor': 14.25}, {'Descrição': 'ZONA SUL FL 1008 PIZZ', 'Instituição': 'MASTERCARD', '(R$)Valor': 13.57}, {'Descrição': 'ZONA SUL FL 08', 'Instituição': 'MASTERCARD', '(R$)Valor': 13.18}, {'Descrição': 'TAPIOKINHA', 'Instituição': 'MASTERCARD', '(R$)Valor': 12}, {'Descrição': 'MAIS1 CAFE RJ/RIO DE J', 'Instituição': 'MASTERCARD', '(R$)Valor': 11.5}, {'Descrição': 'SCP ESSENCIAL- FEV/25', 'Instituição': 'MASTERCARD', '(R$)Valor': 10.42}, {'Descrição': 'RAIA432', 'Instituição': 'MASTERCARD', '(R$)Valor': 9.59}, {'Descrição': 'RAIA432', 'Instituição': 'MASTERCARD', '(R$)Valor': 8.09}, {'Descrição': 'ZONA SUL FL 08', 'Instituição': 'MASTERCARD', '(R$)Valor': 6.99}, {'Descrição': 'OGGI', 'Instituição': 'MASTERCARD', '(R$)Valor': 5.99}, {'Descrição': 'CONQ', 'Instituição': 'MASTERCARD', '(R$)Valor': 5}], 'mensagem': 'Consulta executada com sucesso. 61 registro(s) encontrado(s).'}

**[20:16:35]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[20:16:35]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[20:16:35]** 🔄 **FLOW:** 📝 SQL recebido: SELECT 
                grupo AS 'Grupo',
                subgrupo AS 'Subgrupo',
                de...

**[20:16:35]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[20:16:35]** 🔄 **FLOW:** 📊 RESULTADO da query SQL: {'sucesso': True, 'dados': [{'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'ZONA SUL FL 08', '(R$)Total': 1222.91}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'ZONA SUL FL 1008 PIZZ', '(R$)Total': 177.2}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'RAIA432', '(R$)Total': 156.62}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'TOKIO MARINE*VIAG06D06', '(R$)Total': 123.87}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'CONCESSAO METROVIARIA', '(R$)Total': 100}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': '28/02 RAIA432 UBER UBER *TRIP HELP U 03/03', '(R$)Total': 80.08}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'CAFE CARDIN', '(R$)Total': 73.92}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'DROGARIA VENANCIO', '(R$)Total': 71.97}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': '07/03 DROGARIAS UBER* TRIP PACHECO 02/03', '(R$)Total': 70.05}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'UBER UBER *TRIP HELP U', '(R$)Total': 65.88}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'UBER* TRIP', '(R$)Total': 62.9}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'O CARANGUEJO', '(R$)Total': 61}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'FEDREVON CAFETERIA', '(R$)Total': 60.0}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'MANECO GOURMET', '(R$)Total': 40.31}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'REI DO MATE', '(R$)Total': 30.9}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'TAPIOKINHA', '(R$)Total': 29}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'UTILICASA', '(R$)Total': 27.98}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'ZONA SUL FL 27', '(R$)Total': 17.98}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'CASA VELHA', '(R$)Total': 16.99}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'MAIS1 CAFE RJ/RIO DE J', '(R$)Total': 11.5}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'SCP ESSENCIAL- FEV/25', '(R$)Total': 10.42}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'OGGI', '(R$)Total': 5.99}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'CONQ', '(R$)Total': 5}], 'mensagem': 'Consulta executada com sucesso. 23 registro(s) encontrado(s).'}

**[20:16:35]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[20:16:35]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[20:16:35]** 🔄 **FLOW:** 📝 SQL recebido: SELECT 
                grupo,
                SUM(valor) AS total
            FROM despesas_view_01...

**[20:16:35]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[20:16:35]** 🔄 **FLOW:** 📊 RESULTADO da query SQL: {'sucesso': True, 'dados': [{'grupo': 'Outros', 'total': 2522.47}], 'mensagem': 'Consulta executada com sucesso. 1 registro(s) encontrado(s).'}

**[20:16:35]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[20:16:45]** 🔄 **FLOW:** INÍCIO endpoint /despesas_12m

**[20:16:45]** 🔄 **FLOW:** 📦 Dados recebidos: {'view_name': 'despesas_view', 'campo_Agrupamento': 'grupo', 'campo_Pivot': 'data_extrato', 'campo_valor': 'valor', 'numColunasPivot': 12, 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db'}

**[20:16:45]** 🔄 **FLOW:** 📊 Calculando tabela pivot:

**[20:16:45]** 🔄 **FLOW:**    - View: despesas_view

**[20:16:45]** 🔄 **FLOW:**    - Campo agrupamento: grupo

**[20:16:45]** 🔄 **FLOW:**    - Campo pivot: data_extrato

**[20:16:45]** 🔄 **FLOW:**    - Campo valor: valor

**[20:16:45]** 🔄 **FLOW:**    - Num colunas pivot: 12

**[20:16:45]** 🔄 **FLOW:** ✅ Tabela pivot calculada: 7 grupos × 3 colunas

**[20:16:45]** 🔄 **FLOW:** INÍCIO endpoint /despesas_12m

**[20:16:45]** 🔄 **FLOW:** 📦 Dados recebidos: {'view_name': 'despesas_view', 'campo_Agrupamento': 'grupo', 'campo_Pivot': 'data_extrato', 'campo_valor': 'valor', 'numColunasPivot': 12, 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db'}

**[20:16:45]** 🔄 **FLOW:** 📊 Calculando tabela pivot:

**[20:16:45]** 🔄 **FLOW:**    - View: despesas_view

**[20:16:45]** 🔄 **FLOW:**    - Campo agrupamento: grupo

**[20:16:45]** 🔄 **FLOW:**    - Campo pivot: data_extrato

**[20:16:45]** 🔄 **FLOW:**    - Campo valor: valor

**[20:16:45]** 🔄 **FLOW:**    - Num colunas pivot: 12

**[20:16:45]** 🔄 **FLOW:** ✅ Tabela pivot calculada: 7 grupos × 3 colunas

**[20:17:47]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[20:17:47]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'grupos_view', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': 'c:\\Applications_DSB\\FinCtl', 'filtros': ''}
```

**[20:17:47]** 🔄 **FLOW:** Consultando view: grupos_view com campos: ['Todos']

**[20:17:47]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'grupos_view', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[20:17:47]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 12}
```

**[20:17:47]** 🔄 **FLOW:** Consulta executada - View: grupos_view, Registros: 4

**[20:17:47]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[20:17:47]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'idgrupo': 1, 'grupo': 'Alimentação', 'descricao': 'Grupo de classificação: Alimentação'}, {'idgrupo': 10, 'grupo': 'Aluguel', 'descricao': 'aluguel do aluguel do aluguel é mais e mais'}, {'idgrupo': 2, 'grupo': 'Educação', 'descricao': 'Grupo de classificação: Educação'}, {'idgrupo': 3, 'grupo': 'Financas', 'descricao': 'Grupo de classificação: FinancasSSZZ'}, {'idgrupo': 4, 'grupo': 'Lazer', 'descricao': 'Grupo de classificação: Lazer'}, {'idgrupo': 5, 'grupo': 'Moradia', 'descricao': 'Grupo de classificação: Moradia'}, {'idgrupo': 6, 'grupo': 'Outros', 'descricao': 'Grupo de classificação: Outros'}, {'idgrupo': 7, 'grupo': 'Saúde', 'descricao': 'Grupo de classificação: Saúde'}, {'idgrupo': 9, 'grupo': 'Tecnologias', 'descricao': 'equipamentos, assinaturas , manutenção de hardware'}, {'idgrupo': 8, 'grupo': 'Transporte', 'descricao': 'Grupo de classificação: Transporte'}, {'idgrupo': 12, 'grupo': 'Vestuário,Higiene e cuidados', 'descricao': 'Roupas, Corte de cabelo, produtos de hirigene e beleza'}, {'idgrupo': 11, 'grupo': 'Viagens', 'descricao': 'Despesas com passagens, hospedagem e passeios'}], 'erro': None, 'sucesso': True, 'total_registros': 12}, 'mensagem': 'sucesso'}

**[20:17:50]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[20:17:50]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'grupos_view', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': 'c:\\Applications_DSB\\FinCtl', 'filtros': ''}
```

**[20:17:50]** 🔄 **FLOW:** Consultando view: grupos_view com campos: ['Todos']

**[20:17:50]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'grupos_view', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[20:17:50]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 12}
```

**[20:17:50]** 🔄 **FLOW:** Consulta executada - View: grupos_view, Registros: 4

**[20:17:50]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[20:17:50]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'idgrupo': 1, 'grupo': 'Alimentação', 'descricao': 'Grupo de classificação: Alimentação'}, {'idgrupo': 10, 'grupo': 'Aluguel', 'descricao': 'aluguel do aluguel do aluguel é mais e mais'}, {'idgrupo': 2, 'grupo': 'Educação', 'descricao': 'Grupo de classificação: Educação'}, {'idgrupo': 3, 'grupo': 'Financas', 'descricao': 'Grupo de classificação: FinancasSSZZ'}, {'idgrupo': 4, 'grupo': 'Lazer', 'descricao': 'Grupo de classificação: Lazer'}, {'idgrupo': 5, 'grupo': 'Moradia', 'descricao': 'Grupo de classificação: Moradia'}, {'idgrupo': 6, 'grupo': 'Outros', 'descricao': 'Grupo de classificação: Outros'}, {'idgrupo': 7, 'grupo': 'Saúde', 'descricao': 'Grupo de classificação: Saúde'}, {'idgrupo': 9, 'grupo': 'Tecnologias', 'descricao': 'equipamentos, assinaturas , manutenção de hardware'}, {'idgrupo': 8, 'grupo': 'Transporte', 'descricao': 'Grupo de classificação: Transporte'}, {'idgrupo': 12, 'grupo': 'Vestuário,Higiene e cuidados', 'descricao': 'Roupas, Corte de cabelo, produtos de hirigene e beleza'}, {'idgrupo': 11, 'grupo': 'Viagens', 'descricao': 'Despesas com passagens, hospedagem e passeios'}], 'erro': None, 'sucesso': True, 'total_registros': 12}, 'mensagem': 'sucesso'}

**[20:17:54]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[20:17:54]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'subgrupos_view', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': 'c:\\Applications_DSB\\FinCtl', 'filtros': 'idgrupo = 1'}
```

**[20:17:54]** 🔄 **FLOW:** Consultando view: subgrupos_view com campos: ['Todos']

**[20:17:54]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'subgrupos_view', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[20:17:54]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 3}
```

**[20:17:54]** 🔄 **FLOW:** Consulta executada - View: subgrupos_view, Registros: 4

**[20:17:54]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[20:17:54]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'idsubgrupo': 12, 'idgrupo': 1, 'subgrupo': 'Café/bar/Quiosques', 'descricao': 'Despesas com lanches ou café em cafeterias e pequenos estabelecimento.', 'dicasDeClassificacao': 'Cafeteria, café, bar, cafe, Lanchonete, Galeto, Churrascaria', 'observacoes': '', 'data_criacao': '2025-11-03 13:03:33', 'data_atualizacao': '2025-11-03 13:03:33'}, {'idsubgrupo': 11, 'idgrupo': 1, 'subgrupo': 'Restaurantes', 'descricao': 'Despesas com almoço, jantar ou outros em restaurantes', 'dicasDeClassificacao': 'Restaurante , Rest. , Pizzaria', 'observacoes': '', 'data_criacao': '2025-11-03 13:01:18', 'data_atualizacao': '2025-11-03 13:01:18'}, {'idsubgrupo': 13, 'idgrupo': 1, 'subgrupo': 'Supermercados', 'descricao': 'Despesas em supermercados', 'dicasDeClassificacao': 'Zona Sul, Casa Pedro, Zona, Sul, Pedro', 'observacoes': '', 'data_criacao': '2025-11-03 13:05:47', 'data_atualizacao': '2025-11-03 13:05:47'}], 'erro': None, 'sucesso': True, 'total_registros': 3}, 'mensagem': 'sucesso'}

**[20:18:03]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[20:18:03]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'desp_mensal_view', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': 'c:\\Applications_DSB\\FinCtl', 'filtros': ''}
```

**[20:18:03]** 🔄 **FLOW:** Consultando view: desp_mensal_view com campos: ['Todos']

**[20:18:03]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'desp_mensal_view', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[20:18:03]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 13}
```

**[20:18:03]** 🔄 **FLOW:** Consulta executada - View: desp_mensal_view, Registros: 4

**[20:18:03]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[20:18:03]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'id_desp_mensal': 1, 'descricao': 'Aluguel do Apto de Ipanema', 'vencimento': '05/11/2025', 'valor': 3053.89, 'pagamento': 'S', 'obs': 'Se pagar atrasado tem juros', 'data_criacao': None}, {'id_desp_mensal': 2, 'descricao': 'Caroline Buterine', 'vencimento': '05/11/2025', 'valor': 500, 'pagamento': 'S', 'obs': 'Pgto mensal Clinica Buterine', 'data_criacao': None}, {'id_desp_mensal': 7, 'descricao': 'Conta de Gás - Naturgy', 'vencimento': '10/11/2025', 'valor': 69.2, 'pagamento': 'S', 'obs': '', 'data_criacao': None}, {'id_desp_mensal': 11, 'descricao': 'Limpeza do apto', 'vencimento': '07/11/2025', 'valor': 315, 'pagamento': 'S', 'obs': 'Incluso UBER estimado R$ 140,00', 'data_criacao': None}, {'id_desp_mensal': 4, 'descricao': 'Pagamento Cartão MASTERCARD', 'vencimento': '26/11/2025', 'valor': 3200, 'pagamento': 'N', 'obs': 'Vencimento em todo di 26 do mes', 'data_criacao': None}, {'id_desp_mensal': 3, 'descricao': 'Pagamento Cartão VISA', 'vencimento': '16/11/2025', 'valor': 1700, 'pagamento': 'N', 'obs': '', 'data_criacao': None}, {'id_desp_mensal': 9, 'descricao': 'Pagto Lucinha - INSS', 'vencimento': '15/11/2025', 'valor': 800, 'pagamento': 'N', 'obs': 'Vl. mensal ', 'data_criacao': None}, {'id_desp_mensal': 6, 'descricao': 'Pgto Conta de Luz Ap. Ipa', 'vencimento': '08/11/2025', 'valor': 95, 'pagamento': 'N', 'obs': 'Conta Light', 'data_criacao': None}, {'id_desp_mensal': 12, 'descricao': 'Pgto Curso MBA', 'vencimento': '10/11/2025', 'valor': 370, 'pagamento': 'N', 'obs': 'MBA Mercado de Capitais - UCB', 'data_criacao': None}, {'id_desp_mensal': 10, 'descricao': 'Pgto Lucinha - POLICON', 'vencimento': '07/11/20025', 'valor': 228, 'pagamento': 'S', 'obs': '2 planos', 'data_criacao': None}, {'id_desp_mensal': 5, 'descricao': 'Pgto cta VIVO', 'vencimento': '10/11/2025', 'valor': 331, 'pagamento': 'N', 'obs': '', 'data_criacao': None}, {'id_desp_mensal': 13, 'descricao': 'Pilates Ipanema', 'vencimento': '07/11/2025', 'valor': 380, 'pagamento': 'S', 'obs': 'Academia de Pilates', 'data_criacao': None}, {'id_desp_mensal': 8, 'descricao': 'Prevent Senior', 'vencimento': '30/11/2025', 'valor': 1350, 'pagamento': 'N', 'obs': 'Plano Prevent', 'data_criacao': None}], 'erro': None, 'sucesso': True, 'total_registros': 13}, 'mensagem': 'sucesso'}

**[20:18:03]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[20:18:03]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'desp_mensal_view', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': 'c:\\Applications_DSB\\FinCtl', 'filtros': ''}
```

**[20:18:03]** 🔄 **FLOW:** Consultando view: desp_mensal_view com campos: ['Todos']

**[20:18:03]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'desp_mensal_view', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[20:18:03]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 13}
```

**[20:18:03]** 🔄 **FLOW:** Consulta executada - View: desp_mensal_view, Registros: 4

**[20:18:03]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[20:18:03]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'id_desp_mensal': 1, 'descricao': 'Aluguel do Apto de Ipanema', 'vencimento': '05/11/2025', 'valor': 3053.89, 'pagamento': 'S', 'obs': 'Se pagar atrasado tem juros', 'data_criacao': None}, {'id_desp_mensal': 2, 'descricao': 'Caroline Buterine', 'vencimento': '05/11/2025', 'valor': 500, 'pagamento': 'S', 'obs': 'Pgto mensal Clinica Buterine', 'data_criacao': None}, {'id_desp_mensal': 7, 'descricao': 'Conta de Gás - Naturgy', 'vencimento': '10/11/2025', 'valor': 69.2, 'pagamento': 'S', 'obs': '', 'data_criacao': None}, {'id_desp_mensal': 11, 'descricao': 'Limpeza do apto', 'vencimento': '07/11/2025', 'valor': 315, 'pagamento': 'S', 'obs': 'Incluso UBER estimado R$ 140,00', 'data_criacao': None}, {'id_desp_mensal': 4, 'descricao': 'Pagamento Cartão MASTERCARD', 'vencimento': '26/11/2025', 'valor': 3200, 'pagamento': 'N', 'obs': 'Vencimento em todo di 26 do mes', 'data_criacao': None}, {'id_desp_mensal': 3, 'descricao': 'Pagamento Cartão VISA', 'vencimento': '16/11/2025', 'valor': 1700, 'pagamento': 'N', 'obs': '', 'data_criacao': None}, {'id_desp_mensal': 9, 'descricao': 'Pagto Lucinha - INSS', 'vencimento': '15/11/2025', 'valor': 800, 'pagamento': 'N', 'obs': 'Vl. mensal ', 'data_criacao': None}, {'id_desp_mensal': 6, 'descricao': 'Pgto Conta de Luz Ap. Ipa', 'vencimento': '08/11/2025', 'valor': 95, 'pagamento': 'N', 'obs': 'Conta Light', 'data_criacao': None}, {'id_desp_mensal': 12, 'descricao': 'Pgto Curso MBA', 'vencimento': '10/11/2025', 'valor': 370, 'pagamento': 'N', 'obs': 'MBA Mercado de Capitais - UCB', 'data_criacao': None}, {'id_desp_mensal': 10, 'descricao': 'Pgto Lucinha - POLICON', 'vencimento': '07/11/20025', 'valor': 228, 'pagamento': 'S', 'obs': '2 planos', 'data_criacao': None}, {'id_desp_mensal': 5, 'descricao': 'Pgto cta VIVO', 'vencimento': '10/11/2025', 'valor': 331, 'pagamento': 'N', 'obs': '', 'data_criacao': None}, {'id_desp_mensal': 13, 'descricao': 'Pilates Ipanema', 'vencimento': '07/11/2025', 'valor': 380, 'pagamento': 'S', 'obs': 'Academia de Pilates', 'data_criacao': None}, {'id_desp_mensal': 8, 'descricao': 'Prevent Senior', 'vencimento': '30/11/2025', 'valor': 1350, 'pagamento': 'N', 'obs': 'Plano Prevent', 'data_criacao': None}], 'erro': None, 'sucesso': True, 'total_registros': 13}, 'mensagem': 'sucesso'}

**[20:18:07]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[20:18:07]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'receitas_mensais_view', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': 'c:\\Applications_DSB\\FinCtl', 'filtros': ''}
```

**[20:18:07]** 🔄 **FLOW:** Consultando view: receitas_mensais_view com campos: ['Todos']

**[20:18:07]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'receitas_mensais_view', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[20:18:07]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 2}
```

**[20:18:07]** 🔄 **FLOW:** Consulta executada - View: receitas_mensais_view, Registros: 4

**[20:18:07]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[20:18:07]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'idreceita': 2, 'descricao': 'Aluguel Apto DC', 'valor': 1375.0, 'recebimento': '25/10/2025', 'obs': 'Dep. no SantanderNN'}, {'idreceita': 1, 'descricao': 'INSS', 'valor': 3125.0, 'recebimento': '03/10/2025', 'obs': 'Pensao do INSS'}], 'erro': None, 'sucesso': True, 'total_registros': 2}, 'mensagem': 'sucesso'}

**[20:18:13]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[20:18:13]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'despesas_select_view', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': 'c:\\Applications_DSB\\FinCtl', 'filtros': ''}
```

**[20:18:13]** 🔄 **FLOW:** Consultando view: despesas_select_view com campos: ['Todos']

**[20:18:13]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'despesas_select_view', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[20:18:13]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 9}
```

**[20:18:13]** 🔄 **FLOW:** Consulta executada - View: despesas_select_view, Registros: 4

**[20:18:13]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[20:18:13]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'lcto': 'MASTERCARD_FEV_2025'}, {'lcto': 'MASTERCARD_JAN_2025'}, {'lcto': 'MASTERCARD_MAR_2025'}, {'lcto': 'SANTANDER_FEV_2025'}, {'lcto': 'SANTANDER_JAN_2025'}, {'lcto': 'SANTANDER_MAR_2025'}, {'lcto': 'VISA_FEV_2025'}, {'lcto': 'VISA_JAN_2025'}, {'lcto': 'VISA_MAR_2025'}], 'erro': None, 'sucesso': True, 'total_registros': 9}, 'mensagem': 'sucesso'}

**[20:18:24]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[20:18:24]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'despesas_view', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': 'c:\\Applications_DSB\\FinCtl', 'filtros': "lcto = 'MASTERCARD_FEV_2025'"}
```

**[20:18:24]** 🔄 **FLOW:** Consultando view: despesas_view com campos: ['Todos']

**[20:18:24]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'despesas_view', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[20:18:24]** ❌ **ERRO:** Erro na função consultar_bd  
```
Tipo: OperationalError
Mensagem: no such column: lcto
```  
**Stack Trace:**
```
  File "C:\Applications_DSB\framework_dsb\backend\source_code\data_manager.py", line 138, in consultar_bd
    cursor.execute(sql)

```

**[20:18:24]** 🔄 **FLOW:** Consulta executada - View: despesas_view, Registros: 4

**[20:18:24]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[20:18:24]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [], 'erro': 'Erro na consulta: no such column: lcto', 'sucesso': False, 'total_registros': 0}, 'mensagem': 'sucesso'}

