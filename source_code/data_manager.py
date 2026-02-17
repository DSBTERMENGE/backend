"""
DATA MANAGER - FRAMEWORK DSB
============================

Módulo especializado em operações de banco de dados genéricas.
Fornece operações CRUD e consultas para múltiplas aplicações.

ARQUITETURA: FUNÇÕES STATELESS (Thread-Safe        # Validações usando função orquestradora das validações
        campos_dados = list(dados_form_in.keys())
        erro_validacao = validacoes_comuns('UPDATE', tabela, campos_dados, database_path, database_name, dados_form_in, tabela_alvo, campos_obrigatorios)
        if erro_validacao:
            return erro_validacao Todas as funções são independentes e sem estado
- Thread-safe para uso em aplicações web Flask
- Sem instâncias ou estado compartilhado entre requisições
- Cada função cria/fecha conexão conforme necessário

CONCEITO:
- TABELAS: Operações CRUD (INSERT, UPDATE, DELETE, SELECT simples)
- VIEWs: Consultas complexas com JOINs para exibição/relatórios

FLUXO DE DADOS:
1. dados_form_out: Estrutura de campos enviada para o frontend criar o formulário
2. dados_form_in: Valores preenchidos pelo usuário que retornam do frontend
3. Funções extraem apenas campos da tabela do dados_form_in para operações CRUD

OPERAÇÕES:
- INSERT: Extrai campos da tabela de dados_form_in (não precisa PK)
- UPDATE: Extrai campos + PK de dados_form_in (função descobre qual é a PK)
- DELETE: Extrai apenas PK de dados_form_in (função descobre qual é a PK)
- SELECT: Aplica filtros na tabela/VIEW

EXEMPLO DE USO:
# ANTES (com classe)
db = db_manager('despesas', ['descricao', 'valor'])
resultado = db.insert_data()

# DEPOIS (função direta)
resultado = inserir_dados('despesas', dados_form_in, database_path)
"""

import psycopg2
import psycopg2.extras
import os
import sys
import bcrypt
from db_config import PG_CONFIG

# Import do debugger no topo
backend_path = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(backend_path)
from debugger import error_catcher

# Importa função de log para diagnóstico - DESATIVADO
# import sys
# sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
# from log_helper import log_acompanhamento

# Importa debugger personalizado
from debugger import flow_marker, error_catcher

# Configuração padrão do banco PostgreSQL
DB_PATH = None  # Não usado em PostgreSQL
DB_NAME = "financas"  # Nome do database PostgreSQL


# =============================================================================
#                          FUNÇÕES AUXILIARES
# =============================================================================

def _get_pg_connection(database_name=None):
    """
    Cria e retorna uma conexão PostgreSQL
    Usa configurações de db_config.py
    
    @param database_name: Nome do banco (ex: 'financas', 'inventario', 'game')
    """
    # Filtrar apenas parâmetros válidos do PostgreSQL
    valid_params = ['host', 'port', 'user', 'password', 'database', 'dbname']
    config = {k: v for k, v in PG_CONFIG.items() if k in valid_params}
    
    if database_name:
        config['database'] = database_name
    return psycopg2.connect(**config)

def _obter_campos_tabela(tabela, database_file=None):
    """
    Obtém lista de nomes de campos de uma tabela consultando information_schema
    
    @param {str} tabela - Nome da tabela
    @param {str} database_file - Não usado em PostgreSQL (mantido para compatibilidade)
    @return {list} - Lista com nomes dos campos da tabela
    
    Exemplo:
        _obter_campos_tabela('papeis_rf') → ['id_papel_rf', 'id_tipo_investimento', 'codigo_ativo', ...]
    """
    conn = None
    try:
        conn = _get_pg_connection(DB_NAME)
        cursor = conn.cursor()
        
        # Consulta PostgreSQL information_schema para obter campos
        sql = """
            SELECT column_name
            FROM information_schema.columns
            WHERE table_name = %s
            ORDER BY ordinal_position
        """
        
        cursor.execute(sql, (tabela,))
        campos = [row[0] for row in cursor.fetchall()]
        
        flow_marker(f"📋 Campos da tabela '{tabela}': {campos}")
        return campos
        
    except Exception as e:
        error_catcher(f"Erro ao obter campos da tabela '{tabela}'", e)
        return []
    finally:
        if conn:
            cursor.close()
            conn.close()

def _descobrir_pk(tabela, database_file=None):
    """
    Descobre a chave primária de uma tabela consultando information_schema do PostgreSQL
    
    @param {str} tabela - Nome da tabela
    @param {str} database_file - Não usado em PostgreSQL (mantido para compatibilidade)
    @return {str|None} - Nome do campo chave primária ou None se não encontrada
    
    Exemplo:
        _descobrir_pk('papeis_rf') → 'id_papel_rf'
        _descobrir_pk('bancos') → 'id_banco'
    """
    conn = None
    try:
        # Usa database_name global se disponível
        conn = _get_pg_connection(DB_NAME)
        cursor = conn.cursor()
        
        # Consulta PostgreSQL information_schema para obter PK
        sql = """
            SELECT c.column_name
            FROM information_schema.table_constraints tc
            JOIN information_schema.constraint_column_usage AS ccu USING (constraint_schema, constraint_name)
            JOIN information_schema.columns AS c ON c.table_schema = tc.constraint_schema
                AND tc.table_name = c.table_name AND ccu.column_name = c.column_name
            WHERE tc.constraint_type = 'PRIMARY KEY'
                AND tc.table_name = %s
            ORDER BY c.ordinal_position
            LIMIT 1
        """
        
        cursor.execute(sql, (tabela,))
        result = cursor.fetchone()
        
        if result:
            pk_field = result[0]
            flow_marker(f"🔑 PK descoberta para tabela '{tabela}': {pk_field}")
            return pk_field
        else:
            flow_marker(f"⚠️ Nenhuma PK encontrada para tabela '{tabela}'")
            return None
            
    except Exception as e:
        error_catcher(f"Erro ao descobrir PK da tabela '{tabela}'", e)
        return None
    finally:
        if conn:
            cursor.close()
            conn.close()

