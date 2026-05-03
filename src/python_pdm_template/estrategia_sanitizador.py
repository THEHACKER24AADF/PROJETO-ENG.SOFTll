from .base_sanitizador import EstrategiaSanitizacao
class SanitizadorTXT(EstrategiaSanitizacao):
    def Sanitizar(self, conteudo: str) -> str:
        # Lógica temporária apenas para a CLI/GUI poder testar
        conteudo_limpo = conteudo.replace("DADO_SENSIVEL", "***")
        return conteudo_limpo