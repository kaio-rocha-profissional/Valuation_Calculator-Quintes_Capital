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

# --- CSS AVANÇADO (CENTRALIZAÇÃO E TRANSIÇÕES SUAVES) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap');
    
    /* 1. Animação de Entrada Suave */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); filter: blur(5px); }
        to { opacity: 1; transform: translateY(0); filter: blur(0); }
    }

    .stApp { 
        background: radial-gradient(circle at top right, #0a192f, #02060c);
        color: #FFFFFF; 
        font-family: 'Inter', sans-serif;
    }

    /* Aplica a transição lenta em toda a aplicação */
    [data-testid="stVerticalBlock"] > div {
        animation: fadeIn 1.5s ease-out forwards;
    }

    header, footer {visibility: hidden !important;}

    /* 2. Centralização Absoluta da Landing Page */
    .hero-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 85vh; /* Ocupa quase toda a tela verticalmente */
        text-align: center;
        max-width: 900px;
        margin: 0 auto;
    }

    .hero-title {
        font-weight: 800; 
        font-size: 4rem; 
        letter-spacing: -2px; 
        line-height: 1.1;
        margin-bottom: 25px; 
        background: linear-gradient(to right, #ffffff, #94a3b8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .subheadline {
        font-size: 1.3rem; 
        color: #a8b2d1; 
        margin-bottom: 45px;
        max-width: 700px;
        font-weight: 300;
        line-height: 1.6;
    }

    /* Botão com Hover Suave */
    div.stButton > button {
        background: linear-gradient(90deg, #1e40af 0%, #3b82f6 100%);
        color: white; border: none; padding: 20px 50px; border-radius: 50px;
        font-weight: 700; text-transform: uppercase; letter-spacing: 2px;
        transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 10px 30px rgba(59, 130, 246, 0.2);
    }
    div.stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 15px 40px rgba(59, 130, 246, 0.4);
        border: none; color: white;
    }

    /* 3. Estilo Iframe Fullscreen */
    .fullscreen-wrapper {
        position: fixed;
        top: 0; left: 0; width: 100vw; height: 100vh;
        z-index: 9999;
        background: #000;
        animation: fadeIn 2s ease-in-out;
    }

    /* 4. Grid de Resultados */
    .res-card {
        background: rgba(255, 255, 255, 0.02);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 30px; padding: 70px 40px; margin: 40px 0;
    }
    .res-value { font-size: 5rem; font-weight: 800; letter-spacing: -3px; }

    .offer-box {
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 20px; padding: 30px; text-align: left; height: 100%;
        transition: background 0.3s;
    }
    .offer-box:hover { background: rgba(255, 255, 255, 0.07); }

    /* Ajuste para remover paddings padrão do Streamlit */
    [data-testid="stAppViewBlockContainer"] {
        padding-top: 2rem !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- LOGICA DE NAVEGAÇÃO ---

# ETAPA 1: LANDING PAGE CENTRALIZADA
if st.session_state.etapa == 1:
    st.markdown('<div class="hero-container">', unsafe_allow_html=True)
    st.image("https://quintes.com.br/wp-content/uploads/2023/07/Logo-Branca-Simbolo-Preto-Texto.png", width=220)
    
    st.markdown("""
        <p style="color:#3b82f6; font-weight:700; letter-spacing:3px; margin-top:50px; font-size:0.9rem;">INTELIGÊNCIA EM M&A</p>
        <h1 class="hero-title">Quanto vale o esforço<br>de uma vida inteira?</h1>
        <p class="subheadline">Descubra o valor de mercado real da sua empresa com a metodologia utilizada pelas maiores boutiques de investimento do país.</p>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,1.5,1])
    with col2:
        if st.button("INICIAR VALUATION AGORA"):
            st.session_state.etapa = 2
            st.rerun()
            
    st.markdown('<p style="margin-top:60px; color:#475569; font-size:0.8rem; letter-spacing:1px;">CONFIANÇA • PRECISÃO • SIGILO</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ETAPA 2: FORMULÁRIO EM TELA CHEIA (FULLSCREEN)
elif st.session_state.etapa == 2:
    # Remove qualquer margem para o iframe dominar a tela
    st.markdown("""
        <style>
            [data-testid="stAppViewBlockContainer"] { padding: 0 !important; max-width: 100% !important; }
            .stMain { background-color: #000 !important; }
        </style>
    """, unsafe_allow_html=True)
    
    fillout_url = "https://forms.fillout.com/t/1qwGDDvuKKus"
    
    st.components.v1.html(f"""
        <div class="fullscreen-wrapper">
            <iframe src="{fillout_url}" 
                    style="width:100%; height:100%; border:none; margin:0; padding:0; overflow:hidden;"
                    allow="camera; microphone; geolocation">
            </iframe>
        </div>
    """, height=1000) # height alto para garantir o preenchimento

# ETAPA 3: RESULTADO (MANTÉM O PADRÃO PREMIUM)
elif st.session_state.etapa == 3:
    ebitda = float(st.query_params.get("ebitda", 0))
    empresa = st.query_params.get("empresa", "Sua Empresa")
    valuation = ebitda * 6

    st.markdown('<div class="hero-container" style="min-height: auto; padding-top: 50px;">', unsafe_allow_html=True)
    st.image("https://quintes.com.br/wp-content/uploads/2023/07/Logo-Branca-Simbolo-Preto-Texto.png", width=140)
    
    st.markdown(f"""
        <div class="res-card">
            <div style="color: #3b82f6; font-weight:700; letter-spacing:3px; text-transform:uppercase; font-size:0.8rem; margin-bottom:20px;">Resultado Estimado • {empresa}</div>
            <div class="res-value"><span style="font-size:2rem; color:#64748b; vertical-align:middle; margin-right:10px;">R$</span>{valuation:,.0f}</div>
            <div style="color:#64748b; font-size:1.1rem; margin-top:20px; font-weight:400;">Cálculo baseado em Múltiplo Setorial de 6.0x EBITDA</div>
        </div>
        <h2 style="font-size:2rem; font-weight:700; margin-bottom:40px;">Como deseja proceder com este valuation?</h2>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="offer-box"><h3>Relatório Completo</h3><p>Receba o book financeiro detalhado com múltiplos do seu setor.</p></div>', unsafe_allow_html=True)
        st.button("BAIXAR PDF", key="opt1")
    with c2:
        st.markdown('<div class="offer-box"><h3>Plataforma M&A</h3><p>Monitore o valor da sua empresa mensalmente com nosso software.</p></div>', unsafe_allow_html=True)
        st.button("VER DASHBOARD", key="opt2")
    with c3:
        st.markdown('<div class="offer-box"><h3>Consultoria</h3><p>Agende uma conversa estratégica com um advisor de fusões e aquisições.</p></div>', unsafe_allow_html=True)
        st.button("AGENDAR CALL", key="opt3")

    st.markdown('<br><br>', unsafe_allow_html=True)
    if st.button("REFAZER DIAGNÓSTICO", type="secondary"):
        st.query_params.clear()
        st.session_state.etapa = 1
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