def _limpar_filtros_asterisco(filtros):
    """
    Remove condições com asterisco (*) dos filtros
    Asterisco indica "todos" no frontend, deve ser removido do SQL
    
    @param {str} filtros - String de filtros (ex: "idgrupo = 5 AND idmes = *")
    @return {str} - Filtros limpos (ex: "idgrupo = 5")
    
    Exemplos:
        "idgrupo = 5 AND idmes = *" → "idgrupo = 5"
        "idgrupo = * AND idmes = *" → ""
        "idgrupo = 5 AND idmes = 10" → "idgrupo = 5 AND idmes = 10"
    """
    if not filtros or not filtros.strip():
        return ""
    
    # Divide por AND
    condicoes = filtros.split(' AND ')
    
    # Filtra condições que NÃO contêm *
    condicoes_validas = [c.strip() for c in condicoes if ' = *' not in c and ' = \'*\'' not in c]
    
    # Reconstrói string
    return ' AND '.join(condicoes_validas)


# =============================================================================
#                          FUNÇÕES PRINCIPAIS
# =============================================================================


def consultar_bd(view, campos, database_path=None, database_name=None, filtros=None):
    """
    Consulta dados de uma view no banco de dados
    # O que será retornado é um dicionário de dados quando forem encontrados dados
    Função principal para consultas de dados, thread-safe e stateless
    Integra validações e retorna dados estruturados ou erro detalhado
    
    @param {str} view - Nome da view a consultar
    @param {list} campos - Lista de campos ou ["Todos"]
    @param {str} database_path - Caminho do banco (opcional)
    @param {str} database_name - Nome do banco (opcional)
    @param {dict} filtros - Filtros WHERE (opcional)
    @return {dict} - {dados: [...], erro: str, sucesso: bool}
    """
    # Validações usando função centralizada
    try:
        erro_validacao = validacoes_comuns('READ', view, campos, database_path, database_name)
        if erro_validacao:
            return erro_validacao
        
        database_caminho = os.path.join(database_path, database_name)
        
        flow_marker("INÍCIO consultar_bd", {"view": view, "campos": campos, "database": database_caminho})
        
        conn = _get_pg_connection(database_name)
        try:
            cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            
            # Determinar campos da consulta
            if campos == ["Todos"] or not campos:
                sql = f"SELECT * FROM {view}"
            else:
                campos_str = ", ".join(campos)
                sql = f"SELECT {campos_str} FROM {view}"
            
            # Adicionar filtros se fornecidos
            if filtros and filtros.strip():
                # Limpar filtros com * (equivalente a "todos")
                filtros_limpos = _limpar_filtros_asterisco(filtros)
                if filtros_limpos:
                    sql += " WHERE " + filtros_limpos
            
            cursor.execute(sql)
            
            resultados = cursor.fetchall()
            
            # Obter nomes das colunas
            colunas = [desc[0] for desc in cursor.description]
            
            # RealDictCursor já retorna dicionários
            dados = [dict(row) for row in resultados]
            
            # Será enviado um array com os campos com valor "" para permitir o funcionamento dos formulários no Frontend
            if not dados and cursor.description:
                colunas = [desc[0] for desc in cursor.description]
                registro_vazio = {coluna: "" for coluna in colunas}
                dados.append(registro_vazio)
            
            resultado_final = {
                "dados": dados,
                "erro": None,
                "sucesso": True,
                "total_registros": len(dados)
            }
            
            flow_marker("SUCESSO consultar_bd", {"registros_encontrados": len(dados)})
            return resultado_final
            
        finally:
            cursor.close()
            conn.close()
            
    except Exception as e:
        
        error_catcher("Erro na função consultar_bd", e)
        
        return {
            "dados": [],
            "erro": f"Erro na consulta: {str(e)}",
            "sucesso": False,
            "total_registros": 0
        }

# Reconstruir para atender o código atual
def get_view(nome_view, filtros=None, database_path=None, database_name=None):
    """
    
    """
    return consultar_bd(nome_view, ["Todos"], database_path, database_name, filtros)


def inserir_dados(tabela, dados_form_in, database_path=None, database_name=None, tabela_alvo=None, campos_obrigatorios=None):
    """
    Insere dados em uma tabela (stateless)
    
    @param {str} tabela - Nome da tabela/view para consulta
    @param {dict} dados_form_in - Dados do formulário
    @param {str} database_path - Caminho do banco (opcional)
    @param {str} database_name - Nome do banco (opcional)
    @param {str} tabela_alvo - Tabela real para INSERT (opcional, usa tabela se não fornecido)
    @param {list} campos_obrigatorios - Campos obrigatórios para INSERT (opcional)
    @return {dict} - Resultado da operação
    """
    try:
        # Validações usando função centralizada
        campos_dados = list(dados_form_in.keys())
        erro_validacao = validacoes_comuns('INSERT', tabela, campos_dados, database_path, database_name, dados_form_in, tabela_alvo, campos_obrigatorios)
        if erro_validacao:
            return erro_validacao
        
        # =================================================================
        # CONSTRUÇÃO DA SQL INSERT - PROCESSO ITERATIVO
        # =================================================================
        
        # PASSO 1: Iniciar SQL base
        sql = "INSERT INTO"
        
        # PASSO 2: Usar tabela_alvo para operação INSERT
        sql += f" {tabela_alvo}"
        
        # PASSO 3: Obter database_file para operações
        database_file = os.path.join(database_path, database_name)
        
        # PASSO 4: Obter campos da tabela_alvo que existem nos dados enviados
        campos_tabela_alvo = _obter_campos_tabela(tabela_alvo, database_file)
        campos_para_inserir = [campo for campo in campos_dados if campo in campos_tabela_alvo]
        
        if not campos_para_inserir:
            return {"erro": "Nenhum campo válido encontrado para inserção"}
        
        # PASSO 5: Construir parte dos campos (campo1, campo2, campo3)
        campos_str = ", ".join(campos_para_inserir)
        sql += f" ({campos_str})"
        
        # PASSO 6: Construir parte dos valores (%s, %s, %s) - PostgreSQL usa %s
        placeholders = ", ".join(["%s" for _ in campos_para_inserir])
        sql += f" VALUES ({placeholders})"
        
        # PASSO 7: Obter valores dos dados na mesma ordem dos campos
        valores_para_inserir = []
        for campo in campos_para_inserir:
            valor = dados_form_in[campo]
            
            # Trata valores vazios: converte string vazia para None (NULL no SQL)
            if valor == '':
                valor = None
            
            # Converte valores monetários (campos com "valor" no nome)
            elif 'valor' in campo.lower():
                valor = _converter_valor_monetario_para_float(valor)
            
            valores_para_inserir.append(valor)
        
        # =================================================================
        # EXECUÇÃO DA SQL INSERT
        # =================================================================
        
        conn = _get_pg_connection(database_name)
        try:
            cursor = conn.cursor()
            
            # Descobrir qual é a PK da tabela ANTES do INSERT
            pk_field = _descobrir_pk(tabela_alvo, None)  # database_file não é usado em PG
            
            # Se PK existe e não veio nos dados, adicionar RETURNING para pegar ID gerado
            if pk_field and (pk_field not in dados_form_in or not dados_form_in[pk_field]):
                sql += f" RETURNING {pk_field}"
                cursor.execute(sql, valores_para_inserir)
                result = cursor.fetchone()
                id_gerado = result[0] if result else None
                dados_form_in[pk_field] = id_gerado
            else:
                cursor.execute(sql, valores_para_inserir)
                id_gerado = dados_form_in.get(pk_field)
            
            conn.commit()
            
            return {
                "sucesso": True,
                "registros_afetados": cursor.rowcount,
                "registro_completo": dados_form_in,  # COM PK PREENCHIDA
                "id_inserido": id_gerado,
                "sql_executada": sql
            }
        finally:
            cursor.close()
            conn.close()
            
    except Exception as e:
        return {"erro": str(e)}

