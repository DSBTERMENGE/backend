"""Servicos transacionais da agenda historica do FinCtl."""

import calendar
import hashlib
import json
import re
from datetime import date

from data_manager import _get_pg_connection


COMPETENCIA_RE = re.compile(r"^\d{4}-(0[1-9]|1[0-2])$")
INTERVALOS_RECORRENCIA = {
    "M": 1,
    "2M": 2,
    "3M": 3,
    "6M": 6,
    "A": 12,
}


class AgendaServiceError(Exception):
    """Erro funcional esperado ao gerar uma competencia."""

    def __init__(self, codigo, mensagem, http_status=409):
        super().__init__(mensagem)
        self.codigo = codigo
        self.mensagem = mensagem
        self.http_status = http_status


def _partes_competencia(competencia):
    if not isinstance(competencia, str) or not COMPETENCIA_RE.fullmatch(competencia):
        raise AgendaServiceError(
            "competencia_invalida",
            "Competencia invalida. Use o formato AAAA-MM.",
            400,
        )
    ano, mes = competencia.split("-")
    return int(ano), int(mes)


def _proxima_competencia(competencia):
    ano, mes = _partes_competencia(competencia)
    if mes == 12:
        return f"{ano + 1:04d}-01"
    return f"{ano:04d}-{mes + 1:02d}"


def _diferenca_meses(data_inicio, ano_destino, mes_destino):
    return (ano_destino - data_inicio.year) * 12 + (mes_destino - data_inicio.month)


def _recorrencia_devida(recorrencia, data_inicio, ano_destino, mes_destino, tem_historico):
    diferenca = _diferenca_meses(data_inicio, ano_destino, mes_destino)
    if diferenca < 0:
        return False
    if recorrencia == "N":
        return diferenca == 0 and not tem_historico
    intervalo = INTERVALOS_RECORRENCIA.get(recorrencia)
    if intervalo is None:
        raise AgendaServiceError(
            "recorrencia_invalida",
            f"Recorrencia nao reconhecida: {recorrencia}",
            500,
        )
    return diferenca % intervalo == 0


def _calcular_data_prevista(ano, mes, dia_preferencial, data_inicio):
    dia = dia_preferencial or data_inicio.day
    ultimo_dia = calendar.monthrange(ano, mes)[1]
    return date(ano, mes, min(dia, ultimo_dia))


def _avaliar_bloqueio_inativacao(tipo_item, status, competencia):
    """Descreve o conflito que impede inativar um cadastro na agenda aberta."""
    if tipo_item == "CONTA" and status == "PAGA":
        return {
            "permitido": False,
            "codigo": "conta_paga_na_competencia_aberta",
            "mensagem": (
                f"A conta esta paga na competencia aberta {competencia}. "
                "Apague a Data de pagamento na Agenda Mensal antes de inativar."
            ),
        }
    if tipo_item == "COMPROMISSO" and status == "CONCLUIDO":
        return {
            "permitido": False,
            "codigo": "compromisso_concluido_na_competencia_aberta",
            "mensagem": (
                f"O compromisso esta concluido na competencia aberta {competencia}. "
                "Apague a Data real na Agenda Mensal antes de inativar."
            ),
        }
    return {"permitido": True, "codigo": None, "mensagem": "Inativacao permitida."}


