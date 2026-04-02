import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import datetime

# --- CONFIGURAÇÃO DA PÁGINA (Precisa ser a primeira linha) ---
st.set_page_config(
    page_title="Valuation Cortesia | Quintes Capital", 
    layout="centered", # Centralizado como na imagem de referência
    page_icon="https://quintes.com.br/wp-content/uploads/2023/07/Favicon-Quintes.png" # Logo Quintes
)

# Conexão com o Google Sheets (Para salvar o lead - prospecção inversa)
conn = st.connection("gsheets", type=GSheetsConnection)

# --- SESSÃO DE CONTROLE (Para saber em qual etapa o usuário está) ---
if 'etapa' not in st.session_state:
    st.session_state.etapa = 1

# --- ESTILIZAÇÃO CUSTOMIZADA (CSS) ---
# Aqui fazemos a "mágica" para imitar as cores, fontes e estilo da sua referência.
# Cores da Quintes: Preto, Branco, Azul Claro e Roxo/Dourado.
st.markdown("""
    <style>
    /* Importando Fontes (Google Fonts) */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');
    
    /* Configurações Globais */
    .stApp {
        background-color: #ffffff; /* Fundo Branco Limpo */
        color: #1a1a1a; /* Texto Preto Suave */
        font-family: 'Poppins', sans-serif;
    }
    
    /* Hero Section (A parte de cima) */
    .hero-container {
        text-align: center;
        padding: 60px 0;
        margin-bottom: 30px;
    }
    
    .logo-img {
        width: 150px;
        margin-bottom: 20px;
    }
    
    .hero-title {
        color: #007bff; /* Azul Quintes */
        font-weight: 700;
        font-size: 3.5rem; /* Fonte grande como na referência */
        line-height: 1.1;
        margin-bottom: 10px;
    }
    
    .hero-title span {
        font-weight: 400; /* Parte "cortesia" mais fina */
    }
    
    .hero-subtitle {
        color: #555555; /* Texto cinza suave */
        font-size: 1.2rem;
        max-width: 600px;
        margin: 0 auto;
    }
    
    /* Formulário Customizado */
    div.stForm {
        background-color: #f9f9f9; /* Fundo do formulário cinza muito claro */
        border: 1px solid #eeeeee;
        border-radius: 15px;
        padding: 30px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05); /* Sombra suave */
    }
    
    /* Inputs de Texto */
    div.stForm .stTextInput > div > div > input,
    div.stForm .stNumberInput > div > div > input,
    div.stForm .stSelectbox > div > div > select {
        border-radius: 10px;
        border: 1px solid #dddddd;
        padding: 10px;
        height: 50px;
    }
    
    div.stForm label {
        color: #1a1a1a !important;
        font-weight: 600;
    }
    
    /* Botão Principal */
    div.stForm .stButton>button {
        background-color: #007bff; /* Azul Quintes */
        color: white;
        border-radius: 50px; /* Arredondado como o botão da imagem */
        height: 55px;
        width: 100%;
        font-weight: 700;
        font-size: 1.1rem;
        border: none;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }
    
    div.stForm .stButton>button:hover {
        background-color: #0056b3; /* Azul mais escuro no hover */
        transform: translateY(-2px);
    }
    
    /* TELA DE RESULTADO (Etapa 2) */
    .valuation-box {
        text-align: center;
        margin-top: 50px;
    }
    
    .valuation-title {
        font-weight: 700;
        color: #007bff;
        font-size: 2.2rem;
        margin-bottom: 20px;
    }
    
    .valuation-value {
        font-size: 4rem;
        font-weight: 700;
        color: #1a1a1a;
        line-height: 1;
        margin-bottom: 10px;
    }
    
    .valuation-info {
        color: #555;
        font-size: 1rem;
        margin-bottom: 40px;
    }
    
    /* Título das Ofertas */
    .plans-title {
        text-align: center;
        font-weight: 700;
        font-size: 2.5rem;
        color: #1a1a1a;
        margin-bottom: 40px;
    }
    
    /* Ofertas Customizadas (Adaptando o visual dos cards da referência) */
    div[data-testid="stHorizontalBlock"] > div > div {
        background-color: #ffffff;
        border: 1px solid #eeeeee;
        border-radius: 15px;
        padding: 25px;
        text-align: center;
        transition: all 0.3s ease;
    }
    
    div[data-testid="stHorizontalBlock"] > div > div:hover {
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        transform: translateY(-5px);
        border-color: #007bff;
    }
    
    /* Botões dentro das ofertas */
    div[data-testid="stHorizontalBlock"] .stButton>button {
        background-color: #f9f9f9;
        color: #1a1a1a;
        border: 1px solid #dddddd;
        border-radius: 50px;
        margin-top: 15px;
    }
    
    div[data-testid="stHorizontalBlock"] .stButton>button:hover {
        background-color: #007bff;
        color: white;
        border-color: #007bff;
    }
    
    /* Botão Falar com Consultor */
    .special-btn > div > div > button {
        background-color: #007bff !important;
        color: white !important;
        border: none !important;
        width: 100% !important;
        margin-top: 20px !important;
        height: 50px !important;
        border-radius: 50px !important;
        font-weight: 700;
    }
    
    .special-btn > div > div > button:hover {
        background-color: #0056b3 !important;
    }
    
    </style>
    """, unsafe_allow_html=True)