def atualizar_dados(tabela, dados_form_in, database_path=None, database_name=None, tabela_alvo=None, campos_obrigatorios=None):
    """
    Atualiza dados em uma tabela (stateless)
    
    @param {str} tabela - Nome da tabela
    @param {dict} dados_form_in - Dados do formulário (deve conter PK)
    @param {str} database_path - Caminho do banco (opcional)
    @param {str} database_name - Nome do banco (opcional)
    @return {dict} - Resultado da operação
    """
    try:
        # Validações usando função orquestradora das validações
        campos_dados = list(dados_form_in.keys())
        erro_validacao = validacoes_comuns('UPDATE', tabela, campos_dados, database_path, database_name, dados_form_in, tabela_alvo, campos_obrigatorios)
        if erro_validacao:
            return erro_validacao

        # =================================================================
        # CONSTRUÇÃO DA SQL UPDATE - 4 PASSOS
        # =================================================================
        
        # PASSO 1: SQL = "UPDATE " & tabela_alvo
        sql = f"UPDATE {tabela_alvo}"
        
        # PASSO 2: cpo_para_salvar = obter campos que pertencem à tabela_alvo
        database_file = os.path.join(database_path, database_name)
        campos_tabela_alvo = _obter_campos_tabela(tabela_alvo, database_file)
        
        # Filtrar campos: apenas os que existem na tabela_alvo
        campos_enviados = list(dados_form_in.keys())
        cpo_para_salvar = [campo for campo in campos_enviados if campo in campos_tabela_alvo]
        
        # PASSO 3: Obter valores de cada campo e montar cláusulas SET
        set_clauses = []
        valores_para_salvar = []
        
        # 🔑 Descobrir PK da tabela usando information_schema (método correto do framework)
        pk_field = _descobrir_pk(tabela_alvo, database_file)
        
        for campo in cpo_para_salvar:
            if campo != pk_field:  # Exclui PK dos campos de SET
                set_clauses.append(f"{campo} = %s")  # PostgreSQL usa %s
                valor = dados_form_in.get(campo)
                
                # Trata valores vazios: converte string vazia para None (NULL no SQL)
                if valor == '':
                    valor = None
                
                # Converte valores monetários (campos com "valor" no nome)
                elif 'valor' in campo.lower():
                    valor = _converter_valor_monetario_para_float(valor)
                
                valores_para_salvar.append(valor)
        
        if not set_clauses:
            return {"erro": "Nenhum campo válido encontrado para atualização"}
        
        # Complementa SQL com SET
        sql += " SET " + ", ".join(set_clauses)
        
        # PASSO 4: Obter valor da chave primária para cláusula WHERE
        if pk_field and pk_field in dados_form_in:
            sql += f" WHERE {pk_field} = %s"
            valores_para_salvar.append(dados_form_in[pk_field])
        else:
            return {"erro": f"Chave primária '{pk_field}' não encontrada nos dados enviados"}
        
        # Executar UPDATE
        conn = _get_pg_connection(database_name)
        cursor = conn.cursor()
        
        try:
            cursor.execute(sql, tuple(valores_para_salvar))
            conn.commit()
            
            return {
                "sucesso": True,
                "registros_afetados": cursor.rowcount,
                "sql_executada": sql
            }
        finally:
            cursor.close()
            conn.close()
            
    except Exception as e:
        return {"erro": str(e)}

