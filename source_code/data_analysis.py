"""
DATA ANALYSIS - FRAMEWORK DSB
==============================

Módulo especializado em análises estatísticas e relatórios analíticos.
Complementa o data_manager.py focando em agregações complexas e métricas.

ARQUITETURA: FUNÇÕES STATELESS (Thread-Safe)
- Todas as funções são independentes e sem estado
- Thread-safe para uso em aplicações web Flask
- Cada função cria/fecha conexão conforme necessário

CONCEITO:
- data_manager.py → Operações CRUD básicas
- data_analysis.py → Análises estatísticas e relatórios

ANÁLISES DISPONÍVEIS:
- Curva ABC (Análise de Pareto)
- Tendências temporais (futuro)
- Comparações entre períodos (futuro)
- Top N itens (futuro)
- Distribuições percentuais (futuro)

RETORNO PADRÃO:
Todas as funções retornam dicionários estruturados com:
- sucesso: bool
- dados: array de resultados
- resumo: totalizadores e métricas
- erro: mensagem (se sucesso=False)
"""

import sqlite3
import os
import sys
from typing import Dict, List, Any, Optional

# Import do debugger no topo
backend_path = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(backend_path)
from debugger import error_catcher


# =============================================================================
#                          CURVA ABC (ANÁLISE DE PARETO)
# =============================================================================

