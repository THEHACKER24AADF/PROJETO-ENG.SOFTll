from src.python_pdm_template.estrategia_sanitizador import SanitizadorTXT


def test_deve_falhar_ao_tentar_mascarar_cpf_real():
    """
    TDD (Red): Este teste deve FALHAR propositalmente.
    A funcionalidade de Regex para CPF ainda será implementada.
    """
    # 1. Preparação (Arrange)
    sanitizador = SanitizadorTXT()
    texto_sujo = "O cliente João tem o CPF 123.456.789-00 cadastrado."
    texto_esperado = "O cliente João tem o CPF ***.***.***-** cadastrado."

    # 2. Ação (Act)
    resultado = sanitizador.sanitizar(texto_sujo)

    # 3. Verificação (Assert)
    assert resultado == texto_esperado