def verificar_dependencias_delete(tabela_alvo, id_campo, id_valor, database_name=None):
    """
    Verifica se existem registros dependentes antes de deletar
    
    @param {str} tabela_alvo - Nome da tabela onde está o registro a deletar
    @param {str} id_campo - Nome do campo chave primária
    @param {int|str} id_valor - Valor da chave primária do registro
    @param {str} database_name - Nome do banco (opcional)
    @return {dict} - {'tem_dependencias': bool, 'quantidade': int, 'detalhes': list}
    
    @example
    verificar_dependencias_delete('grupos', 'id_grupo', 5, 'financas')
    Retorna: {'tem_dependencias': True, 'quantidade': 12, 'detalhes': [{'tabela': 'desp_global', 'quantidade': 10}, ...]}
    """
    try:
        conn = _get_pg_connection(database_name)
        cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        
        # Consulta para encontrar todas as FKs que referenciam esta tabela
        query_fks = """
            SELECT
                tc.table_name AS tabela_dependente,
                kcu.column_name AS coluna_fk
            FROM information_schema.table_constraints AS tc
            JOIN information_schema.key_column_usage AS kcu
                ON tc.constraint_name = kcu.constraint_name
            JOIN information_schema.constraint_column_usage AS ccu
                ON ccu.constraint_name = tc.constraint_name
            WHERE tc.constraint_type = 'FOREIGN KEY'
                AND ccu.table_name = %s
                AND ccu.column_name = %s
        """
        
        cursor.execute(query_fks, [tabela_alvo, id_campo])
        foreign_keys = cursor.fetchall()
        
        total_dependencias = 0
        detalhes = []
        
        # Para cada FK encontrada, conta quantos registros dependem
        for fk in foreign_keys:
            tabela_dep = fk['tabela_dependente']
            coluna_fk = fk['coluna_fk']
            
            # Conta registros dependentes
            query_count = f"SELECT COUNT(*) as total FROM {tabela_dep} WHERE {coluna_fk} = %s"
            cursor.execute(query_count, [id_valor])
            resultado = cursor.fetchone()
            quantidade = resultado['total']
            
            if quantidade > 0:
                total_dependencias += quantidade
                detalhes.append({
                    'tabela': tabela_dep,
                    'quantidade': quantidade
                })
        
        cursor.close()
        conn.close()
        
        return {
            'tem_dependencias': total_dependencias > 0,
            'quantidade': total_dependencias,
            'detalhes': detalhes
        }
        
    except Exception as e:
        return {
            'erro': str(e),
            'tem_dependencias': None,
            'quantidade': 0,
            'detalhes': []
        }

def excluir_dados(tabela, dados_form_in, database_path=None, database_name=None, tabela_alvo=None, forcar=False):
    """
    Exclui dados de uma tabela (stateless)
    
    @param {str} tabela - Nome da tabela/view para consulta
    @param {dict} dados_form_in - Dados do formulário (deve conter PK)
    @param {str} database_path - Caminho do banco (opcional)
    @param {str} database_name - Nome do banco (opcional)
    @param {str} tabela_alvo - Tabela real para DELETE (opcional, usa tabela se não fornecido)
    @param {bool} forcar - Se True, ignora verificação de dependências (default: False)
    @return {dict} - Resultado da operação
    """
    try:
        # Validações usando função centralizada
        campos_dados = list(dados_form_in.keys())
        erro_validacao = validacoes_comuns('DELETE', tabela, campos_dados, database_path, database_name, dados_form_in)
        if erro_validacao:
            return erro_validacao
        
        # =================================================================
        # VERIFICAÇÃO DE DEPENDÊNCIAS (apenas se não forçar)
        # =================================================================
        if not forcar:
            # Descobrir PK para verificação
            database_file = os.path.join(database_path, database_name)
            pk_field = _descobrir_pk(tabela_alvo, database_file)
            
            if pk_field and pk_field in dados_form_in:
                resultado_verificacao = verificar_dependencias_delete(
                    tabela_alvo, 
                    pk_field, 
                    dados_form_in[pk_field], 
                    database_name
                )
                
                # Se encontrou dependências, retorna erro para o frontend
                if resultado_verificacao.get('tem_dependencias'):
                    return {
                        'erro': 'dependencias_encontradas',
                        'quantidade': resultado_verificacao['quantidade'],
                        'detalhes': resultado_verificacao['detalhes']
                    }
        
        # =================================================================
        # CONSTRUÇÃO DA SQL DELETE - PROCESSO ITERATIVO
        # =================================================================
        
        # PASSO 1: Iniciar SQL base
        sql = "DELETE FROM"
        
        # PASSO 2: Usar tabela_alvo para operação DELETE
        sql += f" {tabela_alvo}"
        
        # PASSO 3: Obter database_file para operações
        database_file = os.path.join(database_path, database_name)
        
        # PASSO 4: Descobrir e obter PK
        pk_field = _descobrir_pk(tabela_alvo, database_file)
        if not pk_field:
            return {"erro": f"Não foi possível identificar chave primária da tabela {tabela_alvo}"}
        
        # PASSO 5: Montar WHERE com PK
        sql += f" WHERE {pk_field} = %s"
        
        # PASSO 6: Obter valor da PK dos dados
        if pk_field not in dados_form_in:
            return {"erro": f"Chave primária '{pk_field}' não encontrada nos dados"}
        
        valor_pk = dados_form_in[pk_field]
        
        conn = _get_pg_connection(database_name)
        try:
            cursor = conn.cursor()
            cursor.execute(sql, [valor_pk])
            conn.commit()
            
            return {
                "sucesso": True,
                "registros_afetados": cursor.rowcount
            }
        finally:
            cursor.close()
            conn.close()
            
    except Exception as e:
        return {"erro": str(e)}

