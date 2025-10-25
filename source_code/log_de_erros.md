**[09:41:53]** === LOG TRUNCADO ===

**[09:41:53]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[09:41:53]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Descrição': 'Aluguel do Apto de Ipanema', '(R$)Valor': '3.125,00', 'Vencimento': '05/10/20025', 'Pago': 'N', 'Observação': 'Se pagar atrasado tem juros'}, {'Descrição': 'Caroline Buterine', '(R$)Valor': '500,00', 'Vencimento': '05/10/20025', 'Pago': 'N', 'Observação': 'Pgto mensal Clinica Buterine'}, {'Descrição': 'Conta de Gás - Naturgy', '(R$)Valor': '65,00', 'Vencimento': '10/10/2025', 'Pago': 'N', 'Observação': ''}, {'Descrição': 'Limpeza do apto', '(R$)Valor': '340,00', 'Vencimento': '25/10/2025', 'Pago': 'N', 'Observação': 'Incluso UBER estimado R$ 140,00'}, {'Descrição': 'Pagamento Cartão MASTERCARD', '(R$)Valor': '3.200,00', 'Vencimento': '26/10/2025', 'Pago': 'N', 'Observação': 'Vencimento em todo di 26 do mes'}, {'Descrição': 'Pagamento Cartão VISA', '(R$)Valor': '1.700,00', 'Vencimento': '16/10/2025', 'Pago': 'N', 'Observação': ''}, {'Descrição': 'Pagto Lucinha - INSS', '(R$)Valor': '800,00', 'Vencimento': '15/10/2025', 'Pago': 'N', 'Observação': 'Vl. mensal '}, {'Descrição': 'Pgto Conta de Luz Ap. Ipa', '(R$)Valor': '95,00', 'Vencimento': '08/10/2025', 'Pago': 'N', 'Observação': 'Conta Light'}, {'Descrição': 'Pgto Curso MBA', '(R$)Valor': '370,00', 'Vencimento': '10/10/2025', 'Pago': 'N', 'Observação': 'MBA Mercado de Capitais - UCB'}, {'Descrição': 'Pgto Lucinha - POLICON', '(R$)Valor': '228,00', 'Vencimento': '10/10/20025', 'Pago': 'N', 'Observação': '2 planos'}, {'Descrição': 'Pgto cta VIVO', '(R$)Valor': '331,00', 'Vencimento': '10/10/2025', 'Pago': 'N', 'Observação': ''}, {'Descrição': 'Prevent Senior', '(R$)Valor': '1.350,00', 'Vencimento': '30/10/2025', 'Pago': 'N', 'Observação': 'Plano Prevent'}], 'erro': None, 'sucesso': True, 'total_registros': 12}, 'mensagem': 'sucesso'}

**[09:41:53]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[09:41:53]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[09:41:53]** 🔄 **FLOW:** Consultando view: rec_mensal_report com campos: ['Todos']

**[09:41:53]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[09:41:53]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 2}
```

**[09:41:53]** 🔄 **FLOW:** Consulta executada - View: rec_mensal_report, Registros: 4

**[09:41:53]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[09:41:53]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Idreceita': 2, 'Descrição': 'Aluguel Apto DC', 'Valor': '1.375,00', 'Recebto': '25/10/2025', 'Observação': 'Dep. no SantanderNN'}, {'Idreceita': 1, 'Descrição': 'INSS', 'Valor': '3.105.00', 'Recebto': '03/10/2025', 'Observação': 'Pensao do INSS'}], 'erro': None, 'sucesso': True, 'total_registros': 2}, 'mensagem': 'sucesso'}

**[09:43:27]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[09:43:27]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[09:43:27]** 🔄 **FLOW:** Consultando view: desp_mensal_report com campos: ['Todos']

**[09:43:27]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[09:43:27]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 12}
```

**[09:43:27]** 🔄 **FLOW:** Consulta executada - View: desp_mensal_report, Registros: 4