def calcular_curva_abc(
    view_name: str,
    campo_descricao: str,
    campo_valor: str,
    filtros: Optional[Dict[str, Any]] = None,
    database_path: Optional[str] = None,
    database_name: Optional[str] = None,
    limite_a: float = 80.0,
    limite_b: float = 95.0
) -> Dict[str, Any]:
    """
    Calcula Curva ABC (Análise de Pareto) a partir de uma view
    
    CONCEITO:
    Classifica itens em 3 categorias baseadas em importância acumulada:
    - Classe A: Itens mais importantes (até limite_a% do valor total)
    - Classe B: Itens intermediários (entre limite_a% e limite_b%)
    - Classe C: Itens menos relevantes (acima de limite_b%)
    
    Regra 80/20 típica: 20% dos itens representam 80% do valor
    
    @param view_name: Nome da view para análise
                     Ex: 'despesas_view', 'produtos_view', 'clientes_view'
    
    @param campo_descricao: Campo para agrupamento/descrição
                           Ex: 'descricao', 'subgrupo', 'fornecedor', 'cliente'
    
    @param campo_valor: Campo numérico para agregação (SUM)
                       Ex: 'valor', 'preco', 'quantidade', 'faturamento'
    
    @param filtros: Dicionário com filtros opcionais
                   Ex: {'ano': '2024', 'mes': '10', 'instituicao': 'Itau'}
                   Gera: WHERE ano='2024' AND mes='10' AND instituicao='Itau'
                   None = sem filtros
    
    @param database_path: Caminho do banco (opcional, usa config padrão)
    @param database_name: Nome do banco (opcional, usa config padrão)
    
    @param limite_a: Percentual acumulado para Classe A (padrão: 80.0)
    @param limite_b: Percentual acumulado para Classe B (padrão: 95.0)
    
    @return: Dicionário estruturado com:
        {
            "sucesso": True/False,
            "dados": [
                {
                    "descricao": "Aluguel",
                    "valor_total": 80000.00,
                    "quantidade": 12,
                    "percentual": 40.0,
                    "percentual_acumulado": 40.0,
                    "classe": "A",
                    "ordem": 1
                },
                ...
            ],
            "resumo": {
                "total_geral": 200000.00,
                "total_itens": 8,
                "classe_a": {
                    "itens": 3,
                    "valor": 160000.00,
                    "percentual_valor": 80.0,
                    "percentual_itens": 37.5
                },
                "classe_b": {...},
                "classe_c": {...}
            },
            "criterios": {
                "view": "despesas_view",
                "campo_agrupamento": "descricao",
                "campo_valor": "valor",
                "limite_a": 80.0,
                "limite_b": 95.0,
                "filtros_aplicados": {...}
            }
        }
    
    @example Curva ABC de despesas por descrição em 2024:
        resultado = calcular_curva_abc(
            view_name='despesas_view',
            campo_descricao='descricao',
            campo_valor='valor',
            filtros={'ano': '2024'}
        )
        
        # Exibir itens Classe A (mais importantes)
        itens_a = [item for item in resultado['dados'] if item['classe'] == 'A']
        print(f"Classe A tem {len(itens_a)} itens representando {resultado['resumo']['classe_a']['percentual_valor']}%")
    
    @example Curva ABC de subgrupos (categorias):
        resultado = calcular_curva_abc(
            view_name='despesas_view',
            campo_descricao='subgrupo',
            campo_valor='valor',
            filtros={'ano': '2024', 'mes': '10'}
        )
    
    @example Curva ABC de fornecedores:
        resultado = calcular_curva_abc(
            view_name='despesas_view',
            campo_descricao='instituicao',
            campo_valor='valor',
            filtros={},
            limite_a=70.0,  # Classe A mais restritiva
            limite_b=90.0
        )
    """
    try:
        # =================================================================
        # VALIDAÇÕES INICIAIS
        # =================================================================
        
        if not view_name:
            return {"sucesso": False, "erro": "Parâmetro 'view_name' não fornecido"}
        
        if not campo_descricao:
            return {"sucesso": False, "erro": "Parâmetro 'campo_descricao' não fornecido"}
        
        if not campo_valor:
            return {"sucesso": False, "erro": "Parâmetro 'campo_valor' não fornecido"}
        
        if not (0 < limite_a < 100):
            return {"sucesso": False, "erro": "Parâmetro 'limite_a' deve estar entre 0 e 100"}
        
        if not (limite_a < limite_b < 100):
            return {"sucesso": False, "erro": "Parâmetro 'limite_b' deve ser maior que limite_a e menor que 100"}
        
        # Usar configuração padrão se não fornecido
        if not database_path or not database_name:
            try:
                from config import CAMINHO_BD
                database_file = CAMINHO_BD
            except ImportError:
                return {"sucesso": False, "erro": "Configuração de banco de dados não encontrada"}
        else:
            database_file = os.path.join(database_path, database_name)
        
        if not os.path.exists(database_file):
            return {"sucesso": False, "erro": f"Banco de dados não encontrado: {database_file}"}
        
        # =================================================================
        # CONSTRUIR SQL DE AGREGAÇÃO
        # =================================================================
        
        # SQL base: agrupa por campo_descricao e soma campo_valor
        sql = f"""
            SELECT 
                {campo_descricao} AS descricao,
                SUM({campo_valor}) AS valor_total,
                COUNT(*) AS quantidade
            FROM {view_name}
        """
        
        # Adicionar WHERE se houver filtros
        valores_where = []
        if filtros and len(filtros) > 0:
            where_clauses = []
            for campo, valor in filtros.items():
                where_clauses.append(f"{campo} = ?")
                valores_where.append(valor)
            sql += " WHERE " + " AND ".join(where_clauses)
        
        # GROUP BY e ORDER BY
        sql += f"""
            GROUP BY {campo_descricao}
            HAVING SUM({campo_valor}) > 0
            ORDER BY valor_total DESC
        """
        
        # =================================================================
        # EXECUTAR CONSULTA
        # =================================================================
        
        conn = sqlite3.connect(database_file)
        conn.row_factory = sqlite3.Row  # Permite acesso por nome de coluna
        cursor = conn.cursor()
        
        cursor.execute(sql, valores_where)
        rows = cursor.fetchall()
        conn.close()
        
        if not rows or len(rows) == 0:
            return {
                "sucesso": True,
                "dados": [],
                "resumo": {
                    "total_geral": 0.0,
                    "total_itens": 0,
                    "classe_a": {"itens": 0, "valor": 0.0, "percentual_valor": 0.0, "percentual_itens": 0.0},
                    "classe_b": {"itens": 0, "valor": 0.0, "percentual_valor": 0.0, "percentual_itens": 0.0},
                    "classe_c": {"itens": 0, "valor": 0.0, "percentual_valor": 0.0, "percentual_itens": 0.0}
                },
                "criterios": {
                    "view": view_name,
                    "campo_agrupamento": campo_descricao,
                    "campo_valor": campo_valor,
                    "limite_a": limite_a,
                    "limite_b": limite_b,
                    "filtros_aplicados": filtros or {}
                }
            }
        
        # =================================================================
        # CALCULAR PERCENTUAIS E CLASSIFICAR
        # =================================================================
        
        # Calcular total geral
        total_geral = sum(float(row['valor_total']) for row in rows)
        total_itens = len(rows)
        
        # Processar cada item
        dados = []
        acumulado = 0.0
        ordem = 1
        
        for row in rows:
            valor_total = float(row['valor_total'])
            quantidade = int(row['quantidade'])
            descricao = row['descricao']
            
            # Percentual do item
            percentual = (valor_total / total_geral) * 100.0 if total_geral > 0 else 0.0
            
            # Percentual acumulado
            acumulado += percentual
            
            # Classificação ABC
            if acumulado <= limite_a:
                classe = 'A'
            elif acumulado <= limite_b:
                classe = 'B'
            else:
                classe = 'C'
            
            # Adicionar item processado
            dados.append({
                "descricao": descricao,
                "valor_total": round(valor_total, 2),
                "quantidade": quantidade,
                "percentual": round(percentual, 2),
                "percentual_acumulado": round(acumulado, 2),
                "classe": classe,
                "ordem": ordem
            })
            
            ordem += 1
        
        # =================================================================
        # CALCULAR RESUMO POR CLASSE
        # =================================================================
        
        # Separar por classe
        itens_a = [item for item in dados if item['classe'] == 'A']
        itens_b = [item for item in dados if item['classe'] == 'B']
        itens_c = [item for item in dados if item['classe'] == 'C']
        
        # Calcular totais por classe
        def calcular_totais_classe(itens_classe):
            if not itens_classe:
                return {"itens": 0, "valor": 0.0, "percentual_valor": 0.0, "percentual_itens": 0.0}
            
            valor_classe = sum(item['valor_total'] for item in itens_classe)
            qtd_itens_classe = len(itens_classe)
            
            return {
                "itens": qtd_itens_classe,
                "valor": round(valor_classe, 2),
                "percentual_valor": round((valor_classe / total_geral) * 100.0, 2) if total_geral > 0 else 0.0,
                "percentual_itens": round((qtd_itens_classe / total_itens) * 100.0, 2) if total_itens > 0 else 0.0
            }
        
        resumo = {
            "total_geral": round(total_geral, 2),
            "total_itens": total_itens,
            "classe_a": calcular_totais_classe(itens_a),
            "classe_b": calcular_totais_classe(itens_b),
            "classe_c": calcular_totais_classe(itens_c)
        }
        
        # =================================================================
        # MONTAR RESULTADO FINAL
        # =================================================================
        
        return {
            "sucesso": True,
            "dados": dados,
            "resumo": resumo,
            "criterios": {
                "view": view_name,
                "campo_agrupamento": campo_descricao,
                "campo_valor": campo_valor,
                "limite_a": limite_a,
                "limite_b": limite_b,
                "filtros_aplicados": filtros or {}
            }
        }
        
    except sqlite3.Error as e:
        return {"sucesso": False, "erro": f"Erro no banco de dados: {str(e)}"}
    except Exception as e:
        return {"sucesso": False, "erro": f"Erro ao calcular curva ABC: {str(e)}"}


# =============================================================================
#                          FUNÇÕES AUXILIARES
# =============================================================================

# =============================================================================
#                     EVOLUÇÃO 12 ÚLTIMOS MESES (TABELA PIVOTADA)
# =============================================================================