def validar_inativacao_cadastro(id_agendamento, database_name="financas"):
    """Impede inativacao quando a ocorrencia aberta ja foi realizada."""
    try:
        id_agendamento = int(id_agendamento)
    except (TypeError, ValueError) as exc:
        raise AgendaServiceError(
            "agendamento_invalido", "Identificador do cadastro invalido.", 400
        ) from exc

    conn = _get_pg_connection(database_name)
    conn.set_session(readonly=True, autocommit=False)
    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT o.tipo_item, o.status, o.competencia
            FROM agenda_ocorrencias o
            JOIN agenda_competencias c
              ON c.competencia = o.competencia
            WHERE o.id_agendamento = %s
              AND c.status = 'ABERTA'
            """,
            (id_agendamento,),
        )
        ocorrencia = cursor.fetchone()
        if not ocorrencia:
            return {
                "sucesso": True,
                "permitido": True,
                "codigo": None,
                "mensagem": "Inativacao permitida.",
            }

        tipo_item, status, competencia = ocorrencia
        resultado = _avaliar_bloqueio_inativacao(
            tipo_item, status, competencia
        )
        return {"sucesso": True, **resultado}
    finally:
        conn.rollback()
        if "cursor" in locals():
            cursor.close()
        conn.close()


def _avaliar_competencia_editavel(competencia, status):
    """Permite alteracoes de ocorrencias somente na competencia aberta."""
    if status != "ABERTA":
        return {
            "permitido": False,
            "codigo": "competencia_encerrada",
            "mensagem": (
                f"A competencia {competencia} esta encerrada e permite somente consulta."
            ),
        }
    return {
        "permitido": True,
        "codigo": None,
        "mensagem": "Alteracao permitida.",
    }


def validar_competencia_editavel(competencia, database_name="financas"):
    """Valida uma competencia antes de incluir uma ocorrencia pela API generica."""
    _partes_competencia(competencia)
    conn = _get_pg_connection(database_name)
    conn.set_session(readonly=True, autocommit=False)
    try:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT status FROM agenda_competencias WHERE competencia = %s",
            (competencia,),
        )
        registro = cursor.fetchone()
        if not registro:
            raise AgendaServiceError(
                "competencia_nao_encontrada",
                f"A competencia {competencia} nao foi encontrada.",
                404,
            )
        return {"sucesso": True, **_avaliar_competencia_editavel(competencia, registro[0])}
    finally:
        conn.rollback()
        if "cursor" in locals():
            cursor.close()
        conn.close()


def validar_ocorrencia_editavel(id_ocorrencia, database_name="financas"):
    """Consulta a competencia real da ocorrencia antes de altera-la ou exclui-la."""
    try:
        id_ocorrencia = int(id_ocorrencia)
    except (TypeError, ValueError) as exc:
        raise AgendaServiceError(
            "ocorrencia_invalida", "Identificador da ocorrencia invalido.", 400
        ) from exc

    conn = _get_pg_connection(database_name)
    conn.set_session(readonly=True, autocommit=False)
    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT o.competencia, c.status
            FROM agenda_ocorrencias o
            JOIN agenda_competencias c
              ON c.competencia = o.competencia
            WHERE o.id_ocorrencia = %s
            """,
            (id_ocorrencia,),
        )
        registro = cursor.fetchone()
        if not registro:
            raise AgendaServiceError(
                "ocorrencia_nao_encontrada",
                "A ocorrencia da agenda nao foi encontrada.",
                404,
            )
        competencia, status = registro
        return {"sucesso": True, **_avaliar_competencia_editavel(competencia, status)}
    finally:
        conn.rollback()
        if "cursor" in locals():
            cursor.close()
        conn.close()


def _classificar_sincronizacao(esperadas, atuais):
    """Classifica a diferenca entre cadastros devidos e ocorrencias abertas."""
    atuais_por_cadastro = {item["id_agendamento"]: item for item in atuais}
    entrar = [
        item for id_agendamento, item in esperadas.items()
        if id_agendamento not in atuais_por_cadastro
    ]
    sair = []
    permanecer = []
    conflitos = []

    for item in atuais:
        if item["ativo"] != "N":
            permanecer.append(item)
            continue

        realizado = (
            item["tipo_item"] == "CONTA" and item["status"] == "PAGA"
        ) or (
            item["tipo_item"] == "COMPROMISSO"
            and item["status"] == "CONCLUIDO"
        )
        if realizado:
            conflitos.append(item)
        else:
            sair.append(item)

    return {
        "entrar": entrar,
        "sair": sair,
        "permanecer": permanecer,
        "conflitos": conflitos,
    }


