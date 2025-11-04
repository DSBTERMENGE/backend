*****************************
SISTEMA DE LOG DE ERROS
SEÇÃO INICIADA EM 03/11/2025 às 18:37:20
*****************************

*****************************
SISTEMA DE LOG DE ERROS
SEÇÃO INICIADA EM 03/11/2025 às 18:37:20
*****************************

**[18:37:38]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[18:37:38]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'grupos_view', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': 'c:\\Applications_DSB\\FinCtl', 'filtros': ''}
```

**[18:37:38]** 🔄 **FLOW:** Consultando view: grupos_view com campos: ['Todos']

**[18:37:38]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'grupos_view', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[18:37:38]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 12}
```

**[18:37:38]** 🔄 **FLOW:** Consulta executada - View: grupos_view, Registros: 4

**[18:37:38]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[18:37:38]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'idgrupo': 1, 'grupo': 'Alimentação', 'descricao': 'Grupo de classificação: Alimentação'}, {'idgrupo': 10, 'grupo': 'Aluguel', 'descricao': 'aluguel do aluguel do aluguel é mais e mais'}, {'idgrupo': 2, 'grupo': 'Educação', 'descricao': 'Grupo de classificação: Educação'}, {'idgrupo': 3, 'grupo': 'Financas', 'descricao': 'Grupo de classificação: FinancasSSZZ'}, {'idgrupo': 4, 'grupo': 'Lazer', 'descricao': 'Grupo de classificação: Lazer'}, {'idgrupo': 5, 'grupo': 'Moradia', 'descricao': 'Grupo de classificação: Moradia'}, {'idgrupo': 6, 'grupo': 'Outros', 'descricao': 'Grupo de classificação: Outros'}, {'idgrupo': 7, 'grupo': 'Saúde', 'descricao': 'Grupo de classificação: Saúde'}, {'idgrupo': 9, 'grupo': 'Tecnologias', 'descricao': 'equipamentos, assinaturas , manutenção de hardware'}, {'idgrupo': 8, 'grupo': 'Transporte', 'descricao': 'Grupo de classificação: Transporte'}, {'idgrupo': 12, 'grupo': 'Vestuário,Higiene e beleza', 'descricao': 'Roupas, Corte de cabelo, produtos de hirigene e beleza'}, {'idgrupo': 11, 'grupo': 'Viagens', 'descricao': 'Despesas com passagens, hospedagem e passeios'}], 'erro': None, 'sucesso': True, 'total_registros': 12}, 'mensagem': 'sucesso'}

**[18:37:52]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[18:37:52]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'subgrupos_view', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': 'c:\\Applications_DSB\\FinCtl', 'filtros': 'idgrupo = 3'}
```

**[18:37:52]** 🔄 **FLOW:** Consultando view: subgrupos_view com campos: ['Todos']

**[18:37:52]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'subgrupos_view', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[18:37:52]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 4}
```

**[18:37:52]** 🔄 **FLOW:** Consulta executada - View: subgrupos_view, Registros: 4

**[18:37:52]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[18:37:52]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'idsubgrupo': 3, 'idgrupo': 3, 'subgrupo': 'Juros/Multas', 'descricao': 'Juros e multas pagas', 'dicasDeClassificacao': 'Juros, multa', 'observacoes': '', 'data_criacao': '2025-10-04 16:44:07', 'data_atualizacao': '2025-10-04 16:44:07'}, {'idsubgrupo': 24, 'idgrupo': 3, 'subgrupo': 'Seguros', 'descricao': 'Gastos com seguro', 'dicasDeClassificacao': 'seguro', 'observacoes': '', 'data_criacao': '2025-11-03 21:32:57', 'data_atualizacao': '2025-11-03 21:32:57'}, {'idsubgrupo': 23, 'idgrupo': 3, 'subgrupo': 'Tarifas Bancarias', 'descricao': 'Tarifas cobradas por bancos', 'dicasDeClassificacao': '', 'observacoes': '', 'data_criacao': '2025-11-03 21:21:02', 'data_atualizacao': '2025-11-03 21:21:02'}, {'idsubgrupo': 1, 'idgrupo': 3, 'subgrupo': 'sdsd', 'descricao': 'dddddddddddddddddd', 'dicasDeClassificacao': 'dddddddddddddddddddddddd', 'observacoes': 'ddddddddddddddddddddddddddd', 'data_criacao': '2025-09-29 10:43:28', 'data_atualizacao': '2025-09-29 10:43:28'}], 'erro': None, 'sucesso': True, 'total_registros': 4}, 'mensagem': 'sucesso'}