# --- ETAPA 1: CAPTAÇÃO E CÁLCULO (Adaptada para o novo Layout) ---
if st.session_state.etapa == 1:
    
    # Hero Section Customizada com Logo Quintes
    st.markdown("""
        <div class="hero-container">
            <img src="https://quintes.com.br/wp-content/uploads/2023/07/Logo-Branca-Simbolo-Preto-Texto.png" class="logo-img">
            <h1 class="hero-title">Sua Análise de<br>Market Share <span>Cortesia</span></h1>
            <p class="hero-subtitle">Descubra o valuation da sua operação telecom de forma instantânea e gratuita.</p>
        </div>
    """, unsafe_allow_html=True)

    with st.form("form_captacao"):
        col1, col2 = st.columns(2)
        
        with col1:
            nome = st.text_input("Seu Nome *")
            email = st.text_input("E-mail Corporativo *")
            empresa = st.text_input("Nome do Provedor *")
        with col2:
            whatsapp = st.text_input("WhatsApp (com DDD) *")
            uf = st.selectbox("Estado", ["SP", "RJ", "MG", "PR", "SC", "RS", "Outro"])
            assinantes = st.number_input("Qtd de Assinantes", min_value=0)

        col3, col4 = st.columns(2)
        with col3:
            ebitda_anual = st.number_input("EBITDA Anual (R$)", min_value=0.0)
             churn = st.slider("Churn Rate Mensal (%)", 0.0, 10.0, 1.5)
        with col4:
            mrr = st.number_input("Receita Mensal (MRR)", min_value=0.0)
            ticket_medio = st.number_input("Ticket Médio (ARPU)", min_value=0.0)

        submit = st.form_submit_button("Gerar meu Valuation Cortesia 🚀")

        if submit:
            if not nome or not email or ebitda_anual == 0:
                st.error("Por favor, preencha os dados essenciais para o cálculo.")
            else:
                # LÓGICA DE CÁLCULO M&A
                valuation_estimado = ebitda_anual * 6 
                
                # SALVANDO NA SESSÃO
                st.session_state.dados_cliente = {
                    "nome": nome, "empresa": empresa, "whatsapp": whatsapp,
                    "ebitda": ebitda_anual, "valuation": valuation_estimado
                }
                st.session_state.etapa = 2
                st.rerun()

# --- ETAPA 2: RESULTADO E CONVERSÃO (Adaptada para o novo Layout) ---
elif st.session_state.etapa == 2:
    dados = st.session_state.dados_cliente
    
    # Animação de Sucesso
    st.balloons()
    
    # Valuation Detalhado Customizado
    st.markdown(f"""
        <div class="valuation-box">
            <h2 class="valuation-title">Valuation Estimado de {dados['empresa']}</h2>
            <div class="valuation-value">R$ {dados['valuation']:,.2f}</div>
