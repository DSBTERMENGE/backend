# LOG DE ERROS DO BACKEND

**Sessão iniciada:** 26/09/2025 20:01:34  
**Sistema:** Python Backend  
**Arquivo:** Framework DSB  

---

**[20:02:14]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[20:02:14]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'grupos_view', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': 'c:\\Applications_DSB\\FinCtl', 'filtros': 'grupo=*'}
```

**[20:02:14]** 🔄 **FLOW:** Consultando view: grupos_view com campos: ['Todos']

**[20:02:14]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'grupos_view', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[20:02:14]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 12}
```

**[20:02:14]** 🔄 **FLOW:** Consulta executada - View: grupos_view, Registros: 4

**[20:02:14]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[20:02:14]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'idgrupo': 1, 'grupo': 'Alimentação', 'descricao': 'Grupo de classificação: Alimentação'}, {'idgrupo': 10, 'grupo': 'Aluguel', 'descricao': 'aluguel do aluguel do aluguel é mais e mais'}, {'idgrupo': 2, 'grupo': 'Educação', 'descricao': 'Grupo de classificação: Educação'}, {'idgrupo': 3, 'grupo': 'Financas', 'descricao': 'Grupo de classificação: FinancasSSZZ'}, {'idgrupo': 12, 'grupo': 'Jurubeba', 'descricao': 'Gerimum e gléia de Gerimum'}, {'idgrupo': 4, 'grupo': 'Lazer', 'descricao': 'Grupo de classificação: Lazer'}, {'idgrupo': 5, 'grupo': 'Moradia', 'descricao': 'Grupo de classificação: Moradia'}, {'idgrupo': 6, 'grupo': 'Outros', 'descricao': 'Grupo de classificação: Outros'}, {'idgrupo': 7, 'grupo': 'Saúde', 'descricao': 'Grupo de classificação: Saúde'}, {'idgrupo': 8, 'grupo': 'Transporte', 'descricao': 'Grupo de classificação: Transporte'}, {'idgrupo': 11, 'grupo': 'wwwww22345', 'descricao': 'q1qa23333'}, {'idgrupo': 9, 'grupo': 'wwwwww', 'descricao': '343rr3r3r'}], 'erro': None, 'sucesso': True, 'total_registros': 12}, 'mensagem': 'sucesso'}

**[20:02:17]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[20:02:17]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'subgrupos_view', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': 'c:\\Applications_DSB\\FinCtl', 'filtros': 'idgrupo=3'}
```

**[20:02:17]** 🔄 **FLOW:** Consultando view: subgrupos_view com campos: ['Todos']

**[20:02:17]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'subgrupos_view', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[20:02:17]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 1}
```

**[20:02:17]** 🔄 **FLOW:** Consulta executada - View: subgrupos_view, Registros: 4

**[20:02:17]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[20:02:17]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'idsubgrupo': '', 'idgrupo': '', 'subgrupo': '', 'descricao': '', 'dicasDeClassificacao': '', 'observacoes': '', 'data_criacao': '', 'data_atualizacao': ''}], 'erro': None, 'sucesso': True, 'total_registros': 1}, 'mensagem': 'sucesso'}

**[20:03:47]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[20:03:47]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'grupos_view', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': 'c:\\Applications_DSB\\FinCtl', 'filtros': 'grupo=*'}
```

**[20:03:47]** 🔄 **FLOW:** Consultando view: grupos_view com campos: ['Todos']

**[20:03:47]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'grupos_view', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[20:03:47]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 12}
```

**[20:03:47]** 🔄 **FLOW:** Consulta executada - View: grupos_view, Registros: 4

**[20:03:47]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[20:03:47]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'idgrupo': 1, 'grupo': 'Alimentação', 'descricao': 'Grupo de classificação: Alimentação'}, {'idgrupo': 10, 'grupo': 'Aluguel', 'descricao': 'aluguel do aluguel do aluguel é mais e mais'}, {'idgrupo': 2, 'grupo': 'Educação', 'descricao': 'Grupo de classificação: Educação'}, {'idgrupo': 3, 'grupo': 'Financas', 'descricao': 'Grupo de classificação: FinancasSSZZ'}, {'idgrupo': 12, 'grupo': 'Jurubeba', 'descricao': 'Gerimum e gléia de Gerimum'}, {'idgrupo': 4, 'grupo': 'Lazer', 'descricao': 'Grupo de classificação: Lazer'}, {'idgrupo': 5, 'grupo': 'Moradia', 'descricao': 'Grupo de classificação: Moradia'}, {'idgrupo': 6, 'grupo': 'Outros', 'descricao': 'Grupo de classificação: Outros'}, {'idgrupo': 7, 'grupo': 'Saúde', 'descricao': 'Grupo de classificação: Saúde'}, {'idgrupo': 8, 'grupo': 'Transporte', 'descricao': 'Grupo de classificação: Transporte'}, {'idgrupo': 11, 'grupo': 'wwwww22345', 'descricao': 'q1qa23333'}, {'idgrupo': 9, 'grupo': 'wwwwww', 'descricao': '343rr3r3r'}], 'erro': None, 'sucesso': True, 'total_registros': 12}, 'mensagem': 'sucesso'}

**[20:04:14]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[20:04:14]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'subgrupos_view', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': 'c:\\Applications_DSB\\FinCtl', 'filtros': 'idgrupo=3'}
```

**[20:04:14]** 🔄 **FLOW:** Consultando view: subgrupos_view com campos: ['Todos']

**[20:04:14]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'subgrupos_view', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[20:04:14]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 1}
```

**[20:04:14]** 🔄 **FLOW:** Consulta executada - View: subgrupos_view, Registros: 4

**[20:04:14]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[20:04:14]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'idsubgrupo': '', 'idgrupo': '', 'subgrupo': '', 'descricao': '', 'dicasDeClassificacao': '', 'observacoes': '', 'data_criacao': '', 'data_atualizacao': ''}], 'erro': None, 'sucesso': True, 'total_registros': 1}, 'mensagem': 'sucesso'}

**[20:06:38]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[20:06:38]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'subgrupos_view', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': 'c:\\Applications_DSB\\FinCtl', 'filtros': 'idgrupo=4'}
```

**[20:06:38]** 🔄 **FLOW:** Consultando view: subgrupos_view com campos: ['Todos']

**[20:06:38]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'subgrupos_view', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[20:06:38]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 1}
```

**[20:06:38]** 🔄 **FLOW:** Consulta executada - View: subgrupos_view, Registros: 4

**[20:06:38]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[20:06:38]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'idsubgrupo': '', 'idgrupo': '', 'subgrupo': '', 'descricao': '', 'dicasDeClassificacao': '', 'observacoes': '', 'data_criacao': '', 'data_atualizacao': ''}], 'erro': None, 'sucesso': True, 'total_registros': 1}, 'mensagem': 'sucesso'}

