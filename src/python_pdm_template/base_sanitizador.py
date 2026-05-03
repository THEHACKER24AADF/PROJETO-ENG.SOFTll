from abc import ABC, abstractmethod

class EstrategiaSanitizacao(ABC):
    @abstractmethod
    def sanitizar(self, conteudo: str) -> str:
        """
        Contrato: Todas as estratégias de limpeza devem receber 
        uma string suja e retornar uma string limpa.
        """
        pass

    