def _assinatura_previa_sincronizacao(competencia, grupos):
    conteudo = {
        "competencia": competencia,
        "entrar": sorted(item["id_agendamento"] for item in grupos["entrar"]),
        "sair": sorted(item["id_ocorrencia"] for item in grupos["sair"]),
        "conflitos": sorted(
            item["id_ocorrencia"] for item in grupos["conflitos"]
        ),
    }
    serializado = json.dumps(conteudo, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(serializado.encode("utf-8")).hexdigest()


def _montar_previa_sincronizacao(cursor, competencia):
    """Monta a comparacao usando o cursor da consulta ou transacao atual."""
    ano, mes = _partes_competencia(competencia)

    cursor.execute("SELECT id_agendamento, descricao FROM agenda_cadastros")
    descricoes = dict(cursor.fetchall())

    esperadas = {}
    for cadastro in _buscar_cadastros_agenda(cursor, competencia):
        ocorrencia = _preparar_ocorrencia_agenda(cadastro, ano, mes)
        if not ocorrencia:
            continue
        ocorrencia["descricao"] = descricoes.get(
            ocorrencia["id_agendamento"], ""
        )
        esperadas[ocorrencia["id_agendamento"]] = ocorrencia

    cursor.execute(
        """
            SELECT
                o.id_ocorrencia,
                o.id_agendamento,
                o.tipo_item,
                c.descricao,
                o.data_prevista,
                o.valor,
                o.status,
                o.data_realizacao,
                o.observacoes,
                c.ativo
            FROM agenda_ocorrencias o
            JOIN agenda_cadastros c
              ON c.id_agendamento = o.id_agendamento
             AND c.tipo_item = o.tipo_item
            WHERE o.competencia = %s
            ORDER BY o.data_prevista, o.id_ocorrencia
        """,
        (competencia,),
    )
    atuais = [
        {
                "id_ocorrencia": row[0],
                "id_agendamento": row[1],
                "tipo_item": row[2],
                "descricao": row[3],
                "data_prevista": row[4],
                "valor": row[5],
                "status": row[6],
                "data_realizacao": row[7],
                "observacoes": row[8],
                "ativo": row[9],
        }
        for row in cursor.fetchall()
    ]

    grupos = _classificar_sincronizacao(esperadas, atuais)
    resumo = {nome: len(itens) for nome, itens in grupos.items()}
    ha_diferencas = bool(resumo["entrar"] or resumo["sair"])
    return {
        "sucesso": True,
        "competencia": competencia,
        "resumo": resumo,
        **grupos,
        "ha_diferencas": ha_diferencas,
        "pode_confirmar": ha_diferencas and not resumo["conflitos"],
        "assinatura_previa": _assinatura_previa_sincronizacao(
            competencia, grupos
        ),
    }


def _obter_competencia_aberta(cursor, bloquear=False):
    sufixo = " FOR UPDATE" if bloquear else ""
    cursor.execute(
        "SELECT competencia FROM agenda_competencias "
        f"WHERE status = 'ABERTA'{sufixo}"
    )
    abertas = cursor.fetchall()
    if len(abertas) != 1:
        raise AgendaServiceError(
            "competencia_aberta_invalida",
            "Deve existir exatamente uma competencia aberta.",
            409,
        )
    return abertas[0][0]


def obter_previa_sincronizacao(database_name="financas"):
    """Compara a agenda aberta com os cadastros, sem modificar o banco."""
    conn = _get_pg_connection(database_name)
    conn.set_session(readonly=True, autocommit=False)
    try:
        cursor = conn.cursor()
        competencia = _obter_competencia_aberta(cursor)
        return _montar_previa_sincronizacao(cursor, competencia)
    finally:
        conn.rollback()
        if "cursor" in locals():
            cursor.close()
        conn.close()


def confirmar_sincronizacao(
    competencia,
    assinatura_previa,
    confirmacao,
    database_name="financas",
):
    """Aplica a previa ainda valida em uma unica transacao."""
    if confirmacao is not True:
        raise AgendaServiceError(
            "confirmacao_obrigatoria",
            "A sincronizacao exige confirmacao explicita.",
            400,
        )
    _partes_competencia(competencia)
    if not assinatura_previa:
        raise AgendaServiceError(
            "assinatura_previa_obrigatoria",
            "Gere uma nova previa antes de confirmar.",
            400,
        )

    conn = _get_pg_connection(database_name)
    conn.set_session(readonly=False, autocommit=False)
    try:
        cursor = conn.cursor()
        competencia_aberta = _obter_competencia_aberta(cursor, bloquear=True)
        if competencia != competencia_aberta:
            raise AgendaServiceError(
                "competencia_alterada",
                "A competencia aberta mudou. Gere uma nova previa.",
            )

        previa = _montar_previa_sincronizacao(cursor, competencia_aberta)
        if previa["conflitos"]:
            raise AgendaServiceError(
                "conflitos_na_sincronizacao",
                "Existem itens pagos ou concluidos vinculados a cadastros inativos.",
            )

        if not previa["ha_diferencas"]:
            conn.commit()
            return {
                "sucesso": True,
                "competencia": competencia_aberta,
                "ja_sincronizada": True,
                "incluidos": 0,
                "excluidos": 0,
            }

        if assinatura_previa != previa["assinatura_previa"]:
            raise AgendaServiceError(
                "previa_desatualizada",
                "A agenda ou os cadastros mudaram. Gere uma nova previa.",
            )

        incluidos = 0
        for item in previa["entrar"]:
            cursor.execute(
                """
                INSERT INTO agenda_ocorrencias (
                    id_agendamento, tipo_item, competencia, data_prevista,
                    valor, status, observacoes
                )
                VALUES (%s, %s, %s, %s, %s, 'PENDENTE', %s)
                """,
                (
                    item["id_agendamento"],
                    item["tipo_item"],
                    competencia_aberta,
                    item["data_prevista"],
                    item["valor"],
                    item["observacoes"],
                ),
            )
            incluidos += 1

        excluidos = 0
        for item in previa["sair"]:
            cursor.execute(
                """
                DELETE FROM agenda_ocorrencias
                WHERE id_ocorrencia = %s AND competencia = %s
                  AND status = 'PENDENTE'
                """,
                (item["id_ocorrencia"], competencia_aberta),
            )
            if cursor.rowcount != 1:
                raise AgendaServiceError(
                    "falha_exclusao_sincronizacao",
                    "Uma ocorrencia deixou de estar disponivel para exclusao.",
                )
            excluidos += 1

        conn.commit()
        return {
            "sucesso": True,
            "competencia": competencia_aberta,
            "ja_sincronizada": False,
            "incluidos": incluidos,
            "excluidos": excluidos,
        }
    except Exception:
        conn.rollback()
        raise
    finally:
        if "cursor" in locals():
            cursor.close()
        conn.close()


def _buscar_cadastros_agenda(cursor, competencia_destino):
    cursor.execute(
        """
        SELECT
            c.id_agendamento,
            c.tipo_item,
            c.valor_padrao,
            c.data_inicio,
            c.data_fim,
            c.dia_preferencial,
            c.recorrencia,
            c.observacoes,
            anterior.valor AS valor_anterior,
            anterior.observacoes AS observacoes_anteriores,
            anterior.competencia AS competencia_anterior
        FROM agenda_cadastros c
        LEFT JOIN LATERAL (
            SELECT o.valor, o.observacoes, o.competencia
            FROM agenda_ocorrencias o
            WHERE o.id_agendamento = c.id_agendamento
              AND o.competencia < %s
            ORDER BY o.competencia DESC
            LIMIT 1
        ) anterior ON TRUE
        WHERE c.ativo = 'S'
        ORDER BY c.id_agendamento
        """,
        (competencia_destino,),
    )
    return cursor.fetchall()


def _buscar_cadastros_receitas(cursor, competencia_destino):
    cursor.execute(
        """
        SELECT
            c.id_receita_cadastro,
            c.valor_padrao,
            c.data_inicio,
            c.data_fim,
            c.dia_preferencial,
            c.recorrencia,
            c.observacoes,
            anterior.valor AS valor_anterior,
            anterior.observacoes AS observacoes_anteriores,
            anterior.competencia AS competencia_anterior
        FROM receita_cadastros c
        LEFT JOIN LATERAL (
            SELECT o.valor, o.observacoes, o.competencia
            FROM receita_ocorrencias o
            WHERE o.id_receita_cadastro = c.id_receita_cadastro
              AND o.competencia < %s
            ORDER BY o.competencia DESC
            LIMIT 1
        ) anterior ON TRUE
        WHERE c.ativo = 'S'
        ORDER BY c.id_receita_cadastro
        """,
        (competencia_destino,),
    )
    return cursor.fetchall()


def _preparar_ocorrencia_agenda(cadastro, ano_destino, mes_destino):
    (
        id_agendamento,
        tipo_item,
        valor_padrao,
        data_inicio,
        data_fim,
        dia_preferencial,
        recorrencia,
        observacoes_cadastro,
        valor_anterior,
        observacoes_anteriores,
        competencia_anterior,
    ) = cadastro
    if not _recorrencia_devida(
        recorrencia,
        data_inicio,
        ano_destino,
        mes_destino,
        competencia_anterior is not None,
    ):
        return None

    data_prevista = _calcular_data_prevista(
        ano_destino, mes_destino, dia_preferencial, data_inicio
    )
    if data_fim and data_prevista > data_fim:
        return None

    valor = None
    observacoes = observacoes_cadastro
    if tipo_item == "CONTA":
        valor = valor_anterior if valor_anterior is not None else valor_padrao
        if valor == 0 and observacoes_anteriores:
            observacoes = observacoes_anteriores

    return {
        "id_agendamento": id_agendamento,
        "tipo_item": tipo_item,
        "data_prevista": data_prevista,
        "valor": valor,
        "observacoes": observacoes,
    }


def _preparar_ocorrencia_receita(cadastro, ano_destino, mes_destino):
    (
        id_receita_cadastro,
        valor_padrao,
        data_inicio,
        data_fim,
        dia_preferencial,
        recorrencia,
        observacoes_cadastro,
        valor_anterior,
        _observacoes_anteriores,
        competencia_anterior,
    ) = cadastro
    if not _recorrencia_devida(
        recorrencia,
        data_inicio,
        ano_destino,
        mes_destino,
        competencia_anterior is not None,
    ):
        return None

    data_prevista = _calcular_data_prevista(
        ano_destino, mes_destino, dia_preferencial, data_inicio
    )
    if data_fim and data_prevista > data_fim:
        return None

    return {
        "id_receita_cadastro": id_receita_cadastro,
        "data_prevista": data_prevista,
        "valor": valor_anterior if valor_anterior is not None else valor_padrao,
        "observacoes": observacoes_cadastro,
    }


def obter_previa_virada(competencia_origem, database_name="financas"):
    """Retorna a conferencia da origem e a previsao da proxima geracao."""

    competencia_destino = _proxima_competencia(competencia_origem)
    ano_destino, mes_destino = _partes_competencia(competencia_destino)
    conn = _get_pg_connection(database_name)
    conn.set_session(readonly=True, autocommit=False)

    try:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT status FROM agenda_competencias WHERE competencia = %s",
            (competencia_origem,),
        )
        origem = cursor.fetchone()
        if not origem:
            raise AgendaServiceError(
                "competencia_origem_inexistente",
                f"Competencia de origem nao encontrada: {competencia_origem}",
                404,
            )
        if origem[0] != "ABERTA":
            raise AgendaServiceError(
                "competencia_origem_nao_aberta",
                "A previa somente pode ser gerada para a competencia aberta.",
            )

        cursor.execute(
            """
            SELECT
                id_ocorrencia, descricao, data_prevista, valor, status,
                situacao_exibicao, observacoes
            FROM agenda_ocorrencias_view
            WHERE competencia = %s AND tipo_item = 'CONTA'
            ORDER BY data_prevista, descricao
            """,
            (competencia_origem,),
        )
        colunas_contas = [descricao[0] for descricao in cursor.description]
        contas = [dict(zip(colunas_contas, linha)) for linha in cursor.fetchall()]

        cursor.execute(
            """
            SELECT
                id_ocorrencia, descricao, data_prevista, status,
                situacao_exibicao, observacoes
            FROM agenda_ocorrencias_view
            WHERE competencia = %s AND tipo_item = 'COMPROMISSO'
            ORDER BY data_prevista, descricao
            """,
            (competencia_origem,),
        )
        colunas_compromissos = [descricao[0] for descricao in cursor.description]
        compromissos = [
            dict(zip(colunas_compromissos, linha)) for linha in cursor.fetchall()
        ]

        cursor.execute(
            """
            SELECT id_receita_ocorrencia, descricao, data_prevista, valor, observacoes
            FROM receita_ocorrencias_view
            WHERE competencia = %s
            ORDER BY data_prevista, descricao
            """,
            (competencia_origem,),
        )
        colunas_receitas = [descricao[0] for descricao in cursor.description]
        receitas = [dict(zip(colunas_receitas, linha)) for linha in cursor.fetchall()]

        agenda_prevista = []
        for cadastro in _buscar_cadastros_agenda(cursor, competencia_destino):
            ocorrencia = _preparar_ocorrencia_agenda(
                cadastro, ano_destino, mes_destino
            )
            if ocorrencia:
                agenda_prevista.append(ocorrencia)

        receitas_previstas = []
        for cadastro in _buscar_cadastros_receitas(cursor, competencia_destino):
            ocorrencia = _preparar_ocorrencia_receita(
                cadastro, ano_destino, mes_destino
            )
            if ocorrencia:
                receitas_previstas.append(ocorrencia)

        total_previsto = sum((conta["valor"] for conta in contas), 0)
        total_pago = sum(
            (conta["valor"] for conta in contas if conta["status"] == "PAGA"), 0
        )
        total_pendente = total_previsto - total_pago
        total_receitas = sum((receita["valor"] for receita in receitas), 0)

        return {
            "sucesso": True,
            "competencia_origem": competencia_origem,
            "competencia_destino": competencia_destino,
            "status_origem": origem[0],
            "resumo_origem": {
                "contas": len(contas),
                "contas_pagas": sum(1 for conta in contas if conta["status"] == "PAGA"),
                "contas_pendentes": sum(
                    1 for conta in contas if conta["status"] == "PENDENTE"
                ),
                "contas_vencidas": sum(
                    1 for conta in contas if conta["situacao_exibicao"] == "VENCIDA"
                ),
                "total_previsto": total_previsto,
                "total_pago": total_pago,
                "saldo_pendente": total_pendente,
                "compromissos": len(compromissos),
                "receitas": len(receitas),
                "total_receitas": total_receitas,
            },
            "geracao_prevista": {
                "contas": sum(
                    1 for item in agenda_prevista if item["tipo_item"] == "CONTA"
                ),
                "compromissos": sum(
                    1
                    for item in agenda_prevista
                    if item["tipo_item"] == "COMPROMISSO"
                ),
                "receitas": len(receitas_previstas),
            },
            "contas": contas,
            "compromissos": compromissos,
            "receitas": receitas,
        }
    finally:
        conn.rollback()
        if "cursor" in locals():
            cursor.close()
        conn.close()


