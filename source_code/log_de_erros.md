*****************************
SISTEMA DE LOG DE ERROS
SEÇÃO INICIADA EM 23/10/2025 às 13:55:16
*****************************

*****************************
SISTEMA DE LOG DE ERROS
SEÇÃO INICIADA EM 23/10/2025 às 13:55:16
*****************************

**[15:18:35]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[15:18:35]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[15:18:35]** 🔄 **FLOW:** Consultando view: desp_mensal_report com campos: ['Todos']

**[15:18:35]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[15:18:35]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 12}
```

**[15:18:35]** 🔄 **FLOW:** Consulta executada - View: desp_mensal_report, Registros: 4

**[15:18:35]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[15:18:35]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Descrição': 'Aluguel do Apto de Ipanema', 'Valor': '3.125,00', 'Vencimento': '05/10/20025', 'Pagamento': 'N', 'Observação': 'Se pagar atrasado tem juros'}, {'Descrição': 'Caroline Buterine', 'Valor': '500,00', 'Vencimento': '05/10/20025', 'Pagamento': 'N', 'Observação': 'Pgto mensal Clinica Buterine'}, {'Descrição': 'Pagamento Cartão VISA', 'Valor': '1.700,00', 'Vencimento': '16/10/2025', 'Pagamento': 'N', 'Observação': ''}, {'Descrição': 'Pagamento Cartão MASTERCARD', 'Valor': '3.200,00', 'Vencimento': '26/10/2025', 'Pagamento': 'N', 'Observação': 'Vencimento em todo di 26 do mes'}, {'Descrição': 'Pgto cta VIVO', 'Valor': '331,00', 'Vencimento': '10/10/2025', 'Pagamento': 'N', 'Observação': ''}, {'Descrição': 'Pgto Conta de Luz Ap. Ipa', 'Valor': '95,00', 'Vencimento': '08/10/2025', 'Pagamento': 'N', 'Observação': 'Conta Light'}, {'Descrição': 'Conta de Gás - Naturgy', 'Valor': '65,00', 'Vencimento': '10/10/2025', 'Pagamento': 'N', 'Observação': ''}, {'Descrição': 'Prevent Senior', 'Valor': '1.350,00', 'Vencimento': '30/10/2025', 'Pagamento': 'N', 'Observação': 'Plano Prevent'}, {'Descrição': 'Pagto Lucinha - INSS', 'Valor': '800,00', 'Vencimento': '15/10/2025', 'Pagamento': 'N', 'Observação': 'Vl. mensal '}, {'Descrição': 'Pgto Lucinha - POLICON', 'Valor': '228,00', 'Vencimento': '10/10/20025', 'Pagamento': 'N', 'Observação': '2 planos'}, {'Descrição': 'Limpeza do apto', 'Valor': '340,00', 'Vencimento': '25/10/2025', 'Pagamento': 'N', 'Observação': 'Incluso UBER estimado R$ 140,00'}, {'Descrição': 'Pgto Curso MBA', 'Valor': '370,00', 'Vencimento': '10/10/2025', 'Pagamento': 'N', 'Observação': 'MBA Mercado de Capitais - UCB'}], 'erro': None, 'sucesso': True, 'total_registros': 12}, 'mensagem': 'sucesso'}

**[15:18:35]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[15:18:35]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[15:18:35]** 🔄 **FLOW:** Consultando view: desp_mensal_report com campos: ['Todos']

**[15:18:35]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[15:18:35]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 12}
```

**[15:18:35]** 🔄 **FLOW:** Consulta executada - View: desp_mensal_report, Registros: 4

