*****************************
SISTEMA DE LOG DE ERROS
SEÇÃO INICIADA EM 08/11/2025 às 20:49:16
*****************************

**[20:49:17]** 🔄 **FLOW:** Validação bem-sucedida. Dados validados: {'periodo': 'MAR_2025', 'arquivos_validados': ['Extrato_MASTERCARD_Mar_2025.pdf', 'Extrato_SANTANDER_Mar_2025.pdf', 'Extrato_VISA_Mar_2025.pdf']}

**[20:49:17]** 🔄 **FLOW:** Iniciando extração e salvamento dos extratos

**[20:49:19]** 🔄 **FLOW:** Processo concluído com sucesso: 📊 EXTRAÇÃO CONCLUÍDA

Total: 86 despesas salvas
Erros: 0

Detalhamento:
  • MASTERCARD: 61 despesas
  • SANTANDER: 14 despesas
  • VISA: 11 despesas

**[20:49:43]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[20:49:43]** 🔄 **FLOW:** 📝 SQL recebido: SELECT DISTINCT substr(data_extrato, -4, 4) AS ano FROM despesas WHERE data_extrato LIKE '%_%' ORDER...

**[20:49:43]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[20:49:43]** 🔄 **FLOW:** 📊 RESULTADO da query SQL: {'sucesso': True, 'dados': [{'ano': '2025'}], 'mensagem': 'Consulta executada com sucesso. 1 registro(s) encontrado(s).'}

**[20:49:43]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[20:49:45]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[20:49:45]** 🔄 **FLOW:** 📝 SQL recebido: SELECT DISTINCT substr(data_extrato, 1, instr(data_extrato, '_')-1) AS mes FROM despesas WHERE data_...

**[20:49:45]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[20:49:45]** 🔄 **FLOW:** 📊 RESULTADO da query SQL: {'sucesso': True, 'dados': [{'mes': 'FEV'}, {'mes': 'JAN'}, {'mes': 'MAR'}], 'mensagem': 'Consulta executada com sucesso. 3 registro(s) encontrado(s).'}

**[20:49:45]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[20:49:46]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[20:49:46]** 🔄 **FLOW:** 📝 SQL recebido: SELECT DISTINCT instituicao FROM despesas WHERE instituicao IS NOT NULL AND instituicao <> '' AND da...

**[20:49:46]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[20:49:46]** 🔄 **FLOW:** 📊 RESULTADO da query SQL: {'sucesso': True, 'dados': [{'instituicao': 'MASTERCARD'}, {'instituicao': 'SANTANDER'}, {'instituicao': 'VISA'}], 'mensagem': 'Consulta executada com sucesso. 3 registro(s) encontrado(s).'}

**[20:49:46]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[20:49:51]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[20:49:51]** 🔄 **FLOW:** 📝 SQL recebido: SELECT DISTINCT instituicao FROM despesas WHERE instituicao IS NOT NULL AND instituicao <> '' AND da...

**[20:49:51]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[20:49:51]** 🔄 **FLOW:** 📊 RESULTADO da query SQL: {'sucesso': True, 'dados': [{'instituicao': 'MASTERCARD'}, {'instituicao': 'SANTANDER'}, {'instituicao': 'VISA'}], 'mensagem': 'Consulta executada com sucesso. 3 registro(s) encontrado(s).'}

**[20:49:51]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[20:49:53]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[20:49:53]** 🔄 **FLOW:** 📝 SQL recebido: SELECT descricao AS 'Descrição', instituicao AS 'Instituição', valor AS '(R$)Valor' FROM despesas_vi...

