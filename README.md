# 🛡️ Sanitizador de Arquivos com Foco na LGPD

Uma aplicação web desenvolvida em Python para detecção e higienização automática de dados sensíveis em arquivos de texto não estruturados (`.txt`). O sistema foi projetado para mitigar riscos de vazamento de informações e garantir conformidade com as diretrizes da Lei Geral de Proteção de Dados (LGPD).

## Propósito do Projeto

Em ambientes corporativos e acadêmicos, o compartilhamento de logs, relatórios e bases de dados brutos frequentemente expõe dados pessoais de titulares (PII) ou termos confidenciais de compliance. Este projeto resolve esse problema através de uma esteira automatizada que realiza duas ações críticas:
1. **Auditoria Visual (Detecção):** Escaneia o arquivo à procura de potenciais quebras de sigilo ou riscos financeiros (como senhas exponenciadas ou cartões de crédito).
2. **Mascaramento (Sanitização):** Anonimiza dados estruturados (como CPFs e e-mails) por meio de substituição por caracteres opacos antes que o arquivo seja compartilhado.

---

## Tecnologias Utilizadas

* **Python 3.11+**: Linguagem core para o processamento de texto e lógica de negócio.
* **Streamlit**: Framework utilizado para a construção de uma interface web interativa, responsiva e de rápido deploy.
* **Regex (Expressões Regulares)**: Mecanismo de alta performance utilizado para a varredura e substituição padronizada de dados sensíveis.
* **PDM**: Gerenciador moderno de pacotes e dependências de ambiente virtual.

---

## 🛡️ Regras de Negócio e Cobertura do Detector

O sistema atua em duas frentes distintas durante a leitura de um arquivo:

### 1. Motor de Detecção de Riscos (Alertas Visuais)
Identifica trechos suspeitos na interface do usuário, apontando o número exato da linha para auditoria manual:
* **Dados Financeiros:** Padrões numéricos correspondentes a cartões de crédito.
* **Termos de Compliance:** Presença de palavras-chave como *confidenciais*, *vazamento*, *uso interno* e variações.
* **Credenciais:** Identificação de menções a senhas provisórias ou chaves de acesso.

### 2. Motor de Sanitização (Mascaramento)
Substitui automaticamente dados pessoais por máscaras de segurança (`***`), gerando um novo arquivo pronto para download seguro:
* **CPFs:** Identificação de padrões com ou sem pontuação (`000.000.000-00`).
* **E-mails:** Captura de endereços eletrônicos estruturados baseados em domínios válidos.

---

## 📂 Estrutura do Projeto

```text
├── .venv/                          # Ambiente virtual local
├── src/
│   └── python_pdm_template/
│       ├── __init__.py
│       ├── detector_suspeito.py    # Lógica de varredura e auditoria de termos
│       ├── estrategia_sanitizador.py # Mecanismo de mascaramento via Regex
│       └── view_web.py             # Interface gráfica construída em Streamlit
├── tests/                          # Suíte de testes unitários (PyTest)
├── requirements.txt                # Passaporte de dependências para deploy na nuvem
└── README.md                       # Documentação principal do repositório