def _resumo_competencia_existente(cursor, competencia_origem, competencia_destino):
    cursor.execute(
        "SELECT status FROM agenda_competencias WHERE competencia = %s",
        (competencia_destino,),
    )
    destino = cursor.fetchone()
    if not destino:
        return None

    cursor.execute(
        "SELECT COUNT(*) FROM agenda_ocorrencias WHERE competencia = %s",
        (competencia_destino,),
    )
    total_agenda = cursor.fetchone()[0]
    cursor.execute(
        "SELECT COUNT(*) FROM receita_ocorrencias WHERE competencia = %s",
        (competencia_destino,),
    )
    total_receitas = cursor.fetchone()[0]
    return {
        "sucesso": True,
        "ja_existente": True,
        "competencia_origem": competencia_origem,
        "competencia_destino": competencia_destino,
        "status_destino": destino[0],
        "ocorrencias_agenda_criadas": total_agenda,
        "receitas_criadas": total_receitas,
        "mensagem": "A competencia seguinte ja havia sido gerada.",
    }


def _validar_confirmacao_virada(
    competencia_origem, competencia_destino_confirmada, confirmacao
):
    """Exige confirmacao explicita do mes exibido na previa."""

    competencia_destino = _proxima_competencia(competencia_origem)
    if confirmacao is not True:
        raise AgendaServiceError(
            "confirmacao_obrigatoria",
            "Confirme explicitamente a geracao da competencia seguinte.",
        )
    if competencia_destino_confirmada != competencia_destino:
        raise AgendaServiceError(
            "competencia_destino_divergente",
            (
                "A competencia de destino confirmada nao corresponde ao mes "
                "seguinte da origem. Gere uma nova previa antes de continuar."
            ),
        )
    return competencia_destino