**[18:39:00]** 🔄 **FLOW:** INÍCIO endpoint /update_data_db

**[18:39:00]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'tabela_alvo': 'subgrupos', 'campos': ['Todos'], 'campos_obrigatorios': ['subgrupo'], 'database_name': 'financas.db', 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'dados': {'data_atualizacao': '2025-09-29 10:43:28', 'data_criacao': '2025-09-29 10:43:28', 'descricao': 'Investimentos financeiros', 'dicasDeClassificacao': '', 'idgrupo': '3', 'idsubgrupo': 1, 'observacoes': '', 'subgrupo': 'Investimentos'}, 'application_path': 'c:\\Applications_DSB\\FinCtl', 'filtros': 'idgrupo = 3'}
```

**[18:39:00]** 🔄 **FLOW:** Atualizando tabela: subgrupos

**[18:39:00]** 🔄 **FLOW:** Update executado - Tabela: subgrupos

**[18:39:00]** 🔄 **FLOW:** 🔍 RESULTADO da função atualizar_dados  
```
{'sucesso': True, 'registros_afetados': 1, 'sql_executada': 'UPDATE subgrupos SET data_atualizacao = ?, data_criacao = ?, descricao = ?, dicasDeClassificacao = ?, idgrupo = ?, observacoes = ?, subgrupo = ? WHERE idsubgrupo = ?'}
```

**[18:39:00]** 🔄 **FLOW:** 🔄 Consultando dados atualizados após update

**[18:39:00]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'subgrupos_view', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[18:39:00]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 4}
```

**[18:39:00]** 🔄 **FLOW:** 📊 Dados atualizados consultados  
```
{'view': 'subgrupos_view', 'filtros_aplicados': 'idgrupo = 3', 'total_registros': 4}
```

**[18:39:00]** 🔄 **FLOW:** ✅ Resposta completa com dados atualizados (UPDATE)  
```
{'total_registros': 4}
```

**[18:39:53]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[18:39:53]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'subgrupos_view', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': 'c:\\Applications_DSB\\FinCtl', 'filtros': 'idgrupo = 7'}
```

**[18:39:53]** 🔄 **FLOW:** Consultando view: subgrupos_view com campos: ['Todos']

**[18:39:53]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'subgrupos_view', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[18:39:53]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 1}
```

**[18:39:53]** 🔄 **FLOW:** Consulta executada - View: subgrupos_view, Registros: 4

**[18:39:53]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[18:39:53]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'idsubgrupo': 2, 'idgrupo': 7, 'subgrupo': 'abcdef', 'descricao': 'qqqqqqqqqqqqqqqq', 'dicasDeClassificacao': 'qqqqqqqqqqqqqqqqqqqq', 'observacoes': 'qqqqqqqqqqqqqqqqqqqqssssssssss', 'data_criacao': '2025-10-04 16:42:04', 'data_atualizacao': '2025-10-04 16:42:04'}], 'erro': None, 'sucesso': True, 'total_registros': 1}, 'mensagem': 'sucesso'}

**[18:41:00]** 🔄 **FLOW:** INÍCIO endpoint /update_data_db

