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

import os
import sys
from typing import Dict, List, Any, Optional
import psycopg2
from db_config import get_connection_string

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
                where_clauses.append(f"{campo} = %s")  # PostgreSQL usa %s
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
        
        conn = psycopg2.connect(get_connection_string())
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
        acumulado_percentual = 0.0
        acumulado_valor = 0.0
        ordem = 1
        
        for row in rows:
            valor_total = float(row['valor_total'])
            quantidade = int(row['quantidade'])
            descricao = row['descricao']
            
            # Percentual do item
            percentual = (valor_total / total_geral) * 100.0 if total_geral > 0 else 0.0
            
            # Acumulados
            acumulado_percentual += percentual
            acumulado_valor += valor_total
            
            # Classificação ABC
            if acumulado_percentual <= limite_a:
                classe = 'A'
            elif acumulado_percentual <= limite_b:
                classe = 'B'
            else:
                classe = 'C'
            
            # Adicionar item processado
            dados.append({
                "descricao": descricao,
                "valor_total": round(valor_total, 2),
                "quantidade": quantidade,
                "percentual": round(percentual, 2),
                "percentual_acumulado": round(acumulado_percentual, 2),
                "valor_acumulado": round(acumulado_valor, 2),
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
        
    except psycopg2.Error as e:
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
                sql += f" AND {campo} = %s"  # PostgreSQL usa %s
                valores_where.append(valor)
        
        # GROUP BY
        sql += f"""
            GROUP BY {campo_descricao}, {campo_ano}, {campo_mes}
            ORDER BY {campo_descricao}, {campo_ano}, {campo_mes}
        """
        
        # =================================================================
        # EXECUTAR CONSULTA
        # =================================================================
        
        conn = psycopg2.connect(get_connection_string())
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
    except psycopg2.Error as e:
        return {"sucesso": False, "erro": f"Erro no banco de dados: {str(e)}"}
    except Exception as e:
        return {"sucesso": False, "erro": f"Erro ao calcular evolução: {str(e)}"}


# =============================================================================
#                  TABELA PIVOT GENÉRICA
# =============================================================================

def validarDadosTabPivot(
    view_name: str,
    campo_Agrupamento: str,
    campo_Pivot: str,
    campo_valor: str,
    numColunasPivot: int,
    database_path: Optional[str],
    database_name: Optional[str]
) -> tuple[bool, Optional[str]]:
    """
    Valida todos os parâmetros necessários para calcular tabela pivot.
    
    @param view_name: Nome da view/tabela
    @param campo_Agrupamento: Campo de agrupamento (linhas)
    @param campo_Pivot: Campo que gera as colunas pivot
    @param campo_valor: Campo numérico para agregação
    @param numColunasPivot: Número máximo de colunas
    @param database_path: Caminho do banco
    @param database_name: Nome do arquivo do banco
    
    @return: (validacao_ok: bool, mensagem_erro: str ou None)
    """
    
    # Validar parâmetros obrigatórios
    if not view_name:
        return (False, "Parâmetro 'view_name' não fornecido")
    
    if not campo_Agrupamento:
        return (False, "Parâmetro 'campo_Agrupamento' não fornecido")
    
    if not campo_Pivot:
        return (False, "Parâmetro 'campo_Pivot' não fornecido")
    
    if not campo_valor:
        return (False, "Parâmetro 'campo_valor' não fornecido")
    
    # Validar numColunasPivot
    if numColunasPivot <= 0:
        return (False, f"numColunasPivot deve ser maior que 0, recebido: {numColunasPivot}")
    
    # Validação bem-sucedida
    return (True, None)


def calcular_tabela_pivot(
    view_name: str,
    campo_Agrupamento: str,
    campo_Pivot: str,
    campo_valor: str,
    numColunasPivot: int = 12,
    database_path: Optional[str] = None,
    database_name: Optional[str] = None
) -> Dict[str, Any]:
    """
    Calcula tabela pivot genérica com agregação de valores
    
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
    
    @param numColunasPivot: Número máximo de colunas na pivot table (padrão: 12)
                           Define quantas colunas serão exibidas no máximo
                           Ex: 12 = últimos 12 meses, 6 = últimos 6 meses
                           Se houver menos dados que o limite, mostra apenas os existentes
    
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
        resultado = calcular_tabela_pivot(
            ano_referencia=2024,
            view_name='despesas_view',
            campo_descricao='descricao',
            campo_valor='valor'
        )
    
    @example Evolução de despesas do ano corrente (apenas meses completos):
        resultado = calcular_tabela_pivot(
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
        # VALIDAÇÃO DOS PARÂMETROS ANALÍTICOS
        # =================================================================
        
        validacao_ok, erro_msg = validarDadosTabPivot(
            view_name=view_name,
            campo_Agrupamento=campo_Agrupamento,
            campo_Pivot=campo_Pivot,
            campo_valor=campo_valor,
            numColunasPivot=numColunasPivot,
            database_path=database_path,
            database_name=database_name
        )
        
        if not validacao_ok:
            return {"success": False, "erro": erro_msg}
        
        # =================================================================
        # CONEXÃO POSTGRESQL
        # =================================================================
        
        # Backend API já validou configuração - conectar diretamente
        conn = psycopg2.connect(get_connection_string())
        
        # =================================================================
        # ETAPA 1: BUSCAR VALORES DISTINTOS DO CAMPO PIVOT
        # =================================================================
        cursor = conn.cursor()
        
        # Query para obter valores únicos do campo_Pivot (ordenados)
        sql_pivot = f"""
            SELECT DISTINCT {campo_Pivot} 
            FROM {view_name} 
            ORDER BY {campo_Pivot}
        """
        
        cursor.execute(sql_pivot)
        valores_disponiveis = [row[0] for row in cursor.fetchall()]
        
        # Ordenar cronologicamente se formato "MES_ANO" (ex: JAN_2025)
        ordem_meses = ["JAN", "FEV", "MAR", "ABR", "MAI", "JUN", 
                       "JUL", "AGO", "SET", "OUT", "NOV", "DEZ"]
        
        def chave_ordenacao(mes_ano):
            try:
                mes, ano = mes_ano.split('_')
                return (int(ano), ordem_meses.index(mes))
            except (ValueError, IndexError):
                # Se não for formato MES_ANO, mantém valor original para ordenação alfabética
                return (0, mes_ano)
        
        valores_disponiveis.sort(key=chave_ordenacao)
        
        # Determinar número real de colunas (menor entre disponíveis e limite)
        num_real_colunas = min(len(valores_disponiveis), numColunasPivot)
        
        # Pegar apenas os últimos N valores
        nomeCamposPivot = valores_disponiveis[-num_real_colunas:] if num_real_colunas > 0 else []
        
        # Se não houver valores, retornar erro
        if len(nomeCamposPivot) == 0:
            conn.close()
            return {
                "sucesso": False,
                "erro": f"Nenhum valor encontrado no campo '{campo_Pivot}' da view '{view_name}'"
            }
        
        # =================================================================
        # ETAPA 2: BUSCAR GRUPOS ÚNICOS (AGRUPAMENTO)
        # =================================================================
        
        # Query para obter grupos distintos (ordenados)
        sql_grupos = f"""
            SELECT DISTINCT {campo_Agrupamento} 
            FROM {view_name} 
            ORDER BY {campo_Agrupamento}
        """
        
        cursor.execute(sql_grupos)
        arrayGrupos = [row[0] for row in cursor.fetchall()]
        
        # Se não houver grupos, retornar erro
        if len(arrayGrupos) == 0:
            conn.close()
            return {
                "sucesso": False,
                "erro": f"Nenhum grupo encontrado no campo '{campo_Agrupamento}' da view '{view_name}'"
            }
        
        # =================================================================
        # ETAPA 3: CRIAR MATRIZ BIDIMENSIONAL
        # =================================================================
        
        # Calcular dimensões da matriz
        numDeLinhas = len(arrayGrupos) + 2  # +1 cabeçalho, +1 TOTAL GERAL
        numDeColunas = len(nomeCamposPivot) + 1  # +1 coluna TOTAL
        
        # Criar matriz vazia inicializada com zeros
        matriz = [[0 for _ in range(numDeColunas)] for _ in range(numDeLinhas)]
        
        # =================================================================
        # ETAPA 4: PREPARAR CABEÇALHO (LINHA 0)
        # =================================================================
        
        # Primeira célula: nome do campo de agrupamento
        matriz[0][0] = "Agrupamentos"
        
        # Células intermediárias: nomes das colunas pivot
        for i in range(len(nomeCamposPivot)):
            matriz[0][i + 1] = nomeCamposPivot[i]
        
        # Última célula: coluna TOTAL
        matriz[0][numDeColunas - 1] = "TOTAL"
        
        # =================================================================
        # ETAPA 5: PREPARAR COLUNA DE AGRUPAMENTOS
        # =================================================================
        for i in range(len(arrayGrupos)):
            matriz[i + 1][0] = arrayGrupos[i]
        
        matriz[numDeLinhas - 1][0] = "TOTAL GERAL"
        
        # =================================================================
        # ETAPA 6: EXTRAIR E PREENCHER VALORES NA MATRIZ
        # =================================================================
        # Loop externo: percorre cada coluna pivot
        for j in range(len(nomeCamposPivot)):
            valor_pivot_atual = nomeCamposPivot[j]
            total_coluna = 0
            
            # SQL para extrair dados agrupados para esta coluna pivot
            sql_dados = f"""
                SELECT {campo_Agrupamento}, SUM({campo_valor})
                FROM {view_name}
                WHERE {campo_Pivot} = %s
                GROUP BY {campo_Agrupamento}
            """
            
            cursor.execute(sql_dados, (valor_pivot_atual,))
            resultados = cursor.fetchall()
            
            # Loop interno: preenche valores na matriz
            for row in resultados:
                nome_grupo = row[0]
                valor = row[1] or 0
                
                # Localiza a linha correspondente ao grupo
                if nome_grupo in arrayGrupos:
                    indice_linha = arrayGrupos.index(nome_grupo)
                    matriz[indice_linha + 1][j + 1] = valor
                    total_coluna += valor
            
            # Grava o total desta coluna na última linha
            matriz[numDeLinhas - 1][j + 1] = total_coluna
        
        # =================================================================
        # ETAPA 7: CONVERTER MATRIZ EM DICIONÁRIO E RETORNAR
        # =================================================================
        
        # Fechar conexão
        conn.close()
        
        # Preparar estrutura de retorno
        resultado = {
            "success": True,
            "labels": [matriz[i][0] for i in range(1, numDeLinhas)],  # Coluna 0, sem header
            "colunas": nomeCamposPivot,  # Nomes das colunas pivot
            "dados": [matriz[i][1:] for i in range(1, numDeLinhas)]  # Valores, sem coluna 0
        }
        
        return resultado
        
    except psycopg2.Error as e:
        return {"success": False, "erro": f"Erro no banco de dados: {str(e)}"}
    except Exception as e:
        return {"success": False, "erro": f"Erro ao calcular tabela pivot: {str(e)}"}


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
        
        conn = psycopg2.connect(get_connection_string())
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
                    sql += f" AND {campo} = %s"  # PostgreSQL usa %s
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
    except psycopg2.Error as e:
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
#                     PREPARAR DADOS PARA GRÁFICO PIZZA
# =============================================================================

def preparar_dados_grafico_pizza(
    dados_curva_abc: List[Dict[str, Any]],
    campo_label: str = 'descricao',
    campo_valor: str = 'valor_total',
    campo_percentual: str = 'percentual',
    threshold: float = 2.0
) -> Dict[str, Any]:
    """
    Prepara dados da Curva ABC para exibição em gráfico de pizza (Chart.js)
    
    CONCEITO:
    Agrupa itens com percentual individual < threshold em uma fatia "Diversos"
    para evitar poluição visual no gráfico com fatias muito pequenas.
    
    @param dados_curva_abc: Lista de dicionários retornada por calcular_curva_abc()
                           Deve conter os campos especificados em campo_label, 
                           campo_valor e campo_percentual
    
    @param campo_label: Nome do campo que contém o rótulo (padrão: 'descricao')
                       Exemplos: 'descricao', 'grupo', 'instituicao'
    
    @param campo_valor: Nome do campo que contém o valor numérico (padrão: 'valor_total')
    
    @param campo_percentual: Nome do campo que contém o percentual (padrão: 'percentual')
    
    @param threshold: Percentual mínimo para fatia individual (padrão: 2.0%)
                     Fatias < threshold serão agrupadas em "Diversos"
    
    @return: Dicionário estruturado para Chart.js:
        {
            "sucesso": True/False,
            "labels": ["Moradia", "Saúde", "Transporte", "Diversos"],
            "valores": [4500.50, 2300.00, 1200.00, 350.25],
            "percentuais": [45.2, 23.1, 12.0, 3.5],
            "cores": ["#FF6384", "#36A2EB", "#FFCE56", "#CCCCCC"],
            "resumo": {
                "total_fatias": 4,
                "fatias_individuais": 3,
                "fatias_agrupadas_em_diversos": 5,
                "valor_diversos": 350.25,
                "percentual_diversos": 3.5
            }
        }
    
    @example Preparar gráfico de despesas por grupo com threshold 2%:
        curva = calcular_curva_abc(
            view_name='despesas_view',
            campo_descricao='grupo',
            campo_valor='valor',
            filtros={'ano': '2025', 'mes': 'MAR'}
        )
        
        dados_pizza = preparar_dados_grafico_pizza(
            dados_curva_abc=curva['dados'],
            campo_label='descricao',  # curva ABC renomeia para 'descricao'
            threshold=2.0
        )
        
        # Usar em Chart.js:
        chart_config = {
            "type": "pie",
            "data": {
                "labels": dados_pizza['labels'],
                "datasets": [{
                    "data": dados_pizza['valores'],
                    "backgroundColor": dados_pizza['cores']
                }]
            }
        }
    """
    try:
        # =================================================================
        # VALIDAÇÕES
        # =================================================================
        
        if not dados_curva_abc or len(dados_curva_abc) == 0:
            return {
                "sucesso": True,
                "labels": [],
                "valores": [],
                "percentuais": [],
                "cores": [],
                "resumo": {
                    "total_fatias": 0,
                    "fatias_individuais": 0,
                    "fatias_agrupadas_em_diversos": 0,
                    "valor_diversos": 0.0,
                    "percentual_diversos": 0.0
                }
            }
        
        if not (0 < threshold <= 100):
            return {"sucesso": False, "erro": "Threshold deve estar entre 0 e 100"}
        
        # Validar se campos existem no primeiro item
        primeiro_item = dados_curva_abc[0]
        if campo_label not in primeiro_item:
            return {"sucesso": False, "erro": f"Campo '{campo_label}' não encontrado nos dados"}
        if campo_valor not in primeiro_item:
            return {"sucesso": False, "erro": f"Campo '{campo_valor}' não encontrado nos dados"}
        if campo_percentual not in primeiro_item:
            return {"sucesso": False, "erro": f"Campo '{campo_percentual}' não encontrado nos dados"}
        
        # =================================================================
        # SEPARAR FATIAS INDIVIDUAIS E DIVERSOS
        # =================================================================
        
        fatias_individuais = []
        fatias_diversos = []
        
        for item in dados_curva_abc:
            percentual = float(item[campo_percentual])
            
            if percentual >= threshold:
                fatias_individuais.append(item)
            else:
                fatias_diversos.append(item)
        
        # =================================================================
        # MONTAR ARRAYS PARA GRÁFICO
        # =================================================================
        
        labels = []
        valores = []
        percentuais = []
        
        # Adicionar fatias individuais
        for item in fatias_individuais:
            labels.append(str(item[campo_label]))
            valores.append(round(float(item[campo_valor]), 2))
            percentuais.append(round(float(item[campo_percentual]), 2))
        
        # Adicionar "Diversos" se houver fatias pequenas
        if fatias_diversos:
            valor_diversos = sum(float(item[campo_valor]) for item in fatias_diversos)
            percentual_diversos = sum(float(item[campo_percentual]) for item in fatias_diversos)
            
            labels.append("Diversos")
            valores.append(round(valor_diversos, 2))
            percentuais.append(round(percentual_diversos, 2))
        
        # =================================================================
        # GERAR CORES (Paleta padrão Chart.js + cinza para Diversos)
        # =================================================================
        
        cores_padrao = [
            "#FF6384",  # Vermelho rosado
            "#36A2EB",  # Azul
            "#FFCE56",  # Amarelo
            "#4BC0C0",  # Turquesa
            "#9966FF",  # Roxo
            "#FF9F40",  # Laranja
            "#FF6384",  # Repete se necessário
            "#36A2EB",
            "#FFCE56"
        ]
        
        cores = []
        for i in range(len(labels)):
            if i < len(fatias_individuais):
                # Cor normal da paleta
                cores.append(cores_padrao[i % len(cores_padrao)])
            else:
                # Cinza para "Diversos"
                cores.append("#CCCCCC")
        
        # =================================================================
        # MONTAR RESULTADO
        # =================================================================
        
        return {
            "sucesso": True,
            "labels": labels,
            "valores": valores,
            "percentuais": percentuais,
            "cores": cores,
            "resumo": {
                "total_fatias": len(labels),
                "fatias_individuais": len(fatias_individuais),
                "fatias_agrupadas_em_diversos": len(fatias_diversos),
                "valor_diversos": round(sum(float(item[campo_valor]) for item in fatias_diversos), 2) if fatias_diversos else 0.0,
                "percentual_diversos": round(sum(float(item[campo_percentual]) for item in fatias_diversos), 2) if fatias_diversos else 0.0
            }
        }
        
    except Exception as e:
        return {"sucesso": False, "erro": f"Erro ao preparar dados pizza: {str(e)}"}
