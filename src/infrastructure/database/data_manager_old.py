# scripts/data_manager.py (Versão com a função salvar_despesas restaurada)

import sqlite3
import logging
from infrastructure.config.config import CAMINHO_BANCO_DE_DADOS as DB_NAME

# Pega o logger de diagnóstico para este módulo
log = logging.getLogger(__name__)

def _executar_sql(sql, parametros=(), fetchone=False, fetchall=False, commit=False):
    """Função auxiliar para executar comandos SQL."""
    try:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, parametros)
            if commit:
                conn.commit()
                return cursor.lastrowid
            if fetchone:
                return cursor.fetchone()
            if fetchall:
                return cursor.fetchall()
    except sqlite3.Error as e:
        log.error(f"Erro no banco de dados: {e}", exc_info=True)
        raise e

def obter_todas_classificacoes():
    """Busca todas as classificações no banco de dados."""
    sql = "SELECT id_classificacao, grupo, subgrupo, descricao_exemplos, dicas_classificacao FROM classificacao ORDER BY grupo, subgrupo"
    registros = _executar_sql(sql, fetchall=True)
    if registros is None: return []
    
    colunas = ['id_classificacao', 'grupo', 'subgrupo', 'descricao_exemplos', 'dicas_classificacao']
    return [dict(zip(colunas, reg)) for reg in registros]

def adicionar_classificacao(grupo, subgrupo, descricao, dicas):
    """Adiciona uma nova classificação, agora com dicas."""
    sql_insert = "INSERT INTO classificacao (grupo, subgrupo, descricao_exemplos, dicas_classificacao) VALUES (?, ?, ?, ?)"
    return _executar_sql(sql_insert, (grupo, subgrupo, descricao, dicas), commit=True)

def alterar_classificacao(id_classificacao, grupo, subgrupo, descricao, dicas):
    """Altera uma classificação existente, incluindo as dicas."""
    sql = "UPDATE classificacao SET grupo = ?, subgrupo = ?, descricao_exemplos = ?, dicas_classificacao = ? WHERE id_classificacao = ?"
    _executar_sql(sql, (grupo, subgrupo, descricao, dicas, id_classificacao), commit=True)
    return True

def excluir_classificacao(id_classificacao):
    """Exclui uma classificação pelo seu ID."""
    sql = "DELETE FROM classificacao WHERE id_classificacao = ?"
    _executar_sql(sql, (id_classificacao,), commit=True)
    return True

def checar_uso_classificacao(id_classificacao):
    """Verifica se uma classificação está em uso na tabela de despesas."""
    sql = "SELECT COUNT(*) FROM despesas WHERE id_classificacao = ?"
    resultado = _executar_sql(sql, (id_classificacao,), fetchone=True)
    return resultado[0] if resultado else 0

# ====================================================================
# SUA FUNÇÃO ORIGINAL, RESTAURADA E INTEGRADA
# ====================================================================
def salvar_despesas(lista_despesas_classificadas: list):
    """
    Salva uma lista de despesas (já validadas e classificadas pelo orquestrador) 
    no banco de dados.
    """
    if not lista_despesas_classificadas:
        log.info("Nenhuma despesa para salvar.")
        return

    # A sua lógica de pegar a data do primeiro item para o log é boa.
    data_extrato_atual_str = lista_despesas_classificadas[0].get('data_extrato', 'PERIODO_DESCONHECIDO')
    
    # O seu código já usava a variável do config, mas a função _executar_sql já faz isso,
    # então podemos simplificar para usar a mesma estrutura das outras funções.
    
    # Prepara os dados para inserção a partir da lista de dicionários
    dados_para_inserir = [
        (
            d.get('id_classificacao'),
            d.get('data_extrato'),
            d.get('instituicao'),
            d.get('descricao'),
            d.get('valor')
        ) for d in lista_despesas_classificadas
    ]

    comando_insert = """
        INSERT INTO despesas 
        (id_classificacao, data_extrato, instituicao, descricao, valor) 
        VALUES (?, ?, ?, ?, ?);
    """
    
    # Reutilizando a função _executar_sql para consistência
    try:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.executemany(comando_insert, dados_para_inserir)
            conn.commit()
            log.info(f"{cursor.rowcount} despesas de '{data_extrato_atual_str}' foram salvas com sucesso.")
    except sqlite3.Error as e:
        log.error(f"Erro ao salvar dados no banco de dados para o período '{data_extrato_atual_str}'.", exc_info=True)
        raise e
    
