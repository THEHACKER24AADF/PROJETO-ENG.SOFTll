"""Módulo responsável pela detecção de riscos financeiros e de conformidade."""

import re


class DetectorConteudoSuspeito:
    """Varre o texto para identificar padrões financeiros e termos de conformidade de risco."""

    def __init__(self):
        """Inicializa os padrões de regex para riscos financeiros e compliance."""
        # Regex para Cartões de Crédito (Visa, Mastercard, etc. - grupos de 4 dígitos)
        self.padrao_cartao = r"\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b"

        # Palavras-chave expandidas para cobrir plurais e variações comuns
        self.termos_compliance = [
            "confidencial", "confidenciais",
            "segredo", "secretíssimo",
            "propina", "suborno",
            "caixa dois", "caixa 2",
            "faturamento oculto",
            "senha provisória", "senha",
            "documento interno", "uso interno",
            "vazamento", "vazado", "vazados", "vazar"
        ]

    def detectar(self, conteudo: str) -> list[dict]:
        """Varre o texto linha por linha e retorna uma lista de alertas encontrados.

        Args:
            conteudo (str): O texto bruto do arquivo a ser analisado.

        Returns:
            list[dict]: Uma lista de dicionários contendo os alertas com linha, tipo e trecho.
        """
        alertas = []
        linhas = conteudo.splitlines()

        for index, linha in enumerate(linhas, start=1):
            # 1. Verificação de Risco Financeiro (Cartão de Crédito)
            if re.search(self.padrao_cartao, linha):
                alertas.append(
                    {
                        "linha": index,
                        "categoria": "Risco Financeiro (Cartão de Crédito)",
                        "trecho": "Padrão numérico suspeito detectado.",
                    }
                )

            # 2. Verificação de Risco de Conformidade (Termos Sensíveis)
            for termo in self.termos_compliance:
                # Busca o termo ignorando maiúsculas/minúsculas (\b garante a palavra inteira)
                if re.search(r"\b" + re.escape(termo) + r"\b", linha, re.IGNORECASE):
                    alertas.append(
                        {
                            "linha": index,
                            "categoria": "Risco de Conformidade",
                            "trecho": f"Termo sensível encontrado: '{termo}'",
                        }
                    )

        return alertas