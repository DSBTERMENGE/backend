**[08:38:20]** === LOG TRUNCADO ===

**[08:38:20]** 🔄 **FLOW:** Consultando view: desp_mensal_report com campos: ['Todos']

**[08:38:20]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[08:38:20]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 12}
```

**[08:38:20]** 🔄 **FLOW:** Consulta executada - View: desp_mensal_report, Registros: 4

**[08:38:20]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[08:38:20]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Descrição': 'Aluguel do Apto de Ipanema', 'Valor': '3.125,00', 'Vencimento': '05/10/20025', 'Pagamento': '', 'Observação': 'Se pagar atrasado tem juros'}, {'Descrição': 'Caroline Buterine', 'Valor': '500,00', 'Vencimento': '05/10/20025', 'Pagamento': '', 'Observação': 'Pgto mensal Clinica Buterine'}, {'Descrição': 'Pagamento Cartão VISA', 'Valor': '1.700,00', 'Vencimento': '16/10/2025', 'Pagamento': '', 'Observação': ''}, {'Descrição': 'Pagamento Cartão MASTERCARD', 'Valor': '3.200,00', 'Vencimento': '26/10/2025', 'Pagamento': '', 'Observação': 'Vencimento em todo di 26 do mes'}, {'Descrição': 'Pgto cta VIVO', 'Valor': '331,00', 'Vencimento': '10/10/2025', 'Pagamento': '', 'Observação': ''}, {'Descrição': 'Pgto Conta de Luz Ap. Ipa', 'Valor': '95,00', 'Vencimento': '08/10/2025', 'Pagamento': '', 'Observação': 'Conta Light'}, {'Descrição': 'Conta de Gás - Naturgy', 'Valor': '65,00', 'Vencimento': '10/10/2025', 'Pagamento': '', 'Observação': ''}, {'Descrição': 'Prevent Senior', 'Valor': '1.350,00', 'Vencimento': '30/10/2025', 'Pagamento': '', 'Observação': 'Plano Prevent'}, {'Descrição': 'Pagto Lucinha - INSS', 'Valor': '800,00', 'Vencimento': '15/10/2025', 'Pagamento': '', 'Observação': 'Vl. mensal '}, {'Descrição': 'Pgto Lucinha - POLICON', 'Valor': '228,00', 'Vencimento': '10/10/20025', 'Pagamento': '', 'Observação': '2 planos'}, {'Descrição': 'Limpeza do apto', 'Valor': '340,00', 'Vencimento': '25/10/2025', 'Pagamento': '', 'Observação': 'Incluso UBER estimado R$ 140,00'}, {'Descrição': 'Pgto Curso MBA', 'Valor': '370,00', 'Vencimento': '10/10/2025', 'Pagamento': '', 'Observação': 'MBA Mercado de Capitais - UCB'}], 'erro': None, 'sucesso': True, 'total_registros': 12}, 'mensagem': 'sucesso'}

**[09:22:22]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[09:22:22]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[09:22:22]** 🔄 **FLOW:** Consultando view: desp_mensal_report com campos: ['Todos']

**[09:22:22]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[09:22:22]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 12}
```

**[09:22:22]** 🔄 **FLOW:** Consulta executada - View: desp_mensal_report, Registros: 4

**[09:22:22]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[09:22:22]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Descrição': 'Aluguel do Apto de Ipanema', 'Valor': '3.125,00', 'Vencimento': '05/10/20025', 'Pagamento': '', 'Observação': 'Se pagar atrasado tem juros'}, {'Descrição': 'Caroline Buterine', 'Valor': '500,00', 'Vencimento': '05/10/20025', 'Pagamento': '', 'Observação': 'Pgto mensal Clinica Buterine'}, {'Descrição': 'Pagamento Cartão VISA', 'Valor': '1.700,00', 'Vencimento': '16/10/2025', 'Pagamento': '', 'Observação': ''}, {'Descrição': 'Pagamento Cartão MASTERCARD', 'Valor': '3.200,00', 'Vencimento': '26/10/2025', 'Pagamento': '', 'Observação': 'Vencimento em todo di 26 do mes'}, {'Descrição': 'Pgto cta VIVO', 'Valor': '331,00', 'Vencimento': '10/10/2025', 'Pagamento': '', 'Observação': ''}, {'Descrição': 'Pgto Conta de Luz Ap. Ipa', 'Valor': '95,00', 'Vencimento': '08/10/2025', 'Pagamento': '', 'Observação': 'Conta Light'}, {'Descrição': 'Conta de Gás - Naturgy', 'Valor': '65,00', 'Vencimento': '10/10/2025', 'Pagamento': '', 'Observação': ''}, {'Descrição': 'Prevent Senior', 'Valor': '1.350,00', 'Vencimento': '30/10/2025', 'Pagamento': '', 'Observação': 'Plano Prevent'}, {'Descrição': 'Pagto Lucinha - INSS', 'Valor': '800,00', 'Vencimento': '15/10/2025', 'Pagamento': '', 'Observação': 'Vl. mensal '}, {'Descrição': 'Pgto Lucinha - POLICON', 'Valor': '228,00', 'Vencimento': '10/10/20025', 'Pagamento': '', 'Observação': '2 planos'}, {'Descrição': 'Limpeza do apto', 'Valor': '340,00', 'Vencimento': '25/10/2025', 'Pagamento': '', 'Observação': 'Incluso UBER estimado R$ 140,00'}, {'Descrição': 'Pgto Curso MBA', 'Valor': '370,00', 'Vencimento': '10/10/2025', 'Pagamento': '', 'Observação': 'MBA Mercado de Capitais - UCB'}], 'erro': None, 'sucesso': True, 'total_registros': 12}, 'mensagem': 'sucesso'}

**[09:37:52]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[09:37:52]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[09:37:52]** 🔄 **FLOW:** Consultando view: desp_mensal_report com campos: ['Todos']