def atualizar_dados_lote(tabela_alvo, dados_lote, pk_field, database_path=None, database_name=None, campos_permitidos=None):
    """
    Atualiza múltiplos registros em uma tabela (operação em lote)
    FUNÇÃO GENÉRICA: Pode ser usada para qualquer tabela do sistema
    
    Performance: 1 conexão + N UPDATEs + 1 COMMIT (muito mais rápido que N requests HTTP)
    
    @param {str} tabela_alvo - Nome da tabela para UPDATE (ex: 'despesas', 'produtos')
    @param {list[dict]} dados_lote - Array de objetos com dados para atualizar
                                     Ex: [{'iddespesa': 1234, 'idgrupo': 3, 'idsubgrupo': 5}, {...}]
    @param {str} pk_field - Nome do campo chave primária (ex: 'iddespesa', 'idproduto')
    @param {str} database_path - Caminho do banco (opcional, usa config padrão)
    @param {str} database_name - Nome do banco (opcional, usa config padrão)
    @param {list} campos_permitidos - Lista de campos que podem ser atualizados (segurança)
                                     Ex: ['idgrupo', 'idsubgrupo'] - só atualiza esses campos
                                     Se None, atualiza todos os campos enviados (exceto PK)
    
    @return {dict} - Resultado com estatísticas:
                     {
                         "sucesso": True/False,
                         "total_processados": 1000,
                         "atualizados": 950,
                         "erros": 50,
                         "erros_detalhes": [{registro: {...}, erro: "..."}]
                     }
    
    @example Reclassificação de despesas:
        resultado = atualizar_dados_lote(
            tabela_alvo='despesas',
            dados_lote=[
                {'iddespesa': 1234, 'idgrupo': 3, 'idsubgrupo': 5},
                {'iddespesa': 1235, 'idgrupo': 2, 'idsubgrupo': 8}
            ],
            pk_field='iddespesa',
            database_path='C:/Apps/data',
            database_name='financas.db',
            campos_permitidos=['idgrupo', 'idsubgrupo']
        )
    
    @example Atualização de preços em massa:
        resultado = atualizar_dados_lote(
            tabela_alvo='produtos',
            dados_lote=[
                {'idproduto': 10, 'preco': 25.50, 'estoque': 100},
                {'idproduto': 11, 'preco': 30.00, 'estoque': 50}
            ],
            pk_field='idproduto',
            campos_permitidos=['preco', 'estoque']
        )
    """
    try:
        # =================================================================
        # VALIDAÇÕES INICIAIS
        # =================================================================
        
        if not tabela_alvo:
            return {"sucesso": False, "erro": "Parâmetro 'tabela_alvo' não fornecido"}
        
        if not dados_lote or not isinstance(dados_lote, list) or len(dados_lote) == 0:
            return {"sucesso": False, "erro": "Parâmetro 'dados_lote' deve ser um array não vazio"}
        
        if not pk_field:
            return {"sucesso": False, "erro": "Parâmetro 'pk_field' não fornecido"}
        
        # Usar configuração padrão se não fornecido
        if not database_name:
            database_name = DB_NAME  # Usa configuração padrão do data_manager
        
        # PostgreSQL não usa arquivo local - database_path é ignorado
        # Comentário sobre validação removida pois PostgreSQL conecta via TCP/IP
        
        # =================================================================
        # OBTER ESTRUTURA DA TABELA
        # =================================================================
        
        # Obter campos válidos da tabela
        campos_tabela = _obter_campos_tabela(tabela_alvo, database_name)
        
        if not campos_tabela:
            return {"sucesso": False, "erro": f"Não foi possível obter estrutura da tabela '{tabela_alvo}'"}
        
        # Verificar se PK existe na tabela
        if pk_field not in campos_tabela:
            return {"sucesso": False, "erro": f"Campo PK '{pk_field}' não existe na tabela '{tabela_alvo}'"}
        
        # =================================================================
        # PROCESSAMENTO EM LOTE
        # =================================================================
        
        stats = {
            "sucesso": True,
            "total_processados": len(dados_lote),
            "atualizados": 0,
            "erros": 0,
            "erros_detalhes": []
        }
        
        conn = _get_pg_connection(database_name)
        cursor = conn.cursor()
        
        try:
            for idx, registro in enumerate(dados_lote):
                try:
                    # Validar que registro é um dicionário
                    if not isinstance(registro, dict):
                        raise ValueError(f"Registro na posição {idx} não é um dicionário")
                    
                    # Validar que PK existe no registro
                    if pk_field not in registro:
                        raise ValueError(f"Campo PK '{pk_field}' não encontrado no registro")
                    
                    valor_pk = registro[pk_field]
                    
                    # Identificar campos para atualizar (excluindo PK)
                    campos_update = {k: v for k, v in registro.items() if k != pk_field}
                    
                    # Aplicar filtro de campos permitidos (segurança)
                    if campos_permitidos:
                        campos_update = {k: v for k, v in campos_update.items() if k in campos_permitidos}
                    
                    # Validar que restaram campos para atualizar
                    if not campos_update:
                        raise ValueError("Nenhum campo válido para atualizar após filtros")
                    
                    # Validar que campos existem na tabela
                    campos_invalidos = [c for c in campos_update.keys() if c not in campos_tabela]
                    if campos_invalidos:
                        raise ValueError(f"Campos inválidos: {campos_invalidos}")
                    
                    # =================================================================
                    # CONSTRUIR E EXECUTAR SQL UPDATE
                    # =================================================================
                    
                    # Montar cláusulas SET
                    set_clauses = [f"{campo} = %s" for campo in campos_update.keys()]
                    sql = f"UPDATE {tabela_alvo} SET {', '.join(set_clauses)} WHERE {pk_field} = %s"
                    
                    # Montar valores (campos + pk)
                    valores = list(campos_update.values()) + [valor_pk]
                    
                    # Executar UPDATE
                    cursor.execute(sql, valores)
                    
                    # Verificar se registro foi atualizado
                    if cursor.rowcount > 0:
                        stats["atualizados"] += 1
                    else:
                        # Registro não encontrado (PK não existe)
                        stats["erros"] += 1
                        stats["erros_detalhes"].append({
                            "registro": registro,
                            "erro": f"Registro com {pk_field}={valor_pk} não encontrado"
                        })
                
                except Exception as e_registro:
                    # Erro individual - registra mas continua processando
                    stats["erros"] += 1
                    stats["erros_detalhes"].append({
                        "registro": registro,
                        "erro": str(e_registro)
                    })
            
            # =================================================================
            # COMMIT ÚNICO NO FINAL (PERFORMANCE!)
            # =================================================================
            conn.commit()
            
        finally:
            conn.close()
        
        # Limitar erros_detalhes a 100 registros para evitar payload muito grande
        if len(stats["erros_detalhes"]) > 100:
            stats["erros_detalhes"] = stats["erros_detalhes"][:100]
            stats["aviso"] = "Lista de erros truncada em 100 registros"
        
        return stats
        
    except Exception as e:
        return {
            "sucesso": False,
            "erro": f"Erro geral na atualização em lote: {str(e)}",
            "total_processados": 0,
            "atualizados": 0,
            "erros": 0
        }


