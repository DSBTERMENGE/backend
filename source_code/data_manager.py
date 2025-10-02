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

import sqlite3
import os
import sys

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

# Configuração padrão do banco - pode ser sobrescrita nas funções
DB_NAME = "financas.db"


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
        
        with sqlite3.connect(database_caminho) as conn:
            cursor = conn.cursor()
            
            # Determinar campos da consulta
            if campos == ["Todos"] or not campos:
                sql = f"SELECT * FROM {view}"
            else:
                campos_str = ", ".join(campos)
                sql = f"SELECT {campos_str} FROM {view}"
            
            # Adicionar filtros se fornecidos
            if filtros and filtros.strip():
                sql += " WHERE " + filtros
            
            cursor.execute(sql)
            
            resultados = cursor.fetchall()
            
            # Obter nomes das colunas
            colunas = [desc[0] for desc in cursor.description]
            
            # Converter para lista de dicionários
            dados = []
            for linha in resultados:
                registro = dict(zip(colunas, linha))
                dados.append(registro)
            
            # Será enviado um array com os campos com valor "" para permitir o funcionamento dos formulários no Frontend
            if not dados and colunas:
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
        
        # PASSO 6: Construir parte dos valores (?, ?, ?)
        placeholders = ", ".join(["?" for _ in campos_para_inserir])
        sql += f" VALUES ({placeholders})"
        
        # PASSO 7: Obter valores dos dados na mesma ordem dos campos
        valores_para_inserir = [dados_form_in[campo] for campo in campos_para_inserir]
        
        # =================================================================
        # EXECUÇÃO DA SQL INSERT
        # =================================================================
        
        with sqlite3.connect(database_file) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, valores_para_inserir)
            conn.commit()
            
            # =================================================================
            # TRATAMENTO DA PK AUTOINCREMENT
            # =================================================================
            
            # Descobrir qual é a PK da tabela
            database_file = os.path.join(database_path, database_name)
            pk_field = _descobrir_pk(tabela_alvo, database_file)
            
            # Verificar se PK veio vazia/None nos dados enviados
            if pk_field and (pk_field not in dados_form_in or not dados_form_in[pk_field]):
                # PK estava vazia - pegar ID gerado pelo autoincrement
                id_gerado = cursor.lastrowid
                dados_form_in[pk_field] = id_gerado
            
            return {
                "sucesso": True,
                "registros_afetados": cursor.rowcount,
                "registro_completo": dados_form_in,  # COM PK PREENCHIDA
                "id_inserido": cursor.lastrowid,
                "sql_executada": sql
            }
            
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
        
        # Campos para salvar (que existem na tabela_alvo e estão nos dados enviados)
        campos_enviados = list(dados_form_in.keys())
        cpo_para_salvar = [campo for campo in campos_enviados if campo in campos_tabela_alvo]
        
        # PASSO 3: Obter valores de cada campo do array de dados
        valores_para_salvar = []
        set_clauses = []
        
        # Descobre chave primária para excluir dos campos de update
        database_file = os.path.join(database_path, database_name)
        pk_field = _descobrir_pk(tabela_alvo, database_file)
        
        for campo in cpo_para_salvar:
            if campo != pk_field:  # Exclui PK dos campos de SET
                set_clauses.append(f"{campo} = ?")
                valores_para_salvar.append(dados_form_in.get(campo))
        
        if not set_clauses:
            return {"erro": "Nenhum campo válido encontrado para atualização"}
        
        # Complementa SQL com SET
        sql += " SET " + ", ".join(set_clauses)
        
        # PASSO 4: Obter valor da chave primária para cláusula WHERE
        if pk_field and pk_field in dados_form_in:
            sql += f" WHERE {pk_field} = ?"
            valores_para_salvar.append(dados_form_in[pk_field])
        else:
            return {"erro": f"Chave primária '{pk_field}' não encontrada nos dados"}

        # =================================================================
        # EXECUÇÃO DA SQL UPDATE
        # =================================================================
        
        with sqlite3.connect(database_file) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, valores_para_salvar)
            conn.commit()
            
            return {
                "sucesso": True,
                "registros_afetados": cursor.rowcount,
                "sql_executada": sql
            }
            
    except Exception as e:
        return {"erro": str(e)}

def excluir_dados(tabela, dados_form_in, database_path=None, database_name=None, tabela_alvo=None):
    """
    Exclui dados de uma tabela (stateless)
    
    @param {str} tabela - Nome da tabela/view para consulta
    @param {dict} dados_form_in - Dados do formulário (deve conter PK)
    @param {str} database_path - Caminho do banco (opcional)
    @param {str} database_name - Nome do banco (opcional)
    @param {str} tabela_alvo - Tabela real para DELETE (opcional, usa tabela se não fornecido)
    @return {dict} - Resultado da operação
    """
    try:
        # Validações usando função centralizada
        campos_dados = list(dados_form_in.keys())
        erro_validacao = validacoes_comuns('DELETE', tabela, campos_dados, database_path, database_name, dados_form_in)
        if erro_validacao:
            return erro_validacao
        
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
        sql += f" WHERE {pk_field} = ?"
        
        # PASSO 6: Obter valor da PK dos dados
        if pk_field not in dados_form_in:
            return {"erro": f"Chave primária '{pk_field}' não encontrada nos dados"}
        
        valor_pk = dados_form_in[pk_field]
        
        with sqlite3.connect(database_file) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, [valor_pk])
            conn.commit()
            
            return {
                "sucesso": True,
                "registros_afetados": cursor.rowcount
            }
            
    except Exception as e:
        return {"erro": str(e)}