**[09:37:52]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[09:37:52]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 12}
```

**[09:37:52]** 🔄 **FLOW:** Consulta executada - View: desp_mensal_report, Registros: 4

**[09:37:52]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[09:37:52]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Descrição': 'Aluguel do Apto de Ipanema', 'Valor': '3.125,00', 'Vencimento': '05/10/20025', 'Pagamento': '', 'Observação': 'Se pagar atrasado tem juros'}, {'Descrição': 'Caroline Buterine', 'Valor': '500,00', 'Vencimento': '05/10/20025', 'Pagamento': '', 'Observação': 'Pgto mensal Clinica Buterine'}, {'Descrição': 'Pagamento Cartão VISA', 'Valor': '1.700,00', 'Vencimento': '16/10/2025', 'Pagamento': '', 'Observação': ''}, {'Descrição': 'Pagamento Cartão MASTERCARD', 'Valor': '3.200,00', 'Vencimento': '26/10/2025', 'Pagamento': '', 'Observação': 'Vencimento em todo di 26 do mes'}, {'Descrição': 'Pgto cta VIVO', 'Valor': '331,00', 'Vencimento': '10/10/2025', 'Pagamento': '', 'Observação': ''}, {'Descrição': 'Pgto Conta de Luz Ap. Ipa', 'Valor': '95,00', 'Vencimento': '08/10/2025', 'Pagamento': '', 'Observação': 'Conta Light'}, {'Descrição': 'Conta de Gás - Naturgy', 'Valor': '65,00', 'Vencimento': '10/10/2025', 'Pagamento': '', 'Observação': ''}, {'Descrição': 'Prevent Senior', 'Valor': '1.350,00', 'Vencimento': '30/10/2025', 'Pagamento': '', 'Observação': 'Plano Prevent'}, {'Descrição': 'Pagto Lucinha - INSS', 'Valor': '800,00', 'Vencimento': '15/10/2025', 'Pagamento': '', 'Observação': 'Vl. mensal '}, {'Descrição': 'Pgto Lucinha - POLICON', 'Valor': '228,00', 'Vencimento': '10/10/20025', 'Pagamento': '', 'Observação': '2 planos'}, {'Descrição': 'Limpeza do apto', 'Valor': '340,00', 'Vencimento': '25/10/2025', 'Pagamento': '', 'Observação': 'Incluso UBER estimado R$ 140,00'}, {'Descrição': 'Pgto Curso MBA', 'Valor': '370,00', 'Vencimento': '10/10/2025', 'Pagamento': '', 'Observação': 'MBA Mercado de Capitais - UCB'}], 'erro': None, 'sucesso': True, 'total_registros': 12}, 'mensagem': 'sucesso'}

**[09:37:56]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[09:37:56]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[09:37:56]** 🔄 **FLOW:** Consultando view: desp_mensal_report com campos: ['Todos']

**[09:37:56]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[09:37:56]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 12}
```

**[09:37:56]** 🔄 **FLOW:** Consulta executada - View: desp_mensal_report, Registros: 4

**[09:37:56]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[09:37:56]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Descrição': 'Aluguel do Apto de Ipanema', 'Valor': '3.125,00', 'Vencimento': '05/10/20025', 'Pagamento': '', 'Observação': 'Se pagar atrasado tem juros'}, {'Descrição': 'Caroline Buterine', 'Valor': '500,00', 'Vencimento': '05/10/20025', 'Pagamento': '', 'Observação': 'Pgto mensal Clinica Buterine'}, {'Descrição': 'Pagamento Cartão VISA', 'Valor': '1.700,00', 'Vencimento': '16/10/2025', 'Pagamento': '', 'Observação': ''}, {'Descrição': 'Pagamento Cartão MASTERCARD', 'Valor': '3.200,00', 'Vencimento': '26/10/2025', 'Pagamento': '', 'Observação': 'Vencimento em todo di 26 do mes'}, {'Descrição': 'Pgto cta VIVO', 'Valor': '331,00', 'Vencimento': '10/10/2025', 'Pagamento': '', 'Observação': ''}, {'Descrição': 'Pgto Conta de Luz Ap. Ipa', 'Valor': '95,00', 'Vencimento': '08/10/2025', 'Pagamento': '', 'Observação': 'Conta Light'}, {'Descrição': 'Conta de Gás - Naturgy', 'Valor': '65,00', 'Vencimento': '10/10/2025', 'Pagamento': '', 'Observação': ''}, {'Descrição': 'Prevent Senior', 'Valor': '1.350,00', 'Vencimento': '30/10/2025', 'Pagamento': '', 'Observação': 'Plano Prevent'}, {'Descrição': 'Pagto Lucinha - INSS', 'Valor': '800,00', 'Vencimento': '15/10/2025', 'Pagamento': '', 'Observação': 'Vl. mensal '}, {'Descrição': 'Pgto Lucinha - POLICON', 'Valor': '228,00', 'Vencimento': '10/10/20025', 'Pagamento': '', 'Observação': '2 planos'}, {'Descrição': 'Limpeza do apto', 'Valor': '340,00', 'Vencimento': '25/10/2025', 'Pagamento': '', 'Observação': 'Incluso UBER estimado R$ 140,00'}, {'Descrição': 'Pgto Curso MBA', 'Valor': '370,00', 'Vencimento': '10/10/2025', 'Pagamento': '', 'Observação': 'MBA Mercado de Capitais - UCB'}], 'erro': None, 'sucesso': True, 'total_registros': 12}, 'mensagem': 'sucesso'}

**[10:07:36]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[10:07:36]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[10:07:36]** 🔄 **FLOW:** Consultando view: desp_mensal_report com campos: ['Todos']

