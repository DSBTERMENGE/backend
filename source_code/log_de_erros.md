*****************************
SISTEMA DE LOG DE ERROS
SEÇÃO INICIADA EM 14/10/2025 às 19:38:56
*****************************

**[19:38:56]** 🔄 **FLOW:** Caminho calculado: C:\Applications_DSB\framework_dsb\extratorDePDF

**[19:38:56]** 🔄 **FLOW:** Arquivo existe? True

**[19:38:57]** ❌ **ERRO:** Erro ao importar módulos de extração: No module named 'classificacao'  
```
Tipo: ModuleNotFoundError
Mensagem: No module named 'classificacao'
```  
**Stack Trace:**
```
  File "C:\Applications_DSB\framework_dsb\backend\source_code\backend_api.py", line 98, in processar_extratos_pdf
    from orquestrador_extracao import processar_e_salvar_extratos
  File "C:\Applications_DSB\framework_dsb\extratorDePDF\orquestrador_extracao.py", line 17, in <module>
    import classificacao

```

