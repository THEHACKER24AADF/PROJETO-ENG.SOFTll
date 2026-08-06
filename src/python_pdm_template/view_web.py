"""Interface web do Sanitizador de Arquivos utilizando Streamlit."""

import streamlit as st
from src.python_pdm_template.detector_suspeito import DetectorConteudoSuspeito
from src.python_pdm_template.estrategia_sanitizador import SanitizadorTXT

# Configuração inicial da página
st.set_page_config(page_title="Sanitizador de Arquivos", page_icon="🛡️")

st.title("1. Importar Dados")

# Componente de upload de arquivos
arquivo_carregado = st.file_uploader(
    "Selecione o arquivo .txt com os dados brutos", type=["txt"]
)

if arquivo_carregado is not None:
    st.info(f"Arquivo '{arquivo_carregado.name}' carregado com sucesso!")

    # Inicializa o estado da sessão para manter os dados após interações
    if "conteudo_limpo" not in st.session_state:
        st.session_state.conteudo_limpo = None
        st.session_state.alertas = []
        st.session_state.processado = False

    # Lê o conteúdo do arquivo carregado pelo usuário
    conteudo_bruto = arquivo_carregado.getvalue().decode("utf-8")

    # Botão de disparo da higienização
    if st.button("Iniciar Higienização"):
        # 1. Executa a varredura do detector de riscos financeiros/compliance
        detector = DetectorConteudoSuspeito()
        st.session_state.alertas = detector.detectar(conteudo_bruto)

        # 2. Executa o mascaramento dos dados sensíveis (Regex)
        sanitizador = SanitizadorTXT()
        st.session_state.conteudo_limpo = sanitizador.sanitizar(conteudo_bruto)
        st.session_state.processado = True

    # Renderiza os resultados na tela caso o processamento tenha sido concluído
    if st.session_state.processado:
        st.write("---")
        
        # Exibe o painel de riscos caso o detector tenha encontrado algo
        if st.session_state.alertas:
            st.error(
                f"🚨 [ALERTA DE SEGURANÇA] Foram encontrados {len(st.session_state.alertas)} riscos no arquivo:"
            )
            for alerta in st.session_state.alertas:
                st.markdown(
                    f"• **Linha {alerta['linha']}** | *[{alerta['categoria']}]* ➔ {alerta['trecho']}"
                )
        else:
            st.success("✓ Nenhum risco financeiro ou de compliance detectado.")

        # Confirmação de sucesso do processamento do arquivo limpo
        st.success("Sanitização concluída com sucesso!")

        # Componente oficial para download do arquivo tratado
        st.download_button(
            label="Baixar Arquivo Limpo",
            data=st.session_state.conteudo_limpo,
            file_name="dados_clientes_limpo.txt",
            mime="text/plain",
        )