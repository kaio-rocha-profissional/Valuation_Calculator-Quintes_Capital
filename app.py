import streamlit as st

# Configuração da página
st.set_page_config(page_title="Quintes Capital - Resultado Valuation", layout="centered")

# --- ESTILIZAÇÃO CUSTOMIZADA ---
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #007BFF; color: white; }
    </style>
    """, unsafe_allow_html=True)

import streamlit as st

import streamlit as st

# --- CAPTAÇÃO DA URL (Ajustada para o seu novo formulário) ---
query_params = st.query_params

# Puxando os dados (se não existirem, usa o padrão entre aspas)
nome = query_params.get("nome", "Investidor")
empresa = query_params.get("empresa", "sua empresa")
cargo = query_params.get("cargo", "Sócio")
local = query_params.get("local", "") # Vai pegar o Estado/UF

# Variáveis de Cálculo com tratamento de erro
try:
    # O Fillout pode mandar pontos/vírgulas, limpamos isso aqui
    assinantes = int(float(query_params.get("assinantes", 0)))
    ticket_medio = float(query_params.get("ticket", 0))
    receita_mes = float(query_params.get("receita", 0))
except:
    assinantes = ticket_medio = receita_mes = 0

# ... segue a lógica de cálculo que fizemos antes ...
    
    # As 4 ofertas do seu Funil
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📄 Relatório + Plano de Ação"):
            st.info("Solicitação enviada! Gerando seu PDF...")
            
    with col2:
        if st.button("💻 Plano SaaS (12 meses)"):
            st.info("Excelente! Ativando seu acesso ao software...")

    if st.button("🤝 Falar com Advisor (M&A)"):
        st.success("Prioridade máxima! Kaio ou um consultor Quintes entrará em contato em instantes.")