**[18:41:00]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'tabela_alvo': 'subgrupos', 'campos': ['Todos'], 'campos_obrigatorios': ['subgrupo'], 'database_name': 'financas.db', 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'dados': {'data_atualizacao': '2025-10-04 16:42:04', 'data_criacao': '2025-10-04 16:42:04', 'descricao': 'Pgto Plano de saúde', 'dicasDeClassificacao': 'Prevent Senior, Prevent', 'idgrupo': '7', 'idsubgrupo': 2, 'observacoes': '', 'subgrupo': 'Planos de Saude'}, 'application_path': 'c:\\Applications_DSB\\FinCtl', 'filtros': 'idgrupo = 7'}
```

**[18:41:00]** 🔄 **FLOW:** Atualizando tabela: subgrupos

**[18:41:00]** 🔄 **FLOW:** Update executado - Tabela: subgrupos

**[18:41:00]** 🔄 **FLOW:** 🔍 RESULTADO da função atualizar_dados  
```
{'sucesso': True, 'registros_afetados': 1, 'sql_executada': 'UPDATE subgrupos SET data_atualizacao = ?, data_criacao = ?, descricao = ?, dicasDeClassificacao = ?, idgrupo = ?, observacoes = ?, subgrupo = ? WHERE idsubgrupo = ?'}
```

**[18:41:00]** 🔄 **FLOW:** 🔄 Consultando dados atualizados após update

**[18:41:00]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'subgrupos_view', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[18:41:00]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 1}
```

**[18:41:00]** 🔄 **FLOW:** 📊 Dados atualizados consultados  
```
{'view': 'subgrupos_view', 'filtros_aplicados': 'idgrupo = 7', 'total_registros': 1}
```

**[18:41:00]** 🔄 **FLOW:** ✅ Resposta completa com dados atualizados (UPDATE)  
```
{'total_registros': 1}
```

**[18:41:10]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[18:41:10]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'subgrupos_view', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': 'c:\\Applications_DSB\\FinCtl', 'filtros': 'idgrupo = 1'}
```

**[18:41:10]** 🔄 **FLOW:** Consultando view: subgrupos_view com campos: ['Todos']

**[18:41:10]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'subgrupos_view', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[18:41:10]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 3}
```

**[18:41:10]** 🔄 **FLOW:** Consulta executada - View: subgrupos_view, Registros: 4

**[18:41:10]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[18:41:10]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'idsubgrupo': 12, 'idgrupo': 1, 'subgrupo': 'Café/bar/Quiosques', 'descricao': 'Despesas com lanches ou café em cafeterias e pequenos estabelecimento.', 'dicasDeClassificacao': 'Cafeteria, café, bar', 'observacoes': '', 'data_criacao': '2025-11-03 13:03:33', 'data_atualizacao': '2025-11-03 13:03:33'}, {'idsubgrupo': 11, 'idgrupo': 1, 'subgrupo': 'Restaurantes', 'descricao': 'Despesas com almoço, jantar ou outros em restaurantes', 'dicasDeClassificacao': 'Restaurante , Rest. , Pizzaria', 'observacoes': '', 'data_criacao': '2025-11-03 13:01:18', 'data_atualizacao': '2025-11-03 13:01:18'}, {'idsubgrupo': 13, 'idgrupo': 1, 'subgrupo': 'Supermercados', 'descricao': 'Despesas em supermercados', 'dicasDeClassificacao': 'Zona Sul', 'observacoes': '', 'data_criacao': '2025-11-03 13:05:47', 'data_atualizacao': '2025-11-03 13:05:47'}], 'erro': None, 'sucesso': True, 'total_registros': 3}, 'mensagem': 'sucesso'}

**[18:41:16]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[18:41:16]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'subgrupos_view', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': 'c:\\Applications_DSB\\FinCtl', 'filtros': 'idgrupo = 10'}
```

**[18:41:16]** 🔄 **FLOW:** Consultando view: subgrupos_view com campos: ['Todos']

**[18:41:16]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'subgrupos_view', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[18:41:16]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 1}
```

**[18:41:16]** 🔄 **FLOW:** Consulta executada - View: subgrupos_view, Registros: 4

**[18:41:16]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[18:41:16]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'idsubgrupo': '', 'idgrupo': '', 'subgrupo': '', 'descricao': '', 'dicasDeClassificacao': '', 'observacoes': '', 'data_criacao': '', 'data_atualizacao': ''}], 'erro': None, 'sucesso': True, 'total_registros': 1}, 'mensagem': 'sucesso'}