**[15:18:35]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[15:18:35]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Descrição': 'Aluguel do Apto de Ipanema', 'Valor': '3.125,00', 'Vencimento': '05/10/20025', 'Pagamento': 'N', 'Observação': 'Se pagar atrasado tem juros'}, {'Descrição': 'Caroline Buterine', 'Valor': '500,00', 'Vencimento': '05/10/20025', 'Pagamento': 'N', 'Observação': 'Pgto mensal Clinica Buterine'}, {'Descrição': 'Pagamento Cartão VISA', 'Valor': '1.700,00', 'Vencimento': '16/10/2025', 'Pagamento': 'N', 'Observação': ''}, {'Descrição': 'Pagamento Cartão MASTERCARD', 'Valor': '3.200,00', 'Vencimento': '26/10/2025', 'Pagamento': 'N', 'Observação': 'Vencimento em todo di 26 do mes'}, {'Descrição': 'Pgto cta VIVO', 'Valor': '331,00', 'Vencimento': '10/10/2025', 'Pagamento': 'N', 'Observação': ''}, {'Descrição': 'Pgto Conta de Luz Ap. Ipa', 'Valor': '95,00', 'Vencimento': '08/10/2025', 'Pagamento': 'N', 'Observação': 'Conta Light'}, {'Descrição': 'Conta de Gás - Naturgy', 'Valor': '65,00', 'Vencimento': '10/10/2025', 'Pagamento': 'N', 'Observação': ''}, {'Descrição': 'Prevent Senior', 'Valor': '1.350,00', 'Vencimento': '30/10/2025', 'Pagamento': 'N', 'Observação': 'Plano Prevent'}, {'Descrição': 'Pagto Lucinha - INSS', 'Valor': '800,00', 'Vencimento': '15/10/2025', 'Pagamento': 'N', 'Observação': 'Vl. mensal '}, {'Descrição': 'Pgto Lucinha - POLICON', 'Valor': '228,00', 'Vencimento': '10/10/20025', 'Pagamento': 'N', 'Observação': '2 planos'}, {'Descrição': 'Limpeza do apto', 'Valor': '340,00', 'Vencimento': '25/10/2025', 'Pagamento': 'N', 'Observação': 'Incluso UBER estimado R$ 140,00'}, {'Descrição': 'Pgto Curso MBA', 'Valor': '370,00', 'Vencimento': '10/10/2025', 'Pagamento': 'N', 'Observação': 'MBA Mercado de Capitais - UCB'}], 'erro': None, 'sucesso': True, 'total_registros': 12}, 'mensagem': 'sucesso'}

**[15:21:19]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[15:21:19]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[15:21:19]** 🔄 **FLOW:** Consultando view: desp_mensal_report com campos: ['Todos']

**[15:21:19]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[15:21:19]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 12}
```

**[15:21:19]** 🔄 **FLOW:** Consulta executada - View: desp_mensal_report, Registros: 4

**[15:21:19]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[15:21:19]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Descrição': 'Aluguel do Apto de Ipanema', 'Valor': '3.125,00', 'Vencimento': '05/10/20025', 'Pagamento': 'N', 'Observação': 'Se pagar atrasado tem juros'}, {'Descrição': 'Caroline Buterine', 'Valor': '500,00', 'Vencimento': '05/10/20025', 'Pagamento': 'N', 'Observação': 'Pgto mensal Clinica Buterine'}, {'Descrição': 'Pagamento Cartão VISA', 'Valor': '1.700,00', 'Vencimento': '16/10/2025', 'Pagamento': 'N', 'Observação': ''}, {'Descrição': 'Pagamento Cartão MASTERCARD', 'Valor': '3.200,00', 'Vencimento': '26/10/2025', 'Pagamento': 'N', 'Observação': 'Vencimento em todo di 26 do mes'}, {'Descrição': 'Pgto cta VIVO', 'Valor': '331,00', 'Vencimento': '10/10/2025', 'Pagamento': 'N', 'Observação': ''}, {'Descrição': 'Pgto Conta de Luz Ap. Ipa', 'Valor': '95,00', 'Vencimento': '08/10/2025', 'Pagamento': 'N', 'Observação': 'Conta Light'}, {'Descrição': 'Conta de Gás - Naturgy', 'Valor': '65,00', 'Vencimento': '10/10/2025', 'Pagamento': 'N', 'Observação': ''}, {'Descrição': 'Prevent Senior', 'Valor': '1.350,00', 'Vencimento': '30/10/2025', 'Pagamento': 'N', 'Observação': 'Plano Prevent'}, {'Descrição': 'Pagto Lucinha - INSS', 'Valor': '800,00', 'Vencimento': '15/10/2025', 'Pagamento': 'N', 'Observação': 'Vl. mensal '}, {'Descrição': 'Pgto Lucinha - POLICON', 'Valor': '228,00', 'Vencimento': '10/10/20025', 'Pagamento': 'N', 'Observação': '2 planos'}, {'Descrição': 'Limpeza do apto', 'Valor': '340,00', 'Vencimento': '25/10/2025', 'Pagamento': 'N', 'Observação': 'Incluso UBER estimado R$ 140,00'}, {'Descrição': 'Pgto Curso MBA', 'Valor': '370,00', 'Vencimento': '10/10/2025', 'Pagamento': 'N', 'Observação': 'MBA Mercado de Capitais - UCB'}], 'erro': None, 'sucesso': True, 'total_registros': 12}, 'mensagem': 'sucesso'}

**[15:21:19]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[15:21:19]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[15:21:19]** 🔄 **FLOW:** Consultando view: desp_mensal_report com campos: ['Todos']

**[15:21:19]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[15:21:19]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 12}
```

