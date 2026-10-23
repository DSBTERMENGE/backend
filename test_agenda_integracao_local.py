"""Conferencia local do fluxo HTTP e PostgreSQL da virada de competencia."""

import json
import sys
from pathlib import Path
from urllib.request import Request, urlopen


SOURCE_CODE = Path(__file__).parent / "source_code"
sys.path.insert(0, str(SOURCE_CODE))

from data_manager import _get_pg_connection  # noqa: E402


def post_json(endpoint, payload):
    request = Request(
        f"http://localhost:5000{endpoint}",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urlopen(request, timeout=10) as response:
        return json.loads(response.read().decode("utf-8"))


def conferir_virada(competencia_origem, competencia_destino):
    conn = _get_pg_connection("financas")
    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT competencia, status, data_encerramento IS NOT NULL
            FROM agenda_competencias
            WHERE competencia IN (%s, %s)
            ORDER BY competencia
            """,
            (competencia_origem, competencia_destino),
        )
        competencias = cursor.fetchall()
        assert competencias == [
            (competencia_origem, "ENCERRADA", True),
            (competencia_destino, "ABERTA", False),
        ], competencias

        cursor.execute(
            "SELECT COUNT(*) FROM agenda_competencias WHERE status = 'ABERTA'"
        )
        assert cursor.fetchone()[0] == 1

        cursor.execute(
            """
            SELECT tipo_item, status, COUNT(*), COALESCE(SUM(valor), 0)
            FROM agenda_ocorrencias
            WHERE competencia = %s
            GROUP BY tipo_item, status
            ORDER BY tipo_item, status
            """,
            (competencia_destino,),
        )
        agenda = cursor.fetchall()

        cursor.execute(
            """
            SELECT COUNT(*), COALESCE(SUM(valor), 0),
                   MIN(data_prevista), MAX(data_prevista)
            FROM receita_ocorrencias
            WHERE competencia = %s
            """,
            (competencia_destino,),
        )
        receitas = cursor.fetchone()
    finally:
        conn.rollback()
        if "cursor" in locals():
            cursor.close()
        conn.close()

    repeticao = post_json(
        "/agenda/gerar_proxima_competencia",
        {
            "competencia_origem": competencia_origem,
            "competencia_destino": competencia_destino,
            "confirmacao": True,
            "database_name": "financas",
        },
    )
    assert repeticao["sucesso"] is True
    assert repeticao["ja_existente"] is True

    previa = post_json(
        "/agenda/previa_virada",
        {
            "competencia_origem": competencia_destino,
            "database_name": "financas",
        },
    )
    assert previa["sucesso"] is True

    print("competencias:", competencias)
    print("agenda_destino:", agenda)
    print("receitas_destino:", receitas)
    print("repeticao_idempotente:", repeticao["ja_existente"])
    print(
        "nova_previa:",
        previa["competencia_origem"],
        "->",
        previa["competencia_destino"],
    )


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit(
            "Uso: python test_agenda_integracao_local.py AAAA-MM AAAA-MM"
        )
    conferir_virada(sys.argv[1], sys.argv[2])
