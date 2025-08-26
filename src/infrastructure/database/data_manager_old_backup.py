"""
MODELO DE OPERAÇÕES DB_MANAGER
=============================

CONCEITO:
- TABELAS: Operações CRUD (INSERT, UPDATE, DELETE, SELECT simples)
- VIEWs: Consultas complexas com JOINs para exibição/relatórios

PROPRIEDADES:
- tabela: Nome da tabela real para operações CRUD
- consulta: Nome da VIEW para SELECTs complexos (opcional)
- campos: Array com campos necessários (sempre lista)
- dados_form_out: Dicionário de dados que VAI PARA o formulário (template/estrutura)
- dados_form_in: Dicionário de dados que VEM DO formulário (valores preenchidos)

FLUXO DE DADOS:
1. dados_form_out: Estrutura de campos enviada para o frontend criar o formulário
2. dados_form_in: Valores preenchidos pelo usuário que retornam do frontend
3. Classe extrai apenas campos da tabela do dados_form_in para operações CRUD

OPERAÇÕES:
- INSERT: Extrai campos da tabela de dados_form_in (não precisa PK)
- UPDATE: Extrai campos + PK de dados_form_in (classe descobre qual é a PK)
- DELETE: Extrai apenas PK de dados_form_in (classe descobre qual é a PK)
- SELECT: Aplica filtros na tabela/VIEW

FLUXO PK:
1. Classe consulta PRAGMA table_info para descobrir PK da tabela
2. Para UPDATE/DELETE: busca valor da PK em dados_form_in
3. Monta WHERE automaticamente usando PK descoberta

EXEMPLO:
db = db_manager('despesas', ['descricao', 'valor'])
db.dados_form_out = {'descricao': '', 'valor': 0}  # Template para frontend
db.dados_form_in = {'descricao': 'Mercado', 'valor': 100}  # Dados do frontend
db.insert()  # Extrai campos da tabela de dados_form_in
"""

import sqlite3
import os

# Configuração padrão do banco - pode ser sobrescrita na instanciação
DB_NAME = "financas.db"