**[09:43:27]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[09:43:27]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Descrição': 'Aluguel do Apto de Ipanema', '(R$)Valor': '3.125,00', 'Vencimento': '05/10/20025', 'Pago': 'N', 'Observação': 'Se pagar atrasado tem juros'}, {'Descrição': 'Caroline Buterine', '(R$)Valor': '500,00', 'Vencimento': '05/10/20025', 'Pago': 'N', 'Observação': 'Pgto mensal Clinica Buterine'}, {'Descrição': 'Conta de Gás - Naturgy', '(R$)Valor': '65,00', 'Vencimento': '10/10/2025', 'Pago': 'N', 'Observação': ''}, {'Descrição': 'Limpeza do apto', '(R$)Valor': '340,00', 'Vencimento': '25/10/2025', 'Pago': 'N', 'Observação': 'Incluso UBER estimado R$ 140,00'}, {'Descrição': 'Pagamento Cartão MASTERCARD', '(R$)Valor': '3.200,00', 'Vencimento': '26/10/2025', 'Pago': 'N', 'Observação': 'Vencimento em todo di 26 do mes'}, {'Descrição': 'Pagamento Cartão VISA', '(R$)Valor': '1.700,00', 'Vencimento': '16/10/2025', 'Pago': 'N', 'Observação': ''}, {'Descrição': 'Pagto Lucinha - INSS', '(R$)Valor': '800,00', 'Vencimento': '15/10/2025', 'Pago': 'N', 'Observação': 'Vl. mensal '}, {'Descrição': 'Pgto Conta de Luz Ap. Ipa', '(R$)Valor': '95,00', 'Vencimento': '08/10/2025', 'Pago': 'N', 'Observação': 'Conta Light'}, {'Descrição': 'Pgto Curso MBA', '(R$)Valor': '370,00', 'Vencimento': '10/10/2025', 'Pago': 'N', 'Observação': 'MBA Mercado de Capitais - UCB'}, {'Descrição': 'Pgto Lucinha - POLICON', '(R$)Valor': '228,00', 'Vencimento': '10/10/20025', 'Pago': 'N', 'Observação': '2 planos'}, {'Descrição': 'Pgto cta VIVO', '(R$)Valor': '331,00', 'Vencimento': '10/10/2025', 'Pago': 'N', 'Observação': ''}, {'Descrição': 'Prevent Senior', '(R$)Valor': '1.350,00', 'Vencimento': '30/10/2025', 'Pago': 'N', 'Observação': 'Plano Prevent'}], 'erro': None, 'sucesso': True, 'total_registros': 12}, 'mensagem': 'sucesso'}

**[09:43:27]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[09:43:27]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[09:43:27]** 🔄 **FLOW:** Consultando view: rec_mensal_report com campos: ['Todos']

**[09:43:27]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[09:43:27]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 2}
```

**[09:43:27]** 🔄 **FLOW:** Consulta executada - View: rec_mensal_report, Registros: 4

**[09:43:27]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[09:43:27]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Idreceita': 2, 'Descrição': 'Aluguel Apto DC', 'Valor': '1.375,00', 'Recebto': '25/10/2025', 'Observação': 'Dep. no SantanderNN'}, {'Idreceita': 1, 'Descrição': 'INSS', 'Valor': '3.105.00', 'Recebto': '03/10/2025', 'Observação': 'Pensao do INSS'}], 'erro': None, 'sucesso': True, 'total_registros': 2}, 'mensagem': 'sucesso'}

**[09:45:26]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[09:45:26]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[09:45:26]** 🔄 **FLOW:** Consultando view: desp_mensal_report com campos: ['Todos']

**[09:45:26]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[09:45:26]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 12}
```

**[09:45:26]** 🔄 **FLOW:** Consulta executada - View: desp_mensal_report, Registros: 4