"""
==================================================================
                      FUNÇÕES AUXILIARES
==================================================================
"""
def _converter_valor_monetario_para_float(valor):
    """
    Converte valor monetário (string ou número) para float.
    Detecta automaticamente o formato do valor:
    - Brasileiro com milhar: "1.234,56" ou "1.234.567,89"
    - Brasileiro sem milhar: "1234,56"
    - Americano: "1234.56"
    - Inteiro: "1234" ou 1234
    - Float: 1234.56
    
    @param {str|int|float} valor - Valor a ser convertido
    @return {float} - Valor convertido para float
    """
    # Se já é número, retorna como float
    if isinstance(valor, (int, float)):
        return float(valor)
    
    # Se não é string, tenta converter
    if not isinstance(valor, str):
        return float(valor)
    
    # Remove espaços em branco
    valor = valor.strip()
    
    # Se vazio, retorna 0
    if not valor:
        return 0.0
    
    # Detecta formato analisando vírgula e ponto
    tem_virgula = ',' in valor
    tem_ponto = '.' in valor
    
    if tem_virgula and tem_ponto:
        # Formato brasileiro: "1.234,56" ou "1.234.567,89"
        # Remove pontos (separadores de milhar) e substitui vírgula por ponto
        valor = valor.replace('.', '').replace(',', '.')
        return float(valor)
    
    elif tem_virgula and not tem_ponto:
        # Formato brasileiro sem milhar: "1234,56"
        valor = valor.replace(',', '.')
        return float(valor)
    
    elif tem_ponto and not tem_virgula:
        # Pode ser americano "1234.56" ou milhar sem decimal "1.234"
        partes = valor.split('.')
        if len(partes[-1]) == 2:
            # Provavelmente decimal americano: "1234.56"
            return float(valor)
        elif len(partes[-1]) == 3 and len(partes) > 1:
            # Provavelmente milhar: "1.234"
            valor = valor.replace('.', '')
            return float(valor)
        else:
            # Caso padrão: trata como americano
            return float(valor)
    
    else:
        # Só dígitos: "1234"
        return float(valor)

def _obter_campos_tabela(tabela, database_file=None):
    """
    Obtém lista de campos da tabela (função auxiliar)
    
    @param {str} tabela - Nome da tabela
    @param {str} database_file - Não usado em PostgreSQL (compatibilidade)
    @return {list} - Lista de nomes dos campos
    """
    try:
        conn = _get_pg_connection(database_file)
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT column_name 
                FROM information_schema.columns 
                WHERE table_name = %s
                ORDER BY ordinal_position
            """, (tabela,))
            return [row[0] for row in cursor.fetchall()]
        finally:
            cursor.close()
            conn.close()
    except:
        return []

def _obter_colunas_view(nome_view, database_file=None):
    """
    Obtém colunas de uma view (função auxiliar)
    
    @param {str} nome_view - Nome da view
    @param {str} database_file - Não usado em PostgreSQL (compatibilidade)
    @return {list} - Lista de nomes das colunas
    """
    try:
        conn = _get_pg_connection(database_file)
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT column_name 
                FROM information_schema.columns 
                WHERE table_name = %s
                ORDER BY ordinal_position
            """, (nome_view,))
            return [row[0] for row in cursor.fetchall()]
        finally:
            cursor.close()
            conn.close()
    except:
        return []

def executar_sql(sql, database_path, database_name):
    """
    Executa SQL direto no banco de dados com retorno estruturado
    
    @param {str} sql - Comando SQL a executar
    @param {str} database_path - Caminho do banco
    @param {str} database_name - Nome do banco
    @return {dict} - Resultado estruturado da operação
    
    Retorna para consultas SELECT:
    {"sucesso": True, "dados": [{"campo1": "valor1", "campo2": "valor2"}], "mensagem": "Consulta executada"}
    
    Retorna para DDL/DML:
    {"sucesso": True, "registros_afetados": N, "mensagem": "Operação executada"}
    
    Retorna para erros:
    {"sucesso": False, "erro": "mensagem_erro"}
    """
    try: 
        conn = _get_pg_connection(database_name)
        try:
            cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            cursor.execute(sql)
            
            # Detecta se é uma consulta SELECT (retorna dados)
            sql_upper = sql.strip().upper()
            if sql_upper.startswith('SELECT') or sql_upper.startswith('WITH'):
                # Consulta que retorna dados
                dados_brutos = cursor.fetchall()
                
                if dados_brutos:
                    # RealDictCursor já retorna dicionários
                    dados_estruturados = [dict(row) for row in dados_brutos]
                    
                    return {
                        "sucesso": True,
                        "dados": dados_estruturados,
                        "mensagem": f"Consulta executada com sucesso. {len(dados_estruturados)} registro(s) encontrado(s)."
                    }
                else:
                    return {
                        "sucesso": True,
                        "dados": [],
                        "mensagem": "Consulta executada com sucesso. Nenhum registro encontrado."
                    }
            else:
                # Comando DDL/DML (CREATE, INSERT, UPDATE, DELETE, etc.)
                conn.commit()
                return {
                    "sucesso": True,
                    "registros_afetados": cursor.rowcount,
                    "mensagem": f"Operação executada com sucesso. {cursor.rowcount} registro(s) afetado(s)."
                }
        finally:
            cursor.close()
            conn.close()
            
    except Exception as e:
        return {
            "sucesso": False,
            "erro": str(e)
        }

"""
==================================================================
                     FUNÇÕES AUXILIARES
==================================================================
"""
def _descobrir_pk(tabela, database_file=None):
    """
    Descobre qual é a chave primária de uma tabela
    
    @param {str} tabela - Nome da tabela
    @param {str} database_file - Não usado em PostgreSQL (compatibilidade)
    @return {str|None} - Nome da coluna PK ou None
    """
    try:
        conn = _get_pg_connection(database_file)
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT a.attname
                FROM pg_index i
                JOIN pg_attribute a ON a.attrelid = i.indrelid
                                   AND a.attnum = ANY(i.indkey)
                WHERE i.indrelid = %s::regclass
                  AND i.indisprimary
            """, (tabela,))
            result = cursor.fetchone()
            return result[0] if result else None
        finally:
            cursor.close()
            conn.close()
    except:
        return None

"""
==================================================================
                      VALIDAÇÕES
