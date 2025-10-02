**[14:40:00]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[14:40:00]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'grupos_view', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': 'c:\\Applications_DSB\\FinCtl', 'filtros': 'idgrupo = *'}
```

**[14:40:00]** 🔄 **FLOW:** Consultando view: grupos_view com campos: ['Todos']

**[14:40:00]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'grupos_view', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[14:40:00]** ❌ **ERRO:** Erro na função consultar_bd  
```
Tipo: OperationalError
Mensagem: near "*": syntax error
```  
**Stack Trace:**
```
  File "C:\Applications_DSB\framework_dsb\backend\source_code\data_manager.py", line 100, in consultar_bd
    cursor.execute(sql)

```

**[14:40:00]** 🔄 **FLOW:** Consulta executada - View: grupos_view, Registros: 4

**[14:40:00]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[14:40:00]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [], 'erro': 'Erro na consulta: near "*": syntax error', 'sucesso': False, 'total_registros': 0}, 'mensagem': 'sucesso'}

**[14:47:14]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[14:47:14]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'grupos_view', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': 'c:\\Applications_DSB\\FinCtl', 'filtros': 'idgrupo = *'}
```

**[14:47:14]** 🔄 **FLOW:** Consultando view: grupos_view com campos: ['Todos']

**[14:47:14]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'grupos_view', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[14:47:15]** ❌ **ERRO:** Erro na função consultar_bd  
```
Tipo: OperationalError
Mensagem: near "*": syntax error
```  
**Stack Trace:**
```
  File "C:\Applications_DSB\framework_dsb\backend\source_code\data_manager.py", line 100, in consultar_bd
    cursor.execute(sql)

```

**[14:47:15]** 🔄 **FLOW:** Consulta executada - View: grupos_view, Registros: 4

**[14:47:15]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[14:47:15]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [], 'erro': 'Erro na consulta: near "*": syntax error', 'sucesso': False, 'total_registros': 0}, 'mensagem': 'sucesso'}

**[14:49:19]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[14:49:19]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'grupos_view', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': 'c:\\Applications_DSB\\FinCtl', 'filtros': 'idgrupo = *'}
```

**[14:49:19]** 🔄 **FLOW:** Consultando view: grupos_view com campos: ['Todos']

**[14:49:19]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'grupos_view', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[14:49:19]** ❌ **ERRO:** Erro na função consultar_bd  
```
Tipo: OperationalError
Mensagem: near "*": syntax error
```  
**Stack Trace:**
```
  File "C:\Applications_DSB\framework_dsb\backend\source_code\data_manager.py", line 100, in consultar_bd
    cursor.execute(sql)

```

**[14:49:19]** 🔄 **FLOW:** Consulta executada - View: grupos_view, Registros: 4

**[14:49:19]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[14:49:19]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [], 'erro': 'Erro na consulta: near "*": syntax error', 'sucesso': False, 'total_registros': 0}, 'mensagem': 'sucesso'}

**[15:12:41]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[15:12:41]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'grupos_view', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': 'c:\\Applications_DSB\\FinCtl', 'filtros': ''}
```

**[15:12:41]** 🔄 **FLOW:** Consultando view: grupos_view com campos: ['Todos']