# ========================================================
# CÓDIGO NOVO PARA ADICIONAR AO FINAL DO SEU ARQUIVO
# ========================================================

def obter_despesas_para_reclassificar() -> list:
    """
    Busca todas as despesas existentes, retornando apenas os campos
    necessários para a reclassificação (ID e descrição).
    """
    log.info("[DATA_MANAGER] Buscando todas as despesas existentes para reclassificação.")
    sql = "SELECT id_despesa, descricao FROM despesas"
    
    # Usando a conexão local para não interferir na função _executar_sql
    # e garantir que estamos usando o caminho correto do config.
    try:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute(sql)
            registros = cursor.fetchall()
            if not registros:
                log.warning("[DATA_MANAGER] Nenhuma despesa encontrada no banco para reclassificar.")
                return []
            
            colunas = ['id_despesa', 'descricao']
            return [dict(zip(colunas, reg)) for reg in registros]
    except sqlite3.Error as e:
        log.error(f"Erro ao buscar despesas para reclassificação: {e}", exc_info=True)
        raise e

def atualizar_classificacoes_em_lote(despesas_atualizadas: list):
    """
    Recebe uma lista de despesas e atualiza APENAS o id_classificacao de cada uma,
    usando o comando UPDATE para melhor performance.
    """
    if not despesas_atualizadas:
        log.warning("[DATA_MANAGER] Nenhuma classificação para atualizar.")
        return

    # Prepara os dados no formato esperado pelo executemany: [(novo_id_class, id_da_despesa), ...]
    dados_para_update = [
        (d.get('id_classificacao'), d.get('id_despesa'))
        for d in despesas_atualizadas
    ]
    
    sql = "UPDATE despesas SET id_classificacao = ? WHERE id_despesa = ?"

    try:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.executemany(sql, dados_para_update)
            conn.commit()
            log.info(f"{cursor.rowcount} classificações de despesas foram atualizadas no banco.")
    except sqlite3.Error as e:
        log.error(f"Erro ao atualizar classificações em lote: {e}", exc_info=True)
        raise e
    
# ========================================================
# FUNÇÃO PARA EXIBIR A TABELA DE DESPESAS NA INTERFACE
# ========================================================

def obter_todas_despesas() -> list:
    """
    Busca todas as despesas no banco de dados, juntando com a tabela de
    classificação para obter os nomes do grupo e subgrupo.
    """
    log.info("[DATA_MANAGER] Buscando todas as despesas com informações de classificação para exibição.")
    sql = """
        SELECT
            d.id_despesa,
            d.data_extrato,
            d.instituicao,
            d.descricao,
            d.valor,
            c.grupo,
            c.subgrupo
        FROM
            despesas d
        LEFT JOIN
            classificacao c ON d.id_classificacao = c.id_classificacao
        ORDER BY
            d.id_despesa DESC
    """
    registros = _executar_sql(sql, fetchall=True)
    if not registros:
        return []
    
    colunas = ['id_despesa', 'data_extrato', 'instituicao', 'descricao', 'valor', 'grupo', 'subgrupo'
    ]
    return [dict(zip(colunas, reg)) for reg in registros]