def calcular_evolucao_12_U_meses(
    view_name: str,
    campo_descricao: str,
    campo_valor: str,
    campo_ano: str = 'ano',
    campo_mes: str = 'mes',
    filtros: Optional[Dict[str, Any]] = None,
    database_path: Optional[str] = None,
    database_name: Optional[str] = None
) -> Dict[str, Any]:
    """
    Calcula evolução dos últimos 12 meses em formato de tabela pivotada
    
    CONCEITO:
    Gera uma matriz com descrições nas linhas e meses nas colunas.
    A partir do mês atual, retrocede até 12 meses (ou menos se não houver dados).
    Última linha = TOTAL GERAL de cada coluna
    Última coluna = TOTAL de cada linha
    
    @param view_name: Nome da view para análise
                     Ex: 'despesas_view', 'receitas_view'
    
    @param campo_descricao: Campo para agrupamento nas linhas
                           Ex: 'descricao', 'subgrupo', 'instituicao'
    
    @param campo_valor: Campo numérico para agregação (SUM)
                       Ex: 'valor', 'preco', 'quantidade'
    
    @param campo_ano: Nome do campo que contém o ano (padrão: 'ano')
    @param campo_mes: Nome do campo que contém o mês (padrão: 'mes')
    
    @param filtros: Dicionário com filtros adicionais opcionais
                   Ex: {'instituicao': 'Itau', 'tipo': 'Despesa'}
                   Obs: Não incluir ano/mes nos filtros (são calculados automaticamente)
    
    @param database_path: Caminho do banco (opcional, usa config padrão)
    @param database_name: Nome do banco (opcional, usa config padrão)
    
    @return: Dicionário estruturado com:
        {
            "sucesso": True/False,
            "colunas": ["2024-12", "2025-01", "2025-02", ..., "2025-11", "TOTAL"],
            "linhas": [
                {
                    "descricao": "Aluguel",
                    "2024-12": 1500.00,
                    "2025-01": 1500.00,
                    "2025-02": 1500.00,
                    ...
                    "2025-11": 1500.00,
                    "TOTAL": 18000.00
                },
                ...
                {
                    "descricao": "TOTAL GERAL",
                    "2024-12": 2300.00,
                    "2025-01": 2250.00,
                    ...
                    "TOTAL": 27500.00
                }
            ],
            "resumo": {
                "periodo_inicio": "2024-12",
                "periodo_fim": "2025-11",
                "meses_com_dados": 12,
                "total_descricoes": 5,
                "total_geral": 27500.00
            },
            "criterios": {
                "view": "despesas_view",
                "campo_agrupamento": "descricao",
                "campo_valor": "valor",
                "filtros_aplicados": {...}
            }
        }
    
    @example Evolução de despesas por descrição nos últimos 12 meses:
        resultado = calcular_evolucao_12_U_meses(
            view_name='despesas_view',
            campo_descricao='descricao',
            campo_valor='valor'
        )
        
        # Exibir matriz
        print("Colunas:", resultado['colunas'])
        for linha in resultado['linhas']:
            print(linha['descricao'], linha['TOTAL'])
    
    @example Evolução por subgrupo com filtro de instituição:
        resultado = calcular_evolucao_12_U_meses(
            view_name='despesas_view',
            campo_descricao='subgrupo',
            campo_valor='valor',
            filtros={'instituicao': 'Itau'}
        )
    """
    try:
        from datetime import datetime, timedelta
        from dateutil.relativedelta import relativedelta
        
        # =================================================================
        # VALIDAÇÕES INICIAIS
        # =================================================================
        
        if not view_name:
            return {"sucesso": False, "erro": "Parâmetro 'view_name' não fornecido"}
        
        if not campo_descricao:
            return {"sucesso": False, "erro": "Parâmetro 'campo_descricao' não fornecido"}
        
        if not campo_valor:
            return {"sucesso": False, "erro": "Parâmetro 'campo_valor' não fornecido"}
        
        # Usar configuração padrão se não fornecido
        if not database_path or not database_name:
            try:
                from config import CAMINHO_BD
                database_file = CAMINHO_BD
            except ImportError:
                return {"sucesso": False, "erro": "Configuração de banco de dados não encontrada"}
        else:
            database_file = os.path.join(database_path, database_name)
        
        if not os.path.exists(database_file):
            return {"sucesso": False, "erro": f"Banco de dados não encontrado: {database_file}"}
        
        # =================================================================
        # CALCULAR ÚLTIMOS 12 MESES
        # =================================================================
        
        # Mês atual
        data_atual = datetime.now()
        ano_atual = data_atual.year
        mes_atual = data_atual.month
        
        # Gerar lista dos últimos 12 meses (do mais antigo ao mais recente)
        meses_range = []
        for i in range(11, -1, -1):  # 11, 10, 9, ..., 1, 0
            data_mes = data_atual - relativedelta(months=i)
            ano = data_mes.year
            mes = data_mes.month
            coluna = f"{ano}-{mes:02d}"
            meses_range.append({
                'ano': ano,
                'mes': mes,
                'coluna': coluna
            })
        
        # =================================================================
        # CONSTRUIR SQL DE AGREGAÇÃO
        # =================================================================
        
        # SQL: agrupa por descricao, ano, mes e soma valor
        sql = f"""
            SELECT 
                {campo_descricao} AS descricao,
                {campo_ano} AS ano,
                {campo_mes} AS mes,
                SUM({campo_valor}) AS valor_total
            FROM {view_name}
            WHERE 1=1
        """
        
        # Adicionar filtro dos últimos 12 meses
        # Gerar condições (ano, mes) IN (...)
        mes_condicoes = []
        for m in meses_range:
            mes_condicoes.append(f"({campo_ano}={m['ano']} AND {campo_mes}={m['mes']})")
        
        sql += " AND (" + " OR ".join(mes_condicoes) + ")"
        
        # Adicionar filtros adicionais
        valores_where = []
        if filtros and len(filtros) > 0:
            for campo, valor in filtros.items():
                sql += f" AND {campo} = ?"
                valores_where.append(valor)
        
        # GROUP BY
        sql += f"""
            GROUP BY {campo_descricao}, {campo_ano}, {campo_mes}
            ORDER BY {campo_descricao}, {campo_ano}, {campo_mes}
        """
        
        # =================================================================
        # EXECUTAR CONSULTA
        # =================================================================
        
        conn = sqlite3.connect(database_file)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute(sql, valores_where)
        rows = cursor.fetchall()
        conn.close()
        
        # =================================================================
        # PIVOTAR DADOS (Transformar linhas em colunas)
        # =================================================================
        
        # Estrutura: {descricao: {coluna: valor}}
        pivot_dict = {}
        colunas_com_dados = set()
        
        for row in rows:
            descricao = row['descricao']
            ano = int(row['ano'])
            mes = int(row['mes'])
            valor = float(row['valor_total'])
            
            coluna = f"{ano}-{mes:02d}"
            colunas_com_dados.add(coluna)
            
            if descricao not in pivot_dict:
                pivot_dict[descricao] = {}
            
            pivot_dict[descricao][coluna] = valor
        
        # Se não há dados, retornar vazio
        if not pivot_dict:
            colunas_finais = [m['coluna'] for m in meses_range] + ["TOTAL"]
            return {
                "sucesso": True,
                "colunas": colunas_finais,
                "linhas": [],
                "resumo": {
                    "periodo_inicio": meses_range[0]['coluna'] if meses_range else None,
                    "periodo_fim": meses_range[-1]['coluna'] if meses_range else None,
                    "meses_com_dados": 0,
                    "total_descricoes": 0,
                    "total_geral": 0.0
                },
                "criterios": {
                    "view": view_name,
                    "campo_agrupamento": campo_descricao,
                    "campo_valor": campo_valor,
                    "filtros_aplicados": filtros or {}
                }
            }
        
        # =================================================================
        # FILTRAR APENAS COLUNAS COM DADOS
        # =================================================================
        
        # Pegar apenas meses que têm dados (mantendo ordem cronológica)
        colunas_ordenadas = [m['coluna'] for m in meses_range if m['coluna'] in colunas_com_dados]
        
        # =================================================================
        # CONSTRUIR LINHAS COM TOTAIS
        # =================================================================
        
        linhas_finais = []
        totais_colunas = {col: 0.0 for col in colunas_ordenadas}
        totais_colunas['TOTAL'] = 0.0
        
        # Ordenar descrições alfabeticamente
        descricoes_ordenadas = sorted(pivot_dict.keys())
        
        for descricao in descricoes_ordenadas:
            linha = {"descricao": descricao}
            total_linha = 0.0
            
            # Preencher cada coluna
            for coluna in colunas_ordenadas:
                valor = pivot_dict[descricao].get(coluna, 0.0)
                linha[coluna] = round(valor, 2)
                total_linha += valor
                totais_colunas[coluna] += valor
            
            # Adicionar total da linha
            linha['TOTAL'] = round(total_linha, 2)
            totais_colunas['TOTAL'] += total_linha
            
            linhas_finais.append(linha)
        
        # =================================================================
        # ADICIONAR LINHA TOTAL GERAL
        # =================================================================
        
        linha_total = {"descricao": "TOTAL GERAL"}
        for coluna in colunas_ordenadas:
            linha_total[coluna] = round(totais_colunas[coluna], 2)
        linha_total['TOTAL'] = round(totais_colunas['TOTAL'], 2)
        
        linhas_finais.append(linha_total)
        
        # =================================================================
        # MONTAR RESULTADO FINAL
        # =================================================================
        
        colunas_finais = colunas_ordenadas + ["TOTAL"]
        
        return {
            "sucesso": True,
            "colunas": colunas_finais,
            "linhas": linhas_finais,
            "resumo": {
                "periodo_inicio": colunas_ordenadas[0] if colunas_ordenadas else None,
                "periodo_fim": colunas_ordenadas[-1] if colunas_ordenadas else None,
                "meses_com_dados": len(colunas_ordenadas),
                "total_descricoes": len(descricoes_ordenadas),
                "total_geral": round(totais_colunas['TOTAL'], 2)
            },
            "criterios": {
                "view": view_name,
                "campo_agrupamento": campo_descricao,
                "campo_valor": campo_valor,
                "filtros_aplicados": filtros or {}
            }
        }
        
    except ImportError:
        return {"sucesso": False, "erro": "Biblioteca 'python-dateutil' não encontrada. Execute: pip install python-dateutil"}
    except sqlite3.Error as e:
        return {"sucesso": False, "erro": f"Erro no banco de dados: {str(e)}"}
    except Exception as e:
        return {"sucesso": False, "erro": f"Erro ao calcular evolução: {str(e)}"}