**[09:45:26]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[09:45:26]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Descrição': 'Aluguel do Apto de Ipanema', '(R$)Valor': '3.125,00', 'Vencimento': '05/10/20025', 'Pago': 'N', 'Observação': 'Se pagar atrasado tem juros'}, {'Descrição': 'Caroline Buterine', '(R$)Valor': '500,00', 'Vencimento': '05/10/20025', 'Pago': 'N', 'Observação': 'Pgto mensal Clinica Buterine'}, {'Descrição': 'Conta de Gás - Naturgy', '(R$)Valor': '65,00', 'Vencimento': '10/10/2025', 'Pago': 'N', 'Observação': ''}, {'Descrição': 'Limpeza do apto', '(R$)Valor': '340,00', 'Vencimento': '25/10/2025', 'Pago': 'N', 'Observação': 'Incluso UBER estimado R$ 140,00'}, {'Descrição': 'Pagamento Cartão MASTERCARD', '(R$)Valor': '3.200,00', 'Vencimento': '26/10/2025', 'Pago': 'N', 'Observação': 'Vencimento em todo di 26 do mes'}, {'Descrição': 'Pagamento Cartão VISA', '(R$)Valor': '1.700,00', 'Vencimento': '16/10/2025', 'Pago': 'N', 'Observação': ''}, {'Descrição': 'Pagto Lucinha - INSS', '(R$)Valor': '800,00', 'Vencimento': '15/10/2025', 'Pago': 'N', 'Observação': 'Vl. mensal '}, {'Descrição': 'Pgto Conta de Luz Ap. Ipa', '(R$)Valor': '95,00', 'Vencimento': '08/10/2025', 'Pago': 'N', 'Observação': 'Conta Light'}, {'Descrição': 'Pgto Curso MBA', '(R$)Valor': '370,00', 'Vencimento': '10/10/2025', 'Pago': 'N', 'Observação': 'MBA Mercado de Capitais - UCB'}, {'Descrição': 'Pgto Lucinha - POLICON', '(R$)Valor': '228,00', 'Vencimento': '10/10/20025', 'Pago': 'N', 'Observação': '2 planos'}, {'Descrição': 'Pgto cta VIVO', '(R$)Valor': '331,00', 'Vencimento': '10/10/2025', 'Pago': 'N', 'Observação': ''}, {'Descrição': 'Prevent Senior', '(R$)Valor': '1.350,00', 'Vencimento': '30/10/2025', 'Pago': 'N', 'Observação': 'Plano Prevent'}], 'erro': None, 'sucesso': True, 'total_registros': 12}, 'mensagem': 'sucesso'}

**[09:45:26]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[09:45:26]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[09:45:26]** 🔄 **FLOW:** Consultando view: rec_mensal_report com campos: ['Todos']

**[09:45:26]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[09:45:26]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 2}
```

**[09:45:26]** 🔄 **FLOW:** Consulta executada - View: rec_mensal_report, Registros: 4

**[09:45:26]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[09:45:26]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Idreceita': 2, 'Descrição': 'Aluguel Apto DC', '(R$)Valor': '1.375,00', 'Recebto': '25/10/2025', 'Observação': 'Dep. no SantanderNN'}, {'Idreceita': 1, 'Descrição': 'INSS', '(R$)Valor': '3.105.00', 'Recebto': '03/10/2025', 'Observação': 'Pensao do INSS'}], 'erro': None, 'sucesso': True, 'total_registros': 2}, 'mensagem': 'sucesso'}

**[09:52:08]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[09:52:08]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[09:52:08]** 🔄 **FLOW:** Consultando view: desp_mensal_report com campos: ['Todos']

**[09:52:08]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[09:52:08]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 12}
```

**[09:52:08]** 🔄 **FLOW:** Consulta executada - View: desp_mensal_report, Registros: 4

**[09:52:08]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[09:52:08]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Descrição': 'Aluguel do Apto de Ipanema', '(R$)Valor': '3.125,00', 'Vencimento': '05/10/20025', 'Pago': 'N', 'Observação': 'Se pagar atrasado tem juros'}, {'Descrição': 'Caroline Buterine', '(R$)Valor': '500,00', 'Vencimento': '05/10/20025', 'Pago': 'N', 'Observação': 'Pgto mensal Clinica Buterine'}, {'Descrição': 'Conta de Gás - Naturgy', '(R$)Valor': '65,00', 'Vencimento': '10/10/2025', 'Pago': 'N', 'Observação': ''}, {'Descrição': 'Limpeza do apto', '(R$)Valor': '340,00', 'Vencimento': '25/10/2025', 'Pago': 'N', 'Observação': 'Incluso UBER estimado R$ 140,00'}, {'Descrição': 'Pagamento Cartão MASTERCARD', '(R$)Valor': '3.200,00', 'Vencimento': '26/10/2025', 'Pago': 'N', 'Observação': 'Vencimento em todo di 26 do mes'}, {'Descrição': 'Pagamento Cartão VISA', '(R$)Valor': '1.700,00', 'Vencimento': '16/10/2025', 'Pago': 'N', 'Observação': ''}, {'Descrição': 'Pagto Lucinha - INSS', '(R$)Valor': '800,00', 'Vencimento': '15/10/2025', 'Pago': 'N', 'Observação': 'Vl. mensal '}, {'Descrição': 'Pgto Conta de Luz Ap. Ipa', '(R$)Valor': '95,00', 'Vencimento': '08/10/2025', 'Pago': 'N', 'Observação': 'Conta Light'}, {'Descrição': 'Pgto Curso MBA', '(R$)Valor': '370,00', 'Vencimento': '10/10/2025', 'Pago': 'N', 'Observação': 'MBA Mercado de Capitais - UCB'}, {'Descrição': 'Pgto Lucinha - POLICON', '(R$)Valor': '228,00', 'Vencimento': '10/10/20025', 'Pago': 'N', 'Observação': '2 planos'}, {'Descrição': 'Pgto cta VIVO', '(R$)Valor': '331,00', 'Vencimento': '10/10/2025', 'Pago': 'N', 'Observação': ''}, {'Descrição': 'Prevent Senior', '(R$)Valor': '1.350,00', 'Vencimento': '30/10/2025', 'Pago': 'N', 'Observação': 'Plano Prevent'}], 'erro': None, 'sucesso': True, 'total_registros': 12}, 'mensagem': 'sucesso'}