**[10:07:36]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[10:07:36]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 12}
```

**[10:07:36]** 🔄 **FLOW:** Consulta executada - View: desp_mensal_report, Registros: 4

**[10:07:36]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[10:07:36]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Descrição': 'Aluguel do Apto de Ipanema', 'Valor': '3.125,00', 'Vencimento': '05/10/20025', 'Pagamento': '', 'Observação': 'Se pagar atrasado tem juros'}, {'Descrição': 'Caroline Buterine', 'Valor': '500,00', 'Vencimento': '05/10/20025', 'Pagamento': '', 'Observação': 'Pgto mensal Clinica Buterine'}, {'Descrição': 'Pagamento Cartão VISA', 'Valor': '1.700,00', 'Vencimento': '16/10/2025', 'Pagamento': '', 'Observação': ''}, {'Descrição': 'Pagamento Cartão MASTERCARD', 'Valor': '3.200,00', 'Vencimento': '26/10/2025', 'Pagamento': '', 'Observação': 'Vencimento em todo di 26 do mes'}, {'Descrição': 'Pgto cta VIVO', 'Valor': '331,00', 'Vencimento': '10/10/2025', 'Pagamento': '', 'Observação': ''}, {'Descrição': 'Pgto Conta de Luz Ap. Ipa', 'Valor': '95,00', 'Vencimento': '08/10/2025', 'Pagamento': '', 'Observação': 'Conta Light'}, {'Descrição': 'Conta de Gás - Naturgy', 'Valor': '65,00', 'Vencimento': '10/10/2025', 'Pagamento': '', 'Observação': ''}, {'Descrição': 'Prevent Senior', 'Valor': '1.350,00', 'Vencimento': '30/10/2025', 'Pagamento': '', 'Observação': 'Plano Prevent'}, {'Descrição': 'Pagto Lucinha - INSS', 'Valor': '800,00', 'Vencimento': '15/10/2025', 'Pagamento': '', 'Observação': 'Vl. mensal '}, {'Descrição': 'Pgto Lucinha - POLICON', 'Valor': '228,00', 'Vencimento': '10/10/20025', 'Pagamento': '', 'Observação': '2 planos'}, {'Descrição': 'Limpeza do apto', 'Valor': '340,00', 'Vencimento': '25/10/2025', 'Pagamento': '', 'Observação': 'Incluso UBER estimado R$ 140,00'}, {'Descrição': 'Pgto Curso MBA', 'Valor': '370,00', 'Vencimento': '10/10/2025', 'Pagamento': '', 'Observação': 'MBA Mercado de Capitais - UCB'}], 'erro': None, 'sucesso': True, 'total_registros': 12}, 'mensagem': 'sucesso'}

**[10:10:17]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[10:10:17]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[10:10:17]** 🔄 **FLOW:** Consultando view: desp_mensal_report com campos: ['Todos']

**[10:10:17]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[10:10:17]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 12}
```

**[10:10:17]** 🔄 **FLOW:** Consulta executada - View: desp_mensal_report, Registros: 4

**[10:10:17]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[10:10:17]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Descrição': 'Aluguel do Apto de Ipanema', 'Valor': '3.125,00', 'Vencimento': '05/10/20025', 'Pagamento': '', 'Observação': 'Se pagar atrasado tem juros'}, {'Descrição': 'Caroline Buterine', 'Valor': '500,00', 'Vencimento': '05/10/20025', 'Pagamento': '', 'Observação': 'Pgto mensal Clinica Buterine'}, {'Descrição': 'Pagamento Cartão VISA', 'Valor': '1.700,00', 'Vencimento': '16/10/2025', 'Pagamento': '', 'Observação': ''}, {'Descrição': 'Pagamento Cartão MASTERCARD', 'Valor': '3.200,00', 'Vencimento': '26/10/2025', 'Pagamento': '', 'Observação': 'Vencimento em todo di 26 do mes'}, {'Descrição': 'Pgto cta VIVO', 'Valor': '331,00', 'Vencimento': '10/10/2025', 'Pagamento': '', 'Observação': ''}, {'Descrição': 'Pgto Conta de Luz Ap. Ipa', 'Valor': '95,00', 'Vencimento': '08/10/2025', 'Pagamento': '', 'Observação': 'Conta Light'}, {'Descrição': 'Conta de Gás - Naturgy', 'Valor': '65,00', 'Vencimento': '10/10/2025', 'Pagamento': '', 'Observação': ''}, {'Descrição': 'Prevent Senior', 'Valor': '1.350,00', 'Vencimento': '30/10/2025', 'Pagamento': '', 'Observação': 'Plano Prevent'}, {'Descrição': 'Pagto Lucinha - INSS', 'Valor': '800,00', 'Vencimento': '15/10/2025', 'Pagamento': '', 'Observação': 'Vl. mensal '}, {'Descrição': 'Pgto Lucinha - POLICON', 'Valor': '228,00', 'Vencimento': '10/10/20025', 'Pagamento': '', 'Observação': '2 planos'}, {'Descrição': 'Limpeza do apto', 'Valor': '340,00', 'Vencimento': '25/10/2025', 'Pagamento': '', 'Observação': 'Incluso UBER estimado R$ 140,00'}, {'Descrição': 'Pgto Curso MBA', 'Valor': '370,00', 'Vencimento': '10/10/2025', 'Pagamento': '', 'Observação': 'MBA Mercado de Capitais - UCB'}], 'erro': None, 'sucesso': True, 'total_registros': 12}, 'mensagem': 'sucesso'}

**[10:24:40]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[10:24:40]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[10:24:41]** 🔄 **FLOW:** Consultando view: desp_mensal_report com campos: ['Todos']

