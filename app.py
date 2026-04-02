import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Valuation Intelligence | Quintes Capital", 
    layout="centered", 
    page_icon="https://quintes.com.br/wp-content/uploads/2023/07/Favicon-Quintes.png"
)

# --- CONTROLE DE NAVEGAÇÃO ---
if 'etapa' not in st.session_state:
    if "ebitda" in st.query_params:
        st.session_state.etapa = 3
    else:
        st.session_state.etapa = 1

# --- CSS CORPORATIVO PREMIUM ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&family=Playfair+Display:wght@700&display=swap');
    
    /* Fundo com Gradiente Sofisticado */
    .stApp { 
        background: radial-gradient(circle at top right, #0a192f, #02060c);
        color: #FFFFFF; 
        font-family: 'Inter', sans-serif; 
    }
    
    header, footer {visibility: hidden;}

    .main-container {
        max-width: 800px;
        margin: 0 auto;
        padding: 40px 20px;
        text-align: center;
    }

    /* Headlines de Impacto */
    .hero-title {
        font-family: 'Inter', sans-serif;
        font-weight: 800;
        font-size: 3.5rem;
        letter-spacing: -2px;
        line-height: 1;
        margin-bottom: 20px;
        background: linear-gradient(to bottom right, #FFFFFF 30%, #99aab5 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .subheadline {
        font-size: 1.2rem;
        font-weight: 300;
        line-height: 1.6;
        color: #a8b2d1;
        margin-bottom: 40px;
        max-width: 600px;
        margin-left: auto;
        margin-right: auto;
    }

    /* Botão Premium (Ação Principal) */
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #1e40af 0%, #3b82f6 100%);
        color: white;
        border: none;
        padding: 18px 40px;
        border-radius: 50px;
        font-weight: 700;
        font-size: 1.1rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: all 0.3s ease;
        box-shadow: 0 10px 20px rgba(59, 130, 246, 0.3);
        width: 100%;
        margin-top: 20px;
    }
    div.stButton > button:first-child:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 30px rgba(59, 130, 246, 0.5);
        border: none;
        color: white;
    }

    /* Card de Resultado Glassmorphism */
    .res-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 24px;
        padding: 60px 40px;
        margin: 40px 0;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
    }
    .res-label { 
        color: #3b82f6; 
        font-size: 0.8rem; 
        font-weight: 700; 
        text-transform: uppercase; 
        letter-spacing: 3px; 
        margin-bottom: 10px;
    }
    .res-value { 
        font-size: 4.5rem; 
        font-weight: 800; 
        color: #FFFFFF; 
        margin: 0;
        letter-spacing: -2px;
    }
    .res-currency { font-size: 1.5rem; vertical-align: top; margin-right: 5px; color: #64748b; }

    /* Grid de Ofertas Corporativas */
    .offer-grid {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        gap: 20px;
        margin-top: 30px;
    }
    .offer-box {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 24px;
        text-align: left;
        transition: 0.3s;
    }
    .offer-box:hover { background: rgba(255, 255, 255, 0.08); }
    .offer-box h3 { font-size: 1rem; color: #FFFFFF; margin-bottom: 10px; font-weight: 600; }
    .offer-box p { font-size: 0.8rem; color: #8892b0; margin-bottom: 0; line-height: 1.4; }

    /* Trust Badges */
    .trust-section {
        margin-top: 60px;
        padding-top: 30px;
        border-top: 1px solid rgba(255, 255, 255, 0.1);
    }
    .trust-text { color: #475569; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 2px; }

    </style>
""", unsafe_allow_html=True)

# --- FLUXO DE TELAS ---

with st.container():
    # PÁGINA 1: LANDING PAGE (CORP IMPACT)
    if st.session_state.etapa == 1:
        st.markdown('<div class="main-container">', unsafe_allow_html=True)
        st.image("https://quintes.com.br/wp-content/uploads/2023/07/Logo-Branca-Simbolo-Preto-Texto.png", width=180)
        
        st.markdown('<p style="color:#3b82f6; font-weight:700; letter-spacing:2px; margin-bottom:10px;">EXCLUSIVO PARA EMPRESÁRIOS</p>', unsafe_allow_html=True)
        st.markdown('<h1 class="hero-title">Quanto vale o esforço de uma vida?</h1>', unsafe_allow_html=True)
        st.markdown('<p class="subheadline">Pare de estimar. Comece a gerir. Utilize nossa inteligência de M&A para descobrir o valor de mercado real da sua operação em menos de 3 minutos.</p>', unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            if st.button("CALCULAR MEU VALUATION"):
                st.session_state.etapa = 2
                st.rerun()
        
        st.markdown("""
            <div class="trust-section">
                <p class="trust-text">Metodologia baseada em transações reais de mercado</p>
                <div style="opacity: 0.5; filter: grayscale(1); margin-top:15px; font-size: 0.9rem;">
                    🔒 Protocolo de Segurança de Dados LGPD
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # PÁGINA 2: FORMULÁRIO (CLEAN FRAME)
    elif st.session_state.etapa == 2:
        st.markdown('<div style="text-align:center; padding: 20px 0;">', unsafe_allow_html=True)
        st.image("https://quintes.com.br/wp-content/uploads/2023/07/Logo-Branca-Simbolo-Preto-Texto.png", width=120)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # O link do seu form real
        fillout_url = "https://forms.fillout.com/t/1qwGDDvuKKus"
        st.components.v1.iframe(fillout_url, height=650, scrolling=True)
        
        if st.button("← CANCELAR E VOLTAR"):
            st.session_state.etapa = 1
            st.rerun()

    # PÁGINA 3: RESULTADO (VIBE DE "REUNIÃO DE DIRETORIA")
    elif st.session_state.etapa == 3:
        ebitda = float(st.query_params.get("ebitda", 0))
        empresa = st.query_params.get("empresa", "Sua Empresa")
        valuation = ebitda * 6

        st.markdown('<div class="main-container" style="padding-top:20px;">', unsafe_allow_html=True)
        st.image("https://quintes.com.br/wp-content/uploads/2023/07/Logo-Branca-Simbolo-Preto-Texto.png", width=120)
        
        st.markdown(f"""
            <div class="res-card">
                <div class="res-label">Estimativa de Valor de Mercado • {empresa}</div>
                <div class="res-value"><span class="res-currency">R$</span>{valuation:,.0f}</div>
                <div style="color:#64748b; font-size:1rem; margin-top:15px; font-weight:500;">
                    Baseado em Múltiplo Setorial de 6.0x EBITDA
                </div>
            </div>
            <h2 style="font-size:1.8rem; font-weight:700; margin-bottom:30px;">O que este número significa para você?</h2>
        """, unsafe_allow_html=True)

        # Três colunas para os Próximos Passos (Estratégico)
        c1, c2, c3 = st.columns(3)
        
        with c1:
            st.markdown('<div class="offer-box"><h3>Relatório Premium</h3><p>Análise completa de indicadores financeiros e benchmarks.</p></div>', unsafe_allow_html=True)
            st.button("RECEBER PDF", key="opt1")
            
        with c2:
            st.markdown('<div class="offer-box"><h3>Plataforma M&A</h3><p>Acompanhe o valor da sua empresa em tempo real (SaaS).</p></div>', unsafe_allow_html=True)
            st.button("ACESSAR DASH", key="opt2")
            
        with c3:
            st.markdown('<div class="offer-box"><h3>Special Advisor</h3><p>Consultoria estratégica para preparar saída ou venda.</p></div>', unsafe_allow_html=True)
            st.button("AGENDAR CALL", key="opt3")

        st.markdown('<br><br>', unsafe_allow_html=True)
        if st.button("REFAZER ANÁLISE", type="secondary"):
            st.query_params.clear()
            st.session_state.etapa = 1
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
