import streamlit as st
import pandas as pd

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Resultado Valuation | Quintes Capital", 
    layout="centered", 
    page_icon="https://quintes.com.br/wp-content/uploads/2023/07/Favicon-Quintes.png"
)

# --- CAPTURA DE PARÂMETROS DA URL (Vindos do Fillout) ---
# Exemplo de URL: myapp.streamlit.app/?nome=Joao&empresa=TelecomX&ebitda=100000
query_params = st.query_params

# Se houver dados na URL, a gente pula direto para a Etapa 2
if query_params and "ebitda" in query_params:
    st.session_state.etapa = 2
    # Convertendo os valores que chegam como string na URL
    st.session_state.dados_cliente = {
        "nome": query_params.get("nome", "Cliente"),
        "empresa": query_params.get("empresa", "Provedor"),
        "ebitda": float(query_params.get("ebitda", 0)),
        "mrr": float(query_params.get("mrr", 0))
    }
elif 'etapa' not in st.session_state:
    st.session_state.etapa = 1

# --- ESTILIZAÇÃO CSS (Igual ao anterior) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');
    .stApp { background-color: #ffffff; font-family: 'Poppins', sans-serif; }
    .hero-container { text-align: center; padding: 40px 0; }
    .logo-img { width: 180px; }
    .valuation-card {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        border-radius: 20px; padding: 40px; text-align: center;
        border: 1px solid #dee2e6; margin-bottom: 30px;
    }
    .valuation-value { font-size: 3.5rem; font-weight: 800; color: #007bff; }
    </style>
""", unsafe_allow_html=True)

# --- ETAPA 1: BOTÃO PARA O FILLOUT (Se o cara cair direto no site) ---
if st.session_state.etapa == 1:
    st.markdown("""
        <div class="hero-container">
            <img src="https://quintes.com.br/wp-content/uploads/2023/07/Logo-Branca-Simbolo-Preto-Texto.png" class="logo-img">
            <h1 style="color:#007bff; font-weight:700;">Calculadora de Valuation</h1>
            <p>Clique no botão abaixo para iniciar sua análise gratuita.</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Substitua pelo link real do seu formulário Fillout
    url_fillout = "https://forms.fillout.com/t/seulinkpersonalizado"
    st.markdown(f'''
        <a href="{url_fillout}" target="_blank" style="text-decoration: none;">
            <div style="background-color: #007bff; color: white; padding: 15px; border-radius: 50px; text-align: center; font-weight: 700;">
                INICIAR FORMULÁRIO NO FILLOUT 🚀
            </div>
        </a>
    ''', unsafe_allow_html=True)

# --- ETAPA 2: EXIBIÇÃO DO RESULTADO (Vindo do Fillout) ---
elif st.session_state.etapa == 2:
    d = st.session_state.dados_cliente
    
    # Lógica de Cálculo: Múltiplo de 6x EBITDA
    valuation_final = d['ebitda'] * 6

    st.markdown(f"""
        <div class="valuation-card">
            <h2 style="margin:0; font-size:1.2rem; text-transform:uppercase;">Resultado para {d['empresa']}</h2>
            <div class="valuation-value">R$ {valuation_final:,.2f}</div>
            <p style="color:#666;">Cálculo baseado no EBITDA Anual informado.</p>
        </div>
    """, unsafe_allow_html=True)

    # ... Restante dos cards de oferta (Relatório, SaaS, Advisor) igual ao código anterior ...
    st.markdown("<h3 style='text-align:center;'>Como deseja evoluir?</h3>", unsafe_allow_html=True)
    # (Coloque aqui as colunas de botões de oferta que vimos antes)