**[09:52:08]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[09:52:08]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[09:52:08]** 🔄 **FLOW:** Consultando view: rec_mensal_report com campos: ['Todos']

**[09:52:08]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[09:52:08]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 2}
```

**[09:52:08]** 🔄 **FLOW:** Consulta executada - View: rec_mensal_report, Registros: 4

**[09:52:08]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[09:52:08]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Idreceita': 2, 'Descrição': 'Aluguel Apto DC', '(R$)Valor': '1.375,00', 'Recebto': '25/10/2025', 'Observação': 'Dep. no SantanderNN'}, {'Idreceita': 1, 'Descrição': 'INSS', '(R$)Valor': '3.105.00', 'Recebto': '03/10/2025', 'Observação': 'Pensao do INSS'}], 'erro': None, 'sucesso': True, 'total_registros': 2}, 'mensagem': 'sucesso'}

**[10:04:27]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[10:04:27]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[10:04:27]** 🔄 **FLOW:** Consultando view: desp_mensal_report com campos: ['Todos']

**[10:04:27]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[10:04:27]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 12}
```

**[10:04:27]** 🔄 **FLOW:** Consulta executada - View: desp_mensal_report, Registros: 4

**[10:04:27]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[10:04:27]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Descrição': 'Aluguel do Apto de Ipanema', '(R$)Valor': '3.125,00', 'Vencimento': '05/10/20025', 'Pago': 'N', 'Observação': 'Se pagar atrasado tem juros'}, {'Descrição': 'Caroline Buterine', '(R$)Valor': '500,00', 'Vencimento': '05/10/20025', 'Pago': 'N', 'Observação': 'Pgto mensal Clinica Buterine'}, {'Descrição': 'Conta de Gás - Naturgy', '(R$)Valor': '65,00', 'Vencimento': '10/10/2025', 'Pago': 'N', 'Observação': ''}, {'Descrição': 'Limpeza do apto', '(R$)Valor': '340,00', 'Vencimento': '25/10/2025', 'Pago': 'N', 'Observação': 'Incluso UBER estimado R$ 140,00'}, {'Descrição': 'Pagamento Cartão MASTERCARD', '(R$)Valor': '3.200,00', 'Vencimento': '26/10/2025', 'Pago': 'N', 'Observação': 'Vencimento em todo di 26 do mes'}, {'Descrição': 'Pagamento Cartão VISA', '(R$)Valor': '1.700,00', 'Vencimento': '16/10/2025', 'Pago': 'N', 'Observação': ''}, {'Descrição': 'Pagto Lucinha - INSS', '(R$)Valor': '800,00', 'Vencimento': '15/10/2025', 'Pago': 'N', 'Observação': 'Vl. mensal '}, {'Descrição': 'Pgto Conta de Luz Ap. Ipa', '(R$)Valor': '95,00', 'Vencimento': '08/10/2025', 'Pago': 'N', 'Observação': 'Conta Light'}, {'Descrição': 'Pgto Curso MBA', '(R$)Valor': '370,00', 'Vencimento': '10/10/2025', 'Pago': 'N', 'Observação': 'MBA Mercado de Capitais - UCB'}, {'Descrição': 'Pgto Lucinha - POLICON', '(R$)Valor': '228,00', 'Vencimento': '10/10/20025', 'Pago': 'N', 'Observação': '2 planos'}, {'Descrição': 'Pgto cta VIVO', '(R$)Valor': '331,00', 'Vencimento': '10/10/2025', 'Pago': 'N', 'Observação': ''}, {'Descrição': 'Prevent Senior', '(R$)Valor': '1.350,00', 'Vencimento': '30/10/2025', 'Pago': 'N', 'Observação': 'Plano Prevent'}], 'erro': None, 'sucesso': True, 'total_registros': 12}, 'mensagem': 'sucesso'}