**[20:49:53]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[20:49:53]** 🔄 **FLOW:** 📊 RESULTADO da query SQL: {'sucesso': True, 'dados': [{'Descrição': 'RAIA432', 'Instituição': 'MASTERCARD', '(R$)Valor': '9,59'}, {'Descrição': 'ZONA SUL FL 08', 'Instituição': 'MASTERCARD', '(R$)Valor': '86,47'}, {'Descrição': '28/02 RAIA432 UBER UBER *TRIP HELP U 03/03', 'Instituição': 'MASTERCARD', '(R$)Valor': '80,08'}, {'Descrição': 'RAIA432', 'Instituição': 'MASTERCARD', '(R$)Valor': '8,09'}, {'Descrição': 'DROGARIA VENANCIO', 'Instituição': 'MASTERCARD', '(R$)Valor': '71,97'}, {'Descrição': 'ZONA SUL FL 08', 'Instituição': 'MASTERCARD', '(R$)Valor': '71,89'}, {'Descrição': 'PGTO CONTA GAS EM CANAIS ', 'Instituição': 'SANTANDER', '(R$)Valor': '70,30'}, {'Descrição': '07/03 DROGARIAS UBER* TRIP PACHECO 02/03', 'Instituição': 'MASTERCARD', '(R$)Valor': '70,05'}, {'Descrição': 'PIX ENV ALLIANZ SEGUROS SA', 'Instituição': 'SANTANDER', '(R$)Valor': '66,79'}, {'Descrição': 'ZONA SUL FL 08', 'Instituição': 'MASTERCARD', '(R$)Valor': '63,37'}, {'Descrição': 'UBER* TRIP', 'Instituição': 'MASTERCARD', '(R$)Valor': '62,90'}, {'Descrição': 'ZONA SUL FL 08', 'Instituição': 'MASTERCARD', '(R$)Valor': '61,73'}, {'Descrição': 'O CARANGUEJO', 'Instituição': 'MASTERCARD', '(R$)Valor': '61,00'}, {'Descrição': 'ZONA SUL FL 08', 'Instituição': 'MASTERCARD', '(R$)Valor': '6,99'}, {'Descrição': 'IOF DESPESA NO EXTERIOR', 'Instituição': 'VISA', '(R$)Valor': '6,57'}, {'Descrição': 'ZONA SUL FL 08', 'Instituição': 'MASTERCARD', '(R$)Valor': '59,92'}, {'Descrição': 'PAYPAL*PAYPAL *NE', 'Instituição': 'VISA', '(R$)Valor': '59,90'}, {'Descrição': 'PEDAGIO ELETRONICO SEM PARAR S', 'Instituição': 'SANTANDER', '(R$)Valor': '59,28'}, {'Descrição': 'ZONA SUL FL 08', 'Instituição': 'MASTERCARD', '(R$)Valor': '58,27'}, {'Descrição': 'MERCADOLIVRE*QUALITY21', 'Instituição': 'VISA', '(R$)Valor': '55,83'}, {'Descrição': 'ZONA SUL FL 08', 'Instituição': 'MASTERCARD', '(R$)Valor': '55,57'}, {'Descrição': 'ZONA SUL FL 08', 'Instituição': 'MASTERCARD', '(R$)Valor': '53,55'}, {'Descrição': 'UCB *MENSALIDADES 02/06', 'Instituição': 'VISA', '(R$)Valor': '50,48'}, {'Descrição': 'UCB *MENSALIDADES 01/06', 'Instituição': 'VISA', '(R$)Valor': '50,48'}, {'Descrição': 'OGGI', 'Instituição': 'MASTERCARD', '(R$)Valor': '5,99'}, {'Descrição': 'CONQ', 'Instituição': 'MASTERCARD', '(R$)Valor': '5,00'}, {'Descrição': 'ZONA SUL FL 08', 'Instituição': 'MASTERCARD', '(R$)Valor': '47,39'}, {'Descrição': 'ZONA SUL FL 08', 'Instituição': 'MASTERCARD', '(R$)Valor': '45,43'}, {'Descrição': 'MERCADOLIVRE*ALISSONEX 06/10', 'Instituição': 'VISA', '(R$)Valor': '445,00'}, {'Descrição': 'TOKIO MARINE*AUTO', 'Instituição': 'VISA', '(R$)Valor': '431,58'}, {'Descrição': 'PIX ENV MARIA CAROLINA BUT', 'Instituição': 'SANTANDER', '(R$)Valor': '400,00'}, {'Descrição': 'MANECO GOURMET', 'Instituição': 'MASTERCARD', '(R$)Valor': '40,31'}, {'Descrição': 'UBER UBER *TRIP HELP U', 'Instituição': 'MASTERCARD', '(R$)Valor': '33,93'}, {'Descrição': 'ZONA SUL FL 08', 'Instituição': 'MASTERCARD', '(R$)Valor': '33,79'}, {'Descrição': 'PIX ENV TELEFONICA BRASIL S A', 'Instituição': 'SANTANDER', '(R$)Valor': '329,99'}, {'Descrição': 'PIX ENV LIGHT SERVICOS DE ', 'Instituição': 'SANTANDER', '(R$)Valor': '317,14'}, {'Descrição': 'UBER UBER *TRIP HELP U', 'Instituição': 'MASTERCARD', '(R$)Valor': '31,95'}, {'Descrição': 'REI DO MATE', 'Instituição': 'MASTERCARD', '(R$)Valor': '30,90'}, {'Descrição': 'ZONA SUL FL 1008 PIZZ', 'Instituição': 'MASTERCARD', '(R$)Valor': '30,79'}, {'Descrição': 'PGTO DE BOLETO OUTROS BAN', 'Instituição': 'SANTANDER', '(R$)Valor': '3.141,48'}, {'Descrição': 'PIX ENV VERA LUCIA SOARES', 'Instituição': 'SANTANDER', '(R$)Valor': '3.076,71'}, {'Descrição': 'ZONA SUL FL 08', 'Instituição': 'MASTERCARD', '(R$)Valor': '29,97'}, {'Descrição': 'UTILICASA', 'Instituição': 'MASTERCARD', '(R$)Valor': '27,98'}, {'Descrição': 'ZONA SUL FL 08', 'Instituição': 'MASTERCARD', '(R$)Valor': '25,70'}, {'Descrição': 'ANUIDADE DIFERENCIADA 04/12', 'Instituição': 'VISA', '(R$)Valor': '25,00'}, {'Descrição': 'ZONA SUL FL 1008 PIZZ', 'Instituição': 'MASTERCARD', '(R$)Valor': '24,68'}, {'Descrição': 'CAFE CARDIN', 'Instituição': 'MASTERCARD', '(R$)Valor': '24,64'}, {'Descrição': 'CAFE CARDIN', 'Instituição': 'MASTERCARD', '(R$)Valor': '24,64'}, {'Descrição': 'CAFE CARDIN', 'Instituição': 'MASTERCARD', '(R$)Valor': '24,64'}, {'Descrição': 'ZONA SUL FL 08', 'Instituição': 'MASTERCARD', '(R$)Valor': '24,57'}, {'Descrição': 'ZONA SUL FL 08', 'Instituição': 'MASTERCARD', '(R$)Valor': '24,37'}, {'Descrição': 'ZONA SUL FL 1008 PIZZ', 'Instituição': 'MASTERCARD', '(R$)Valor': '24,32'}, {'Descrição': 'ZONA SUL FL 08', 'Instituição': 'MASTERCARD', '(R$)Valor': '24,17'}, {'Descrição': 'FEDREVON CAFETERIA', 'Instituição': 'MASTERCARD', '(R$)Valor': '22,50'}, {'Descrição': 'FEDREVON CAFETERIA', 'Instituição': 'MASTERCARD', '(R$)Valor': '22,50'}, {'Descrição': 'ZONA SUL FL 1008 PIZZ', 'Instituição': 'MASTERCARD', '(R$)Valor': '21,08'}, {'Descrição': 'ZONA SUL FL 08', 'Instituição': 'MASTERCARD', '(R$)Valor': '20,90'}, {'Descrição': 'SCP PLUS- FEV/25', 'Instituição': 'VISA', '(R$)Valor': '20,88'}, {'Descrição': 'PIX ENV 033698 BANCO SANTA', 'Instituição': 'SANTANDER', '(R$)Valor': '2.751,96'}, {'Descrição': 'PREPLY INC', 'Instituição': 'VISA', '(R$)Valor': '194,41'}, {'Descrição': 'ZONA SUL FL 08', 'Instituição': 'MASTERCARD', '(R$)Valor': '18,49'}, {'Descrição': 'ZONA SUL FL 27', 'Instituição': 'MASTERCARD', '(R$)Valor': '17,98'}, {'Descrição': 'ZONA SUL FL 1008 PIZZ', 'Instituição': 'MASTERCARD', '(R$)Valor': '17,13'}, {'Descrição': 'TAPIOKINHA', 'Instituição': 'MASTERCARD', '(R$)Valor': '17,00'}, {'Descrição': 'CASA VELHA', 'Instituição': 'MASTERCARD', '(R$)Valor': '16,99'}, {'Descrição': 'ZONA SUL FL 1008 PIZZ', 'Instituição': 'MASTERCARD', '(R$)Valor': '16,41'}, {'Descrição': 'FEDREVON CAFETERIA', 'Instituição': 'MASTERCARD', '(R$)Valor': '15,00'}, {'Descrição': 'ZONA SUL FL 08', 'Instituição': 'MASTERCARD', '(R$)Valor': '145,73'}, {'Descrição': 'ZONA SUL FL 1008 PIZZ', 'Instituição': 'MASTERCARD', '(R$)Valor': '14,97'}, {'Descrição': 'ZONA SUL FL 1008 PIZZ', 'Instituição': 'MASTERCARD', '(R$)Valor': '14,25'}, {'Descrição': 'RAIA432', 'Instituição': 'MASTERCARD', '(R$)Valor': '138,94'}, {'Descrição': 'SUA ACADEMIA', 'Instituição': 'VISA', '(R$)Valor': '133,08'}, {'Descrição': 'ZONA SUL FL 08', 'Instituição': 'MASTERCARD', '(R$)Valor': '130,06'}, {'Descrição': 'ZONA SUL FL 1008 PIZZ', 'Instituição': 'MASTERCARD', '(R$)Valor': '13,57'}, {'Descrição': 'ZONA SUL FL 08', 'Instituição': 'MASTERCARD', '(R$)Valor': '13,18'}, {'Descrição': 'TOKIO MARINE*VIAG06D06', 'Instituição': 'MASTERCARD', '(R$)Valor': '123,87'}, {'Descrição': 'ZONA SUL FL 08', 'Instituição': 'MASTERCARD', '(R$)Valor': '121,40'}, {'Descrição': 'TAPIOKINHA', 'Instituição': 'MASTERCARD', '(R$)Valor': '12,00'}, {'Descrição': 'MAIS1 CAFE RJ/RIO DE J', 'Instituição': 'MASTERCARD', '(R$)Valor': '11,50'}, {'Descrição': 'CONCESSAO METROVIARIA', 'Instituição': 'MASTERCARD', '(R$)Valor': '100,00'}, {'Descrição': 'IOF ADICIONAL AUTOMATICO PERIO', 'Instituição': 'SANTANDER', '(R$)Valor': '10,99'}, {'Descrição': 'SCP ESSENCIAL- FEV/25', 'Instituição': 'MASTERCARD', '(R$)Valor': '10,42'}, {'Descrição': 'PIX ENV 282028 BANCO SANTA', 'Instituição': 'SANTANDER', '(R$)Valor': '1.473,17'}, {'Descrição': 'PGTO DE BOLETO OUTROS BAN', 'Instituição': 'SANTANDER', '(R$)Valor': '1.237,19'}, {'Descrição': 'PIX ENV VERA LUCIA SOARES', 'Instituição': 'SANTANDER', '(R$)Valor': '1.028,00'}, {'Descrição': 'IOF IMPOSTO OPERACOES FINANCEI', 'Instituição': 'SANTANDER', '(R$)Valor': '0,75'}], 'mensagem': 'Consulta executada com sucesso. 86 registro(s) encontrado(s).'}