def rdm(ano, mes, instituicao=None):
    """
    Gera o Relatório de Despesas Mensais (RDM) com filtros opcionais de instituição.
    Retorna: lista de dicionários com os campos:
    Data, Instituição, Grupo, Subgrupo, Descrição, Valor, Valor acm, %, % acm
    """
    import calendar
    log.info(f"[DATA_MANAGER] Gerando relatório RDM (Despesas Mensais) - ano: {ano}, mes: {mes}, instituicao: {instituicao}")
    # Garante que mes está no formato abreviado correto
    meses_abrev = ['JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ']
    mes_abrev = str(mes).upper()
    if mes_abrev not in meses_abrev:
        return []
    periodo = f"{mes_abrev}_{ano}"
    # Monta a query base
    sql = '''
        SELECT
            d.data_extrato,
            d.instituicao,
            c.grupo,
            c.subgrupo,
            d.descricao,
            d.valor
        FROM despesas d
        INNER JOIN classificacao c ON d.id_classificacao = c.id_classificacao
        WHERE d.data_extrato = ?
    '''
    params = [periodo]
    # Aplica filtro de instituição apenas se o usuário selecionou uma específica
    if instituicao and instituicao.strip().lower() != 'todas':
        sql += " AND TRIM(d.instituicao) = ?"
        params.append(instituicao.strip())
    sql += " ORDER BY d.valor DESC"
    # Log para depuração
    log.info(f"[DATA_MANAGER] SQL: {sql} | params: {params}")
    registros = _executar_sql(sql, tuple(params), fetchall=True)
    if not registros:
        return []
    # Monta os dicionários e calcula totais
    colunas = ['data_extrato', 'instituicao', 'grupo', 'subgrupo', 'descricao', 'valor']
    linhas = [dict(zip(colunas, reg)) for reg in registros]
    total = sum(l['valor'] for l in linhas)
    valor_acm = 0
    for idx, linha in enumerate(linhas):
        valor_acm += linha['valor']
        linha['valor_acm'] = valor_acm
        linha['perc'] = round(100 * linha['valor'] / total, 2) if total else 0
        linha['perc_acm'] = round(100 * valor_acm / total, 2) if total else 0
        data_dt = linha['data_extrato']
        if isinstance(data_dt, str) and len(data_dt) >= 7:
            linha['data'] = data_dt
        else:
            linha['data'] = str(data_dt)
    resultado = [
        {
            'Data': l['data'],
            'Instituicao': l['instituicao'],
            'Grupo': l['grupo'],
            'Subgrupo': l['subgrupo'],
            'Descricao': l['descricao'],
            'Valor': l['valor'],
            'Valor_acm': l['valor_acm'],
            '%': l['perc'],
            '%_acm': l['perc_acm']
        }
        for l in linhas
    ]
    return resultado

def rdmcc(ano: str, mes: str):
    """
    Gera relatório consolidado por grupo/subgrupo, com totais e percentuais.
    Parâmetros:
        ano (str): Ano no formato 'AAAA'.
        mes (str): Abreviação do mês em três letras (ex: 'JAN', 'FEV', ...).
    Retorna lista de dicionários para exibição tabular, com indentação nos subgrupos.
    Colunas: Classificação, Valor, % rel., % global
    """
    import calendar
    log.info("[DATA_MANAGER] Gerando relatório RDMCC (Consolidado por Grupo/Subgrupo)")
    meses_abrev = ['JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ']
    mes_abrev = str(mes).upper()
    if mes_abrev not in meses_abrev:
        return []
    try:
        ano_int = int(ano)
        if ano_int < 2000:
            return []
    except Exception:
        return []
    periodo = f"{mes_abrev}_{ano}"
    sql = '''
        SELECT c.grupo, c.subgrupo, SUM(d.valor) as valor
        FROM despesas d
        INNER JOIN classificacao c ON d.id_classificacao = c.id_classificacao
        WHERE d.data_extrato = ?
        GROUP BY c.grupo, c.subgrupo
        ORDER BY c.grupo, c.subgrupo
    '''
    registros = _executar_sql(sql, (periodo,), fetchall=True)
    if not registros:
        return []
    grupos = {}
    total_geral = 0
    for grupo, subgrupo, valor in registros:
        if grupo not in grupos:
            grupos[grupo] = {'total': 0, 'subgrupos': []}
        grupos[grupo]['subgrupos'].append({'subgrupo': subgrupo, 'valor': valor})
        grupos[grupo]['total'] += valor
        total_geral += valor
    resultado = []
    resultado.append({
        'Classificacao': 'Classificação',
        'Valor': 'Valor',
        '% rel.': '% rel.',
        '% global': '% global'
    })
    for grupo, dados in grupos.items():
        perc_rel = 100.0
        perc_global = round(100 * dados['total'] / total_geral, 2) if total_geral else 0
        resultado.append({
            'Classificacao': f'{grupo}',
            'Valor': f"{dados['total']:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'),
            '% rel.': f"{perc_rel:.2f}%",
            '% global': f"{perc_global:.2f}%"
        })
        for sub in dados['subgrupos']:
            perc_rel_sub = round(100 * sub['valor'] / dados['total'], 2) if dados['total'] else 0
            perc_global_sub = round(100 * sub['valor'] / total_geral, 2) if total_geral else 0
            resultado.append({
                'Classificacao': f"  {sub['subgrupo']}",  # Indentação com dois espaços
                'Valor': f"{sub['valor']:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'),
                '% rel.': f"{perc_rel_sub:.2f}%",
                '% global': f"{perc_global_sub:.2f}%"
            })
    resultado.append({
        'Classificacao': 'Total Geral',
        'Valor': f"{total_geral:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'),
        '% rel.': '',
        '% global': ''
    })
    return resultado

