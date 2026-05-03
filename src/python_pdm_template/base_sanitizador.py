"""Módulo contendo a interface base para as estratégias de sanitização."""

from abc import ABC, abstractmethod


class EstrategiaSanitizacao(ABC):
    """Classe abstrata que define o contrato para os sanitizadores."""

    @abstractmethod
    def sanitizar(self, conteudo: str) -> str:
        """
        Recebe o conteúdo sujo e retorna o conteúdo sanitizado.

        Args:
            conteudo (str): O texto original do arquivo.

        Returns:
            str: O texto limpo.
        """