**[15:12:41]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'grupos_view', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[15:12:41]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 12}
```

**[15:12:41]** 🔄 **FLOW:** Consulta executada - View: grupos_view, Registros: 4

**[15:12:41]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[15:12:41]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'idgrupo': 1, 'grupo': 'Alimentação', 'descricao': 'Grupo de classificação: Alimentação'}, {'idgrupo': 10, 'grupo': 'Aluguel', 'descricao': 'aluguel do aluguel do aluguel é mais e mais'}, {'idgrupo': 2, 'grupo': 'Educação', 'descricao': 'Grupo de classificação: Educação'}, {'idgrupo': 3, 'grupo': 'Financas', 'descricao': 'Grupo de classificação: FinancasSSZZ'}, {'idgrupo': 12, 'grupo': 'Jurubeba', 'descricao': 'Gerimum e gléia de Gerimum'}, {'idgrupo': 4, 'grupo': 'Lazer', 'descricao': 'Grupo de classificação: Lazer'}, {'idgrupo': 5, 'grupo': 'Moradia', 'descricao': 'Grupo de classificação: Moradia'}, {'idgrupo': 6, 'grupo': 'Outros', 'descricao': 'Grupo de classificação: Outros'}, {'idgrupo': 7, 'grupo': 'Saúde', 'descricao': 'Grupo de classificação: Saúde'}, {'idgrupo': 8, 'grupo': 'Transporte', 'descricao': 'Grupo de classificação: Transporte'}, {'idgrupo': 11, 'grupo': 'wwwww22345', 'descricao': 'q1qa23333'}, {'idgrupo': 9, 'grupo': 'wwwwww', 'descricao': '343rr3r3r'}], 'erro': None, 'sucesso': True, 'total_registros': 12}, 'mensagem': 'sucesso'}

**[15:12:47]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[15:12:47]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'subgrupos_view', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': 'c:\\Applications_DSB\\FinCtl', 'filtros': 'idgrupo = 3'}
```

**[15:12:47]** 🔄 **FLOW:** Consultando view: subgrupos_view com campos: ['Todos']

**[15:12:47]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'subgrupos_view', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[15:12:47]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 1}
```

**[15:12:47]** 🔄 **FLOW:** Consulta executada - View: subgrupos_view, Registros: 4

**[15:12:47]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[15:12:48]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'idsubgrupo': 1, 'idgrupo': 3, 'subgrupo': 'sdsd', 'descricao': 'dddddddddddddddddd', 'dicasDeClassificacao': 'dddddddddddddddddddddddd', 'observacoes': 'ddddddddddddddddddddddddddd', 'data_criacao': '2025-09-29 10:43:28', 'data_atualizacao': '2025-09-29 10:43:28'}], 'erro': None, 'sucesso': True, 'total_registros': 1}, 'mensagem': 'sucesso'}

**[15:13:15]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[15:13:15]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'grupos_view', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': 'c:\\Applications_DSB\\FinCtl', 'filtros': ''}
```

**[15:13:15]** 🔄 **FLOW:** Consultando view: grupos_view com campos: ['Todos']

**[15:13:15]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'grupos_view', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[15:13:15]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 12}
```

**[15:13:15]** 🔄 **FLOW:** Consulta executada - View: grupos_view, Registros: 4

**[15:13:15]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[15:13:15]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'idgrupo': 1, 'grupo': 'Alimentação', 'descricao': 'Grupo de classificação: Alimentação'}, {'idgrupo': 10, 'grupo': 'Aluguel', 'descricao': 'aluguel do aluguel do aluguel é mais e mais'}, {'idgrupo': 2, 'grupo': 'Educação', 'descricao': 'Grupo de classificação: Educação'}, {'idgrupo': 3, 'grupo': 'Financas', 'descricao': 'Grupo de classificação: FinancasSSZZ'}, {'idgrupo': 12, 'grupo': 'Jurubeba', 'descricao': 'Gerimum e gléia de Gerimum'}, {'idgrupo': 4, 'grupo': 'Lazer', 'descricao': 'Grupo de classificação: Lazer'}, {'idgrupo': 5, 'grupo': 'Moradia', 'descricao': 'Grupo de classificação: Moradia'}, {'idgrupo': 6, 'grupo': 'Outros', 'descricao': 'Grupo de classificação: Outros'}, {'idgrupo': 7, 'grupo': 'Saúde', 'descricao': 'Grupo de classificação: Saúde'}, {'idgrupo': 8, 'grupo': 'Transporte', 'descricao': 'Grupo de classificação: Transporte'}, {'idgrupo': 11, 'grupo': 'wwwww22345', 'descricao': 'q1qa23333'}, {'idgrupo': 9, 'grupo': 'wwwwww', 'descricao': '343rr3r3r'}], 'erro': None, 'sucesso': True, 'total_registros': 12}, 'mensagem': 'sucesso'}

**[15:13:21]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[15:13:21]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'subgrupos_view', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': 'c:\\Applications_DSB\\FinCtl', 'filtros': 'idgrupo = 12'}
```

