"""
DATA MANAGER - FRAMEWORK DSB
============================

Módulo especializado em operações de banco de dados genéricas.
Fornece operações CRUD e consultas para múltiplas aplicações.

ARQUITETURA: FUNÇÕES STATELESS (Thread-Safe)
- Todas as funções são independentes e sem estado
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

# Importa função de log para diagnóstico
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from log_helper import log_acompanhamento

# Importa debugger personalizado
from debugger import flow_marker, error_catcher

# Importa função de validação
from .validador_dados import validar_bd

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
    # Validação do banco de dados
    try:
        if not validar_bd(database_path, database_name):
            return {
                "dados": [],
                "erro": f"Banco de dados inválido: {os.path.join(database_path, database_name)}",
            }
        
        # Validação da view
        if not valida_view_or_tab(view, database_path, database_name):
            return {
                "dados": [],
                "erro": f"View/tabela '{view}' não encontrada no banco de dados",
            }

        # Validação dos campos enviados pelo desenvolvedor
        if not valida_campos(campos, view, database_path, database_name):
            return {
                "dados": [],
                "erro": f"Campos inválidos para a view/tabela '{view}'",
            }
        
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
            if filtros:
                where_conditions = []
                for campo, valor in filtros.items():
                    where_conditions.append(f"{campo} = ?")
                if where_conditions:
                    sql += " WHERE " + " AND ".join(where_conditions)
                    cursor.execute(sql, list(filtros.values()))
                else:
                    cursor.execute(sql)
            else:
                cursor.execute(sql)
            
            resultados = cursor.fetchall()
            
            # Obter nomes das colunas
            colunas = [desc[0] for desc in cursor.description]
            
            # Converter para lista de dicionários
            dados = []
            for linha in resultados:
                registro = dict(zip(colunas, linha))
                dados.append(registro)
            
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


def inserir_dados(tabela, dados_form_in, database_path=None, database_name=None):
    """
    Insere dados em uma tabela (stateless)
    
    @param {str} tabela - Nome da tabela
    @param {dict} dados_form_in - Dados do formulário
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
        
        # Obter campos da tabela
        campos_tabela = _obter_campos_tabela(tabela, database_file)
        if not campos_tabela:
            return {"erro": f"Não foi possível obter campos da tabela {tabela}"}
        
        # Extrair apenas campos que existem na tabela
        dados_insert = {k: v for k, v in dados_form_in.items() if k in campos_tabela}
        
        if not dados_insert:
            return {"erro": "Nenhum campo válido encontrado para inserção"}
        
        # Montar SQL de inserção
        campos = list(dados_insert.keys())
        valores = list(dados_insert.values())
        placeholders = ", ".join(["?" for _ in campos])
        campos_str = ", ".join(campos)
        
        sql = f"INSERT INTO {tabela} ({campos_str}) VALUES ({placeholders})"
        
        with sqlite3.connect(database_file) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, valores)
            conn.commit()
            
            return {
                "sucesso": True,
                "id_inserido": cursor.lastrowid,
                "registros_afetados": cursor.rowcount
            }
            
    except Exception as e:
        return {"erro": str(e)}


def atualizar_dados(tabela, dados_form_in, database_path=None, database_name=None):
    """
    Atualiza dados em uma tabela (stateless)
    
    @param {str} tabela - Nome da tabela
    @param {dict} dados_form_in - Dados do formulário (deve conter PK)
    @param {str} database_path - Caminho do banco (opcional)
    @param {str} database_name - Nome do banco (opcional)
    @return {dict} - Resultado da operação
    """
    try:
        # Validação do banco de dados
        if not validar_bd(database_path, database_name):
            return {
                "erro": f"Banco de dados inválido: {os.path.join(database_path, database_name)}",
                "sucesso": False
            }
        
        # Validação da tabela alvo
        if not valida_view_or_tab(tabela, database_path, database_name):
            return {
                "erro": f"Tabela '{tabela}' não encontrada no banco de dados",
                "sucesso": False
            }

        # Validação dos campos (usando os campos dos dados como referência)
        campos_dados = list(dados_form_in.keys())
        if not valida_campos(campos_dados, tabela, database_path, database_name):
            return {
                "erro": f"Campos inválidos para a tabela '{tabela}'",
                "sucesso": False
            }
        
        database_file = os.path.join(database_path, database_name)
        
        # Descobrir PK da tabela
        pk_field = _descobrir_pk(tabela, database_file)
        if not pk_field:
            return {"erro": f"Não foi possível identificar chave primária da tabela {tabela}"}
        
        if pk_field not in dados_form_in:
            return {"erro": f"Chave primária '{pk_field}' não encontrada nos dados"}
        
        # Obter campos da tabela
        campos_tabela = _obter_campos_tabela(tabela, database_file)
        if not campos_tabela:
            return {"erro": f"Não foi possível obter campos da tabela {tabela}"}
        
        # Extrair dados para update (excluindo PK)
        dados_update = {k: v for k, v in dados_form_in.items() 
                       if k in campos_tabela and k != pk_field}
        
        if not dados_update:
            return {"erro": "Nenhum campo válido encontrado para atualização"}
        
        # Montar SQL de update
        set_clause = ", ".join([f"{campo} = ?" for campo in dados_update.keys()])
        valores = list(dados_update.values())
        valores.append(dados_form_in[pk_field])  # Adiciona valor da PK no final
        
        sql = f"UPDATE {tabela} SET {set_clause} WHERE {pk_field} = ?"
        
        with sqlite3.connect(database_file) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, valores)
            conn.commit()
            
            return {
                "sucesso": True,
                "registros_afetados": cursor.rowcount
            }
            
    except Exception as e:
        return {"erro": str(e)}


def excluir_dados(tabela, dados_form_in, database_path=None, database_name=None):
    """
    Exclui dados de uma tabela (stateless)
    
    @param {str} tabela - Nome da tabela
    @param {dict} dados_form_in - Dados do formulário (deve conter PK)
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
        
        # Descobrir PK da tabela
        pk_field = _descobrir_pk(tabela, database_file)
        if not pk_field:
            return {"erro": f"Não foi possível identificar chave primária da tabela {tabela}"}
        
        if pk_field not in dados_form_in:
            return {"erro": f"Chave primária '{pk_field}' não encontrada nos dados"}
        
        sql = f"DELETE FROM {tabela} WHERE {pk_field} = ?"
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
