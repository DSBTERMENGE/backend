**[21:59:27]** === LOG TRUNCADO ===

**[21:59:27]** 🔄 **FLOW:** INÍCIO endpoint /consultar_dados_db

**[21:59:27]** 🔄 **FLOW:** Dados recebidos no endpoint  
```
{'view': 'subgrupos_view', 'campos': ['Todos'], 'database_path': 'c:\\Applications_DSB\\FinCtl\\data', 'database_name': 'financas.db', 'application_path': 'c:\\Applications_DSB\\FinCtl', 'filtros': 'idgrupo = 3'}
```

**[21:59:27]** 🔄 **FLOW:** Consultando view: subgrupos_view com campos: ['Todos']

**[21:59:27]** 🔄 **FLOW:** INÍCIO consultar_bd  
```
{'view': 'subgrupos_view', 'campos': ['Todos'], 'database': 'c:\\Applications_DSB\\FinCtl\\data\\financas.db'}
```

**[21:59:27]** 🔄 **FLOW:** SUCESSO consultar_bd  
```
{'registros_encontrados': 2}
```

**[21:59:27]** 🔄 **FLOW:** Consulta executada - View: subgrupos_view, Registros: 4

**[21:59:27]** 🔄 **FLOW:** ✅ ENVIANDO RESPOSTA AO FRONTEND: 4 registros

**[21:59:27]** 🔄 **FLOW:** 📤 ESTRUTURA DA RESPOSTA: {'dados': {'dados': [{'idsubgrupo': 3, 'idgrupo': 3, 'subgrupo': 'gigoloror', 'descricao': 'tesouro ndndndndn', 'dicasDeClassificacao': 'weatern digital', 'observacoes': 'rua do lavradio', 'data_criacao': '2025-10-04 16:44:07', 'data_atualizacao': '2025-10-04 16:44:07'}, {'idsubgrupo': 1, 'idgrupo': 3, 'subgrupo': 'sdsd', 'descricao': 'dddddddddddddddddd', 'dicasDeClassificacao': 'dddddddddddddddddddddddd', 'observacoes': 'ddddddddddddddddddddddddddd', 'data_criacao': '2025-09-29 10:43:28', 'data_atualizacao': '2025-09-29 10:43:28'}], 'erro': None, 'sucesso': True, 'total_registros': 2}, 'mensagem': 'sucesso'}