def gerar_proxima_competencia(
    competencia_origem,
    competencia_destino_confirmada,
    confirmacao=False,
    database_name="financas",
):
    """Encerra a origem e gera a competencia seguinte em uma unica transacao."""

    competencia_destino = _validar_confirmacao_virada(
        competencia_origem, competencia_destino_confirmada, confirmacao
    )
    ano_destino, mes_destino = _partes_competencia(competencia_destino)
    conn = _get_pg_connection(database_name)

    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT status
            FROM agenda_competencias
            WHERE competencia = %s
            FOR UPDATE
            """,
            (competencia_origem,),
        )
        origem = cursor.fetchone()
        if not origem:
            raise AgendaServiceError(
                "competencia_origem_inexistente",
                f"Competencia de origem nao encontrada: {competencia_origem}",
                404,
            )

        if origem[0] == "ENCERRADA":
            resumo = _resumo_competencia_existente(
                cursor, competencia_origem, competencia_destino
            )
            if resumo:
                conn.rollback()
                return resumo
            raise AgendaServiceError(
                "competencia_origem_encerrada",
                "A competencia de origem esta encerrada e a seguinte nao existe.",
            )

        cursor.execute(
            "SELECT competencia FROM agenda_competencias WHERE status = 'ABERTA'"
        )
        aberta = cursor.fetchone()
        if not aberta or aberta[0] != competencia_origem:
            raise AgendaServiceError(
                "competencia_origem_nao_aberta",
                "A competencia informada nao e a competencia aberta atual.",
            )

        resumo = _resumo_competencia_existente(
            cursor, competencia_origem, competencia_destino
        )
        if resumo:
            raise AgendaServiceError(
                "competencia_destino_ja_existe",
                "A competencia seguinte ja existe enquanto a origem permanece aberta.",
            )

        cursor.execute(
            """
            UPDATE agenda_competencias
            SET status = 'ENCERRADA', data_encerramento = CURRENT_TIMESTAMP
            WHERE competencia = %s AND status = 'ABERTA'
            """,
            (competencia_origem,),
        )
        if cursor.rowcount != 1:
            raise AgendaServiceError(
                "falha_encerramento",
                "Nao foi possivel encerrar a competencia de origem.",
            )

        cursor.execute(
            "INSERT INTO agenda_competencias (competencia) VALUES (%s)",
            (competencia_destino,),
        )

        total_agenda = 0
        for cadastro in _buscar_cadastros_agenda(cursor, competencia_destino):
            ocorrencia = _preparar_ocorrencia_agenda(
                cadastro, ano_destino, mes_destino
            )
            if not ocorrencia:
                continue

            cursor.execute(
                """
                INSERT INTO agenda_ocorrencias (
                    id_agendamento, tipo_item, competencia, data_prevista,
                    valor, status, observacoes
                )
                VALUES (%s, %s, %s, %s, %s, 'PENDENTE', %s)
                """,
                (
                    ocorrencia["id_agendamento"],
                    ocorrencia["tipo_item"],
                    competencia_destino,
                    ocorrencia["data_prevista"],
                    ocorrencia["valor"],
                    ocorrencia["observacoes"],
                ),
            )
            total_agenda += 1

        total_receitas = 0
        for cadastro in _buscar_cadastros_receitas(cursor, competencia_destino):
            ocorrencia = _preparar_ocorrencia_receita(
                cadastro, ano_destino, mes_destino
            )
            if not ocorrencia:
                continue
            cursor.execute(
                """
                INSERT INTO receita_ocorrencias (
                    id_receita_cadastro, competencia, data_prevista,
                    valor, observacoes
                )
                VALUES (%s, %s, %s, %s, %s)
                """,
                (
                    ocorrencia["id_receita_cadastro"],
                    competencia_destino,
                    ocorrencia["data_prevista"],
                    ocorrencia["valor"],
                    ocorrencia["observacoes"],
                ),
            )
            total_receitas += 1

        conn.commit()
        return {
            "sucesso": True,
            "ja_existente": False,
            "competencia_origem": competencia_origem,
            "competencia_destino": competencia_destino,
            "status_destino": "ABERTA",
            "ocorrencias_agenda_criadas": total_agenda,
            "receitas_criadas": total_receitas,
            "mensagem": "Competencia seguinte gerada com sucesso.",
        }
    except Exception:
        conn.rollback()
        raise
    finally:
        if "cursor" in locals():
            cursor.close()
        conn.close()\n