**[15:21:19]** 🔄 **FLOW:** Consulta executada - View: desp_mensal_report, Registros: 4

**[15:21:19]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[15:21:19]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Descrição': 'Aluguel do Apto de Ipanema', 'Valor': '3.125,00', 'Vencimento': '05/10/20025', 'Pagamento': 'N', 'Observação': 'Se pagar atrasado tem juros'}, {'Descrição': 'Caroline Buterine', 'Valor': '500,00', 'Vencimento': '05/10/20025', 'Pagamento': 'N', 'Observação': 'Pgto mensal Clinica Buterine'}, {'Descrição': 'Pagamento Cartão VISA', 'Valor': '1.700,00', 'Vencimento': '16/10/2025', 'Pagamento': 'N', 'Observação': ''}, {'Descrição': 'Pagamento Cartão MASTERCARD', 'Valor': '3.200,00', 'Vencimento': '26/10/2025', 'Pagamento': 'N', 'Observação': 'Vencimento em todo di 26 do mes'}, {'Descrição': 'Pgto cta VIVO', 'Valor': '331,00', 'Vencimento': '10/10/2025', 'Pagamento': 'N', 'Observação': ''}, {'Descrição': 'Pgto Conta de Luz Ap. Ipa', 'Valor': '95,00', 'Vencimento': '08/10/2025', 'Pagamento': 'N', 'Observação': 'Conta Light'}, {'Descrição': 'Conta de Gás - Naturgy', 'Valor': '65,00', 'Vencimento': '10/10/2025', 'Pagamento': 'N', 'Observação': ''}, {'Descrição': 'Prevent Senior', 'Valor': '1.350,00', 'Vencimento': '30/10/2025', 'Pagamento': 'N', 'Observação': 'Plano Prevent'}, {'Descrição': 'Pagto Lucinha - INSS', 'Valor': '800,00', 'Vencimento': '15/10/2025', 'Pagamento': 'N', 'Observação': 'Vl. mensal '}, {'Descrição': 'Pgto Lucinha - POLICON', 'Valor': '228,00', 'Vencimento': '10/10/20025', 'Pagamento': 'N', 'Observação': '2 planos'}, {'Descrição': 'Limpeza do apto', 'Valor': '340,00', 'Vencimento': '25/10/2025', 'Pagamento': 'N', 'Observação': 'Incluso UBER estimado R$ 140,00'}, {'Descrição': 'Pgto Curso MBA', 'Valor': '370,00', 'Vencimento': '10/10/2025', 'Pagamento': 'N', 'Observação': 'MBA Mercado de Capitais - UCB'}], 'erro': None, 'sucesso': True, 'total_registros': 12}, 'mensagem': 'sucesso'}

**[15:22:59]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[15:22:59]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[15:22:59]** 🔄 **FLOW:** Consultando view: desp_mensal_report com campos: ['Todos']

