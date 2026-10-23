"""Testes unitarios das regras puras de geracao da agenda."""

import sys
import unittest
from datetime import date
from decimal import Decimal
from pathlib import Path
from unittest.mock import MagicMock, patch


SOURCE_CODE = Path(__file__).parent / "source_code"
sys.path.insert(0, str(SOURCE_CODE))

from agenda_service import (  # noqa: E402
    AgendaServiceError,
    _avaliar_bloqueio_inativacao,
    _avaliar_competencia_editavel,
    _assinatura_previa_sincronizacao,
    _classificar_sincronizacao,
    _calcular_data_prevista,
    _preparar_ocorrencia_agenda,
    _preparar_ocorrencia_receita,
    _proxima_competencia,
    _recorrencia_devida,
    _validar_confirmacao_virada,
    confirmar_sincronizacao,
    gerar_proxima_competencia,
    validar_ocorrencia_editavel,
)


class AgendaServiceTests(unittest.TestCase):
    def test_competencia_aberta_permite_alteracao(self):
        resultado = _avaliar_competencia_editavel("2026-02", "ABERTA")
        self.assertTrue(resultado["permitido"])

    def test_competencia_encerrada_permite_somente_consulta(self):
        resultado = _avaliar_competencia_editavel("2026-01", "ENCERRADA")
        self.assertFalse(resultado["permitido"])
        self.assertEqual(resultado["codigo"], "competencia_encerrada")

    @patch("agenda_service._get_pg_connection")
    def test_validacao_da_ocorrencia_consulta_status_no_banco(self, obter_conexao):
        conexao = MagicMock()
        cursor = conexao.cursor.return_value
        cursor.fetchone.return_value = ("2026-01", "ENCERRADA")
        obter_conexao.return_value = conexao

        resultado = validar_ocorrencia_editavel(17)

        self.assertFalse(resultado["permitido"])
        cursor.execute.assert_called_once()
        self.assertEqual(cursor.execute.call_args.args[1], (17,))
        conexao.rollback.assert_called_once()
        conexao.close.assert_called_once()

    def test_assinatura_da_previa_independe_da_ordem(self):
        grupos_a = {
            "entrar": [{"id_agendamento": 2}, {"id_agendamento": 1}],
            "sair": [{"id_ocorrencia": 20}, {"id_ocorrencia": 10}],
            "permanecer": [],
            "conflitos": [],
        }
        grupos_b = {
            **grupos_a,
            "entrar": list(reversed(grupos_a["entrar"])),
            "sair": list(reversed(grupos_a["sair"])),
        }
        self.assertEqual(
            _assinatura_previa_sincronizacao("2026-02", grupos_a),
            _assinatura_previa_sincronizacao("2026-02", grupos_b),
        )

    def test_sincronizacao_exige_confirmacao_explicita(self):
        with self.assertRaises(AgendaServiceError) as contexto:
            confirmar_sincronizacao("2026-02", "assinatura", False)
        self.assertEqual(contexto.exception.codigo, "confirmacao_obrigatoria")

    @patch("agenda_service._montar_previa_sincronizacao")
    @patch("agenda_service._obter_competencia_aberta", return_value="2026-02")
    @patch("agenda_service._get_pg_connection")
    def test_sincronizacao_aplica_inclusao_e_exclusao_atomicas(
        self, obter_conexao, obter_aberta, montar_previa
    ):
        conexao = MagicMock()
        cursor = conexao.cursor.return_value
        cursor.rowcount = 1
        obter_conexao.return_value = conexao
        montar_previa.return_value = {
            "ha_diferencas": True,
            "assinatura_previa": "assinatura-atual",
            "conflitos": [],
            "entrar": [{
                "id_agendamento": 7,
                "tipo_item": "CONTA",
                "data_prevista": date(2026, 2, 15),
                "valor": Decimal("111.11"),
                "observacoes": "Nova conta",
            }],
            "sair": [{"id_ocorrencia": 9}],
        }

        resultado = confirmar_sincronizacao(
            "2026-02", "assinatura-atual", True
        )

        self.assertEqual(resultado["incluidos"], 1)
        self.assertEqual(resultado["excluidos"], 1)
        self.assertFalse(resultado["ja_sincronizada"])
        conexao.commit.assert_called_once()
        conexao.rollback.assert_not_called()
        obter_aberta.assert_called_once_with(cursor, bloquear=True)
        self.assertEqual(cursor.execute.call_count, 2)

    @patch("agenda_service._montar_previa_sincronizacao")
    @patch("agenda_service._obter_competencia_aberta", return_value="2026-02")
    @patch("agenda_service._get_pg_connection")
    def test_previa_desatualizada_desfaz_transacao(
        self, obter_conexao, obter_aberta, montar_previa
    ):
        conexao = MagicMock()
        obter_conexao.return_value = conexao
        montar_previa.return_value = {
            "ha_diferencas": True,
            "assinatura_previa": "assinatura-nova",
            "conflitos": [],
            "entrar": [],
            "sair": [{"id_ocorrencia": 9}],
        }

        with self.assertRaises(AgendaServiceError) as contexto:
            confirmar_sincronizacao("2026-02", "assinatura-antiga", True)

        self.assertEqual(contexto.exception.codigo, "previa_desatualizada")
        conexao.rollback.assert_called_once()
        conexao.commit.assert_not_called()

    @patch("agenda_service._montar_previa_sincronizacao")
    @patch("agenda_service._obter_competencia_aberta", return_value="2026-02")
    @patch("agenda_service._get_pg_connection")
    def test_sincronizacao_repetida_sem_diferencas_e_idempotente(
        self, obter_conexao, obter_aberta, montar_previa
    ):
        conexao = MagicMock()
        obter_conexao.return_value = conexao
        montar_previa.return_value = {
            "ha_diferencas": False,
            "assinatura_previa": "assinatura-vazia",
            "conflitos": [],
            "entrar": [],
            "sair": [],
        }

        resultado = confirmar_sincronizacao(
            "2026-02", "qualquer-assinatura-anterior", True
        )

        self.assertTrue(resultado["ja_sincronizada"])
        self.assertEqual(resultado["incluidos"], 0)
        self.assertEqual(resultado["excluidos"], 0)
        conexao.commit.assert_called_once()
        conexao.rollback.assert_not_called()

    def test_classificacao_da_previa_de_sincronizacao(self):
        esperadas = {
            1: {"id_agendamento": 1, "descricao": "Permanece"},
            2: {"id_agendamento": 2, "descricao": "Nova"},
        }
        atuais = [
            {
                "id_agendamento": 1, "tipo_item": "CONTA",
                "status": "PENDENTE", "ativo": "S",
            },
            {
                "id_agendamento": 3, "tipo_item": "CONTA",
                "status": "PENDENTE", "ativo": "N",
            },
            {
                "id_agendamento": 4, "tipo_item": "COMPROMISSO",
                "status": "CONCLUIDO", "ativo": "N",
            },
        ]
        grupos = _classificar_sincronizacao(esperadas, atuais)
        self.assertEqual([item["id_agendamento"] for item in grupos["entrar"]], [2])
        self.assertEqual([item["id_agendamento"] for item in grupos["sair"]], [3])
        self.assertEqual(
            [item["id_agendamento"] for item in grupos["permanecer"]], [1]
        )
        self.assertEqual(
            [item["id_agendamento"] for item in grupos["conflitos"]], [4]
        )

    def test_sincronizacao_nao_retira_item_ativo_fora_da_lista_esperada(self):
        atuais = [{
            "id_agendamento": 9, "tipo_item": "CONTA",
            "status": "PENDENTE", "ativo": "S",
        }]
        grupos = _classificar_sincronizacao({}, atuais)
        self.assertEqual(grupos["sair"], [])
        self.assertEqual(grupos["permanecer"], atuais)

    def test_inativacao_bloqueada_para_ocorrencia_realizada(self):
        conta = _avaliar_bloqueio_inativacao("CONTA", "PAGA", "2026-02")
        compromisso = _avaliar_bloqueio_inativacao(
            "COMPROMISSO", "CONCLUIDO", "2026-02"
        )
        self.assertFalse(conta["permitido"])
        self.assertEqual(conta["codigo"], "conta_paga_na_competencia_aberta")
        self.assertFalse(compromisso["permitido"])
        self.assertEqual(
            compromisso["codigo"],
            "compromisso_concluido_na_competencia_aberta",
        )

    def test_inativacao_permitida_para_ocorrencia_pendente(self):
        resultado = _avaliar_bloqueio_inativacao(
            "CONTA", "PENDENTE", "2026-02"
        )
        self.assertTrue(resultado["permitido"])

    def test_proxima_competencia(self):
        self.assertEqual(_proxima_competencia("2025-11"), "2025-12")
        self.assertEqual(_proxima_competencia("2025-12"), "2026-01")

    def test_competencia_invalida(self):
        for competencia in ("12/2025", "2025-00", "2025-13", None):
            with self.subTest(competencia=competencia):
                with self.assertRaises(AgendaServiceError) as contexto:
                    _proxima_competencia(competencia)
                self.assertEqual(contexto.exception.codigo, "competencia_invalida")

    def test_ajuste_do_ultimo_dia(self):
        self.assertEqual(
            _calcular_data_prevista(2025, 2, 31, date(2025, 1, 31)),
            date(2025, 2, 28),
        )
        self.assertEqual(
            _calcular_data_prevista(2024, 2, 31, date(2024, 1, 31)),
            date(2024, 2, 29),
        )

    def test_recorrencias_em_meses(self):
        inicio = date(2025, 1, 10)
        self.assertTrue(_recorrencia_devida("M", inicio, 2025, 2, True))
        self.assertTrue(_recorrencia_devida("2M", inicio, 2025, 3, True))
        self.assertFalse(_recorrencia_devida("2M", inicio, 2025, 2, True))
        self.assertTrue(_recorrencia_devida("3M", inicio, 2025, 4, True))
        self.assertTrue(_recorrencia_devida("6M", inicio, 2025, 7, True))
        self.assertTrue(_recorrencia_devida("A", inicio, 2026, 1, True))

    def test_nao_recorrente_gera_uma_vez(self):
        inicio = date(2025, 5, 20)
        self.assertTrue(_recorrencia_devida("N", inicio, 2025, 5, False))
        self.assertFalse(_recorrencia_devida("N", inicio, 2025, 5, True))
        self.assertFalse(_recorrencia_devida("N", inicio, 2025, 6, False))

    def test_recorrencia_anterior_ao_inicio_e_codigo_invalido(self):
        inicio = date(2025, 5, 20)
        self.assertFalse(_recorrencia_devida("M", inicio, 2025, 4, False))
        with self.assertRaises(AgendaServiceError) as contexto:
            _recorrencia_devida("SEMANAL", inicio, 2025, 5, False)
        self.assertEqual(contexto.exception.codigo, "recorrencia_invalida")

    def test_conta_copia_valor_zero_e_observacao_anterior(self):
        cadastro = (
            10, "CONTA", Decimal("150.00"), date(2025, 1, 10), None,
            10, "M", "Observacao do cadastro", Decimal("0.00"),
            "Nao foi devida no mes", "2025-12",
        )
        ocorrencia = _preparar_ocorrencia_agenda(cadastro, 2026, 1)
        self.assertEqual(ocorrencia["valor"], Decimal("0.00"))
        self.assertEqual(ocorrencia["observacoes"], "Nao foi devida no mes")

    def test_compromisso_nao_tem_valor(self):
        cadastro = (
            20, "COMPROMISSO", None, date(2025, 1, 31), None,
            31, "A", "Aniversario", None, None, "2025-01",
        )
        ocorrencia = _preparar_ocorrencia_agenda(cadastro, 2026, 1)
        self.assertIsNone(ocorrencia["valor"])
        self.assertEqual(ocorrencia["data_prevista"], date(2026, 1, 31))

    def test_cadastro_fora_da_vigencia_nao_gera_ocorrencia(self):
        cadastro = (
            30, "CONTA", Decimal("50.00"), date(2025, 1, 5),
            date(2025, 12, 31), 5, "M", None, Decimal("50.00"), None,
            "2025-12",
        )
        self.assertIsNone(_preparar_ocorrencia_agenda(cadastro, 2026, 1))

    def test_receita_copia_valor_anterior_inclusive_zero(self):
        cadastro = (
            40, Decimal("1000.00"), date(2025, 1, 5), None,
            5, "M", "Receita mensal", Decimal("0.00"), None, "2025-12",
        )
        ocorrencia = _preparar_ocorrencia_receita(cadastro, 2026, 1)
        self.assertEqual(ocorrencia["valor"], Decimal("0.00"))

    def test_confirmacao_explicita_da_virada(self):
        self.assertEqual(
            _validar_confirmacao_virada("2025-12", "2026-01", True),
            "2026-01",
        )
        with self.assertRaises(AgendaServiceError) as contexto:
            _validar_confirmacao_virada("2025-12", "2026-01", False)
        self.assertEqual(contexto.exception.codigo, "confirmacao_obrigatoria")

    def test_destino_confirmado_deve_ser_o_mes_seguinte(self):
        with self.assertRaises(AgendaServiceError) as contexto:
            _validar_confirmacao_virada("2025-12", "2026-02", True)
        self.assertEqual(contexto.exception.codigo, "competencia_destino_divergente")

    @patch("agenda_service._get_pg_connection")
    def test_falha_funcional_desfaz_transacao(self, obter_conexao):
        conexao = MagicMock()
        cursor = conexao.cursor.return_value
        cursor.fetchone.return_value = None
        obter_conexao.return_value = conexao

        with self.assertRaises(AgendaServiceError) as contexto:
            gerar_proxima_competencia("2025-12", "2026-01", True)

        self.assertEqual(contexto.exception.codigo, "competencia_origem_inexistente")
        conexao.rollback.assert_called_once()
        conexao.commit.assert_not_called()
        cursor.close.assert_called_once()
        conexao.close.assert_called_once()

    @patch("agenda_service._get_pg_connection")
    def test_repeticao_de_virada_concluida_e_idempotente(self, obter_conexao):
        conexao = MagicMock()
        cursor = conexao.cursor.return_value
        cursor.fetchone.side_effect = [
            ("ENCERRADA",),
            ("ABERTA",),
            (13,),
            (2,),
        ]
        obter_conexao.return_value = conexao

        resultado = gerar_proxima_competencia("2025-12", "2026-01", True)

        self.assertTrue(resultado["ja_existente"])
        self.assertEqual(resultado["ocorrencias_agenda_criadas"], 13)
        self.assertEqual(resultado["receitas_criadas"], 2)
        conexao.rollback.assert_called_once()
        conexao.commit.assert_not_called()


if __name__ == "__main__":
    unittest.main()