"""
==================================================================
                      FUNÇÕES AUXILIARES
==================================================================
"""
def _obter_campos_tabela(tabela, database_file):
    """
    Obtém lista de campos da tabela (função auxiliar)
    
    @param {str} tabela - Nome da tabela
    @param {str} database_file - Caminho do banco
    @return {list} - Lista de nomes dos campos
    """
    try:
        with sqlite3.connect(database_file) as conn:
            cursor = conn.cursor()
            cursor.execute(f"PRAGMA table_info({tabela})")
            return [row[1] for row in cursor.fetchall()]
    except:
        return []

def _obter_colunas_view(nome_view, database_file):
    """
    Obtém colunas de uma view (função auxiliar)
    
    @param {str} nome_view - Nome da view
    @param {str} database_file - Caminho do banco
    @return {list} - Lista de nomes das colunas
    """
    try:
        with sqlite3.connect(database_file) as conn:
            cursor = conn.cursor()
            cursor.execute(f"PRAGMA table_info({nome_view})")
            return [row[1] for row in cursor.fetchall()]
    except:
        return []

def executar_sql(sql, database_path=None, database_name=None):
    """
    Executa SQL direto no banco (CREATE TABLE, CREATE VIEW, etc.)
    
    @param {str} sql - Comando SQL a executar
    @param {str} database_path - Caminho do banco (opcional)
    @param {str} database_name - Nome do banco (opcional)
    @return {dict} - Resultado da operação
    """
    try:
        # Define valores padrão se não fornecidos
        if database_path is None:
            database_path = "c:\\Applications_DSB\\database"
        if database_name is None:
            database_name = "finctl.db"
        
        database_file = os.path.join(database_path, database_name)
        
        with sqlite3.connect(database_file) as conn:
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            
            return {
                "sucesso": True,
                "registros_afetados": cursor.rowcount
            }
            
    except Exception as e:
        return {"erro": str(e)}

"""
==================================================================
                     FUNÇÕES AUXILIARES
==================================================================
"""
def _descobrir_pk(tabela, database_file):
    """
    Descobre qual é a chave primária de uma tabela
    
    @param {str} tabela - Nome da tabela
    @param {str} database_file - Caminho do banco
    @return {str|None} - Nome da coluna PK ou None
    """
    try:
        with sqlite3.connect(database_file) as conn:
            cursor = conn.cursor()
            cursor.execute(f"PRAGMA table_info({tabela})")
            for row in cursor.fetchall():
                if row[5] == 1:  # Coluna 5 é pk (0=não, 1=sim)
                    return row[1]  # Coluna 1 é nome do campo
    except:
        return None
    return None

"""
==================================================================
                      VALIDAÇÕES
==================================================================
"""

def valida_bd(path_name, bd_name):
    """
    Valida se o banco de dados existe no caminho especificado
    
    @param {str} path_name - Caminho do diretório do banco
    @param {str} bd_name - Nome do arquivo do banco
    @return {bool} - True se existe, False se não existe
    """
    try:
        # Constrói o caminho completo do banco
        caminho_completo = os.path.join(path_name, bd_name)
        
        # Verifica se o arquivo existe
        if os.path.exists(caminho_completo):
            return True
        else:
            # Log de erro quando BD não existe
            error_catcher(
                f"Banco de dados não encontrado: {caminho_completo}",
                f"Path: {path_name}, Nome: {bd_name}"
            )
            return False
            
    except Exception as e:
        # Log de erro para exceções
        error_catcher(
            f"Erro ao validar banco de dados: {str(e)}",
            f"Path: {path_name}, Nome: {bd_name}"
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
        caminho_completo = os.path.join(path_name, bd_name)
        
        # Conecta ao banco e verifica se view/tabela existe
        with sqlite3.connect(caminho_completo) as conn:
            cursor = conn.cursor()
            
            # Query para verificar se view ou tabela existe
            cursor.execute("""
                SELECT name FROM sqlite_master 
                WHERE type IN ('table', 'view') 
                AND name = ?
            """, (nome_view_tab,))
            
            resultado = cursor.fetchone()
            
            if resultado:
                return True
            else:
                # Log de erro quando view/tabela não existe
                error_catcher(
                    f"View/Tabela não encontrada: {nome_view_tab}",
                    f"Banco: {caminho_completo}"
                )
                return False
                
    except Exception as e:
        # Log de erro para exceções
        error_catcher(
            f"Erro ao validar view/tabela: {str(e)}",
            f"View: {nome_view_tab}, Banco: {os.path.join(path_name, bd_name)}"
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
        with sqlite3.connect(caminho_completo) as conn:
            cursor = conn.cursor()
            
            # Obtém informações dos campos da tabela/view
            cursor.execute(f"PRAGMA table_info({nome_view_tab})")
            colunas_existentes = cursor.fetchall()
            
            # Extrai apenas os nomes das colunas
            nomes_colunas = [coluna[1] for coluna in colunas_existentes]
            
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
                
    except Exception as e:
        # Log de erro para exceções
        error_catcher(
            f"Erro ao validar campos: {str(e)}",
            f"Campos: {campos}, View: {nome_view_tab}, Banco: {os.path.join(path_name, bd_name)}"
        )
        return False

def valida_PrimaryKey(campos, tabela, database_path, database_name):
    """
    Valida se a chave primária da tabela está presente nos campos enviados
    
    @param {list} campos - Lista de campos a verificar
    @param {str} tabela - Nome da tabela
    @param {str} database_path - Caminho do diretório do banco
    @param {str} database_name - Nome do arquivo do banco
    @return {bool} - True se PK está presente, False caso contrário
    """
    try:
        # Constrói o caminho completo do banco
        database_file = os.path.join(database_path, database_name)
        
        # Descobre qual é a chave primária da tabela
        pk_field = _descobrir_pk(tabela, database_file)
        
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