**[18:41:22]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[18:41:22]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'subgrupos_view', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': 'c:\\Applications_DSB\\FinCtl', 'filtros': 'idgrupo = 2'}
```

**[18:41:22]** 🔄 **FLOW:** Consultando view: subgrupos_view com campos: ['Todos']

**[18:41:22]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'subgrupos_view', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[18:41:22]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 3}
```

**[18:41:22]** 🔄 **FLOW:** Consulta executada - View: subgrupos_view, Registros: 4

**[18:41:22]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[18:41:22]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'idsubgrupo': 19, 'idgrupo': 2, 'subgrupo': 'Cursos', 'descricao': 'Cursos em geral ', 'dicasDeClassificacao': 'FGV, UBEC, UCB', 'observacoes': '', 'data_criacao': '2025-11-03 21:01:37', 'data_atualizacao': '2025-11-03 21:01:37'}, {'idsubgrupo': 18, 'idgrupo': 2, 'subgrupo': 'Linguas', 'descricao': 'Estudo de linguas', 'dicasDeClassificacao': 'Preply, preply', 'observacoes': '', 'data_criacao': '2025-11-03 21:00:58', 'data_atualizacao': '2025-11-03 21:00:58'}, {'idsubgrupo': 20, 'idgrupo': 2, 'subgrupo': 'Materiais', 'descricao': 'Materiais para educação', 'dicasDeClassificacao': '', 'observacoes': '', 'data_criacao': '2025-11-03 21:02:37', 'data_atualizacao': '2025-11-03 21:02:37'}], 'erro': None, 'sucesso': True, 'total_registros': 3}, 'mensagem': 'sucesso'}

**[18:41:30]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[18:41:30]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'subgrupos_view', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': 'c:\\Applications_DSB\\FinCtl', 'filtros': 'idgrupo = 3'}
```

**[18:41:30]** 🔄 **FLOW:** Consultando view: subgrupos_view com campos: ['Todos']

**[18:41:30]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'subgrupos_view', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[18:41:30]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 4}
```

**[18:41:30]** 🔄 **FLOW:** Consulta executada - View: subgrupos_view, Registros: 4

**[18:41:30]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[18:41:30]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'idsubgrupo': 1, 'idgrupo': 3, 'subgrupo': 'Investimentos', 'descricao': 'Investimentos financeiros', 'dicasDeClassificacao': '', 'observacoes': '', 'data_criacao': '2025-09-29 10:43:28', 'data_atualizacao': '2025-09-29 10:43:28'}, {'idsubgrupo': 3, 'idgrupo': 3, 'subgrupo': 'Juros/Multas', 'descricao': 'Juros e multas pagas', 'dicasDeClassificacao': 'Juros, multa', 'observacoes': '', 'data_criacao': '2025-10-04 16:44:07', 'data_atualizacao': '2025-10-04 16:44:07'}, {'idsubgrupo': 24, 'idgrupo': 3, 'subgrupo': 'Seguros', 'descricao': 'Gastos com seguro', 'dicasDeClassificacao': 'seguro', 'observacoes': '', 'data_criacao': '2025-11-03 21:32:57', 'data_atualizacao': '2025-11-03 21:32:57'}, {'idsubgrupo': 23, 'idgrupo': 3, 'subgrupo': 'Tarifas Bancarias', 'descricao': 'Tarifas cobradas por bancos', 'dicasDeClassificacao': '', 'observacoes': '', 'data_criacao': '2025-11-03 21:21:02', 'data_atualizacao': '2025-11-03 21:21:02'}], 'erro': None, 'sucesso': True, 'total_registros': 4}, 'mensagem': 'sucesso'}

**[18:41:34]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[18:41:34]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'subgrupos_view', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': 'c:\\Applications_DSB\\FinCtl', 'filtros': 'idgrupo = 4'}
```

**[18:41:34]** 🔄 **FLOW:** Consultando view: subgrupos_view com campos: ['Todos']

**[18:41:34]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'subgrupos_view', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[18:41:34]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 2}
```

**[18:41:34]** 🔄 **FLOW:** Consulta executada - View: subgrupos_view, Registros: 4

