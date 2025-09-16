# LOG DE ERROS DO BACKEND

**Sessão iniciada:** 16/09/2025 18:23:38  
**Sistema:** Python Backend  
**Arquivo:** Framework DSB  

---

**[18:24:04]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[18:24:04]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'grupos_view', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\framework_dsb\\backend\\src\\infrastructure\\database', 'database_name': 'financas.db', 'application_path': 'c:\\Applications_DSB\\FinCtl'}
```

**[18:24:04]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[18:24:04]** 🔄 **FLOW:** Consultando view: grupos_view com campos: ['Todos']

**[18:24:04]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'grupos_view', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\framework_dsb\\backend\\src\\infrastructure\\database', 'database_name': 'financas.db', 'application_path': 'c:\\Applications_DSB\\FinCtl'}
```

**[18:24:04]** 🔄 **FLOW:** Consultando view: grupos_view com campos: ['Todos']

**[18:24:04]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'grupos_view', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\framework_dsb\\backend\\src\\infrastructure\\database\\financas.db'}
```

**[18:24:04]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 8}
```

**[18:24:04]** 🔄 **FLOW:** Consulta executada - View: grupos_view, Registros: 4

**[18:24:04]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[18:24:04]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'idgrupo': 1, 'grupo': 'Alimentação', 'descricao': 'Grupo de classificação: Alimentação'}, {'idgrupo': 2, 'grupo': 'Educação', 'descricao': 'Grupo de classificação: Educação'}, {'idgrupo': 3, 'grupo': 'Financas', 'descricao': 'Grupo de classificação: FinancasSSSSSSSSS'}, {'idgrupo': 4, 'grupo': 'Lazer', 'descricao': 'Grupo de classificação: Lazer'}, {'idgrupo': 5, 'grupo': 'Moradia', 'descricao': 'Grupo de classificação: Moradia'}, {'idgrupo': 6, 'grupo': 'Outros', 'descricao': 'Grupo de classificação: Outros'}, {'idgrupo': 7, 'grupo': 'Saúde', 'descricao': 'Grupo de classificação: Saúde'}, {'idgrupo': 8, 'grupo': 'Transporte', 'descricao': 'Grupo de classificação: Transporte'}], 'erro': None, 'sucesso': True, 'total_registros': 8}, 'mensagem': 'sucesso'}

**[18:24:04]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'grupos_view', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\framework_dsb\\backend\\src\\infrastructure\\database\\financas.db'}
```

**[18:24:04]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 8}
```

**[18:24:04]** 🔄 **FLOW:** Consulta executada - View: grupos_view, Registros: 4

**[18:24:04]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[18:24:04]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'idgrupo': 1, 'grupo': 'Alimentação', 'descricao': 'Grupo de classificação: Alimentação'}, {'idgrupo': 2, 'grupo': 'Educação', 'descricao': 'Grupo de classificação: Educação'}, {'idgrupo': 3, 'grupo': 'Financas', 'descricao': 'Grupo de classificação: FinancasSSSSSSSSS'}, {'idgrupo': 4, 'grupo': 'Lazer', 'descricao': 'Grupo de classificação: Lazer'}, {'idgrupo': 5, 'grupo': 'Moradia', 'descricao': 'Grupo de classificação: Moradia'}, {'idgrupo': 6, 'grupo': 'Outros', 'descricao': 'Grupo de classificação: Outros'}, {'idgrupo': 7, 'grupo': 'Saúde', 'descricao': 'Grupo de classificação: Saúde'}, {'idgrupo': 8, 'grupo': 'Transporte', 'descricao': 'Grupo de classificação: Transporte'}], 'erro': None, 'sucesso': True, 'total_registros': 8}, 'mensagem': 'sucesso'}

**[18:24:30]** 🔄 **FLOW:** INÍCIO endpoint /update_data_db

**[18:24:30]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'tabela_alvo': 'grupos', 'campos': ['Todos'], 'campos_obrigatorios': ['grupo'], 'database_name': 'financas.db', 'database_path': 'c:\\Applications_DSB\\framework_dsb\\backend\\src\\infrastructure\\database', 'dados': {'descricao': 'Grupo de classificação: FinancasSSZZZZZZ', 'grupo': 'Financas', 'idgrupo': 3}, 'application_path': 'c:\\Applications_DSB\\FinCtl'}
```

**[18:24:30]** 🔄 **FLOW:** Atualizando tabela: grupos

**[18:24:30]** 🔄 **FLOW:** Update executado - Tabela: grupos

**[18:24:30]** 🔄 **FLOW:** 🔍 RESULTADO da função atualizar_dados  
```
{'sucesso': True, 'registros_afetados': 1, 'sql_executada': 'UPDATE grupos SET descricao = ?, grupo = ? WHERE idgrupo = ?'}
```

**[18:25:07]** 🔄 **FLOW:** INÍCIO endpoint /update_data_db

**[18:25:07]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'tabela_alvo': 'grupos', 'campos': ['Todos'], 'campos_obrigatorios': ['grupo'], 'database_name': 'financas.db', 'database_path': 'c:\\Applications_DSB\\framework_dsb\\backend\\src\\infrastructure\\database', 'dados': {'descricao': 'Grupo de classificação: FinancasSSZZyyyy', 'grupo': 'Financas', 'idgrupo': 3}, 'application_path': 'c:\\Applications_DSB\\FinCtl'}
```

**[18:25:07]** 🔄 **FLOW:** Atualizando tabela: grupos

**[18:25:07]** 🔄 **FLOW:** Update executado - Tabela: grupos

**[18:25:07]** 🔄 **FLOW:** 🔍 RESULTADO da função atualizar_dados  
```
{'sucesso': True, 'registros_afetados': 1, 'sql_executada': 'UPDATE grupos SET descricao = ?, grupo = ? WHERE idgrupo = ?'}
```

**[18:25:55]** 🔄 **FLOW:** INÍCIO endpoint /update_data_db

**[18:25:55]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'tabela_alvo': 'grupos', 'campos': ['Todos'], 'campos_obrigatorios': ['grupo'], 'database_name': 'financas.db', 'database_path': 'c:\\Applications_DSB\\framework_dsb\\backend\\src\\infrastructure\\database', 'dados': {'descricao': 'Grupo de classificação: FinancasSSZZ', 'grupo': 'Financas', 'idgrupo': 3}, 'application_path': 'c:\\Applications_DSB\\FinCtl'}
```

**[18:25:55]** 🔄 **FLOW:** Atualizando tabela: grupos

**[18:25:55]** 🔄 **FLOW:** Update executado - Tabela: grupos

**[18:25:55]** 🔄 **FLOW:** 🔍 RESULTADO da função atualizar_dados  
```
{'sucesso': True, 'registros_afetados': 1, 'sql_executada': 'UPDATE grupos SET descricao = ?, grupo = ? WHERE idgrupo = ?'}
```