# =============================================================================
#                  EVOLUÇÃO MENSAL DE UM ANO ESPECÍFICO
# =============================================================================

def calcular_evolucao_mensal_ano(
    ano_referencia: int,
    view_name: str,
    campo_descricao: str,
    campo_valor: str,
    campo_ano: str = 'ano',
    campo_mes: str = 'mes',
    filtros: Optional[Dict[str, Any]] = None,
    database_path: Optional[str] = None,
    database_name: Optional[str] = None
) -> Dict[str, Any]:
    """
    Calcula evolução mensal de um ano específico em formato de tabela pivotada
    
    CONCEITO:
    Gera uma matriz com descrições nas linhas e meses nas colunas para um ano.
    
    REGRAS DE EXIBIÇÃO:
    - ANO CORRENTE: Mostra apenas meses completos (que já passaram)
      Ex: Se estamos em Março/2025 → mostra JAN e FEV (março ainda em curso)
      Ex: Se estamos em Janeiro/2025 → não mostra nada (janeiro em curso)
    
    - ANOS ANTERIORES: Mostra todos os meses que têm dados
      Ex: 2024 com dados em 12 meses → mostra 12 colunas
      Ex: 2024 com dados em 5 meses → mostra 5 colunas
    
    Última linha = TOTAL GERAL de cada coluna
    Última coluna = TOTAL de cada linha
    
    @param ano_referencia: Ano para análise (Ex: 2024, 2025)
    
    @param view_name: Nome da view para análise
                     Ex: 'despesas_view', 'receitas_view'
    
    @param campo_descricao: Campo para agrupamento nas linhas
                           Ex: 'descricao', 'subgrupo', 'instituicao'
    
    @param campo_valor: Campo numérico para agregação (SUM)
                       Ex: 'valor', 'preco', 'quantidade'
    
    @param campo_ano: Nome do campo que contém o ano (padrão: 'ano')
    @param campo_mes: Nome do campo que contém o mês (padrão: 'mes')
    
    @param filtros: Dicionário com filtros adicionais opcionais
                   Ex: {'instituicao': 'Itau', 'tipo': 'Despesa'}
                   Obs: Não incluir ano nos filtros (é usado ano_referencia)
    
    @param database_path: Caminho do banco (opcional, usa config padrão)
    @param database_name: Nome do banco (opcional, usa config padrão)
    
    @return: Dicionário estruturado com:
        {
            "sucesso": True/False,
            "colunas": ["JAN", "FEV", "MAR", ..., "DEZ", "TOTAL"],
            "linhas": [
                {
                    "descricao": "Aluguel",
                    "JAN": 1500.00,
                    "FEV": 1500.00,
                    "MAR": 1500.00,
                    ...
                    "TOTAL": 18000.00
                },
                ...
                {
                    "descricao": "TOTAL GERAL",
                    "JAN": 2300.00,
                    "FEV": 2250.00,
                    ...
                    "TOTAL": 27500.00
                }
            ],
            "resumo": {
                "ano": 2024,
                "meses_com_dados": 12,
                "total_descricoes": 5,
                "total_geral": 27500.00,
                "ano_corrente": False
            },
            "criterios": {
                "view": "despesas_view",
                "campo_agrupamento": "descricao",
                "campo_valor": "valor",
                "filtros_aplicados": {...}
            }
        }
    
    @example Evolução de despesas por descrição em 2024 (ano completo):
        resultado = calcular_evolucao_mensal_ano(
            ano_referencia=2024,
            view_name='despesas_view',
            campo_descricao='descricao',
            campo_valor='valor'
        )
    
    @example Evolução de despesas do ano corrente (apenas meses completos):
        resultado = calcular_evolucao_mensal_ano(
            ano_referencia=2025,
            view_name='despesas_view',
            campo_descricao='subgrupo',
            campo_valor='valor',
            filtros={'instituicao': 'Itau'}
        )
    """
    try:
        from datetime import datetime
        
        # =================================================================
        # VALIDAÇÕES INICIAIS
        # =================================================================
        
        if not ano_referencia:
            return {"sucesso": False, "erro": "Parâmetro 'ano_referencia' não fornecido"}
        
        if not view_name:
            return {"sucesso": False, "erro": "Parâmetro 'view_name' não fornecido"}
        
        if not campo_descricao:
            return {"sucesso": False, "erro": "Parâmetro 'campo_descricao' não fornecido"}
        
        if not campo_valor:
            return {"sucesso": False, "erro": "Parâmetro 'campo_valor' não fornecido"}
        
        # Validar ano
        if ano_referencia < 1900 or ano_referencia > 2100:
            return {"sucesso": False, "erro": f"Ano '{ano_referencia}' inválido"}
        
        # Usar configuração padrão se não fornecido
        if not database_path or not database_name:
            try:
                from config import CAMINHO_BD
                database_file = CAMINHO_BD
            except ImportError:
                return {"sucesso": False, "erro": "Configuração de banco de dados não encontrada"}
        else:
            database_file = os.path.join(database_path, database_name)
        
        if not os.path.exists(database_file):
            return {"sucesso": False, "erro": f"Banco de dados não encontrado: {database_file}"}
        
        # =================================================================
        # DETERMINAR MESES VÁLIDOS
        # =================================================================
        
        data_atual = datetime.now()
        ano_atual = data_atual.year
        mes_atual = data_atual.month
        
        is_ano_corrente = (ano_referencia == ano_atual)
        
        # Nomes dos meses
        nomes_meses = {
            1: "JAN", 2: "FEV", 3: "MAR", 4: "ABR", 5: "MAI", 6: "JUN",
            7: "JUL", 8: "AGO", 9: "SET", 10: "OUT", 11: "NOV", 12: "DEZ"
        }
        
        # Determinar range de meses
        if is_ano_corrente:
            # Ano corrente: apenas meses completos (anteriores ao mês atual)
            meses_validos = list(range(1, mes_atual))  # [1, 2, ..., mes_atual-1]
            
            # Se estamos em janeiro, não há meses completos
            if mes_atual == 1:
                return {
                    "sucesso": True,
                    "colunas": ["TOTAL"],
                    "linhas": [],
                    "resumo": {
                        "ano": ano_referencia,
                        "meses_com_dados": 0,
                        "total_descricoes": 0,
                        "total_geral": 0.0,
                        "ano_corrente": True,
                        "observacao": "Nenhum mês completo disponível no ano corrente"
                    },
                    "criterios": {
                        "view": view_name,
                        "campo_agrupamento": campo_descricao,
                        "campo_valor": campo_valor,
                        "filtros_aplicados": filtros or {}
                    }
                }
        else:
            # Ano anterior: todos os 12 meses (filtraremos depois pelos que têm dados)
            meses_validos = list(range(1, 13))  # [1, 2, 3, ..., 12]
        
        # =================================================================
        # CONSTRUIR SQL DE AGREGAÇÃO
        # =================================================================
        
        # SQL: agrupa por descricao e mes, soma valor
        sql = f"""
            SELECT 
                {campo_descricao} AS descricao,
                {campo_mes} AS mes,
                SUM({campo_valor}) AS valor_total
            FROM {view_name}
            WHERE {campo_ano} = ?
        """
        
        valores_where = [ano_referencia]
        
        # Adicionar filtro de meses válidos
        if meses_validos:
            placeholders = ','.join(['?'] * len(meses_validos))
            sql += f" AND {campo_mes} IN ({placeholders})"
            valores_where.extend(meses_validos)
        
        # Adicionar filtros adicionais
        if filtros and len(filtros) > 0:
            for campo, valor in filtros.items():
                sql += f" AND {campo} = ?"
                valores_where.append(valor)
        
        # GROUP BY
        sql += f"""
            GROUP BY {campo_descricao}, {campo_mes}
            ORDER BY {campo_descricao}, {campo_mes}
        """
        
        # =================================================================
        # EXECUTAR CONSULTA
        # =================================================================
        
        conn = sqlite3.connect(database_file)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute(sql, valores_where)
        rows = cursor.fetchall()
        conn.close()
        
        # =================================================================
        # PIVOTAR DADOS (Transformar linhas em colunas)
        # =================================================================
        
        # Estrutura: {descricao: {mes: valor}}
        pivot_dict = {}
        meses_com_dados = set()
        
        for row in rows:
            descricao = row['descricao']
            mes = int(row['mes'])
            valor = float(row['valor_total'])
            
            meses_com_dados.add(mes)
            
            if descricao not in pivot_dict:
                pivot_dict[descricao] = {}
            
            pivot_dict[descricao][mes] = valor
        
        # Se não há dados, retornar vazio
        if not pivot_dict:
            colunas_finais = ["TOTAL"]
            return {
                "sucesso": True,
                "colunas": colunas_finais,
                "linhas": [],
                "resumo": {
                    "ano": ano_referencia,
                    "meses_com_dados": 0,
                    "total_descricoes": 0,
                    "total_geral": 0.0,
                    "ano_corrente": is_ano_corrente
                },
                "criterios": {
                    "view": view_name,
                    "campo_agrupamento": campo_descricao,
                    "campo_valor": campo_valor,
                    "filtros_aplicados": filtros or {}
                }
            }
        
        # =================================================================
        # FILTRAR APENAS MESES COM DADOS (mantendo ordem cronológica)
        # =================================================================
        
        meses_ordenados = sorted([m for m in meses_com_dados if m in meses_validos])
        colunas_ordenadas = [nomes_meses[m] for m in meses_ordenados]
        
        # =================================================================
        # CONSTRUIR LINHAS COM TOTAIS
        # =================================================================
        
        linhas_finais = []
        totais_colunas = {mes: 0.0 for mes in meses_ordenados}
        totais_colunas['TOTAL'] = 0.0
        
        # Ordenar descrições alfabeticamente
        descricoes_ordenadas = sorted(pivot_dict.keys())
        
        for descricao in descricoes_ordenadas:
            linha = {"descricao": descricao}
            total_linha = 0.0
            
            # Preencher cada coluna (mês)
            for mes in meses_ordenados:
                valor = pivot_dict[descricao].get(mes, 0.0)
                coluna_nome = nomes_meses[mes]
                linha[coluna_nome] = round(valor, 2)
                total_linha += valor
                totais_colunas[mes] += valor
            
            # Adicionar total da linha
            linha['TOTAL'] = round(total_linha, 2)
            totais_colunas['TOTAL'] += total_linha
            
            linhas_finais.append(linha)
        
        # =================================================================
        # ADICIONAR LINHA TOTAL GERAL
        # =================================================================
        
        linha_total = {"descricao": "TOTAL GERAL"}
        for mes in meses_ordenados:
            coluna_nome = nomes_meses[mes]
            linha_total[coluna_nome] = round(totais_colunas[mes], 2)
        linha_total['TOTAL'] = round(totais_colunas['TOTAL'], 2)
        
        linhas_finais.append(linha_total)
        
        # =================================================================
        # MONTAR RESULTADO FINAL
        # =================================================================
        
        colunas_finais = colunas_ordenadas + ["TOTAL"]
        
        return {
            "sucesso": True,
            "colunas": colunas_finais,
            "linhas": linhas_finais,
            "resumo": {
                "ano": ano_referencia,
                "meses_com_dados": len(meses_ordenados),
                "total_descricoes": len(descricoes_ordenadas),
                "total_geral": round(totais_colunas['TOTAL'], 2),
                "ano_corrente": is_ano_corrente
            },
            "criterios": {
                "view": view_name,
                "campo_agrupamento": campo_descricao,
                "campo_valor": campo_valor,
                "filtros_aplicados": filtros or {}
            }
        }
        
    except sqlite3.Error as e:
        return {"sucesso": False, "erro": f"Erro no banco de dados: {str(e)}"}
    except Exception as e:
        return {"sucesso": False, "erro": f"Erro ao calcular evolução mensal: {str(e)}"}