**[18:41:34]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[18:41:34]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'idsubgrupo': 22, 'idgrupo': 4, 'subgrupo': 'Cinema/Teatro/Shows', 'descricao': 'Gastos com cinema, teatro, shows e similares', 'dicasDeClassificacao': '', 'observacoes': '', 'data_criacao': '2025-11-03 21:05:32', 'data_atualizacao': '2025-11-03 21:05:32'}, {'idsubgrupo': 21, 'idgrupo': 4, 'subgrupo': 'Streaming', 'descricao': '', 'dicasDeClassificacao': 'Netflix', 'observacoes': '', 'data_criacao': '2025-11-03 21:04:00', 'data_atualizacao': '2025-11-03 21:04:00'}], 'erro': None, 'sucesso': True, 'total_registros': 2}, 'mensagem': 'sucesso'}

**[18:41:41]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[18:41:41]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'subgrupos_view', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': 'c:\\Applications_DSB\\FinCtl', 'filtros': 'idgrupo = 5'}
```

**[18:41:41]** 🔄 **FLOW:** Consultando view: subgrupos_view com campos: ['Todos']

**[18:41:41]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'subgrupos_view', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[18:41:41]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 6}
```

**[18:41:41]** 🔄 **FLOW:** Consulta executada - View: subgrupos_view, Registros: 4

**[18:41:41]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[18:41:41]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'idsubgrupo': 5, 'idgrupo': 5, 'subgrupo': 'Aluguel', 'descricao': 'Pagto aluguel apto em Ipanema', 'dicasDeClassificacao': 'MLG, WME, MlgAssessoria', 'observacoes': '', 'data_criacao': '2025-11-03 09:04:28', 'data_atualizacao': '2025-11-03 09:04:28'}, {'idsubgrupo': 7, 'idgrupo': 5, 'subgrupo': 'Condomínio', 'descricao': '', 'dicasDeClassificacao': '', 'observacoes': 'Condomínio predial', 'data_criacao': '2025-11-03 09:12:19', 'data_atualizacao': '2025-11-03 09:12:19'}, {'idsubgrupo': 6, 'idgrupo': 5, 'subgrupo': 'Energia', 'descricao': 'Conta de luz', 'dicasDeClassificacao': 'Light, Light Serviços', 'observacoes': '', 'data_criacao': '2025-11-03 09:10:31', 'data_atualizacao': '2025-11-03 09:10:31'}, {'idsubgrupo': 9, 'idgrupo': 5, 'subgrupo': 'IPTU', 'descricao': 'Pagamento de IPTU', 'dicasDeClassificacao': '', 'observacoes': '', 'data_criacao': '2025-11-03 09:37:06', 'data_atualizacao': '2025-11-03 09:37:06'}, {'idsubgrupo': 10, 'idgrupo': 5, 'subgrupo': 'Seguro Residencial', 'descricao': 'Seguro residencial contra incêndio', 'dicasDeClassificacao': '', 'observacoes': '', 'data_criacao': '2025-11-03 12:49:46', 'data_atualizacao': '2025-11-03 12:49:46'}, {'idsubgrupo': 8, 'idgrupo': 5, 'subgrupo': 'Água', 'descricao': 'Conta de água', 'dicasDeClassificacao': 'Aguas do Rio, Cedae', 'observacoes': '', 'data_criacao': '2025-11-03 09:16:38', 'data_atualizacao': '2025-11-03 09:16:38'}], 'erro': None, 'sucesso': True, 'total_registros': 6}, 'mensagem': 'sucesso'}

**[18:41:49]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[18:41:49]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'subgrupos_view', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': 'c:\\Applications_DSB\\FinCtl', 'filtros': 'idgrupo = 6'}
```

**[18:41:49]** 🔄 **FLOW:** Consultando view: subgrupos_view com campos: ['Todos']

**[18:41:49]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'subgrupos_view', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[18:41:49]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 1}
```

**[18:41:49]** 🔄 **FLOW:** Consulta executada - View: subgrupos_view, Registros: 4

