"""Arquivo principal de execução do Sanitizador."""

import os
from .estrategia_sanitizador import SanitizadorTXT

def main():
    print("\n==================================================")
    print(" 🛡️  SISTEMA DE SANITIZAÇÃO DE DADOS (LGPD) 🛡️")
    print("==================================================\n")

    # Arquivos fixos para facilitar a demonstração
    arquivo_entrada = "dados_clientes.txt"
    arquivo_saida = "dados_clientes_limpo.txt"

    print(f"[*] Buscando arquivo: {arquivo_entrada}...")

    # Barreira de Segurança (Safety): Verifica se o arquivo existe antes de tentar ler
    if not os.path.exists(arquivo_entrada):
        print(f"\n[ERRO] Arquivo '{arquivo_entrada}' não encontrado!")
        print("Verifique se ele está na mesma pasta onde o terminal está rodando.")
        return

    try:
        # 1. Leitura
        print("[*] Lendo dados originais...")
        with open(arquivo_entrada, 'r', encoding='utf-8') as f:
            conteudo_bruto = f.read()

        # 2. Processamento (Orquestração MVC)
        print("[*] Aplicando regras de proteção (Regex)...")
        sanitizador = SanitizadorTXT()
        conteudo_limpo = sanitizador.sanitizar(conteudo_bruto)

        # 3. Escrita
        print("[*] Salvando arquivo seguro...")
        with open(arquivo_saida, 'w', encoding='utf-8') as f:
            f.write(conteudo_limpo)

        print("\n[✓] SUCESSO! Sanitização concluída.")
        print(f"[✓] Arquivo gerado: {arquivo_saida}\n")

    except Exception as e:
        print(f"\n[ERRO CRÍTICO] Falha inesperada no processamento: {e}\n")

if __name__ == "__main__":
    main()