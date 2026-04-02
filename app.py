import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Valuation Intelligence | Quintes Capital", 
    layout="wide", # Mudamos para wide para permitir o tela cheia, controlamos o 'centered' via CSS
    page_icon="https://quintes.com.br/wp-content/uploads/2023/07/Favicon-Quintes.png"
)

# --- CONTROLE DE NAVEGAÇÃO ---
if 'etapa' not in st.session_state:
    if "ebitda" in st.query_params:
        st.session_state.etapa = 3
    else:
        st.session_state.etapa = 1

# --- CSS BASE (CORPORATIVO) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap');
    
    .stApp { 
        background: radial-gradient(circle at top right, #0a192f, #02060c);
        color: #FFFFFF; 
        font-family: 'Inter', sans-serif; 
    }
    
    header, footer {visibility: hidden !important;}

    /* Container para páginas centralizadas (Landing e Resultado) */
    .centered-wrapper {
        max-width: 800px;
        margin: 0 auto;
        padding: 40px 20px;
        text-align: center;
    }

    .hero-title {
        font-weight: 800; font-size: 3.5rem; letter-spacing: -2px; line-height: 1;
        margin-bottom: 20px; color: white;
    }

    .subheadline {
        font-size: 1.2rem; color: #a8b2d1; margin-bottom: 40px;
    }

    /* Botão Premium */
    div.stButton > button {
        background: linear-gradient(90deg, #1e40af 0%, #3b82f6 100%);
        color: white; border: none; padding: 18px 40px; border-radius: 50px;
        font-weight: 700; text-transform: uppercase; letter-spacing: 1px;
        transition: all 0.3s ease; width: 100%;
    }

    /* Estilo para o Iframe em Tela Cheia */
    .fullscreen-frame {
        position: fixed;
        top: 0;
        left: 0;
        bottom: 0;
        right: 0;
        width: 100%;
        height: 100%;
        border: none;
        margin: 0;
        padding: 0;
        overflow: hidden;
        z-index: 999999;
    }

    /* Card de Resultado */
    .res-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 24px; padding: 60px 40px; margin: 40px 0;
    }
    .res-value { font-size: 4.5rem; font-weight: 800; color: #FFFFFF; letter-spacing: -2px; }

    .offer-box {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px; padding: 24px; text-align: left; height: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# --- FLUXO DE TELAS ---

# PÁGINA 1: LANDING PAGE
if st.session_state.etapa == 1:
    st.markdown('<div class="centered-wrapper">', unsafe_allow_html=True)
    st.image("https://quintes.com.br/wp-content/uploads/2023/07/Logo-Branca-Simbolo-Preto-Texto.png", width=180)
    st.markdown('<p style="color:#3b82f6; font-weight:700; letter-spacing:2px; margin-top:40px;">EXCLUSIVO PARA EMPRESÁRIOS</p>', unsafe_allow_html=True)
    st.markdown('<h1 class="hero-title">Quanto vale o esforço de uma vida?</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subheadline">Utilize nossa inteligência de M&A para descobrir o valor de mercado real da sua operação.</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("CALCULAR MEU VALUATION"):
            st.session_state.etapa = 2
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# PÁGINA 2: FORMULÁRIO EM TELA CHEIA
elif st.session_state.etapa == 2:
    # CSS específico para remover as margens do Streamlit nesta etapa
    st.markdown("""
        <style>
            [data-testid="stAppViewBlockContainer"] {
                padding: 0 !important;
                max-width: 100% !important;
            }
            .stMain {
                background-color: #000000 !important;
            }
            /* Esconde o botão de 'Deploy' e menu do Streamlit se aparecerem */
            #MainMenu {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)
    
    # O link do seu formulário Fillout
    fillout_url = "https://forms.fillout.com/t/1qwGDDvuKKus"
    
    # Usando HTML puro para garantir o "Full Screen" dentro do container
    st.components.v1.html(f"""
        <iframe src="{fillout_url}" 
                style="position:fixed; top:0; left:0; width:100%; height:100%; border:none; margin:0; padding:0; overflow:hidden; z-index:999999;"
                allow="camera; microphone; geolocation">
        </iframe>
    """, height=800) # O height aqui é um fallback, o CSS fixo domina

# PÁGINA 3: RESULTADO
elif st.session_state.etapa == 3:
    ebitda = float(st.query_params.get("ebitda", 0))
    empresa = st.query_params.get("empresa", "Sua Empresa")
    valuation = ebitda * 6

    st.markdown('<div class="centered-wrapper">', unsafe_allow_html=True)
    st.image("https://quintes.com.br/wp-content/uploads/2023/07/Logo-Branca-Simbolo-Preto-Texto.png", width=120)
    
    st.markdown(f"""
        <div class="res-card">
            <div style="color: #3b82f6; font-weight:700; letter-spacing:2px; text-transform:uppercase; font-size:0.8rem;">Estimativa de Valor • {empresa}</div>
            <div class="res-value"><span style="font-size:1.5rem; color:#64748b;">R$</span>{valuation:,.0f}</div>
            <div style="color:#64748b; font-size:1rem; margin-top:15px;">Baseado em Múltiplo Setorial de 6.0x EBITDA</div>
        </div>
        <h2 style="font-size:1.8rem; font-weight:700; margin-bottom:30px;">O que este número significa para você?</h2>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="offer-box"><h3>Relatório Premium</h3><p>Análise completa de indicadores financeiros.</p></div>', unsafe_allow_html=True)
        st.button("RECEBER PDF", key="opt1")
    with c2:
        st.markdown('<div