**[10:04:27]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[10:04:27]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[10:04:27]** 🔄 **FLOW:** Consultando view: rec_mensal_report com campos: ['Todos']

**[10:04:27]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[10:04:27]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 2}
```

**[10:04:27]** 🔄 **FLOW:** Consulta executada - View: rec_mensal_report, Registros: 4

**[10:04:27]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[10:04:27]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Idreceita': 2, 'Descrição': 'Aluguel Apto DC', '(R$)Valor': '1.375,00', 'Recebto': '25/10/2025', 'Observação': 'Dep. no SantanderNN'}, {'Idreceita': 1, 'Descrição': 'INSS', '(R$)Valor': '3.105.00', 'Recebto': '03/10/2025', 'Observação': 'Pensao do INSS'}], 'erro': None, 'sucesso': True, 'total_registros': 2}, 'mensagem': 'sucesso'}

**[10:12:38]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[10:12:38]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[10:12:38]** 🔄 **FLOW:** Consultando view: desp_mensal_report com campos: ['Todos']

**[10:12:38]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[10:12:38]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 12}
```

**[10:12:38]** 🔄 **FLOW:** Consulta executada - View: desp_mensal_report, Registros: 4

**[10:12:38]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[10:12:38]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Descrição': 'Aluguel do Apto de Ipanema', '(R$)Valor': '3.125,00', 'Vencimento': '05/10/20025', 'Pago': 'N', 'Observação': 'Se pagar atrasado tem juros'}, {'Descrição': 'Caroline Buterine', '(R$)Valor': '500,00', 'Vencimento': '05/10/20025', 'Pago': 'N', 'Observação': 'Pgto mensal Clinica Buterine'}, {'Descrição': 'Conta de Gás - Naturgy', '(R$)Valor': '65,00', 'Vencimento': '10/10/2025', 'Pago': 'N', 'Observação': ''}, {'Descrição': 'Limpeza do apto', '(R$)Valor': '340,00', 'Vencimento': '25/10/2025', 'Pago': 'N', 'Observação': 'Incluso UBER estimado R$ 140,00'}, {'Descrição': 'Pagamento Cartão MASTERCARD', '(R$)Valor': '3.200,00', 'Vencimento': '26/10/2025', 'Pago': 'N', 'Observação': 'Vencimento em todo di 26 do mes'}, {'Descrição': 'Pagamento Cartão VISA', '(R$)Valor': '1.700,00', 'Vencimento': '16/10/2025', 'Pago': 'N', 'Observação': ''}, {'Descrição': 'Pagto Lucinha - INSS', '(R$)Valor': '800,00', 'Vencimento': '15/10/2025', 'Pago': 'N', 'Observação': 'Vl. mensal '}, {'Descrição': 'Pgto Conta de Luz Ap. Ipa', '(R$)Valor': '95,00', 'Vencimento': '08/10/2025', 'Pago': 'N', 'Observação': 'Conta Light'}, {'Descrição': 'Pgto Curso MBA', '(R$)Valor': '370,00', 'Vencimento': '10/10/2025', 'Pago': 'N', 'Observação': 'MBA Mercado de Capitais - UCB'}, {'Descrição': 'Pgto Lucinha - POLICON', '(R$)Valor': '228,00', 'Vencimento': '10/10/20025', 'Pago': 'N', 'Observação': '2 planos'}, {'Descrição': 'Pgto cta VIVO', '(R$)Valor': '331,00', 'Vencimento': '10/10/2025', 'Pago': 'N', 'Observação': ''}, {'Descrição': 'Prevent Senior', '(R$)Valor': '1.350,00', 'Vencimento': '30/10/2025', 'Pago': 'N', 'Observação': 'Plano Prevent'}], 'erro': None, 'sucesso': True, 'total_registros': 12}, 'mensagem': 'sucesso'}