# =============================================================================
#                    TOTAIS POR PERÍODO (PARA GRÁFICOS)
# =============================================================================

def calcular_totais_por_periodo(
    view_name: str,
    campo_valor: str,
    tipo_periodo: str = 'mes',
    quantidade: int = 12,
    campo_ano: str = 'ano',
    campo_mes: str = 'mes',
    filtros: Optional[Dict[str, Any]] = None,
    database_path: Optional[str] = None,
    database_name: Optional[str] = None
) -> Dict[str, Any]:
    """
    Calcula totais agregados por período de tempo para uso em gráficos
    
    CONCEITO:
    Função genérica para gerar séries temporais que podem ser usadas em:
    - Gráficos de Colunas/Barras (valores por período)
    - Gráficos de Pizza (distribuição percentual)
    - Gráficos de Linha (evolução/tendência temporal)
    
    Retorna os últimos N períodos a partir da data atual, retroativamente.
    
    @param view_name: Nome da view para análise
                     Ex: 'despesas_view', 'receitas_view'
    
    @param campo_valor: Campo numérico para agregação (SUM)
                       Ex: 'valor', 'preco', 'quantidade'
    
    @param tipo_periodo: Tipo de agrupamento temporal
                        Valores aceitos:
                        - 'mes': Agrupa por mês (padrão)
                        - 'trimestre': Agrupa por trimestre (Q1, Q2, Q3, Q4)
                        - 'semestre': Agrupa por semestre (S1, S2)
                        - 'ano': Agrupa por ano
    
    @param quantidade: Quantidade de períodos retroativos
                      Ex: 12 (últimos 12 meses/trimestres/etc)
                      Padrão: 12
    
    @param campo_ano: Nome do campo que contém o ano (padrão: 'ano')
    @param campo_mes: Nome do campo que contém o mês (padrão: 'mes')
    
    @param filtros: Dicionário com filtros adicionais opcionais
                   Ex: {'instituicao': 'Itau', 'subgrupo': 'Alimentação'}
    
    @param database_path: Caminho do banco (opcional, usa config padrão)
    @param database_name: Nome do banco (opcional, usa config padrão)
    
    @return: Dicionário estruturado com:
        {
            "sucesso": True/False,
            "tipo_periodo": "mes",
            "dados": [
                {
                    "periodo": "2024-12",
                    "periodo_formatado": "Dez/2024",
                    "valor": 2500.00,
                    "percentual": 8.5
                },
                {
                    "periodo": "2025-01",
                    "periodo_formatado": "Jan/2025",
                    "valor": 2300.00,
                    "percentual": 7.8
                },
                ...
            ],
            "resumo": {
                "total_geral": 29500.00,
                "total_periodos": 12,
                "media_periodo": 2458.33,
                "maior_valor": {
                    "periodo": "2025-03",
                    "periodo_formatado": "Mar/2025",
                    "valor": 3200.00
                },
                "menor_valor": {
                    "periodo": "2024-12",
                    "periodo_formatado": "Dez/2024",
                    "valor": 2100.00
                }
            },
            "criterios": {
                "view": "despesas_view",
                "campo_valor": "valor",
                "tipo_periodo": "mes",
                "quantidade": 12,
                "filtros_aplicados": {...}
            }
        }
    
    @example Gráfico de colunas dos últimos 12 meses:
        resultado = calcular_totais_por_periodo(
            view_name='despesas_view',
            campo_valor='valor',
            tipo_periodo='mes',
            quantidade=12
        )
        # Usar resultado['dados'] para eixo X (periodo) e Y (valor)
    
    @example Gráfico de pizza por trimestre:
        resultado = calcular_totais_por_periodo(
            view_name='despesas_view',
            campo_valor='valor',
            tipo_periodo='trimestre',
            quantidade=4,
            filtros={'ano': '2024'}
        )
        # Usar resultado['dados'] com periodo e percentual
    
    @example Gráfico de linha - evolução anual:
        resultado = calcular_totais_por_periodo(
            view_name='receitas_view',
            campo_valor='valor',
            tipo_periodo='ano',
            quantidade=5
        )
        # Conectar pontos (periodo, valor) para mostrar tendência
    """
    try:
        from datetime import datetime
        from dateutil.relativedelta import relativedelta
        
        # =================================================================
        # VALIDAÇÕES INICIAIS
        # =================================================================
        
        if not view_name:
            return {"sucesso": False, "erro": "Parâmetro 'view_name' não fornecido"}
        
        if not campo_valor:
            return {"sucesso": False, "erro": "Parâmetro 'campo_valor' não fornecido"}
        
        if tipo_periodo not in ['mes', 'trimestre', 'semestre', 'ano']:
            return {"sucesso": False, "erro": f"Tipo de período '{tipo_periodo}' inválido. Use: 'mes', 'trimestre', 'semestre' ou 'ano'"}
        
        if quantidade < 1 or quantidade > 100:
            return {"sucesso": False, "erro": "Parâmetro 'quantidade' deve estar entre 1 e 100"}
        
        # Usar configuração padrão se não fornecido
        if not database_path or not database_name:
            try:
                from config import CAMINHO_BD
                database_file = CAMINHO_BD
            except ImportError:
                return {"sucesso": False, "erro": "Configuração de banco de dados não encontrada"}
        else:
            database_file = os.path.join(database_path, database_name)
        
        if not os.path.exists(database_file):
            return {"sucesso": False, "erro": f"Banco de dados não encontrado: {database_file}"}
        
        # =================================================================
        # CALCULAR PERÍODOS RETROATIVOS
        # =================================================================
        
        data_atual = datetime.now()
        periodos_range = []
        
        if tipo_periodo == 'mes':
            # Últimos N meses
            for i in range(quantidade - 1, -1, -1):
                data_periodo = data_atual - relativedelta(months=i)
                ano = data_periodo.year
                mes = data_periodo.month
                
                periodos_range.append({
                    'ano': ano,
                    'mes': mes,
                    'periodo': f"{ano}-{mes:02d}",
                    'periodo_formatado': f"{_nome_mes_abrev(mes)}/{ano}",
                    'filtro_sql': f"({campo_ano}={ano} AND {campo_mes}={mes})"
                })
        
        elif tipo_periodo == 'trimestre':
            # Últimos N trimestres
            for i in range(quantidade - 1, -1, -1):
                data_periodo = data_atual - relativedelta(months=i*3)
                ano = data_periodo.year
                mes = data_periodo.month
                trimestre = ((mes - 1) // 3) + 1  # 1-3=Q1, 4-6=Q2, 7-9=Q3, 10-12=Q4
                
                # Meses do trimestre
                meses_trimestre = list(range((trimestre-1)*3 + 1, trimestre*3 + 1))
                
                periodos_range.append({
                    'ano': ano,
                    'trimestre': trimestre,
                    'periodo': f"{ano}-Q{trimestre}",
                    'periodo_formatado': f"Q{trimestre}/{ano}",
                    'filtro_sql': f"({campo_ano}={ano} AND {campo_mes} IN ({','.join(map(str, meses_trimestre))}))"
                })
        
        elif tipo_periodo == 'semestre':
            # Últimos N semestres
            for i in range(quantidade - 1, -1, -1):
                data_periodo = data_atual - relativedelta(months=i*6)
                ano = data_periodo.year
                mes = data_periodo.month
                semestre = 1 if mes <= 6 else 2
                
                # Meses do semestre
                meses_semestre = list(range(1, 7)) if semestre == 1 else list(range(7, 13))
                
                periodos_range.append({
                    'ano': ano,
                    'semestre': semestre,
                    'periodo': f"{ano}-S{semestre}",
                    'periodo_formatado': f"S{semestre}/{ano}",
                    'filtro_sql': f"({campo_ano}={ano} AND {campo_mes} IN ({','.join(map(str, meses_semestre))}))"
                })
        
        elif tipo_periodo == 'ano':
            # Últimos N anos
            for i in range(quantidade - 1, -1, -1):
                ano = data_atual.year - i
                
                periodos_range.append({
                    'ano': ano,
                    'periodo': f"{ano}",
                    'periodo_formatado': f"{ano}",
                    'filtro_sql': f"{campo_ano}={ano}"
                })
        
        # =================================================================
        # CONSTRUIR SQL PARA CADA PERÍODO
        # =================================================================
        
        conn = sqlite3.connect(database_file)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        dados_periodos = []
        
        for periodo_info in periodos_range:
            # SQL base
            sql = f"""
                SELECT SUM({campo_valor}) AS valor_total
                FROM {view_name}
                WHERE {periodo_info['filtro_sql']}
            """
            
            # Adicionar filtros adicionais
            valores_where = []
            if filtros and len(filtros) > 0:
                for campo, valor in filtros.items():
                    sql += f" AND {campo} = ?"
                    valores_where.append(valor)
            
            # Executar consulta
            cursor.execute(sql, valores_where)
            row = cursor.fetchone()
            
            valor = float(row['valor_total']) if row['valor_total'] is not None else 0.0
            
            dados_periodos.append({
                'periodo': periodo_info['periodo'],
                'periodo_formatado': periodo_info['periodo_formatado'],
                'valor': valor
            })
        
        conn.close()
        
        # =================================================================
        # CALCULAR PERCENTUAIS E ESTATÍSTICAS
        # =================================================================
        
        total_geral = sum(p['valor'] for p in dados_periodos)
        
        # Adicionar percentuais
        for periodo in dados_periodos:
            periodo['percentual'] = round((periodo['valor'] / total_geral * 100.0), 2) if total_geral > 0 else 0.0
            periodo['valor'] = round(periodo['valor'], 2)
        
        # Filtrar períodos com dados para estatísticas
        periodos_com_dados = [p for p in dados_periodos if p['valor'] > 0]
        
        # Calcular estatísticas
        if periodos_com_dados:
            maior = max(periodos_com_dados, key=lambda x: x['valor'])
            menor = min(periodos_com_dados, key=lambda x: x['valor'])
            media = total_geral / len(dados_periodos) if len(dados_periodos) > 0 else 0.0
            
            resumo = {
                "total_geral": round(total_geral, 2),
                "total_periodos": len(dados_periodos),
                "periodos_com_dados": len(periodos_com_dados),
                "media_periodo": round(media, 2),
                "maior_valor": {
                    "periodo": maior['periodo'],
                    "periodo_formatado": maior['periodo_formatado'],
                    "valor": maior['valor']
                },
                "menor_valor": {
                    "periodo": menor['periodo'],
                    "periodo_formatado": menor['periodo_formatado'],
                    "valor": menor['valor']
                }
            }
        else:
            resumo = {
                "total_geral": 0.0,
                "total_periodos": len(dados_periodos),
                "periodos_com_dados": 0,
                "media_periodo": 0.0,
                "maior_valor": None,
                "menor_valor": None
            }
        
        # =================================================================
        # MONTAR RESULTADO FINAL
        # =================================================================
        
        return {
            "sucesso": True,
            "tipo_periodo": tipo_periodo,
            "dados": dados_periodos,
            "resumo": resumo,
            "criterios": {
                "view": view_name,
                "campo_valor": campo_valor,
                "tipo_periodo": tipo_periodo,
                "quantidade": quantidade,
                "filtros_aplicados": filtros or {}
            }
        }
        
    except ImportError:
        return {"sucesso": False, "erro": "Biblioteca 'python-dateutil' não encontrada. Execute: pip install python-dateutil"}
    except sqlite3.Error as e:
        return {"sucesso": False, "erro": f"Erro no banco de dados: {str(e)}"}
    except Exception as e:
        return {"sucesso": False, "erro": f"Erro ao calcular totais por período: {str(e)}"}


def _nome_mes_abrev(mes: int) -> str:
    """Retorna nome abreviado do mês"""
    meses = {
        1: "Jan", 2: "Fev", 3: "Mar", 4: "Abr", 5: "Mai", 6: "Jun",
        7: "Jul", 8: "Ago", 9: "Set", 10: "Out", 11: "Nov", 12: "Dez"
    }
    return meses.get(mes, str(mes))


# =============================================================================
#                          FUNÇÕES AUXILIARES
# =============================================================================

def validar_view_campos(view_name: str, campos: List[str], database_file: str) -> Dict[str, Any]:
    """
    Valida se uma view existe e se os campos especificados estão presentes
    
    @param view_name: Nome da view
    @param campos: Lista de campos a validar
    @param database_file: Caminho completo do banco
    @return: {"valido": True/False, "erro": "mensagem"}
    """
    try:
        conn = sqlite3.connect(database_file)
        cursor = conn.cursor()
        
        # Verificar se view existe
        cursor.execute("SELECT name FROM sqlite_master WHERE type='view' AND name=?", (view_name,))
        if not cursor.fetchone():
            conn.close()
            return {"valido": False, "erro": f"View '{view_name}' não encontrada"}
        
        # Verificar campos
        cursor.execute(f"PRAGMA table_info({view_name})")
        colunas_disponiveis = [row[1] for row in cursor.fetchall()]
        conn.close()
        
        # Validar cada campo
        campos_invalidos = [campo for campo in campos if campo not in colunas_disponiveis]
        
        if campos_invalidos:
            return {
                "valido": False, 
                "erro": f"Campos inválidos: {', '.join(campos_invalidos)}. Disponíveis: {', '.join(colunas_disponiveis)}"
            }
        
        return {"valido": True}
        
    except Exception as e:
        return {"valido": False, "erro": f"Erro ao validar view: {str(e)}"}