**[10:24:41]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[10:24:41]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 12}
```

**[10:24:41]** 🔄 **FLOW:** Consulta executada - View: desp_mensal_report, Registros: 4

**[10:24:41]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[10:24:41]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Descrição': 'Aluguel do Apto de Ipanema', 'Valor': '3.125,00', 'Vencimento': '05/10/20025', 'Pagamento': '', 'Observação': 'Se pagar atrasado tem juros'}, {'Descrição': 'Caroline Buterine', 'Valor': '500,00', 'Vencimento': '05/10/20025', 'Pagamento': '', 'Observação': 'Pgto mensal Clinica Buterine'}, {'Descrição': 'Pagamento Cartão VISA', 'Valor': '1.700,00', 'Vencimento': '16/10/2025', 'Pagamento': '', 'Observação': ''}, {'Descrição': 'Pagamento Cartão MASTERCARD', 'Valor': '3.200,00', 'Vencimento': '26/10/2025', 'Pagamento': '', 'Observação': 'Vencimento em todo di 26 do mes'}, {'Descrição': 'Pgto cta VIVO', 'Valor': '331,00', 'Vencimento': '10/10/2025', 'Pagamento': '', 'Observação': ''}, {'Descrição': 'Pgto Conta de Luz Ap. Ipa', 'Valor': '95,00', 'Vencimento': '08/10/2025', 'Pagamento': '', 'Observação': 'Conta Light'}, {'Descrição': 'Conta de Gás - Naturgy', 'Valor': '65,00', 'Vencimento': '10/10/2025', 'Pagamento': '', 'Observação': ''}, {'Descrição': 'Prevent Senior', 'Valor': '1.350,00', 'Vencimento': '30/10/2025', 'Pagamento': '', 'Observação': 'Plano Prevent'}, {'Descrição': 'Pagto Lucinha - INSS', 'Valor': '800,00', 'Vencimento': '15/10/2025', 'Pagamento': '', 'Observação': 'Vl. mensal '}, {'Descrição': 'Pgto Lucinha - POLICON', 'Valor': '228,00', 'Vencimento': '10/10/20025', 'Pagamento': '', 'Observação': '2 planos'}, {'Descrição': 'Limpeza do apto', 'Valor': '340,00', 'Vencimento': '25/10/2025', 'Pagamento': '', 'Observação': 'Incluso UBER estimado R$ 140,00'}, {'Descrição': 'Pgto Curso MBA', 'Valor': '370,00', 'Vencimento': '10/10/2025', 'Pagamento': '', 'Observação': 'MBA Mercado de Capitais - UCB'}], 'erro': None, 'sucesso': True, 'total_registros': 12}, 'mensagem': 'sucesso'}

**[10:47:20]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[10:47:20]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[10:47:20]** 🔄 **FLOW:** Consultando view: desp_mensal_report com campos: ['Todos']

**[10:47:20]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[10:47:20]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 12}
```

**[10:47:20]** 🔄 **FLOW:** Consulta executada - View: desp_mensal_report, Registros: 4

**[10:47:20]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[10:47:20]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Descrição': 'Aluguel do Apto de Ipanema', 'Valor': '3.125,00', 'Vencimento': '05/10/20025', 'Pagamento': '', 'Observação': 'Se pagar atrasado tem juros'}, {'Descrição': 'Caroline Buterine', 'Valor': '500,00', 'Vencimento': '05/10/20025', 'Pagamento': '', 'Observação': 'Pgto mensal Clinica Buterine'}, {'Descrição': 'Pagamento Cartão VISA', 'Valor': '1.700,00', 'Vencimento': '16/10/2025', 'Pagamento': '', 'Observação': ''}, {'Descrição': 'Pagamento Cartão MASTERCARD', 'Valor': '3.200,00', 'Vencimento': '26/10/2025', 'Pagamento': '', 'Observação': 'Vencimento em todo di 26 do mes'}, {'Descrição': 'Pgto cta VIVO', 'Valor': '331,00', 'Vencimento': '10/10/2025', 'Pagamento': '', 'Observação': ''}, {'Descrição': 'Pgto Conta de Luz Ap. Ipa', 'Valor': '95,00', 'Vencimento': '08/10/2025', 'Pagamento': '', 'Observação': 'Conta Light'}, {'Descrição': 'Conta de Gás - Naturgy', 'Valor': '65,00', 'Vencimento': '10/10/2025', 'Pagamento': '', 'Observação': ''}, {'Descrição': 'Prevent Senior', 'Valor': '1.350,00', 'Vencimento': '30/10/2025', 'Pagamento': '', 'Observação': 'Plano Prevent'}, {'Descrição': 'Pagto Lucinha - INSS', 'Valor': '800,00', 'Vencimento': '15/10/2025', 'Pagamento': '', 'Observação': 'Vl. mensal '}, {'Descrição': 'Pgto Lucinha - POLICON', 'Valor': '228,00', 'Vencimento': '10/10/20025', 'Pagamento': '', 'Observação': '2 planos'}, {'Descrição': 'Limpeza do apto', 'Valor': '340,00', 'Vencimento': '25/10/2025', 'Pagamento': '', 'Observação': 'Incluso UBER estimado R$ 140,00'}, {'Descrição': 'Pgto Curso MBA', 'Valor': '370,00', 'Vencimento': '10/10/2025', 'Pagamento': '', 'Observação': 'MBA Mercado de Capitais - UCB'}], 'erro': None, 'sucesso': True, 'total_registros': 12}, 'mensagem': 'sucesso'}

**[19:09:07]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[19:09:07]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[19:09:07]** 🔄 **FLOW:** Consultando view: desp_mensal_report com campos: ['Todos']

**[19:09:07]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[19:09:07]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 12}
```

**[19:09:07]** 🔄 **FLOW:** Consulta executada - View: desp_mensal_report, Registros: 4

**[19:09:07]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[19:09:07]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Descrição': 'Aluguel do Apto de Ipanema', 'Valor': '3.125,00', 'Vencimento': '05/10/20025', 'Pagamento': '', 'Observação': 'Se pagar atrasado tem juros'}, {'Descrição': 'Caroline Buterine', 'Valor': '500,00', 'Vencimento': '05/10/20025', 'Pagamento': '', 'Observação': 'Pgto mensal Clinica Buterine'}, {'Descrição': 'Pagamento Cartão VISA', 'Valor': '1.700,00', 'Vencimento': '16/10/2025', 'Pagamento': '', 'Observação': ''}, {'Descrição': 'Pagamento Cartão MASTERCARD', 'Valor': '3.200,00', 'Vencimento': '26/10/2025', 'Pagamento': '', 'Observação': 'Vencimento em todo di 26 do mes'}, {'Descrição': 'Pgto cta VIVO', 'Valor': '331,00', 'Vencimento': '10/10/2025', 'Pagamento': '', 'Observação': ''}, {'Descrição': 'Pgto Conta de Luz Ap. Ipa', 'Valor': '95,00', 'Vencimento': '08/10/2025', 'Pagamento': '', 'Observação': 'Conta Light'}, {'Descrição': 'Conta de Gás - Naturgy', 'Valor': '65,00', 'Vencimento': '10/10/2025', 'Pagamento': '', 'Observação': ''}, {'Descrição': 'Prevent Senior', 'Valor': '1.350,00', 'Vencimento': '30/10/2025', 'Pagamento': '', 'Observação': 'Plano Prevent'}, {'Descrição': 'Pagto Lucinha - INSS', 'Valor': '800,00', 'Vencimento': '15/10/2025', 'Pagamento': '', 'Observação': 'Vl. mensal '}, {'Descrição': 'Pgto Lucinha - POLICON', 'Valor': '228,00', 'Vencimento': '10/10/20025', 'Pagamento': '', 'Observação': '2 planos'}, {'Descrição': 'Limpeza do apto', 'Valor': '340,00', 'Vencimento': '25/10/2025', 'Pagamento': '', 'Observação': 'Incluso UBER estimado R$ 140,00'}, {'Descrição': 'Pgto Curso MBA', 'Valor': '370,00', 'Vencimento': '10/10/2025', 'Pagamento': '', 'Observação': 'MBA Mercado de Capitais - UCB'}], 'erro': None, 'sucesso': True, 'total_registros': 12}, 'mensagem': 'sucesso'}

**[19:09:09]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[19:09:09]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[19:09:09]** 🔄 **FLOW:** Consultando view: desp_mensal_report com campos: ['Todos']

**[19:09:09]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[19:09:09]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 12}
```

