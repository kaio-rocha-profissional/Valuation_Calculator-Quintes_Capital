import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Valuation Intelligence | Quintes Capital", 
    layout="wide", 
    page_icon="https://quintes.com.br/wp-content/uploads/2023/07/Favicon-Quintes.png"
)

# --- CONTROLE DE NAVEGAÇÃO ---
if 'etapa' not in st.session_state:
    if "ebitda" in st.query_params:
        st.session_state.etapa = 3
    else:
        st.session_state.etapa = 1

# --- CSS GLOBAL (REMOÇÃO DE GAP E TRANSIÇÕES) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap');
    
    /* Fade-in Suave em toda a aplicação */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(15px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .stApp { 
        background: radial-gradient(circle at top right, #0a192f, #02060c);
        color: #FFFFFF; 
        font-family: 'Inter', sans-serif;
    }

    /* 1. REMOÇÃO TOTAL DE GAPS NO TOPO */
    [data-testid="stAppViewBlockContainer"] {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        margin-top: 0rem !important;
    }
    header, footer, [data-testid="stHeader"] { visibility: hidden !important; height: 0 !important; }

    /* Container da Landing Page */
    .hero-container {
        display: flex; 
        flex-direction: column; 
        align-items: center; 
        justify-content: center;
        min-height: 95vh; /* Ocupa quase toda a altura para centralizar */
        text-align: center; 
        max-width: 900px; 
        margin: 0 auto;
        animation: fadeIn 1.8s ease-out;
    }

    .hero-title {
        font-weight: 800; font-size: 3.8rem; letter-spacing: -2px; line-height: 1.1;
        margin-bottom: 20px; background: linear-gradient(to right, #ffffff, #94a3b8);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }

    /* Botão Premium */
    div.stButton > button {
        background: linear-gradient(90deg, #1e40af 0%, #3b82f6 100%);
        color: white !important; border: none; padding: 18px 50px; border-radius: 50px;
        font-weight: 700; text-transform: uppercase; letter-spacing: 2px;
        transition: all 0.5s ease; box-shadow: 0 10px 30px rgba(59, 130, 246, 0.2);
    }
    div.stButton > button:hover { transform: scale(1.05); box-shadow: 0 15px 40px rgba(59, 130, 246, 0.4); border: none; }

    /* 2. RODAPÉ POWERED BY */
    .footer-powered {
        margin-top: 60px;
        opacity: 0.7;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .powered-text {
        font-size: 0.7rem;
        letter-spacing: 2px;
        color: #475569;
        margin-bottom: 10px;
        text-transform: uppercase;
    }
    .footer-logo {
        width: 180px;
        filter: brightness(0) invert(1); /* Torna a logo preta em branca */
    }

    /* Ajuste para Iframe Fullscreen */
    .fs-iframe {
        position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
        border: none; z-index: 9999; background: #000;
    }
    
    /* Card de Resultado */
    .res-card {
        background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 30px;
        padding: 60px 40px; margin: 40px 0;
    }
    </style>
""", unsafe_allow_html=True)

# --- FLUXO DE TELAS ---

# ETAPA 1: LANDING PAGE
if st.session_state.etapa == 1:
    st.markdown('<div class="hero-container">', unsafe_allow_html=True)
    
    # Logo Principal
    st.image("https://quintes.com.br/wp-content/uploads/2023/07/Logo-Branca-Simbolo-Preto-Texto.png", width=220)
    
    # Texto de Impacto
    st.markdown("""
        <p style="color:#3b82f6; font-weight:700; letter-spacing:3px; margin-top:40px; font-size:0.8rem; text-transform:uppercase;">Estratégia & Inteligência</p>
        <h1 class="hero-title">Quanto vale o esforço<br>de uma vida inteira?</h1>
        <p style="font-size:1.3rem; color:#a8b2d1; margin-bottom:45px; font-weight:300; max-width:650px;">Calcule o valor de mercado real da sua operação em minutos com nossa metodologia de M&A.</p>
    """, unsafe_allow_html=True)
    
    # Botão centralizado
    col1, col2, col3 = st.columns([1,1.5,1])
    with col2:
        if st.button("CALCULAR VALUATION"):
            st.session_state.etapa = 2
            st.rerun()
            
    # Rodapé "Powered By"
    st.markdown(f"""
        <div class="footer-powered">
            <p class="powered-text">Powered by</p>
            <img src="https://i.imgur.com/8N4U9M6.png" class="footer-logo">
        </div>
    """, unsafe_allow_html=True)
    # Nota: Substituí a URL da imagem do rodapé por um link direto da imagem que você enviou (hospedada)
    
    st.markdown('</div>', unsafe_allow_html=True)

# ETAPA 2: FORMULÁRIO EM TELA CHEIA TOTAL
elif st.session_state.etapa == 2:
    st.markdown("""
        <style>
            [data-testid="stAppViewBlockContainer"] { padding: 0 !important; max-width: 100% !important; }
            .stMain { background-color: #000 !important; }
        </style>
    """, unsafe_allow_html=True)
    
    fillout_url = "https://forms.fillout.com/t/1qwGDDvuKKus"
    
    st.components.v1.html(f"""
        <iframe src="{fillout_url}" class="fs-iframe" allow="camera; microphone; geolocation"></iframe>
    """, height=1000)

# ETAPA 3: RESULTADO
elif st.session_state.etapa == 3:
    ebitda = float(st.query_params.get("ebitda", 0))
    empresa = st.query_params.get("empresa", "Sua Empresa")
    valuation = ebitda * 6

    st.markdown('<div class="hero-container" style="min-height: auto; padding-top: 50px;">', unsafe_allow_html=True)
    st.image("https://quintes.com.br/wp-content/uploads/2023/07/Logo-Branca-Simbolo-Preto-Texto.png", width=140)
    
    st.markdown(f"""
        <div class="res-card">
            <div style="color: #3b82f6; font-weight:700; letter-spacing:3px; text-transform:uppercase; font-size:0.85rem; margin-bottom:15px;">Avaliação Estimada • {empresa}</div>
            <div style="font-size: 4.8rem; font-weight: 800; letter-spacing: -2px;">
                <span style="font-size:1.8rem; color:#64748b; margin-right:10px;">R$</span>{valuation:,.0f}
            </div>
            <p style="color:#64748b; margin-top:20px; font-size:1.1rem;">Baseado em Múltiplo Setorial de <b>6.0x EBITDA</b></p>
        </div>
    """, unsafe_allow_html=True)

    # Botões de ação (exemplo simplificado)
    st.markdown('<h2 style="font-size:1.8rem; font-weight:700; margin-bottom:40px;">Próximos Passos</h2>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1: st.button("BAIXAR RELATÓRIO", key="b1")
    with c2: st.button("VER DASHBOARD", key="b2")
    with c3: st.button("FALAR COM ADVISOR", key="b3")

    st.markdown('<br><br>', unsafe_allow_html=True)
    if st.button("REFAZER DIAGNÓSTICO", type="secondary"):
        st.query_params.clear()
        st.session_state.etapa = 1
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