**[15:22:59]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[15:22:59]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 12}
```

**[15:22:59]** 🔄 **FLOW:** Consulta executada - View: desp_mensal_report, Registros: 4

**[15:22:59]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[15:22:59]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Descrição': 'Aluguel do Apto de Ipanema', 'Valor': '3.125,00', 'Vencimento': '05/10/20025', 'Pagamento': 'N', 'Observação': 'Se pagar atrasado tem juros'}, {'Descrição': 'Caroline Buterine', 'Valor': '500,00', 'Vencimento': '05/10/20025', 'Pagamento': 'N', 'Observação': 'Pgto mensal Clinica Buterine'}, {'Descrição': 'Pagamento Cartão VISA', 'Valor': '1.700,00', 'Vencimento': '16/10/2025', 'Pagamento': 'N', 'Observação': ''}, {'Descrição': 'Pagamento Cartão MASTERCARD', 'Valor': '3.200,00', 'Vencimento': '26/10/2025', 'Pagamento': 'N', 'Observação': 'Vencimento em todo di 26 do mes'}, {'Descrição': 'Pgto cta VIVO', 'Valor': '331,00', 'Vencimento': '10/10/2025', 'Pagamento': 'N', 'Observação': ''}, {'Descrição': 'Pgto Conta de Luz Ap. Ipa', 'Valor': '95,00', 'Vencimento': '08/10/2025', 'Pagamento': 'N', 'Observação': 'Conta Light'}, {'Descrição': 'Conta de Gás - Naturgy', 'Valor': '65,00', 'Vencimento': '10/10/2025', 'Pagamento': 'N', 'Observação': ''}, {'Descrição': 'Prevent Senior', 'Valor': '1.350,00', 'Vencimento': '30/10/2025', 'Pagamento': 'N', 'Observação': 'Plano Prevent'}, {'Descrição': 'Pagto Lucinha - INSS', 'Valor': '800,00', 'Vencimento': '15/10/2025', 'Pagamento': 'N', 'Observação': 'Vl. mensal '}, {'Descrição': 'Pgto Lucinha - POLICON', 'Valor': '228,00', 'Vencimento': '10/10/20025', 'Pagamento': 'N', 'Observação': '2 planos'}, {'Descrição': 'Limpeza do apto', 'Valor': '340,00', 'Vencimento': '25/10/2025', 'Pagamento': 'N', 'Observação': 'Incluso UBER estimado R$ 140,00'}, {'Descrição': 'Pgto Curso MBA', 'Valor': '370,00', 'Vencimento': '10/10/2025', 'Pagamento': 'N', 'Observação': 'MBA Mercado de Capitais - UCB'}], 'erro': None, 'sucesso': True, 'total_registros': 12}, 'mensagem': 'sucesso'}

**[15:23:00]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[15:23:00]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[15:23:00]** 🔄 **FLOW:** Consultando view: desp_mensal_report com campos: ['Todos']

**[15:23:00]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[15:23:00]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 12}
```

**[15:23:00]** 🔄 **FLOW:** Consulta executada - View: desp_mensal_report, Registros: 4

**[15:23:00]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[15:23:00]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Descrição': 'Aluguel do Apto de Ipanema', 'Valor': '3.125,00', 'Vencimento': '05/10/20025', 'Pagamento': 'N', 'Observação': 'Se pagar atrasado tem juros'}, {'Descrição': 'Caroline Buterine', 'Valor': '500,00', 'Vencimento': '05/10/20025', 'Pagamento': 'N', 'Observação': 'Pgto mensal Clinica Buterine'}, {'Descrição': 'Pagamento Cartão VISA', 'Valor': '1.700,00', 'Vencimento': '16/10/2025', 'Pagamento': 'N', 'Observação': ''}, {'Descrição': 'Pagamento Cartão MASTERCARD', 'Valor': '3.200,00', 'Vencimento': '26/10/2025', 'Pagamento': 'N', 'Observação': 'Vencimento em todo di 26 do mes'}, {'Descrição': 'Pgto cta VIVO', 'Valor': '331,00', 'Vencimento': '10/10/2025', 'Pagamento': 'N', 'Observação': ''}, {'Descrição': 'Pgto Conta de Luz Ap. Ipa', 'Valor': '95,00', 'Vencimento': '08/10/2025', 'Pagamento': 'N', 'Observação': 'Conta Light'}, {'Descrição': 'Conta de Gás - Naturgy', 'Valor': '65,00', 'Vencimento': '10/10/2025', 'Pagamento': 'N', 'Observação': ''}, {'Descrição': 'Prevent Senior', 'Valor': '1.350,00', 'Vencimento': '30/10/2025', 'Pagamento': 'N', 'Observação': 'Plano Prevent'}, {'Descrição': 'Pagto Lucinha - INSS', 'Valor': '800,00', 'Vencimento': '15/10/2025', 'Pagamento': 'N', 'Observação': 'Vl. mensal '}, {'Descrição': 'Pgto Lucinha - POLICON', 'Valor': '228,00', 'Vencimento': '10/10/20025', 'Pagamento': 'N', 'Observação': '2 planos'}, {'Descrição': 'Limpeza do apto', 'Valor': '340,00', 'Vencimento': '25/10/2025', 'Pagamento': 'N', 'Observação': 'Incluso UBER estimado R$ 140,00'}, {'Descrição': 'Pgto Curso MBA', 'Valor': '370,00', 'Vencimento': '10/10/2025', 'Pagamento': 'N', 'Observação': 'MBA Mercado de Capitais - UCB'}], 'erro': None, 'sucesso': True, 'total_registros': 12}, 'mensagem': 'sucesso'}