**[19:09:09]** 🔄 **FLOW:** Consulta executada - View: desp_mensal_report, Registros: 4

**[19:09:09]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[19:09:09]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Descrição': 'Aluguel do Apto de Ipanema', 'Valor': '3.125,00', 'Vencimento': '05/10/20025', 'Pagamento': '', 'Observação': 'Se pagar atrasado tem juros'}, {'Descrição': 'Caroline Buterine', 'Valor': '500,00', 'Vencimento': '05/10/20025', 'Pagamento': '', 'Observação': 'Pgto mensal Clinica Buterine'}, {'Descrição': 'Pagamento Cartão VISA', 'Valor': '1.700,00', 'Vencimento': '16/10/2025', 'Pagamento': '', 'Observação': ''}, {'Descrição': 'Pagamento Cartão MASTERCARD', 'Valor': '3.200,00', 'Vencimento': '26/10/2025', 'Pagamento': '', 'Observação': 'Vencimento em todo di 26 do mes'}, {'Descrição': 'Pgto cta VIVO', 'Valor': '331,00', 'Vencimento': '10/10/2025', 'Pagamento': '', 'Observação': ''}, {'Descrição': 'Pgto Conta de Luz Ap. Ipa', 'Valor': '95,00', 'Vencimento': '08/10/2025', 'Pagamento': '', 'Observação': 'Conta Light'}, {'Descrição': 'Conta de Gás - Naturgy', 'Valor': '65,00', 'Vencimento': '10/10/2025', 'Pagamento': '', 'Observação': ''}, {'Descrição': 'Prevent Senior', 'Valor': '1.350,00', 'Vencimento': '30/10/2025', 'Pagamento': '', 'Observação': 'Plano Prevent'}, {'Descrição': 'Pagto Lucinha - INSS', 'Valor': '800,00', 'Vencimento': '15/10/2025', 'Pagamento': '', 'Observação': 'Vl. mensal '}, {'Descrição': 'Pgto Lucinha - POLICON', 'Valor': '228,00', 'Vencimento': '10/10/20025', 'Pagamento': '', 'Observação': '2 planos'}, {'Descrição': 'Limpeza do apto', 'Valor': '340,00', 'Vencimento': '25/10/2025', 'Pagamento': '', 'Observação': 'Incluso UBER estimado R$ 140,00'}, {'Descrição': 'Pgto Curso MBA', 'Valor': '370,00', 'Vencimento': '10/10/2025', 'Pagamento': '', 'Observação': 'MBA Mercado de Capitais - UCB'}], 'erro': None, 'sucesso': True, 'total_registros': 12}, 'mensagem': 'sucesso'}

**[19:14:06]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[19:14:06]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[19:14:06]** 🔄 **FLOW:** Consultando view: desp_mensal_report com campos: ['Todos']

**[19:14:06]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[19:14:06]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 12}
```

**[19:14:06]** 🔄 **FLOW:** Consulta executada - View: desp_mensal_report, Registros: 4

**[19:14:06]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[19:14:06]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Descrição': 'Aluguel do Apto de Ipanema', 'Valor': '3.125,00', 'Vencimento': '05/10/20025', 'Pagamento': '', 'Observação': 'Se pagar atrasado tem juros'}, {'Descrição': 'Caroline Buterine', 'Valor': '500,00', 'Vencimento': '05/10/20025', 'Pagamento': '', 'Observação': 'Pgto mensal Clinica Buterine'}, {'Descrição': 'Pagamento Cartão VISA', 'Valor': '1.700,00', 'Vencimento': '16/10/2025', 'Pagamento': '', 'Observação': ''}, {'Descrição': 'Pagamento Cartão MASTERCARD', 'Valor': '3.200,00', 'Vencimento': '26/10/2025', 'Pagamento': '', 'Observação': 'Vencimento em todo di 26 do mes'}, {'Descrição': 'Pgto cta VIVO', 'Valor': '331,00', 'Vencimento': '10/10/2025', 'Pagamento': '', 'Observação': ''}, {'Descrição': 'Pgto Conta de Luz Ap. Ipa', 'Valor': '95,00', 'Vencimento': '08/10/2025', 'Pagamento': '', 'Observação': 'Conta Light'}, {'Descrição': 'Conta de Gás - Naturgy', 'Valor': '65,00', 'Vencimento': '10/10/2025', 'Pagamento': '', 'Observação': ''}, {'Descrição': 'Prevent Senior', 'Valor': '1.350,00', 'Vencimento': '30/10/2025', 'Pagamento': '', 'Observação': 'Plano Prevent'}, {'Descrição': 'Pagto Lucinha - INSS', 'Valor': '800,00', 'Vencimento': '15/10/2025', 'Pagamento': '', 'Observação': 'Vl. mensal '}, {'Descrição': 'Pgto Lucinha - POLICON', 'Valor': '228,00', 'Vencimento': '10/10/20025', 'Pagamento': '', 'Observação': '2 planos'}, {'Descrição': 'Limpeza do apto', 'Valor': '340,00', 'Vencimento': '25/10/2025', 'Pagamento': '', 'Observação': 'Incluso UBER estimado R$ 140,00'}, {'Descrição': 'Pgto Curso MBA', 'Valor': '370,00', 'Vencimento': '10/10/2025', 'Pagamento': '', 'Observação': 'MBA Mercado de Capitais - UCB'}], 'erro': None, 'sucesso': True, 'total_registros': 12}, 'mensagem': 'sucesso'}

**[19:16:17]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[19:16:17]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[19:16:17]** 🔄 **FLOW:** Consultando view: desp_mensal_report com campos: ['Todos']

**[19:16:17]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[19:16:17]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 12}
```