**[18:41:49]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[18:41:49]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'idsubgrupo': 4, 'idgrupo': 6, 'subgrupo': 'Não Classificados', 'descricao': 'Itens que o sistema não conseguiu classificar', 'dicasDeClassificacao': '', 'observacoes': 'Os itens nesta categoria poderão ser reclassificados manualmente se o operador achar o lançamento representativo , por algum motivo.', 'data_criacao': '2025-11-02 13:56:17', 'data_atualizacao': '2025-11-02 13:56:17'}], 'erro': None, 'sucesso': True, 'total_registros': 1}, 'mensagem': 'sucesso'}

**[18:41:56]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[18:41:56]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'subgrupos_view', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': 'c:\\Applications_DSB\\FinCtl', 'filtros': 'idgrupo = 7'}
```

**[18:41:56]** 🔄 **FLOW:** Consultando view: subgrupos_view com campos: ['Todos']

**[18:41:56]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'subgrupos_view', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[18:41:56]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 1}
```

**[18:41:56]** 🔄 **FLOW:** Consulta executada - View: subgrupos_view, Registros: 4

**[18:41:56]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[18:41:56]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'idsubgrupo': 2, 'idgrupo': 7, 'subgrupo': 'Planos de Saude', 'descricao': 'Pgto Plano de saúde', 'dicasDeClassificacao': 'Prevent Senior, Prevent', 'observacoes': '', 'data_criacao': '2025-10-04 16:42:04', 'data_atualizacao': '2025-10-04 16:42:04'}], 'erro': None, 'sucesso': True, 'total_registros': 1}, 'mensagem': 'sucesso'}

**[18:42:47]** 🔄 **FLOW:** 🔄 INÍCIO endpoint /incluir_reg_novo_db

**[18:42:47]** 🔄 **FLOW:** 📋 Dados recebidos no endpoint  
```
{'tabela_alvo': 'subgrupos', 'campos': ['Todos'], 'campos_obrigatorios': ['subgrupo'], 'database_name': 'financas.db', 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'dados': {'subgrupo': 'Consultas particulares', 'descricao': 'Consultas médias fora do plano', 'dicasDeClassificacao': '', 'observacoes': '', 'idgrupo': '7'}, 'application_path': 'c:\\Applications_DSB\\FinCtl', 'filtros': 'idgrupo = 7'}
```

**[18:42:47]** 🔄 **FLOW:** 🔧 Parâmetros extraídos  
```
{'tabela_alvo': 'subgrupos', 'database_file': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db', 'campos_para_inserir': ['subgrupo', 'descricao', 'dicasDeClassificacao', 'observacoes', 'idgrupo'], 'filtros': 'idgrupo = 7'}
```

**[18:42:47]** 🔄 **FLOW:** 📤 Resultado da inserção  
```
{'sucesso': True, 'registros_afetados': 1, 'registro_completo': {'subgrupo': 'Consultas particulares', 'descricao': 'Consultas médias fora do plano', 'dicasDeClassificacao': '', 'observacoes': '', 'idgrupo': '7', 'idsubgrupo': 25}, 'id_inserido': 25, 'sql_executada': 'INSERT INTO subgrupos (subgrupo, descricao, dicasDeClassificacao, observacoes, idgrupo) VALUES (?, ?, ?, ?, ?)'}
```

**[18:42:47]** 🔄 **FLOW:** 🔄 Consultando dados atualizados após inserção