==================================================================
"""

def valida_bd(path_name=None, bd_name=None):
    """
    Valida se consegue conectar ao banco de dados PostgreSQL
    Parâmetros mantidos para compatibilidade mas não são usados
    
    @param {str} path_name - Não usado em PostgreSQL (compatibilidade)
    @param {str} bd_name - Não usado em PostgreSQL (compatibilidade)
    @return {bool} - True se conecta, False se não conecta
    """
    try:
        conn = _get_pg_connection(bd_name)
        conn.close()
        return True
    except Exception as e:
        error_catcher(
            f"Erro ao conectar ao banco PostgreSQL: {str(e)}",
            f"Config: {PG_CONFIG['host']}:{PG_CONFIG['port']}/{PG_CONFIG['database']}"
        )
        return False

def valida_view_or_tab(nome_view_tab, path_name, bd_name):
    """
    Valida se a view, tabela ou table_target existe no banco de dados especificado
    
    @param {str} nome_view_tab - Nome da view, tabela ou table_target a verificar
    @param {str} path_name - Caminho do diretório do banco
    @param {str} bd_name - Nome do arquivo do banco
    @return {bool} - True se existe, False se não existe
    """
    try:
        # Primeiro valida se o banco existe
        if not valida_bd(path_name, bd_name):
            return False
            
        # Constrói o caminho completo do banco
        # Conecta ao banco e verifica se view/tabela existe
        conn = _get_pg_connection(bd_name)
        try:
            cursor = conn.cursor()
            
            # Query para verificar se view ou tabela existe no PostgreSQL
            cursor.execute("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_name = %s
            """, (nome_view_tab,))
            
            resultado = cursor.fetchone()
            
            if resultado:
                return True
            else:
                # Log de erro quando view/tabela não existe
                error_catcher(
                    f"View/Tabela não encontrada: {nome_view_tab}",
                    f"Banco: {PG_CONFIG['database']}"
                )
                return False
        finally:
            cursor.close()
            conn.close()
                
    except Exception as e:
        # Log de erro para exceções
        db_info = f"{path_name}/{bd_name}" if path_name else bd_name
        error_catcher(
            f"Erro ao validar view/tabela: {str(e)}",
            f"View: {nome_view_tab}, Banco: {db_info}"
        )
        return False

def valida_campos(campos, nome_view_tab, path_name, bd_name):
    """
    Valida se os campos informados existem na view ou tabela especificada
    
    @param {list} campos - Lista de campos a verificar
    @param {str} nome_view_tab - Nome da view ou tabela
    @param {str} path_name - Caminho do diretório do banco
    @param {str} bd_name - Nome do arquivo do banco
    @return {bool} - True se todos os campos existem, False caso contrário
    """
    try:
        # Primeiro valida se a view/tabela existe
        if not valida_view_or_tab(nome_view_tab, path_name, bd_name):
            return False
            
        # Se campos é ["Todos"], considera válido
        if campos == ["Todos"] or not campos:
            return True
            
        # Constrói o caminho completo do banco
        caminho_completo = os.path.join(path_name, bd_name)
        
        # Conecta ao banco e obtém informações dos campos
        conn = _get_pg_connection(bd_name)
        try:
            cursor = conn.cursor()
            
            # Obtém informações dos campos da tabela/view
            cursor.execute("""
                SELECT column_name 
                FROM information_schema.columns 
                WHERE table_name = %s
            """, (nome_view_tab,))
            colunas_existentes = cursor.fetchall()
            
            # Extrai apenas os nomes das colunas
            nomes_colunas = [coluna[0] for coluna in colunas_existentes]
            
            # Verifica se todos os campos solicitados existem
            campos_inexistentes = []
            for campo in campos:
                if campo not in nomes_colunas:
                    campos_inexistentes.append(campo)
            
            if campos_inexistentes:
                # Log de erro para campos inexistentes
                error_catcher(
                    f"Campos não encontrados na {nome_view_tab}: {', '.join(campos_inexistentes)}",
                    f"Campos disponíveis: {', '.join(nomes_colunas)}"
                )
                return False
            else:
                return True
        finally:
            cursor.close()
            conn.close()
                
    except Exception as e:
        # Log de erro para exceções
        error_catcher(
            f"Erro ao validar campos: {str(e)}",
            f"Campos: {campos}, View: {nome_view_tab}, Banco: {os.path.join(path_name, bd_name)}"
        )
        return False

def valida_PrimaryKey(campos, tabela, database_path=None, database_name=None):
    """
    Valida se a chave primária da tabela está presente nos campos enviados
    
    @param {list} campos - Lista de campos a verificar
    @param {str} tabela - Nome da tabela
    @param {str} database_path - Não usado em PostgreSQL (compatibilidade)
    @param {str} database_name - Não usado em PostgreSQL (compatibilidade)
    @return {bool} - True se PK está presente, False caso contrário
    """
    try:
        # Descobre qual é a chave primária da tabela
        pk_field = _descobrir_pk(tabela, None)
        
        # Verifica se a tabela possui chave primária
        if not pk_field:
            error_catcher(
                f"ERRO DESENVOLVEDOR: Tabela sem chave primária",
                f"Tabela '{tabela}' não possui chave primária definida - Defina uma PK na estrutura da tabela"
            )
            return False
        
        # Verifica se a PK está presente nos campos enviados
        if pk_field not in campos:
            error_catcher(
                f"ERRO DESENVOLVEDOR: Chave primária ausente nos campos",
                f"Campo PK '{pk_field}' não encontrado na lista {campos} - Inclua a PK nos dados ou corrija a lista de campos"
            )
            return False
        
        return True
        
    except Exception as e:
        # Log de erro para exceções
        error_catcher(
            f"Erro ao validar chave primária: {str(e)}",
            f"Campos: {campos}, Tabela: {tabela}, Banco: {os.path.join(database_path, database_name)}"
        )
        return False

def valida_campos_obrigatorios(campos_obrigatorios, campos_enviados):
    """
    Valida se todos os campos obrigatórios estão presentes nos campos enviados
    
    @param {list} campos_obrigatorios - Lista de campos obrigatórios
    @param {list} campos_enviados - Lista de campos enviados
    @return {bool} - True se todos estão presentes, False caso contrário
    """
    try:
        if not campos_obrigatorios:
            return True
            
        campos_faltantes = [campo for campo in campos_obrigatorios if campo not in campos_enviados]
        
        if campos_faltantes:
            error_catcher(
                f"Campos obrigatórios ausentes: {campos_faltantes}",
                f"Obrigatórios: {campos_obrigatorios}, Enviados: {campos_enviados}"
            )
            return False
        
        return True
        
    except Exception as e:
        error_catcher(
            f"Erro ao validar campos obrigatórios: {str(e)}",
            f"Obrigatórios: {campos_obrigatorios}, Enviados: {campos_enviados}"
        )
        return False