**[19:16:17]** 🔄 **FLOW:** Consulta executada - View: desp_mensal_report, Registros: 4

**[19:16:17]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[19:16:17]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Descrição': 'Aluguel do Apto de Ipanema', 'Valor': '3.125,00', 'Vencimento': '05/10/20025', 'Pagamento': '', 'Observação': 'Se pagar atrasado tem juros'}, {'Descrição': 'Caroline Buterine', 'Valor': '500,00', 'Vencimento': '05/10/20025', 'Pagamento': '', 'Observação': 'Pgto mensal Clinica Buterine'}, {'Descrição': 'Pagamento Cartão VISA', 'Valor': '1.700,00', 'Vencimento': '16/10/2025', 'Pagamento': '', 'Observação': ''}, {'Descrição': 'Pagamento Cartão MASTERCARD', 'Valor': '3.200,00', 'Vencimento': '26/10/2025', 'Pagamento': '', 'Observação': 'Vencimento em todo di 26 do mes'}, {'Descrição': 'Pgto cta VIVO', 'Valor': '331,00', 'Vencimento': '10/10/2025', 'Pagamento': '', 'Observação': ''}, {'Descrição': 'Pgto Conta de Luz Ap. Ipa', 'Valor': '95,00', 'Vencimento': '08/10/2025', 'Pagamento': '', 'Observação': 'Conta Light'}, {'Descrição': 'Conta de Gás - Naturgy', 'Valor': '65,00', 'Vencimento': '10/10/2025', 'Pagamento': '', 'Observação': ''}, {'Descrição': 'Prevent Senior', 'Valor': '1.350,00', 'Vencimento': '30/10/2025', 'Pagamento': '', 'Observação': 'Plano Prevent'}, {'Descrição': 'Pagto Lucinha - INSS', 'Valor': '800,00', 'Vencimento': '15/10/2025', 'Pagamento': '', 'Observação': 'Vl. mensal '}, {'Descrição': 'Pgto Lucinha - POLICON', 'Valor': '228,00', 'Vencimento': '10/10/20025', 'Pagamento': '', 'Observação': '2 planos'}, {'Descrição': 'Limpeza do apto', 'Valor': '340,00', 'Vencimento': '25/10/2025', 'Pagamento': '', 'Observação': 'Incluso UBER estimado R$ 140,00'}, {'Descrição': 'Pgto Curso MBA', 'Valor': '370,00', 'Vencimento': '10/10/2025', 'Pagamento': '', 'Observação': 'MBA Mercado de Capitais - UCB'}], 'erro': None, 'sucesso': True, 'total_registros': 12}, 'mensagem': 'sucesso'}

**[19:18:46]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[19:18:46]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[19:18:46]** 🔄 **FLOW:** Consultando view: desp_mensal_report com campos: ['Todos']

**[19:18:46]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[19:18:46]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 12}
```

**[19:18:46]** 🔄 **FLOW:** Consulta executada - View: desp_mensal_report, Registros: 4

**[19:18:46]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[19:18:46]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Descrição': 'Aluguel do Apto de Ipanema', 'Valor': '3.125,00', 'Vencimento': '05/10/20025', 'Pagamento': '', 'Observação': 'Se pagar atrasado tem juros'}, {'Descrição': 'Caroline Buterine', 'Valor': '500,00', 'Vencimento': '05/10/20025', 'Pagamento': '', 'Observação': 'Pgto mensal Clinica Buterine'}, {'Descrição': 'Pagamento Cartão VISA', 'Valor': '1.700,00', 'Vencimento': '16/10/2025', 'Pagamento': '', 'Observação': ''}, {'Descrição': 'Pagamento Cartão MASTERCARD', 'Valor': '3.200,00', 'Vencimento': '26/10/2025', 'Pagamento': '', 'Observação': 'Vencimento em todo di 26 do mes'}, {'Descrição': 'Pgto cta VIVO', 'Valor': '331,00', 'Vencimento': '10/10/2025', 'Pagamento': '', 'Observação': ''}, {'Descrição': 'Pgto Conta de Luz Ap. Ipa', 'Valor': '95,00', 'Vencimento': '08/10/2025', 'Pagamento': '', 'Observação': 'Conta Light'}, {'Descrição': 'Conta de Gás - Naturgy', 'Valor': '65,00', 'Vencimento': '10/10/2025', 'Pagamento': '', 'Observação': ''}, {'Descrição': 'Prevent Senior', 'Valor': '1.350,00', 'Vencimento': '30/10/2025', 'Pagamento': '', 'Observação': 'Plano Prevent'}, {'Descrição': 'Pagto Lucinha - INSS', 'Valor': '800,00', 'Vencimento': '15/10/2025', 'Pagamento': '', 'Observação': 'Vl. mensal '}, {'Descrição': 'Pgto Lucinha - POLICON', 'Valor': '228,00', 'Vencimento': '10/10/20025', 'Pagamento': '', 'Observação': '2 planos'}, {'Descrição': 'Limpeza do apto', 'Valor': '340,00', 'Vencimento': '25/10/2025', 'Pagamento': '', 'Observação': 'Incluso UBER estimado R$ 140,00'}, {'Descrição': 'Pgto Curso MBA', 'Valor': '370,00', 'Vencimento': '10/10/2025', 'Pagamento': '', 'Observação': 'MBA Mercado de Capitais - UCB'}], 'erro': None, 'sucesso': True, 'total_registros': 12}, 'mensagem': 'sucesso'}

**[19:27:24]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[19:27:24]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[19:27:24]** 🔄 **FLOW:** Consultando view: desp_mensal_report com campos: ['Todos']

**[19:27:24]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[19:27:24]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 12}
```

