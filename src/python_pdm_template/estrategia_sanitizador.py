"""Módulo contendo a estratégia de sanitização para arquivos de texto."""

import re
from .base_sanitizador import EstrategiaSanitizacao


class SanitizadorTXT(EstrategiaSanitizacao):
    """Implementa a sanitização específica para arquivos TXT."""

    def sanitizar(self, conteudo: str) -> str:
        """
        Substitui dados sensíveis (CPF e E-mail) no texto por máscaras.

        Args:
            conteudo (str): O texto original do arquivo.

        Returns:
            str: O texto limpo e mascarado.
        """
        # Expressão regular para identificar CPF (padrão: 000.000.000-00)
        padrao_cpf = r"\d{3}\.\d{3}\.\d{3}-\d{2}"

        # Expressão regular para identificar E-mails básicos
        padrao_email = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

        # Aplica as substituições no texto
        conteudo_limpo = re.sub(padrao_cpf, "***.***.***-**", conteudo)
        conteudo_limpo = re.sub(padrao_email, "***********", conteudo_limpo)

        return conteudo_limpo