class db_manager:
    """
    Gerenciador genérico de banco de dados
    
    @param {string} tabela_principal - Nome da tabela
    @param {Array} campos - Array com campos necessários (sempre lista, mesmo com 1 item)
    @param {string} consulta - Nome da VIEW para consultas complexas (opcional)
    """
    def __init__(self, tabela_principal: str, campos: list = None, consulta: str = None, database_path: str = None, database_name: str = None):
        self.tabela = tabela_principal
        self.consulta = consulta
        self.campos = campos or []
        self.dados_form_out = {}  # Dicionário que VAI PARA o formulário
        self.dados_form_in = {}   # Dicionário que VEM DO formulário
        
        # Configuração flexível de banco de dados - Opção 2
        if database_path:
            # Se caminho completo foi fornecido, usa diretamente
            self.database_file = database_path
        elif database_name:
            # Se apenas nome foi fornecido, usa diretório atual
            self.database_file = database_name
        else:
            # Usa configuração padrão do sistema
            self.database_file = DB_NAME
    
    def _descobrir_pk(self):
        """Descobre automaticamente a chave primária da tabela"""
        try:
            with sqlite3.connect(self.database_file) as conn:
                cursor = conn.cursor()
                cursor.execute(f"PRAGMA table_info({self.tabela})")
                for row in cursor.fetchall():
                    if row[5] == 1:  # campo pk = 1
                        return row[1]  # nome do campo
                return 'id'  # fallback padrão
        except:
            return 'id'  # fallback em caso de erro
    
    def get_view(self, nome_view, filtros=None):
        """
        Retorna dados de uma VIEW com filtros automáticos ou manuais
        
        @param {string} nome_view - Nome da VIEW a ser consultada
        @param {dict} filtros - Filtros manuais (opcional, usa dados_form_in se None)
        @return {dict} - Dicionário com dados da VIEW
        """
        try:
            sql = f"SELECT * FROM {nome_view}"
            valores = []
            
            # Usa filtros manuais ou automáticos de dados_form_in
            filtros_usar = filtros if filtros is not None else self.dados_form_in
            
            # Se há filtros, valida e monta WHERE
            if filtros_usar:
                # Obtém colunas da VIEW para validar filtros
                colunas_view = self._obter_colunas_view(nome_view)
                
                condicoes = []
                campos_invalidos = []
                
                for campo, valor in filtros_usar.items():
                    if campo in colunas_view:
                        condicoes.append(f"{campo} = ?")
                        valores.append(valor)
                    else:
                        campos_invalidos.append(campo)
                
                # Informa campos inválidos se houver
                if campos_invalidos:
                    return {"erro": f"Campos não encontrados na VIEW '{nome_view}': {', '.join(campos_invalidos)}"}
                
                # Monta WHERE se há condições válidas
                if condicoes:
                    sql += " WHERE " + " AND ".join(condicoes)
            
            with sqlite3.connect(self.database_file) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute(sql, valores)
                rows = cursor.fetchall()
                return [dict(row) for row in rows]
                
        except Exception as e:
            return {"erro": str(e)}
    
    def _obter_colunas_view(self, nome_view):
        """Obtém lista de colunas de uma VIEW"""
        try:
            with sqlite3.connect(self.database_file) as conn:
                cursor = conn.cursor()
                cursor.execute(f"PRAGMA table_info({nome_view})")
                return [row[1] for row in cursor.fetchall()]
        except:
            return []
    
    def insert_data(self):
        """
        Insere dados na tabela extraindo campos de dados_form_in
        
        @return {dict} - Resultado da operação (sucesso/erro)
        """
        try:
            # Extrai apenas campos da tabela de dados_form_in
            campos_tabela = self._obter_campos_tabela()
            dados_para_insert = {campo: valor for campo, valor in self.dados_form_in.items() 
                               if campo in campos_tabela}
            
            # Remove PK se existir (não é necessária para INSERT)
            pk_field = self._descobrir_pk()
            if pk_field in dados_para_insert:
                del dados_para_insert[pk_field]
            
            # Monta SQL de INSERT
            campos = ', '.join(dados_para_insert.keys())
            placeholders = ', '.join(['?' for _ in dados_para_insert])
            valores = tuple(dados_para_insert.values())
            
            sql = f"INSERT INTO {self.tabela} ({campos}) VALUES ({placeholders})"
            
            with sqlite3.connect(self.database_file) as conn:
                cursor = conn.cursor()
                cursor.execute(sql, valores)
                conn.commit()
                return {"sucesso": True, "id": cursor.lastrowid}
                
        except Exception as e:
            return {"erro": str(e)}
    
    def update_data(self):
        """
        Atualiza dados na tabela extraindo campos de dados_form_in
        Usa PK descoberta automaticamente para WHERE
        
        @return {dict} - Resultado da operação (sucesso/erro)
        """
        try:
            # Descobre PK da tabela
            pk_field = self._descobrir_pk()
            
            # Verifica se PK está nos dados
            if pk_field not in self.dados_form_in:
                return {"erro": f"Campo PK '{pk_field}' não encontrado nos dados"}
            
            pk_valor = self.dados_form_in[pk_field]
            
            # Extrai apenas campos da tabela de dados_form_in (exceto PK)
            campos_tabela = self._obter_campos_tabela()
            dados_para_update = {campo: valor for campo, valor in self.dados_form_in.items() 
                               if campo in campos_tabela and campo != pk_field}
            
            if not dados_para_update:
                return {"erro": "Nenhum campo válido para atualizar"}
            
            # Monta SQL de UPDATE
            set_campos = ', '.join([f"{campo} = ?" for campo in dados_para_update.keys()])
            valores = list(dados_para_update.values()) + [pk_valor]
            
            sql = f"UPDATE {self.tabela} SET {set_campos} WHERE {pk_field} = ?"
            
            with sqlite3.connect(self.database_file) as conn:
                cursor = conn.cursor()
                cursor.execute(sql, valores)
                conn.commit()
                return {"sucesso": True, "linhas_afetadas": cursor.rowcount}
                
        except Exception as e:
            return {"erro": str(e)}
    
    def delete_data(self):
        """
        Deleta dados da tabela usando PK extraída de dados_form_in
        
        @return {dict} - Resultado da operação (sucesso/erro)
        """
        try:
            # Descobre PK da tabela
            pk_field = self._descobrir_pk()
            
            # Verifica se PK está nos dados
            if pk_field not in self.dados_form_in:
                return {"erro": f"Campo PK '{pk_field}' não encontrado nos dados"}
            
            pk_valor = self.dados_form_in[pk_field]
            
            # Monta SQL de DELETE
            sql = f"DELETE FROM {self.tabela} WHERE {pk_field} = ?"
            
            with sqlite3.connect(self.database_file) as conn:
                cursor = conn.cursor()
                cursor.execute(sql, (pk_valor,))
                conn.commit()
                return {"sucesso": True, "linhas_afetadas": cursor.rowcount}
                
        except Exception as e:
            return {"erro": str(e)}
    
    def _obter_campos_tabela(self):
        """Obtém lista de campos da tabela"""
        try:
            with sqlite3.connect(self.database_file) as conn:
                cursor = conn.cursor()
                cursor.execute(f"PRAGMA table_info({self.tabela})")
                return [row[1] for row in cursor.fetchall()]
        except:
            return []

    def consultar_bd(self, view, campos):
        """
        Consulta dados de uma view no banco de dados
        
        Função principal para consultas de dados, substitui get_view()
        Integra validações e retorna dados estruturados ou erro detalhado
        
        @param {str} view - Nome da view a consultar
        @param {list} campos - Lista de campos ou ["Todos"]
        @return {dict} - {dados: [...], erro: str, sucesso: bool}
        """
        try:
            # TODO: Integrar validação completa aqui
            # validador = ValidadorDados()
            # validacao = validador.validar_consulta_completa(...)
            
            # Por enquanto, usar lógica similar ao get_view() existente
            with sqlite3.connect(self.database_file) as conn:
                cursor = conn.cursor()
                
                # Determinar campos da consulta
                if campos == ["Todos"] or not campos:
                    sql = f"SELECT * FROM {view}"
                else:
                    campos_str = ", ".join(campos)
                    sql = f"SELECT {campos_str} FROM {view}"
                
                cursor.execute(sql)
                resultados = cursor.fetchall()
                
                # Obter nomes das colunas
                colunas = [desc[0] for desc in cursor.description]
                
                # Converter para lista de dicionários
                dados = []
                for linha in resultados:
                    registro = dict(zip(colunas, linha))
                    dados.append(registro)
                
                return {
                    "dados": dados,
                    "erro": None,
                    "sucesso": True,
                    "total_registros": len(dados)
                }
                
        except Exception as e:
            return {
                "dados": [],
                "erro": f"Erro na consulta: {str(e)}",
                "sucesso": False,
                "total_registros": 0
            }
