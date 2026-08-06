"""Testes unitários para a estratégia de sanitização de arquivos TXT."""

from src.python_pdm_template.estrategia_sanitizador import SanitizadorTXT


def test_sanitizar_texto_com_dados_sensiveis():
    """Garante que CPFs e e-mails sejam devidamente mascarados."""
    sanitizador = SanitizadorTXT()
    texto_original = "Cliente: João, CPF: 123.456.789-00, Email: joao@email.com"

    texto_esperado = "Cliente: João, CPF: ***.***.***-**, Email: ***********"
    texto_resultado = sanitizador.sanitizar(texto_original)

    assert texto_resultado == texto_esperado


def test_sanitizar_texto_sem_dados_sensiveis():
    """Garante que textos sem dados sensíveis permaneçam inalterados."""
    sanitizador = SanitizadorTXT()
    texto_original = "Texto limpo apenas com informações públicas."

    texto_resultado = sanitizador.sanitizar(texto_original)

    assert texto_resultado == texto_original