def obter_anos_despesas():
    """
    Retorna os anos únicos das despesas em ordem decrescente.
    """
    # Busca todos os data_extrato distintos
    sql = "SELECT DISTINCT data_extrato FROM despesas"
    registros = _executar_sql(sql, fetchall=True)
    if not registros:
        return []
    # Extrai os 4 últimos caracteres como ano
    anos = {str(r[0])[-4:] for r in registros if r[0] and len(str(r[0])) >= 8}
    return sorted([int(a) for a in anos], reverse=True)


def obter_meses_despesas(ano):
    """
    Retorna os meses (número e nome) com despesas para o ano informado, ordem crescente.
    """
    import calendar
    # Corrigido para usar SUBSTR do SQLite
    sql = "SELECT DISTINCT SUBSTR(data_extrato, 1, 3) as mes FROM despesas WHERE SUBSTR(data_extrato, -4, 4) = ? ORDER BY mes"
    registros = _executar_sql(sql, (str(ano),), fetchall=True)
    if not registros:
        return []
    meses_map = {'JAN': 1, 'FEV': 2, 'MAR': 3, 'ABR': 4, 'MAI': 5, 'JUN': 6,
                 'JUL': 7, 'AGO': 8, 'SET': 9, 'OUT': 10, 'NOV': 11, 'DEZ': 12}
    meses = []
    for r in registros:
        abrev = r[0].upper()
        num = meses_map.get(abrev, 0)
        nome = calendar.month_abbr[num].capitalize() if num > 0 and num <= 12 else abrev
        if num > 0:
            meses.append({"numero": num, "nome": nome})
    return meses

def obter_ano_mais_recente():
    """
    Retorna o ano mais recente presente em despesas.
    """
    sql = "SELECT MAX(SUBSTR(data_extrato, -4, 4)) FROM despesas"
    registro = _executar_sql(sql, fetchone=True)
    if not registro or not registro[0]:
        return None
    return int(registro[0])


# Retorna apenas a lista de abreviações dos meses (em maiúsculas, ordenados corretamente) para o ano informado.
# Exemplo de retorno: ['JAN', 'FEV', 'MAR', ...]
# Parâmetros:
#   ano (str ou int): Ano no formato 'AAAA' para filtrar as despesas.
# Retorna:
#   list[str]: Lista de abreviações dos meses presentes em despesas para o ano informado, ordenados de janeiro a dezembro.

def obter_meses_do_ano(ano):
    sql = "SELECT DISTINCT SUBSTR(data_extrato, 1, 3) FROM despesas WHERE SUBSTR(data_extrato, -4, 4) = ?"
    registros = _executar_sql(sql, (str(ano),), fetchall=True)
    if not registros:
        return []
    meses_map = {'JAN': 1, 'FEV': 2, 'MAR': 3, 'ABR': 4, 'MAI': 5, 'JUN': 6,
                 'JUL': 7, 'AGO': 8, 'SET': 9, 'OUT': 10, 'NOV': 11, 'DEZ': 12}
    meses = [r[0].upper() for r in registros if r[0] and r[0].upper() in meses_map]
    return sorted(meses, key=lambda abrev: meses_map[abrev])


def obter_instituicoes_despesas(periodo):
    """
    Retorna as instituições únicas para o período MMM_AAAA, ordenadas alfabeticamente.
    Agora recebe o período já pronto (ex: 'JAN_2025').
    Inclui a opção 'Todas' no início da lista.
    """
    sql = "SELECT DISTINCT instituicao FROM despesas WHERE data_extrato = ? ORDER BY instituicao"
    registros = _executar_sql(sql, (periodo,), fetchall=True)
    instituicoes = [r[0] for r in registros if r[0]]
    return ['Todas'] + instituicoes if instituicoes else ['Todas']