**[20:49:53]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[20:49:53]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[20:49:53]** 🔄 **FLOW:** 📝 SQL recebido: SELECT 
                grupo AS 'Grupo',
                subgrupo AS 'Subgrupo',
                de...

**[20:49:53]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[20:49:53]** 🔄 **FLOW:** 📊 RESULTADO da query SQL: {'sucesso': True, 'dados': [{'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'ZONA SUL FL 08', '(R$)Total': 1210.0}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'MERCADOLIVRE*ALISSONEX 06/10', '(R$)Total': 445.0}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'TOKIO MARINE*AUTO', '(R$)Total': 431.0}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'PIX ENV MARIA CAROLINA BUT', '(R$)Total': 400.0}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'PIX ENV TELEFONICA BRASIL S A', '(R$)Total': 329.0}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'PIX ENV LIGHT SERVICOS DE ', '(R$)Total': 317.0}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'PREPLY INC', '(R$)Total': 194.0}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'ZONA SUL FL 1008 PIZZ', '(R$)Total': 173.0}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'RAIA432', '(R$)Total': 155.0}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'SUA ACADEMIA', '(R$)Total': 133.0}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'TOKIO MARINE*VIAG06D06', '(R$)Total': 123.0}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'CONCESSAO METROVIARIA', '(R$)Total': 100.0}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': '28/02 RAIA432 UBER UBER *TRIP HELP U 03/03', '(R$)Total': 80.0}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'CAFE CARDIN', '(R$)Total': 72.0}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'DROGARIA VENANCIO', '(R$)Total': 71.0}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'PGTO CONTA GAS EM CANAIS ', '(R$)Total': 70.0}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': '07/03 DROGARIAS UBER* TRIP PACHECO 02/03', '(R$)Total': 70.0}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'PIX ENV ALLIANZ SEGUROS SA', '(R$)Total': 66.0}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'UBER UBER *TRIP HELP U', '(R$)Total': 64.0}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'UBER* TRIP', '(R$)Total': 62.0}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'O CARANGUEJO', '(R$)Total': 61.0}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'PEDAGIO ELETRONICO SEM PARAR S', '(R$)Total': 59.0}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'PAYPAL*PAYPAL *NE', '(R$)Total': 59.0}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'FEDREVON CAFETERIA', '(R$)Total': 59.0}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'MERCADOLIVRE*QUALITY21', '(R$)Total': 55.0}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'UCB *MENSALIDADES 02/06', '(R$)Total': 50.0}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'UCB *MENSALIDADES 01/06', '(R$)Total': 50.0}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'MANECO GOURMET', '(R$)Total': 40.0}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'REI DO MATE', '(R$)Total': 30.0}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'TAPIOKINHA', '(R$)Total': 29.0}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'UTILICASA', '(R$)Total': 27.0}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'ANUIDADE DIFERENCIADA 04/12', '(R$)Total': 25.0}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'SCP PLUS- FEV/25', '(R$)Total': 20.0}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'ZONA SUL FL 27', '(R$)Total': 17.0}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'CASA VELHA', '(R$)Total': 16.0}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'MAIS1 CAFE RJ/RIO DE J', '(R$)Total': 11.0}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'SCP ESSENCIAL- FEV/25', '(R$)Total': 10.0}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'IOF ADICIONAL AUTOMATICO PERIO', '(R$)Total': 10.0}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'IOF DESPESA NO EXTERIOR', '(R$)Total': 6.0}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'OGGI', '(R$)Total': 5.0}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'CONQ', '(R$)Total': 5.0}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'PGTO DE BOLETO OUTROS BAN', '(R$)Total': 4.378}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'PIX ENV VERA LUCIA SOARES', '(R$)Total': 4.104}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'PIX ENV 033698 BANCO SANTA', '(R$)Total': 2.751}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'PIX ENV 282028 BANCO SANTA', '(R$)Total': 1.473}, {'Grupo': 'Outros', 'Subgrupo': 'Não Classificados', 'Descrição': 'IOF IMPOSTO OPERACOES FINANCEI', '(R$)Total': 0.0}], 'mensagem': 'Consulta executada com sucesso. 46 registro(s) encontrado(s).'}

**[20:49:53]** 🔄 **FLOW:** ✅ SQL executado com sucesso

**[20:49:53]** 🔄 **FLOW:** INÍCIO endpoint /executar_sql

**[20:49:53]** 🔄 **FLOW:** 📝 SQL recebido: SELECT 
                grupo,
                SUM(valor) AS total
            FROM despesas_view_01...

**[20:49:53]** 🔄 **FLOW:** 💾 Database: financas.db em c:\Applications_DSB\FinCtl\data

**[20:49:53]** 🔄 **FLOW:** 📊 RESULTADO da query SQL: {'sucesso': True, 'dados': [{'grupo': 'Outros', 'total': 5221.706}], 'mensagem': 'Consulta executada com sucesso. 1 registro(s) encontrado(s).'}

**[20:49:53]** 🔄 **FLOW:** ✅ SQL executado com sucesso

