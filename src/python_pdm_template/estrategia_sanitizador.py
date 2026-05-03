"""Módulo contendo a estratégia de sanitização para arquivos de texto."""

from .base_sanitizador import EstrategiaSanitizacao


class SanitizadorTXT(EstrategiaSanitizacao):
    """Implementa a sanitização específica para arquivos TXT."""

    def sanitizar(self, conteudo: str) -> str:
        """
        Substitui dados sensíveis no texto por asteriscos.

        Args:
            conteudo (str): O texto original do arquivo.

        Returns:
            str: O texto limpo e mascarado.
        """
        return conteudo.replace("DADO_SENSIVEL", "***")