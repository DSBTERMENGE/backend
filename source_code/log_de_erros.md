# LOG DE ERROS DO BACKEND

**Sessão iniciada:** 25/09/2025 19:01:08  
**Sistema:** Python Backend  
**Arquivo:** Framework DSB  

---

**[19:33:32]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[19:33:32]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'grupos_view', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': 'c:\\Applications_DSB\\FinCtl', 'filtros': 'grupo=*'}
```

**[19:33:32]** 🔄 **FLOW:** Consultando view: grupos_view com campos: ['Todos']

**[19:33:32]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'grupos_view', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[19:33:32]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 12}
```

**[19:33:32]** 🔄 **FLOW:** Consulta executada - View: grupos_view, Registros: 4

**[19:33:32]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[19:33:32]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'idgrupo': 1, 'grupo': 'Alimentação', 'descricao': 'Grupo de classificação: Alimentação'}, {'idgrupo': 10, 'grupo': 'Aluguel', 'descricao': 'aluguel do aluguel do aluguel é mais e mais'}, {'idgrupo': 2, 'grupo': 'Educação', 'descricao': 'Grupo de classificação: Educação'}, {'idgrupo': 3, 'grupo': 'Financas', 'descricao': 'Grupo de classificação: FinancasSSZZ'}, {'idgrupo': 12, 'grupo': 'Jurubeba', 'descricao': 'Gerimum e gléia de Gerimum'}, {'idgrupo': 4, 'grupo': 'Lazer', 'descricao': 'Grupo de classificação: Lazer'}, {'idgrupo': 5, 'grupo': 'Moradia', 'descricao': 'Grupo de classificação: Moradia'}, {'idgrupo': 6, 'grupo': 'Outros', 'descricao': 'Grupo de classificação: Outros'}, {'idgrupo': 7, 'grupo': 'Saúde', 'descricao': 'Grupo de classificação: Saúde'}, {'idgrupo': 8, 'grupo': 'Transporte', 'descricao': 'Grupo de classificação: Transporte'}, {'idgrupo': 11, 'grupo': 'wwwww22345', 'descricao': 'q1qa23333'}, {'idgrupo': 9, 'grupo': 'wwwwww', 'descricao': '343rr3r3r'}], 'erro': None, 'sucesso': True, 'total_registros': 12}, 'mensagem': 'sucesso'}

**[20:21:01]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[20:21:01]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'grupos_view', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': 'c:\\Applications_DSB\\FinCtl', 'filtros': 'grupo=*'}
```

**[20:21:01]** 🔄 **FLOW:** Consultando view: grupos_view com campos: ['Todos']

**[20:21:01]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'grupos_view', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[20:21:01]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 12}
```

**[20:21:01]** 🔄 **FLOW:** Consulta executada - View: grupos_view, Registros: 4

**[20:21:01]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[20:21:01]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'idgrupo': 1, 'grupo': 'Alimentação', 'descricao': 'Grupo de classificação: Alimentação'}, {'idgrupo': 10, 'grupo': 'Aluguel', 'descricao': 'aluguel do aluguel do aluguel é mais e mais'}, {'idgrupo': 2, 'grupo': 'Educação', 'descricao': 'Grupo de classificação: Educação'}, {'idgrupo': 3, 'grupo': 'Financas', 'descricao': 'Grupo de classificação: FinancasSSZZ'}, {'idgrupo': 12, 'grupo': 'Jurubeba', 'descricao': 'Gerimum e gléia de Gerimum'}, {'idgrupo': 4, 'grupo': 'Lazer', 'descricao': 'Grupo de classificação: Lazer'}, {'idgrupo': 5, 'grupo': 'Moradia', 'descricao': 'Grupo de classificação: Moradia'}, {'idgrupo': 6, 'grupo': 'Outros', 'descricao': 'Grupo de classificação: Outros'}, {'idgrupo': 7, 'grupo': 'Saúde', 'descricao': 'Grupo de classificação: Saúde'}, {'idgrupo': 8, 'grupo': 'Transporte', 'descricao': 'Grupo de classificação: Transporte'}, {'idgrupo': 11, 'grupo': 'wwwww22345', 'descricao': 'q1qa23333'}, {'idgrupo': 9, 'grupo': 'wwwwww', 'descricao': '343rr3r3r'}], 'erro': None, 'sucesso': True, 'total_registros': 12}, 'mensagem': 'sucesso'}

**[20:21:11]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[20:21:11]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': {'idgrupo': '10'}, 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': 'c:\\Applications_DSB\\FinCtl', 'filtros': 'grupo=*'}
```

**[20:21:11]** 🔄 **FLOW:** Consultando view: {'idgrupo': '10'} com campos: ['Todos']

**[20:21:11]** ❌ **ERRO:** Erro ao validar view/tabela: Error binding parameter 1: type 'dict' is not supported  
```
Tipo: str
Mensagem: View: {'idgrupo': '10'}, Banco: c:\Applications_DSB\FinCtl\data\financas.db
```

**[20:21:11]** 🔄 **FLOW:** Consulta executada - View: {'idgrupo': '10'}, Registros: 3

**[20:21:11]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 3 registros

**[20:21:11]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [], 'erro': "Tabela/view '{'idgrupo': '10'}' não encontrada no banco de dados", 'sucesso': False}, 'mensagem': 'sucesso'}