**[18:42:47]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'subgrupos_view', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[18:42:47]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 2}
```

**[18:42:47]** 🔄 **FLOW:** 📊 Dados atualizados consultados  
```
{'view': 'subgrupos_view', 'filtros_aplicados': 'idgrupo = 7', 'total_registros': 2}
```

**[18:42:47]** 🔄 **FLOW:** ✅ Resposta completa com dados atualizados  
```
{'total_registros': 2}
```

**[18:44:21]** 🔄 **FLOW:** 🔄 INÍCIO endpoint /incluir_reg_novo_db

**[18:44:21]** 🔄 **FLOW:** 📋 Dados recebidos no endpoint  
```
{'tabela_alvo': 'subgrupos', 'campos': ['Todos'], 'campos_obrigatorios': ['subgrupo'], 'database_name': 'financas.db', 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'dados': {'subgrupo': 'Fármacia', 'descricao': 'Despesas com medicamentos', 'dicasDeClassificacao': 'Farmácia, Drogaria, Farm., Droga, Raia, Pacheco, Drogasil', 'observacoes': '', 'idgrupo': '7'}, 'application_path': 'c:\\Applications_DSB\\FinCtl', 'filtros': 'idgrupo = 7'}
```

**[18:44:21]** 🔄 **FLOW:** 🔧 Parâmetros extraídos  
```
{'tabela_alvo': 'subgrupos', 'database_file': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db', 'campos_para_inserir': ['subgrupo', 'descricao', 'dicasDeClassificacao', 'observacoes', 'idgrupo'], 'filtros': 'idgrupo = 7'}
```

**[18:44:21]** 🔄 **FLOW:** 📤 Resultado da inserção  
```
{'sucesso': True, 'registros_afetados': 1, 'registro_completo': {'subgrupo': 'Fármacia', 'descricao': 'Despesas com medicamentos', 'dicasDeClassificacao': 'Farmácia, Drogaria, Farm., Droga, Raia, Pacheco, Drogasil', 'observacoes': '', 'idgrupo': '7', 'idsubgrupo': 26}, 'id_inserido': 26, 'sql_executada': 'INSERT INTO subgrupos (subgrupo, descricao, dicasDeClassificacao, observacoes, idgrupo) VALUES (?, ?, ?, ?, ?)'}
```

**[18:44:21]** 🔄 **FLOW:** 🔄 Consultando dados atualizados após inserção

**[18:44:21]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'subgrupos_view', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[18:44:21]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 3}
```

**[18:44:21]** 🔄 **FLOW:** 📊 Dados atualizados consultados  
```
{'view': 'subgrupos_view', 'filtros_aplicados': 'idgrupo = 7', 'total_registros': 3}
```

**[18:44:21]** 🔄 **FLOW:** ✅ Resposta completa com dados atualizados  
```
{'total_registros': 3}
```

**[18:44:58]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[18:44:58]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'subgrupos_view', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': 'c:\\Applications_DSB\\FinCtl', 'filtros': 'idgrupo = 10'}
```

**[18:44:58]** 🔄 **FLOW:** Consultando view: subgrupos_view com campos: ['Todos']

**[18:44:58]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'subgrupos_view', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[18:44:58]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 1}
```

**[18:44:58]** 🔄 **FLOW:** Consulta executada - View: subgrupos_view, Registros: 4

**[18:44:58]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[18:44:58]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'idsubgrupo': '', 'idgrupo': '', 'subgrupo': '', 'descricao': '', 'dicasDeClassificacao': '', 'observacoes': '', 'data_criacao': '', 'data_atualizacao': ''}], 'erro': None, 'sucesso': True, 'total_registros': 1}, 'mensagem': 'sucesso'}

**[18:45:04]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[18:45:04]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'subgrupos_view', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': 'c:\\Applications_DSB\\FinCtl', 'filtros': 'idgrupo = 5'}
```

**[18:45:04]** 🔄 **FLOW:** Consultando view: subgrupos_view com campos: ['Todos']

**[18:45:04]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'subgrupos_view', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[18:45:04]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 6}
```

**[18:45:04]** 🔄 **FLOW:** Consulta executada - View: subgrupos_view, Registros: 4