def valida_Campos_obrigatorios_tem_dados(campos_obrigatorios, dados_enviados):
    """
    Valida se todos os campos obrigatórios possuem dados (não vazios/null)
    
    @param {list} campos_obrigatorios - Lista de campos obrigatórios
    @param {dict} dados_enviados - Dicionário com dados enviados
    @return {bool} - True se todos têm dados, False caso contrário
    """
    try:
        if not campos_obrigatorios or not dados_enviados:
            return True
            
        campos_sem_dados = []
        for campo in campos_obrigatorios:
            valor = dados_enviados.get(campo)
            # Verifica se campo está vazio, None, ou string vazia
            if valor is None or valor == "" or (isinstance(valor, str) and valor.strip() == ""):
                campos_sem_dados.append(campo)
        
        if campos_sem_dados:
            error_catcher(
                f"Campos obrigatórios sem dados: {campos_sem_dados}",
                f"Obrigatórios: {campos_obrigatorios}, Dados: {dados_enviados}"
            )
            return False
        
        return True
        
    except Exception as e:
        error_catcher(
            f"Erro ao validar dados dos campos obrigatórios: {str(e)}",
            f"Obrigatórios: {campos_obrigatorios}, Dados: {dados_enviados}"
        )
        return False

def validacoes_comuns(crud_operation, nome_view_tab, campos, database_path, database_name, dados=None, tabela_alvo=None, campos_obrigatorios=None):
    """
    Executa validações comuns e específicas para operações CRUD
    
    OBJETIVO: Centralizar todas as validações em uma única função para evitar
    repetição de código e garantir consistência entre todas as operações CRUD.
    
    VALIDAÇÕES COMUNS (executam sempre):
    - Valida se o banco de dados existe e é acessível
    - Valida se a tabela/view existe no banco
    
    VALIDAÇÕES ESPECÍFICAS (por tipo de operação):
    - SELECT: Valida campos solicitados
    - INSERT: Valida campos para inserção
    - UPDATE: Valida campos + chave primária obrigatória
    - DELETE: Valida apenas chave primária
    
    @param {str} crud_operation - Tipo de operação: 'SELECT', 'INSERT', 'UPDATE', 'DELETE'
    @param {str} tabela - Nome da tabela/view
    @param {list} campos - Lista de campos envolvidos na operação
    @param {str} database_path - Caminho do diretório do banco
    @param {str} database_name - Nome do arquivo do banco
    @param {dict} dados - Dados da operação (opcional, para validações específicas)
    @return {dict|None} - Dicionário com erro se inválido, None se todas validações passaram
    """
    
    # =================================================================
    # VALIDAÇÕES COMUNS - Executam para todas as operações CRUD
    # =================================================================
    
    # Valida existência e acessibilidade do banco de dados
    if not valida_bd(database_path, database_name):
        return {
            "dados": [],
            "erro": f"Banco de dados inválido: {os.path.join(database_path, database_name)}",
            "sucesso": False
        }
    
    # Valida existência da tabela/view no banco
    if not valida_view_or_tab(nome_view_tab, database_path, database_name):
        return {
            "dados": [],
            "erro": f"Tabela/view '{nome_view_tab}' não encontrada no banco de dados",
            "sucesso": False
        }
    
    if not valida_campos(campos, nome_view_tab, database_path, database_name):
            return {
                "dados": [],
                "erro": f"Campos inválidos para a tabela/view '{nome_view_tab}'",
                "sucesso": False
            }

    # =================================================================
    # VALIDAÇÕES ESPECÍFICAS - Por tipo de operação CRUD
    # =================================================================
    
    # Operações que precisam validar campos
    if crud_operation in ['INSERT', 'UPDATE', 'DELETE']:
        # POR GARANTIA: Valida tabela_alvo pois pode ser diferente de nome_view_tab
        if tabela_alvo and not valida_view_or_tab(tabela_alvo, database_path, database_name):
            return {
                "dados": [],
                "erro": f"Tabela de destino '{tabela_alvo}' não encontrada",
                "sucesso": False
            }
        
    # Validações específicas para INSERT e UPDATE
    if crud_operation in ['INSERT', 'UPDATE']:
        # Teste: verifica se campos_obrigatorios estão contidos em campos
        if not valida_campos_obrigatorios(campos_obrigatorios, campos):
            return {
                "dados": [],
                "erro": f"Campos obrigatórios inválidos",
                "sucesso": False
            }
        
        # Teste: verifica se campos_obrigatorios possuem dados preenchidos
        if not valida_Campos_obrigatorios_tem_dados(campos_obrigatorios, dados):
            return {
                "dados": [],
                "erro": f"Campos obrigatórios sem dados preenchidos",
                "sucesso": False
            }
    

 


    # Se chegou até aqui, todas as validações passaram
    return None


# =============================================================================
#                       AUTENTICAÇÃO DE USUÁRIOS
# =============================================================================

def autoriza_login(username, password, database_path, database_name):
    """
    Autoriza login de usuário verificando credenciais
    
    @param {str} username - Nome de usuário (case-sensitive)
    @param {str} password - Senha do usuário
    @param {str} database_path - Caminho do banco de dados
    @param {str} database_name - Nome do banco de dados
    @return {dict} - {sucesso: bool, message: str}
    """
    resultado = consultar_bd(
        view='usuarios_ativos_view',
        campos=['id', 'username', 'password_hash'],
        database_path=database_path,
        database_name=database_name,
        filtros=f"username = '{username}'"
    )
    
    if not resultado.get('sucesso') or not resultado['dados']:
        return {'sucesso': False, 'message': 'Usuário ou senha não cadastrados'}
    
    user = resultado['dados'][0]
    
    if user['username'] != username:
        return {'sucesso': False, 'message': 'Usuário ou senha não cadastrados'}
    
    hash_bytes = user['password_hash'].encode('utf-8') if isinstance(user['password_hash'], str) else user['password_hash']
    
    if bcrypt.checkpw(password.encode('utf-8'), hash_bytes):
        return {'sucesso': True, 'message': 'Usuário logado', 'id_usuario': user['id']}
    
    return {'sucesso': False, 'message': 'Usuário ou senha não cadastrados'}

