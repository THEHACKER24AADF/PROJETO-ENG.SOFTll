import streamlit as st

# Configuração da página
st.set_page_config(page_title="Sanitizador LGPD", page_icon="🛡️", layout="centered")

# Cabeçalho
st.title("🛡️ Sanitizador de Dados - LGPD")
st.markdown("Proteja dados sensíveis de clientes com mascaramento automático.")
st.divider()

# Área de Upload
st.subheader("1. Importar Dados")
arquivo_sujo = st.file_uploader("Selecione o arquivo .txt com os dados brutos", type=["txt"])

# Área de Processamento
if arquivo_sujo is not None:
    st.info(f"Arquivo '{arquivo_sujo.name}' carregado com sucesso!")
    
    if st.button("Iniciar Sanitização", type="primary"):
        with st.spinner('Aplicando regras de Regex...'):
            # O Controller será conectado aqui na próxima etapa
            st.success("Sanitização concluída com sucesso!")
            
            # Botão provisório para visualização da interface
            st.download_button(
                label="Baixar Arquivo Limpo",
                data="Dados mascarados irão aqui...",
                file_name="dados_clientes_limpo.txt",
                mime="text/plain"
            )