**[19:27:24]** 🔄 **FLOW:** Consulta executada - View: desp_mensal_report, Registros: 4

**[19:27:24]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[19:27:24]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Descrição': 'Aluguel do Apto de Ipanema', 'Valor': '3.125,00', 'Vencimento': '05/10/20025', 'Pagamento': '', 'Observação': 'Se pagar atrasado tem juros'}, {'Descrição': 'Caroline Buterine', 'Valor': '500,00', 'Vencimento': '05/10/20025', 'Pagamento': '', 'Observação': 'Pgto mensal Clinica Buterine'}, {'Descrição': 'Pagamento Cartão VISA', 'Valor': '1.700,00', 'Vencimento': '16/10/2025', 'Pagamento': '', 'Observação': ''}, {'Descrição': 'Pagamento Cartão MASTERCARD', 'Valor': '3.200,00', 'Vencimento': '26/10/2025', 'Pagamento': '', 'Observação': 'Vencimento em todo di 26 do mes'}, {'Descrição': 'Pgto cta VIVO', 'Valor': '331,00', 'Vencimento': '10/10/2025', 'Pagamento': '', 'Observação': ''}, {'Descrição': 'Pgto Conta de Luz Ap. Ipa', 'Valor': '95,00', 'Vencimento': '08/10/2025', 'Pagamento': '', 'Observação': 'Conta Light'}, {'Descrição': 'Conta de Gás - Naturgy', 'Valor': '65,00', 'Vencimento': '10/10/2025', 'Pagamento': '', 'Observação': ''}, {'Descrição': 'Prevent Senior', 'Valor': '1.350,00', 'Vencimento': '30/10/2025', 'Pagamento': '', 'Observação': 'Plano Prevent'}, {'Descrição': 'Pagto Lucinha - INSS', 'Valor': '800,00', 'Vencimento': '15/10/2025', 'Pagamento': '', 'Observação': 'Vl. mensal '}, {'Descrição': 'Pgto Lucinha - POLICON', 'Valor': '228,00', 'Vencimento': '10/10/20025', 'Pagamento': '', 'Observação': '2 planos'}, {'Descrição': 'Limpeza do apto', 'Valor': '340,00', 'Vencimento': '25/10/2025', 'Pagamento': '', 'Observação': 'Incluso UBER estimado R$ 140,00'}, {'Descrição': 'Pgto Curso MBA', 'Valor': '370,00', 'Vencimento': '10/10/2025', 'Pagamento': '', 'Observação': 'MBA Mercado de Capitais - UCB'}], 'erro': None, 'sucesso': True, 'total_registros': 12}, 'mensagem': 'sucesso'}

**[20:28:39]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[20:28:39]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[20:28:39]** 🔄 **FLOW:** Consultando view: desp_mensal_report com campos: ['Todos']

**[20:28:39]** ❌ **ERRO:** View/Tabela não encontrada: desp_mensal_report  
```
Tipo: str
Mensagem: Banco: c:\Applications_DSB\FinCtl\data\financas.db
```

**[20:28:39]** 🔄 **FLOW:** Consulta executada - View: desp_mensal_report, Registros: 3

**[20:28:39]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 3 registros

**[20:28:39]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [], 'erro': "Tabela/view 'desp_mensal_report' não encontrada no banco de dados", 'sucesso': False}, 'mensagem': 'sucesso'}

**[20:28:41]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[20:28:41]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[20:28:41]** 🔄 **FLOW:** Consultando view: desp_mensal_report com campos: ['Todos']

**[20:28:41]** ❌ **ERRO:** View/Tabela não encontrada: desp_mensal_report  
```
Tipo: str
Mensagem: Banco: c:\Applications_DSB\FinCtl\data\financas.db
```

**[20:28:41]** 🔄 **FLOW:** Consulta executada - View: desp_mensal_report, Registros: 3

**[20:28:41]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 3 registros

**[20:28:41]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [], 'erro': "Tabela/view 'desp_mensal_report' não encontrada no banco de dados", 'sucesso': False}, 'mensagem': 'sucesso'}

**[20:28:41]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[20:28:41]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[20:28:41]** 🔄 **FLOW:** Consultando view: desp_mensal_report com campos: ['Todos']

**[20:28:41]** ❌ **ERRO:** View/Tabela não encontrada: desp_mensal_report  
```
Tipo: str
Mensagem: Banco: c:\Applications_DSB\FinCtl\data\financas.db
```

**[20:28:41]** 🔄 **FLOW:** Consulta executada - View: desp_mensal_report, Registros: 3

**[20:28:41]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 3 registros

**[20:28:41]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [], 'erro': "Tabela/view 'desp_mensal_report' não encontrada no banco de dados", 'sucesso': False}, 'mensagem': 'sucesso'}

**[20:29:13]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[20:29:13]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[20:29:13]** 🔄 **FLOW:** Consultando view: desp_mensal_report com campos: ['Todos']

**[20:29:13]** ❌ **ERRO:** View/Tabela não encontrada: desp_mensal_report  
```
Tipo: str
Mensagem: Banco: c:\Applications_DSB\FinCtl\data\financas.db
```

**[20:29:13]** 🔄 **FLOW:** Consulta executada - View: desp_mensal_report, Registros: 3

**[20:29:13]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 3 registros

**[20:29:13]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [], 'erro': "Tabela/view 'desp_mensal_report' não encontrada no banco de dados", 'sucesso': False}, 'mensagem': 'sucesso'}

**[20:29:21]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[20:29:21]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[20:29:21]** 🔄 **FLOW:** Consultando view: desp_mensal_report com campos: ['Todos']

**[20:29:21]** ❌ **ERRO:** View/Tabela não encontrada: desp_mensal_report  
```
Tipo: str
Mensagem: Banco: c:\Applications_DSB\FinCtl\data\financas.db
```