**[18:45:04]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[18:45:04]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'idsubgrupo': 5, 'idgrupo': 5, 'subgrupo': 'Aluguel', 'descricao': 'Pagto aluguel apto em Ipanema', 'dicasDeClassificacao': 'MLG, WME, MlgAssessoria', 'observacoes': '', 'data_criacao': '2025-11-03 09:04:28', 'data_atualizacao': '2025-11-03 09:04:28'}, {'idsubgrupo': 7, 'idgrupo': 5, 'subgrupo': 'Condomínio', 'descricao': '', 'dicasDeClassificacao': '', 'observacoes': 'Condomínio predial', 'data_criacao': '2025-11-03 09:12:19', 'data_atualizacao': '2025-11-03 09:12:19'}, {'idsubgrupo': 6, 'idgrupo': 5, 'subgrupo': 'Energia', 'descricao': 'Conta de luz', 'dicasDeClassificacao': 'Light, Light Serviços', 'observacoes': '', 'data_criacao': '2025-11-03 09:10:31', 'data_atualizacao': '2025-11-03 09:10:31'}, {'idsubgrupo': 9, 'idgrupo': 5, 'subgrupo': 'IPTU', 'descricao': 'Pagamento de IPTU', 'dicasDeClassificacao': '', 'observacoes': '', 'data_criacao': '2025-11-03 09:37:06', 'data_atualizacao': '2025-11-03 09:37:06'}, {'idsubgrupo': 10, 'idgrupo': 5, 'subgrupo': 'Seguro Residencial', 'descricao': 'Seguro residencial contra incêndio', 'dicasDeClassificacao': '', 'observacoes': '', 'data_criacao': '2025-11-03 12:49:46', 'data_atualizacao': '2025-11-03 12:49:46'}, {'idsubgrupo': 8, 'idgrupo': 5, 'subgrupo': 'Água', 'descricao': 'Conta de água', 'dicasDeClassificacao': 'Aguas do Rio, Cedae', 'observacoes': '', 'data_criacao': '2025-11-03 09:16:38', 'data_atualizacao': '2025-11-03 09:16:38'}], 'erro': None, 'sucesso': True, 'total_registros': 6}, 'mensagem': 'sucesso'}

**[18:45:23]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[18:45:23]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'subgrupos_view', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': 'c:\\Applications_DSB\\FinCtl', 'filtros': 'idgrupo = 7'}
```

**[18:45:23]** 🔄 **FLOW:** Consultando view: subgrupos_view com campos: ['Todos']

**[18:45:23]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'subgrupos_view', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[18:45:23]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 3}
```

**[18:45:23]** 🔄 **FLOW:** Consulta executada - View: subgrupos_view, Registros: 4

**[18:45:23]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[18:45:23]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'idsubgrupo': 25, 'idgrupo': 7, 'subgrupo': 'Consultas particulares', 'descricao': 'Consultas médias fora do plano', 'dicasDeClassificacao': '', 'observacoes': '', 'data_criacao': '2025-11-03 21:42:47', 'data_atualizacao': '2025-11-03 21:42:47'}, {'idsubgrupo': 26, 'idgrupo': 7, 'subgrupo': 'Fármacia', 'descricao': 'Despesas com medicamentos', 'dicasDeClassificacao': 'Farmácia, Drogaria, Farm., Droga, Raia, Pacheco, Drogasil', 'observacoes': '', 'data_criacao': '2025-11-03 21:44:21', 'data_atualizacao': '2025-11-03 21:44:21'}, {'idsubgrupo': 2, 'idgrupo': 7, 'subgrupo': 'Planos de Saude', 'descricao': 'Pgto Plano de saúde', 'dicasDeClassificacao': 'Prevent Senior, Prevent', 'observacoes': '', 'data_criacao': '2025-10-04 16:42:04', 'data_atualizacao': '2025-10-04 16:42:04'}], 'erro': None, 'sucesso': True, 'total_registros': 3}, 'mensagem': 'sucesso'}

**[18:45:29]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[18:45:29]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'subgrupos_view', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': 'c:\\Applications_DSB\\FinCtl', 'filtros': 'idgrupo = 9'}
```

**[18:45:29]** 🔄 **FLOW:** Consultando view: subgrupos_view com campos: ['Todos']

**[18:45:29]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'subgrupos_view', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[18:45:29]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 1}
```

**[18:45:29]** 🔄 **FLOW:** Consulta executada - View: subgrupos_view, Registros: 4

**[18:45:29]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[18:45:29]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'idsubgrupo': '', 'idgrupo': '', 'subgrupo': '', 'descricao': '', 'dicasDeClassificacao': '', 'observacoes': '', 'data_criacao': '', 'data_atualizacao': ''}], 'erro': None, 'sucesso': True, 'total_registros': 1}, 'mensagem': 'sucesso'}