**[10:12:38]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[10:12:38]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[10:12:38]** 🔄 **FLOW:** Consultando view: rec_mensal_report com campos: ['Todos']

**[10:12:38]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[10:12:38]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 2}
```

**[10:12:38]** 🔄 **FLOW:** Consulta executada - View: rec_mensal_report, Registros: 4

**[10:12:38]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[10:12:38]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Idreceita': 2, 'Descrição': 'Aluguel Apto DC', '(R$)Valor': '1.375,00', 'Recebto': '25/10/2025', 'Observação': 'Dep. no SantanderNN'}, {'Idreceita': 1, 'Descrição': 'INSS', '(R$)Valor': '3.105.00', 'Recebto': '03/10/2025', 'Observação': 'Pensao do INSS'}], 'erro': None, 'sucesso': True, 'total_registros': 2}, 'mensagem': 'sucesso'}

**[10:19:12]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[10:19:12]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[10:19:12]** 🔄 **FLOW:** Consultando view: desp_mensal_report com campos: ['Todos']

**[10:19:12]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[10:19:12]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 12}
```

**[10:19:12]** 🔄 **FLOW:** Consulta executada - View: desp_mensal_report, Registros: 4

**[10:19:12]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[10:19:12]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Descrição': 'Aluguel do Apto de Ipanema', '(R$)Valor': '3.125,00', 'Vencimento': '05/10/20025', 'Pago': 'N', 'Observação': 'Se pagar atrasado tem juros'}, {'Descrição': 'Caroline Buterine', '(R$)Valor': '500,00', 'Vencimento': '05/10/20025', 'Pago': 'N', 'Observação': 'Pgto mensal Clinica Buterine'}, {'Descrição': 'Conta de Gás - Naturgy', '(R$)Valor': '65,00', 'Vencimento': '10/10/2025', 'Pago': 'N', 'Observação': ''}, {'Descrição': 'Limpeza do apto', '(R$)Valor': '340,00', 'Vencimento': '25/10/2025', 'Pago': 'N', 'Observação': 'Incluso UBER estimado R$ 140,00'}, {'Descrição': 'Pagamento Cartão MASTERCARD', '(R$)Valor': '3.200,00', 'Vencimento': '26/10/2025', 'Pago': 'N', 'Observação': 'Vencimento em todo di 26 do mes'}, {'Descrição': 'Pagamento Cartão VISA', '(R$)Valor': '1.700,00', 'Vencimento': '16/10/2025', 'Pago': 'N', 'Observação': ''}, {'Descrição': 'Pagto Lucinha - INSS', '(R$)Valor': '800,00', 'Vencimento': '15/10/2025', 'Pago': 'N', 'Observação': 'Vl. mensal '}, {'Descrição': 'Pgto Conta de Luz Ap. Ipa', '(R$)Valor': '95,00', 'Vencimento': '08/10/2025', 'Pago': 'N', 'Observação': 'Conta Light'}, {'Descrição': 'Pgto Curso MBA', '(R$)Valor': '370,00', 'Vencimento': '10/10/2025', 'Pago': 'N', 'Observação': 'MBA Mercado de Capitais - UCB'}, {'Descrição': 'Pgto Lucinha - POLICON', '(R$)Valor': '228,00', 'Vencimento': '10/10/20025', 'Pago': 'N', 'Observação': '2 planos'}, {'Descrição': 'Pgto cta VIVO', '(R$)Valor': '331,00', 'Vencimento': '10/10/2025', 'Pago': 'N', 'Observação': ''}, {'Descrição': 'Prevent Senior', '(R$)Valor': '1.350,00', 'Vencimento': '30/10/2025', 'Pago': 'N', 'Observação': 'Plano Prevent'}], 'erro': None, 'sucesso': True, 'total_registros': 12}, 'mensagem': 'sucesso'}

**[10:19:12]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[10:19:12]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[10:19:12]** 🔄 **FLOW:** Consultando view: rec_mensal_report com campos: ['Todos']

