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
    try:
        validacao_bd = validar_bd(database_path, database_name)
        if validacao_bd is True:
            database_caminho = os.path.join(database_path, database_name)
        else:
            # Importar o módulo para acessar a variável global error_message
            from . import validador_dados
            return {
                "dados": [],
                "erro": validador_dados.error_message,
            }
        
               
        # TODO: Integrar validação completa aqui
        # from .validador_dados import validar_consulta_completa
        # validacao = validar_consulta_completa(database_path, database_name, view, campos)
        # if not validacao.get("valido"): return validacao
        # Insere uma linha em branco no log para separar relatórios consecutivos
        
        log_acompanhamento("")
        log_acompanhamento(f"🔍 CONSULTA: view={view}, campos={campos}, filtros={filtros}, database_file={database_caminho}")
        
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
            
            # TESTES DE DIAGNÓSTICO (se for consulta de grupos_view)
            if view == "grupos_view":
                log_acompanhamento(f"🔍 TESTE 1 - EXECUTANDO SQL: SELECT * FROM {view}")
                log_acompanhamento(f"📊 TESTE 1 - REGISTROS OBTIDOS: {len(resultados)} registros")
                log_acompanhamento(f"📋 TESTE 1 - DADOS RETORNADOS: {resultados}")
                
                # TESTE 2: Consulta específica na view (campo único) - MESMA CONEXÃO
                try:
                    log_acompanhamento(f"🔍 TESTE 2 - EXECUTANDO SQL: SELECT idgrupo FROM {view}")
                    cursor.execute(f"SELECT idgrupo FROM {view}")
                    resultado_teste2 = cursor.fetchall()
                    log_acompanhamento(f"📊 TESTE 2 - REGISTROS OBTIDOS: {len(resultado_teste2)} registros")
                    log_acompanhamento(f"📋 TESTE 2 - DADOS RETORNADOS: {resultado_teste2}")
                except Exception as e:
                    log_acompanhamento(f"❌ TESTE 2 - ERRO: {e}")
                
                # TESTE 3: Consulta direta na tabela grupos - MESMA CONEXÃO
                try:
                    log_acompanhamento(f"🔍 TESTE 3 - EXECUTANDO SQL: SELECT * FROM tb_grupos_finctl")
                    cursor.execute("SELECT * FROM tb_grupos_finctl")
                    resultado_teste3 = cursor.fetchall()
                    log_acompanhamento(f"📊 TESTE 3 - REGISTROS OBTIDOS: {len(resultado_teste3)} registros")
                    log_acompanhamento(f"📋 TESTE 3 - DADOS RETORNADOS: {resultado_teste3}")
                except Exception as e:
                    log_acompanhamento(f"❌ TESTE 3 - ERRO: {e}")
                    cursor.execute("SELECT * FROM grupos_view")
                    resultado_teste3 = cursor.fetchall()
                    log_acompanhamento(f"📊 TESTE 3 - REGISTROS OBTIDOS: {len(resultado_teste3)} registros")
                    log_acompanhamento(f"📋 TESTE 3 - DADOS RETORNADOS: {resultado_teste3}")
                except Exception as e:
                    log_acompanhamento(f"❌ TESTE 3 - ERRO: {e}")
            
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
        # Logar erro detalhado no acompanhamento.txt
        log_acompanhamento("❌ ERRO CAPTURADO NA FUNÇÃO consultar_bd:")
        log_acompanhamento(f"   💥 Tipo do erro: {type(e).__name__}")
        log_acompanhamento(f"   📝 Mensagem: {str(e)}")
        log_acompanhamento(f"   🎯 Parâmetros: view={view}, campos={campos}, filtros={filtros}")
        log_acompanhamento(f"   📁 Database: {database_caminho if 'database_caminho' in locals() else 'não definido'}")
        
        # Importar traceback para mostrar linha exata do erro
        import traceback
        log_acompanhamento(f"   🔍 Traceback completo:")
        for linha in traceback.format_exc().splitlines():
            log_acompanhamento(f"      {linha}")
        
        error_catcher("Erro na função consultar_bd", e)
        
        return {
            "dados": [],
            "erro": f"Erro na consulta: {str(e)}",
            "sucesso": False,
            "total_registros": 0
        }


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
        database_file = _construir_caminho_bd(database_path, database_name)
        
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
        database_file = _construir_caminho_bd(database_path, database_name)
        
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
        database_file = _construir_caminho_bd(database_path, database_name)
        
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
        database_file = _construir_caminho_bd(database_path, database_name)
        
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


# COMPATIBILIDADE: Manter referência à função antiga (DEPRECADO)
def get_view(nome_view, filtros=None, database_path=None, database_name=None):
    """
    FUNÇÃO DEPRECADA - Use consultar_bd() em vez desta
    Mantida apenas para compatibilidade com código existente
    """
    return consultar_bd(nome_view, ["Todos"], database_path, database_name, filtros)


# COMPATIBILIDADE: Classe deprecada para compatibilidade com código existente
class db_manager:
    """
    CLASSE DEPRECADA - Use funções stateless em vez desta
    Mantida apenas para compatibilidade com código existente
    """
    def __init__(self, tabela_principal: str, campos: list = None, consulta: str = None, database_path: str = None, database_name: str = None):
        self.tabela = tabela_principal
        self.consulta = consulta
        self.campos = campos or []
        self.dados_form_out = {}
        self.dados_form_in = {}
        self.database_path = database_path
        self.database_name = database_name
    
    def get_view(self, nome_view, filtros=None):
        """DEPRECADO - Use consultar_bd()"""
        log_acompanhamento(f"🔍 DEBUG: db_manager.get_view() chamando consultar_bd() para {nome_view}")
        resultado = consultar_bd(nome_view, ["Todos"], self.database_path, self.database_name, filtros)
        log_acompanhamento(f"📊 DEBUG: consultar_bd() retornou: {resultado}")
        return resultado.get("dados", [])
    
    def insert_data(self):
        """DEPRECADO - Use inserir_dados()"""
        return inserir_dados(self.tabela, self.dados_form_in, self.database_path, self.database_name)
    
    def update_data(self):
        """DEPRECADO - Use atualizar_dados()"""
        return atualizar_dados(self.tabela, self.dados_form_in, self.database_path, self.database_name)
    
    def delete_data(self):
        """DEPRECADO - Use excluir_dados()"""
        return excluir_dados(self.tabela, self.dados_form_in, self.database_path, self.database_name)