**[15:13:21]** 🔄 **FLOW:** Consultando view: subgrupos_view com campos: ['Todos']

**[15:13:21]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'subgrupos_view', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[15:13:21]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 1}
```

**[15:13:21]** 🔄 **FLOW:** Consulta executada - View: subgrupos_view, Registros: 4

**[15:13:21]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[15:13:21]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'idsubgrupo': '', 'idgrupo': '', 'subgrupo': '', 'descricao': '', 'dicasDeClassificacao': '', 'observacoes': '', 'data_criacao': '', 'data_atualizacao': ''}], 'erro': None, 'sucesso': True, 'total_registros': 1}, 'mensagem': 'sucesso'}

**[15:14:21]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[15:14:22]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'grupos_view', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': 'c:\\Applications_DSB\\FinCtl', 'filtros': ''}
```

**[15:14:22]** 🔄 **FLOW:** Consultando view: grupos_view com campos: ['Todos']

**[15:14:22]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'grupos_view', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[15:14:22]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 12}
```

**[15:14:22]** 🔄 **FLOW:** Consulta executada - View: grupos_view, Registros: 4

**[15:14:22]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[15:14:22]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'idgrupo': 1, 'grupo': 'Alimentação', 'descricao': 'Grupo de classificação: Alimentação'}, {'idgrupo': 10, 'grupo': 'Aluguel', 'descricao': 'aluguel do aluguel do aluguel é mais e mais'}, {'idgrupo': 2, 'grupo': 'Educação', 'descricao': 'Grupo de classificação: Educação'}, {'idgrupo': 3, 'grupo': 'Financas', 'descricao': 'Grupo de classificação: FinancasSSZZ'}, {'idgrupo': 12, 'grupo': 'Jurubeba', 'descricao': 'Gerimum e gléia de Gerimum'}, {'idgrupo': 4, 'grupo': 'Lazer', 'descricao': 'Grupo de classificação: Lazer'}, {'idgrupo': 5, 'grupo': 'Moradia', 'descricao': 'Grupo de classificação: Moradia'}, {'idgrupo': 6, 'grupo': 'Outros', 'descricao': 'Grupo de classificação: Outros'}, {'idgrupo': 7, 'grupo': 'Saúde', 'descricao': 'Grupo de classificação: Saúde'}, {'idgrupo': 8, 'grupo': 'Transporte', 'descricao': 'Grupo de classificação: Transporte'}, {'idgrupo': 11, 'grupo': 'wwwww22345', 'descricao': 'q1qa23333'}, {'idgrupo': 9, 'grupo': 'wwwwww', 'descricao': '343rr3r3r'}], 'erro': None, 'sucesso': True, 'total_registros': 12}, 'mensagem': 'sucesso'}

**[15:14:43]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[15:14:43]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'subgrupos_view', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': 'c:\\Applications_DSB\\FinCtl', 'filtros': 'idgrupo = 3'}
```

**[15:14:43]** 🔄 **FLOW:** Consultando view: subgrupos_view com campos: ['Todos']

**[15:14:43]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'subgrupos_view', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[15:14:43]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 1}
```

**[15:14:43]** 🔄 **FLOW:** Consulta executada - View: subgrupos_view, Registros: 4

**[15:14:43]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[15:14:43]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'idsubgrupo': 1, 'idgrupo': 3, 'subgrupo': 'sdsd', 'descricao': 'dddddddddddddddddd', 'dicasDeClassificacao': 'dddddddddddddddddddddddd', 'observacoes': 'ddddddddddddddddddddddddddd', 'data_criacao': '2025-09-29 10:43:28', 'data_atualizacao': '2025-09-29 10:43:28'}], 'erro': None, 'sucesso': True, 'total_registros': 1}, 'mensagem': 'sucesso'}