**[20:29:21]** 🔄 **FLOW:** Consulta executada - View: desp_mensal_report, Registros: 3

**[20:29:21]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 3 registros

**[20:29:21]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [], 'erro': "Tabela/view 'desp_mensal_report' não encontrada no banco de dados", 'sucesso': False}, 'mensagem': 'sucesso'}

**[20:29:37]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[20:29:37]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'grupos_view', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': 'c:\\Applications_DSB\\FinCtl', 'filtros': ''}
```

**[20:29:37]** 🔄 **FLOW:** Consultando view: grupos_view com campos: ['Todos']

**[20:29:37]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'grupos_view', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[20:29:37]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 12}
```

**[20:29:37]** 🔄 **FLOW:** Consulta executada - View: grupos_view, Registros: 4

**[20:29:37]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[20:29:37]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'idgrupo': 1, 'grupo': 'Alimentação', 'descricao': 'Grupo de classificação: Alimentação'}, {'idgrupo': 10, 'grupo': 'Aluguel', 'descricao': 'aluguel do aluguel do aluguel é mais e mais'}, {'idgrupo': 2, 'grupo': 'Educação', 'descricao': 'Grupo de classificação: Educação'}, {'idgrupo': 3, 'grupo': 'Financas', 'descricao': 'Grupo de classificação: FinancasSSZZ'}, {'idgrupo': 12, 'grupo': 'Jurubeba', 'descricao': 'Gerimum e gléia de Gerimum'}, {'idgrupo': 4, 'grupo': 'Lazer', 'descricao': 'Grupo de classificação: Lazer'}, {'idgrupo': 5, 'grupo': 'Moradia', 'descricao': 'Grupo de classificação: Moradia'}, {'idgrupo': 6, 'grupo': 'Outros', 'descricao': 'Grupo de classificação: Outros'}, {'idgrupo': 7, 'grupo': 'Saúde', 'descricao': 'Grupo de classificação: Saúde'}, {'idgrupo': 8, 'grupo': 'Transporte', 'descricao': 'Grupo de classificação: Transporte'}, {'idgrupo': 11, 'grupo': 'wwwww22345', 'descricao': 'q1qa23333'}, {'idgrupo': 9, 'grupo': 'wwwwww', 'descricao': '343rr3r3r'}], 'erro': None, 'sucesso': True, 'total_registros': 12}, 'mensagem': 'sucesso'}

**[20:29:45]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[20:29:45]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[20:29:45]** 🔄 **FLOW:** Consultando view: desp_mensal_report com campos: ['Todos']

**[20:29:45]** ❌ **ERRO:** View/Tabela não encontrada: desp_mensal_report  
```
Tipo: str
Mensagem: Banco: c:\Applications_DSB\FinCtl\data\financas.db
```

**[20:29:45]** 🔄 **FLOW:** Consulta executada - View: desp_mensal_report, Registros: 3

**[20:29:45]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 3 registros

**[20:29:45]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [], 'erro': "Tabela/view 'desp_mensal_report' não encontrada no banco de dados", 'sucesso': False}, 'mensagem': 'sucesso'}

**[20:30:26]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[20:30:26]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': '', 'filtros': ''}
```

**[20:30:26]** 🔄 **FLOW:** Consultando view: desp_mensal_report com campos: ['Todos']

**[20:30:26]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'desp_mensal_report', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[20:30:26]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 12}
```

**[20:30:26]** 🔄 **FLOW:** Consulta executada - View: desp_mensal_report, Registros: 4

**[20:30:26]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[20:30:26]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'Descrição': 'Aluguel do Apto de Ipanema', 'Valor': '3.125,00', 'Vencimento': '05/10/20025', 'Pagamento': 'N', 'Observação': 'Se pagar atrasado tem juros'}, {'Descrição': 'Caroline Buterine', 'Valor': '500,00', 'Vencimento': '05/10/20025', 'Pagamento': 'N', 'Observação': 'Pgto mensal Clinica Buterine'}, {'Descrição': 'Pagamento Cartão VISA', 'Valor': '1.700,00', 'Vencimento': '16/10/2025', 'Pagamento': 'N', 'Observação': ''}, {'Descrição': 'Pagamento Cartão MASTERCARD', 'Valor': '3.200,00', 'Vencimento': '26/10/2025', 'Pagamento': 'N', 'Observação': 'Vencimento em todo di 26 do mes'}, {'Descrição': 'Pgto cta VIVO', 'Valor': '331,00', 'Vencimento': '10/10/2025', 'Pagamento': 'N', 'Observação': ''}, {'Descrição': 'Pgto Conta de Luz Ap. Ipa', 'Valor': '95,00', 'Vencimento': '08/10/2025', 'Pagamento': 'N', 'Observação': 'Conta Light'}, {'Descrição': 'Conta de Gás - Naturgy', 'Valor': '65,00', 'Vencimento': '10/10/2025', 'Pagamento': 'N', 'Observação': ''}, {'Descrição': 'Prevent Senior', 'Valor': '1.350,00', 'Vencimento': '30/10/2025', 'Pagamento': 'N', 'Observação': 'Plano Prevent'}, {'Descrição': 'Pagto Lucinha - INSS', 'Valor': '800,00', 'Vencimento': '15/10/2025', 'Pagamento': 'N', 'Observação': 'Vl. mensal '}, {'Descrição': 'Pgto Lucinha - POLICON', 'Valor': '228,00', 'Vencimento': '10/10/20025', 'Pagamento': 'N', 'Observação': '2 planos'}, {'Descrição': 'Limpeza do apto', 'Valor': '340,00', 'Vencimento': '25/10/2025', 'Pagamento': 'N', 'Observação': 'Incluso UBER estimado R$ 140,00'}, {'Descrição': 'Pgto Curso MBA', 'Valor': '370,00', 'Vencimento': '10/10/2025', 'Pagamento': 'N', 'Observação': 'MBA Mercado de Capitais - UCB'}], 'erro': None, 'sucesso': True, 'total_registros': 12}, 'mensagem': 'sucesso'}