**[10:19:12]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[10:19:12]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 2}
```

**[10:19:12]** 🔄 **FLOW:** Consulta executada - View: rec_mensal_report, Registros: 4

**[10:19:12]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[10:19:12]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Idreceita': 2, 'Descrição': 'Aluguel Apto DC', '(R$)Valor': '1.375,00', 'Recebto': '25/10/2025', 'Observação': 'Dep. no SantanderNN'}, {'Idreceita': 1, 'Descrição': 'INSS', '(R$)Valor': '3.105.00', 'Recebto': '03/10/2025', 'Observação': 'Pensao do INSS'}], 'erro': None, 'sucesso': True, 'total_registros': 2}, 'mensagem': 'sucesso'}

**[10:20:01]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[10:20:01]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[10:20:01]** 🔄 **FLOW:** Consultando view: desp_mensal_report com campos: ['Todos']

**[10:20:01]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[10:20:01]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 12}
```

**[10:20:01]** 🔄 **FLOW:** Consulta executada - View: desp_mensal_report, Registros: 4

**[10:20:01]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[10:20:01]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Descrição': 'Aluguel do Apto de Ipanema', '(R$)Valor': '3.125,00', 'Vencimento': '05/10/20025', 'Pago': 'N', 'Observação': 'Se pagar atrasado tem juros'}, {'Descrição': 'Caroline Buterine', '(R$)Valor': '500,00', 'Vencimento': '05/10/20025', 'Pago': 'N', 'Observação': 'Pgto mensal Clinica Buterine'}, {'Descrição': 'Conta de Gás - Naturgy', '(R$)Valor': '65,00', 'Vencimento': '10/10/2025', 'Pago': 'N', 'Observação': ''}, {'Descrição': 'Limpeza do apto', '(R$)Valor': '340,00', 'Vencimento': '25/10/2025', 'Pago': 'N', 'Observação': 'Incluso UBER estimado R$ 140,00'}, {'Descrição': 'Pagamento Cartão MASTERCARD', '(R$)Valor': '3.200,00', 'Vencimento': '26/10/2025', 'Pago': 'N', 'Observação': 'Vencimento em todo di 26 do mes'}, {'Descrição': 'Pagamento Cartão VISA', '(R$)Valor': '1.700,00', 'Vencimento': '16/10/2025', 'Pago': 'N', 'Observação': ''}, {'Descrição': 'Pagto Lucinha - INSS', '(R$)Valor': '800,00', 'Vencimento': '15/10/2025', 'Pago': 'N', 'Observação': 'Vl. mensal '}, {'Descrição': 'Pgto Conta de Luz Ap. Ipa', '(R$)Valor': '95,00', 'Vencimento': '08/10/2025', 'Pago': 'N', 'Observação': 'Conta Light'}, {'Descrição': 'Pgto Curso MBA', '(R$)Valor': '370,00', 'Vencimento': '10/10/2025', 'Pago': 'N', 'Observação': 'MBA Mercado de Capitais - UCB'}, {'Descrição': 'Pgto Lucinha - POLICON', '(R$)Valor': '228,00', 'Vencimento': '10/10/20025', 'Pago': 'N', 'Observação': '2 planos'}, {'Descrição': 'Pgto cta VIVO', '(R$)Valor': '331,00', 'Vencimento': '10/10/2025', 'Pago': 'N', 'Observação': ''}, {'Descrição': 'Prevent Senior', '(R$)Valor': '1.350,00', 'Vencimento': '30/10/2025', 'Pago': 'N', 'Observação': 'Plano Prevent'}], 'erro': None, 'sucesso': True, 'total_registros': 12}, 'mensagem': 'sucesso'}

**[10:20:02]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[10:20:02]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[10:20:02]** 🔄 **FLOW:** Consultando view: rec_mensal_report com campos: ['Todos']

**[10:20:02]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'rec_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[10:20:02]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 2}
```

**[10:20:02]** 🔄 **FLOW:** Consulta executada - View: rec_mensal_report, Registros: 4

**[10:20:02]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[10:20:02]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Idreceita': 2, 'Descrição': 'Aluguel Apto DC', '(R$)Valor': '1.375,00', 'Recebto': '25/10/2025', 'Observação': 'Dep. no SantanderNN'}, {'Idreceita': 1, 'Descrição': 'INSS', '(R$)Valor': '3.105.00', 'Recebto': '03/10/2025', 'Observação': 'Pensao do INSS'}], 'erro': None, 'sucesso': True, 'total_registros': 2}, 'mensagem': 'sucesso'}

