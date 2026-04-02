import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import datetime

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Valuation Cortesia | Quintes Capital", 
    layout="centered", 
    page_icon="https://quintes.com.br/wp-content/uploads/2023/07/Favicon-Quintes.png"
)

# --- ESTILIZAÇÃO CUSTOMIZADA (CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');
    
    .stApp {
        background-color: #ffffff;
        color: #1a1a1a;
        font-family: 'Poppins', sans-serif;
    }
    
    /* Hero Section */
    .hero-container {
        text-align: center;
        padding: 40px 0 20px 0;
    }
    
    .logo-img {
        width: 180px;
        margin-bottom: 20px;
    }
    
    .hero-title {
        color: #007bff;
        font-weight: 700;
        font-size: 3rem;
        line-height: 1.1;
        margin-bottom: 15px;
    }
    
    .hero-title span { font-weight: 300; color: #1a1a1a; }
    
    /* Cards de Valuation e Ofertas */
    .valuation-card {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        border-radius: 20px;
        padding: 40px;
        text-align: center;
        border: 1px solid #dee2e6;
        margin-bottom: 30px;
    }

    .valuation-value {
        font-size: 3.5rem;
        font-weight: 800;
        color: #007bff;
        margin: 10px 0;
    }

    /* Ajuste para Mobile */
    @media (max-width: 600px) {
        .hero-title { font-size: 2rem; }
        .valuation-value { font-size: 2.2rem; }
    }

    /* Estilo dos Cards de Oferta */
    .offer-card {
        border: 1px solid #eee;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        height: 100%;
        transition: 0.3s;
    }
    .offer-card:hover {
        border-color: #007bff;
        box-shadow: 0 10px 20px rgba(0,123,255,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# --- CONTROLE DE SESSÃO ---
if 'etapa' not in st.session_state:
    st.session_state.etapa = 1

# --- ETAPA 1: LANDING PAGE & FORMULÁRIO ---
if st.session_state.etapa == 1:
    st.markdown("""
        <div class="hero-container">
            <img src="https://quintes.com.br/wp-content/uploads/2023/07/Logo-Branca-Simbolo-Preto-Texto.png" class="logo-img">
            <h1 class="hero-title">Valuation <span>Cortesia</span></h1>
            <p style="font-size:1.2rem; color:#666;">Descubra agora quanto vale sua operação de Telecom.</p>
        </div>
    """, unsafe_allow_html=True)

    with st.form("form_captacao"):
        col1, col2 = st.columns(2)
        with col1:
            nome = st.text_input("Seu Nome")
            empresa = st.text_input("Nome do Provedor")
            ebitda_anual = st.number_input("EBITDA Anual (R$)", min_value=0.0, format="%.2f")
        with col2:
            whatsapp = st.text_input("WhatsApp")
            assinantes = st.number_input("Qtd de Assinantes", min_value=0)
            mrr = st.number_input("Receita Mensal (MRR)", min_value=0.0, format="%.2f")
        
        submit = st.form_submit_button("CALCULAR VALUATION AGORA 🚀")

        if submit:
            if ebitda_anual > 0:
                # Lógica simplificada: Multiplo de 6x EBITDA
                st.session_state.dados_cliente = {
                    "empresa": empresa,
                    "valuation": ebitda_anual * 6
                }
                st.session_state.etapa = 2
                st.rerun()
            else:
                st.warning("Insira o EBITDA para calcular.")

# --- ETAPA 2: RESULTADO E CONVERSÃO ---
elif st.session_state.etapa == 2:
    d = st.session_state.dados_cliente
    
    st.markdown(f"""
        <div class="valuation-card">
            <h2 style="margin:0; font-size:1.2rem; text-transform:uppercase; letter-spacing:2px;">Resultado Estimado</h2>
            <div class="valuation-value">R$ {d['valuation']:,.2f}</div>
            <p style="color:#666;">Empresa: <strong>{d['empresa']}</strong></p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<h3 style='text-align:center; margin-bottom:30px;'>Como deseja evoluir este resultado?</h3>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("<div class='offer-card'><h4>📄 Relatório</h4><p>PDF detalhado com análise de KPIs.</p></div>", unsafe_allow_html=True)
        if st.button("Obter PDF", use_container_width=True):
            st.info("Redirecionando para checkout...")

    with c2:
        st.markdown("<div class='offer-card'><h4>💻 Plano SaaS</h4><p>Dashboard de Valuation em tempo real.</p></div>", unsafe_allow_html=True)
        if st.button("Assinar Software", use_container_width=True):
            st.info("Abrindo painel SaaS...")

    with c3:
        st.markdown("<div class='offer-card'><h4>🤝 Advisor M&A</h4><p>Consultoria para venda da operação.</p></div>", unsafe_allow_html=True)
        if st.button("Falar com Advisor", use_container_width=True):
            st.info("Chamando no WhatsApp...")

    if st.button("← Refazer Cálculo", type="secondary"):
        st.session_state.etapa = 1
        st.rerun()
