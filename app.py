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

# --- CAPTAÇÃO DA URL ---
query_params = st.query_params

# Dados de Contato/Empresa
nome = query_params.get("nome", "Investidor")
empresa = query_params.get("empresa", "sua empresa")
cargo = query_params.get("cargo", "Sócio")
telefone = query_params.get("tel", "")
email = query_params.get("email", "")
local = query_params.get("local", "")

# Variáveis de Cálculo (Convertendo para números)
try:
    assinantes = int(query_params.get("assinantes", 0))
    ticket_medio = float(query_params.get("ticket", 0))
    receita_mes = float(query_params.get("receita", 0))
except:
    assinantes = ticket_medio = receita_mes = 0

# --- LÓGICA DE VALUATION QUINTES CAPITAL ---
if receita_mes > 0:
    # 1. Cálculo por Múltiplo de Faturamento (Comum no setor: 1.5x a 3x a receita anual)
    receita_anual = receita_mes * 12
    valuation_faturamento = receita_anual * 2.5 # Usando múltiplo conservador de 2.5x
    
    # 2. Cálculo por Base de Assinantes (Ex: R$ 2.000 por assinante)
    valuation_base = assinantes * 2000
    
    # Resultado Final: Média ponderada entre os dois métodos
    valuation_final = (valuation_faturamento + valuation_base) / 2
else:
    valuation_final = 0
    
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
