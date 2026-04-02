import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Valuation Intelligence | Quintes Capital", 
    layout="wide", # Permite usar a largura total
    page_icon="https://quintes.com.br/wp-content/uploads/2023/07/Favicon-Quintes.png"
)

# --- CONTROLE DE NAVEGAÇÃO ---
if 'etapa' not in st.session_state:
    if "ebitda" in st.query_params:
        st.session_state.etapa = 3
    else:
        st.session_state.etapa = 1

# --- CSS GLOBAL E ANIMAÇÕES ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap');
    
    /* Fade-in Suave */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .stApp { 
        background: radial-gradient(circle at top right, #0a192f, #02060c);
        color: #FFFFFF; 
        font-family: 'Inter', sans-serif;
    }

    /* Remove elementos padrão do Streamlit */
    header, footer, [data-testid="stHeader"] { visibility: hidden !important; height: 0 !important; }

    /* Estilo de Transição para os blocos */
    .stVerticalBlock {
        animation: fadeIn 1.2s ease-out;
    }

    /* Centralização da Landing Page */
    .hero-container {
        display: flex; flex-direction: column; align-items: center; justify-content: center;
        min-height: 80vh; text-align: center; max-width: 900px; margin: 0 auto;
    }

    .hero-title {
        font-weight: 800; font-size: 3.8rem; letter-spacing: -2px; line-height: 1.1;
        margin-bottom: 20px; background: linear-gradient(to right, #ffffff, #94a3b8);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }

    /* Botão Premium */
    div.stButton > button {
        background: linear-gradient(90deg, #1e40af 0%, #3b82f6 100%);
        color: white; border: none; padding: 18px 45px; border-radius: 50px;
        font-weight: 700; text-transform: uppercase; letter-spacing: 2px;
        transition: all 0.4s ease; box-shadow: 0 10px 30px rgba(59, 130, 246, 0.2);
    }
    div.stButton > button:hover { transform: translateY(-3px); box-shadow: 0 15px 40px rgba(59, 130, 246, 0.4); border: none; color: white; }

    /* CARD DE RESULTADO */
    .res-card {
        background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 30px;
        padding: 60px 40px; margin: 40px 0;
    }
    .res-value { font-size: 4.5rem; font-weight: 800; letter-spacing: -2px; }

    /* BOX DE OFERTAS */
    .offer-box {
        background: rgba(255, 255, 255, 0.04); border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 15px; padding: 25px; text-align: left; height: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# --- LOGICA DE NAVEGAÇÃO ---

# ETAPA 1: LANDING PAGE CENTRALIZADA
if st.session_state.etapa == 1:
    st.markdown('<div class="hero-container">', unsafe_allow_html=True)
    st.image("https://quintes.com.br/wp-content/uploads/2023/07/Logo-Branca-Simbolo-Preto-Texto.png", width=200)
    
    st.markdown("""
        <p style="color:#3b82f6; font-weight:700; letter-spacing:3px; margin-top:40px; font-size:0.8rem;">ESTRATÉGIA CORPORATIVA</p>
        <h1 class="hero-title">Quanto vale o esforço<br>de uma vida inteira?</h1>
        <p style="font-size:1.2rem; color:#a8b2d1; margin-bottom:40px; font-weight:300; max-width:650px;">Descubra o valor de mercado real da sua empresa com inteligência de dados e metodologia de M&A.</p>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,1.5,1])
    with col2:
        if st.button("INICIAR VALUATION"):
            st.session_state.etapa = 2
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# ETAPA 2: FORMULÁRIO EM TELA CHEIA (SEM RECORTE)
elif st.session_state.etapa == 2:
    # ESTA É A CHAVE: Removemos todos os paddings do Streamlit para esta tela específica
    st.markdown("""
        <style>
            /* Remove margens e preenchimentos do container principal do Streamlit */
            [data-testid="stAppViewBlockContainer"] {
                padding: 0 !important;
                max-width: 100% !important;
                margin: 0 !important;
            }
            /* Remove espaços extras no topo */
            [data-testid="stMainViewContainer"] {
                padding-top: 0 !important;
            }
            /* Garante que o iframe ocupe a altura total da janela */
            iframe {
                height: 100vh !important;
                width: 100vw !important;
                border: none !important;
            }
        </style>
    """, unsafe_allow_html=True)
    
    fillout_url = "https://forms.fillout.com/t/1qwGDDvuKKus"
    
    # Renderiza o iframe ocupando toda a viewport
    st.components.v1.iframe(fillout_url, height=0) # O height 0 é ignorado pelo CSS acima que força 100vh

# ETAPA 3: RESULTADO
elif st.session_state.etapa == 3:
    ebitda = float(st.query_params.get("ebitda", 0))
    empresa = st.query_params.get("empresa", "Sua Empresa")
    valuation = ebitda * 6

    st.markdown('<div class="hero-container" style="min-height: auto; padding-top: 40px; max-width: 1000px;">', unsafe_allow_html=True)
    st.image("https://quintes.com.br/wp-content/uploads/2023/07/Logo-Branca-Simbolo-Preto-Texto.png", width=140)
    
    st.markdown(f"""
        <div class="res-card">
            <div style="color: #3b82f6; font-weight:700; letter-spacing:3px; text-transform:uppercase; font-size:0.8rem; margin-bottom:15px;">Avaliação Estimada • {empresa}</div>
            <div class="res-value"><span style="font-size:1.8rem; color:#64748b; margin-right:10px;">R$</span>{valuation:,.0f}</div>
            <p style="color:#64748b; margin-top:20px;">Múltiplo de Saída Estimado: <b>6.0x EBITDA</b></p>
        </div>
        <h2 style="font-size:1.8rem; font-weight:700; margin-bottom:40px; color: #fff;">Próximos Passos Estratégicos</h2>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="offer-box"><h3>Relatório Completo</h3><p style="font-size:0.9rem; color:#8892b0;">Receba o book financeiro com benchmarks setoriais.</p></div>', unsafe_allow_html=True)
        st.button("BAIXAR PDF", key="opt1")
    with c2:
        st.markdown('<div class="offer-box"><h3>Plataforma M&A</h3><p style="font-size:0.9rem; color:#8892b0;">Monitore o valor da sua empresa em tempo real.</p></div>', unsafe_allow_html=True)
        st.button("VER DASH", key="opt2")
    with c3:
        st.markdown('<div class="offer-box"><h3>Advisor Especialista</h3><p style="font-size:0.9rem; color:#8892b0;">Fale com um consultor sobre a venda da operação.</p></div>', unsafe_allow_html=True)
        st.button("AGENDAR", key="opt3")

    st.markdown('<br><br>', unsafe_allow_html=True)
    if st.button("REFAZER VALUATION", type="secondary"):
        st.query_params.clear()
        st.session_state.etapa = 1
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
