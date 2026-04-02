import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Valuation Cortesia | Quintes Capital", 
    layout="centered", 
    page_icon="https://quintes.com.br/wp-content/uploads/2023/07/Favicon-Quintes.png"
)

# --- CONTROLE DE NAVEGAÇÃO ---
if 'etapa' not in st.session_state:
    # Se já vier com parâmetro na URL, pula pro resultado (Etapa 3)
    if "ebitda" in st.query_params:
        st.session_state.etapa = 3
    else:
        st.session_state.etapa = 1

# --- CSS DARK MODE PREMIUM ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    /* Fundo Dark Profundo */
    .stApp { 
        background-color: #0b0e11; 
        color: #ffffff; 
        font-family: 'Poppins', sans-serif; 
    }
    
    /* Hero Section */
    .hero-container { text-align: center; padding: 60px 0 30px 0; }
    .logo-img { width: 200px; margin-bottom: 30px; filter: brightness(0) invert(1); }
    
    .hero-title { 
        color: #ffffff; 
        font-weight: 700; 
        font-size: 2.8rem; 
        line-height: 1.2;
        margin-bottom: 20px;
    }
    .hero-subtitle { 
        color: #a0a0a0; 
        font-size: 1.2rem; 
        max-width: 650px; 
        margin: 0 auto 40px auto;
        line-height: 1.6;
    }

    /* Botão Customizado */
    .stButton > button {
        background: linear-gradient(90deg, #007bff 0%, #0056b3 100%);
        color: white;
        border: none;
        padding: 15px 30px;
        border-radius: 50px;
        font-weight: 700;
        font-size: 1.1rem;
        transition: 0.3s;
        width: 100%;
    }
    .stButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0 10px 20px rgba(0,123,255,0.3);
    }

    /* Card de Resultado */
    .valuation-card {
        background: #161b22;
        border: 1px solid #30363d;
        border-radius: 20px;
        padding: 50px 20px;
        text-align: center;
        margin-bottom: 40px;
    }
    .valuation-value { 
        font-size: 4rem; 
        font-weight: 800; 
        color: #007bff; 
        text-shadow: 0 0 15px rgba(0,123,255,0.4);
    }

    /* Cards de Oferta */
    .offer-card {
        background: #161b22;
        border: 1px solid #30363d;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        height: 250px;
        transition: 0.3s;
    }
    .offer-card:hover { border-color: #007bff; background: #1c2128; }
    .offer-card h3 { color: #007bff; font-size: 1.2rem; margin-bottom: 10px; }
    .offer-card p { color: #8b949e; font-size: 0.9rem; }

    /* Esconder elementos padrão do Streamlit */
    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- PÁGINA 1: LANDING PAGE ---
if st.session_state.etapa == 1:
    st.markdown("""
        <div class="hero-container">
            <img src="https://quintes.com.br/wp-content/uploads/2023/07/Logo-Branca-Simbolo-Preto-Texto.png" class="logo-img">
            <h1 class="hero-title">Descubra o valor da sua empresa em poucos minutos</h1>
            <p class="hero-subtitle">
                Tomar decisões sem saber o valor da sua empresa é como atirar no escuro. 
                Melhore a sua visão empresarial e tenha muito mais resultado realizando o valuation do seu negócio.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("COMEÇAR VALUATION AGORA 🚀"):
        st.session_state.etapa = 2
        st.rerun()

# --- PÁGINA 2: FORMULÁRIO FILLOUT ---
elif st.session_state.etapa == 2:
    st.markdown("""
        <div style="text-align:center; padding-top:20px;">
            <img src="https://quintes.com.br/wp-content/uploads/2023/07/Logo-Branca-Simbolo-Preto-Texto.png" style="width:120px; margin-bottom:20px; filter: brightness(0) invert(1);">
            <h2 style="color:#ffffff;">Análise de Dados</h2>
            <p style="color:#a0a0a0;">Insira as informações da sua operação abaixo.</p>
        </div>
    """, unsafe_allow_html=True)
    
    fillout_url = "https://forms.fillout.com/t/1qwGDDvuKKus"
    st.components.v1.iframe(fillout_url, height=650, scrolling=True)
    
    if st.button("← Voltar"):
        st.session_state.etapa = 1
        st.rerun()

# --- PÁGINA 3: RESULTADO ---
elif st.session_state.etapa == 3:
    # Pegando dados da URL
    ebitda = float(st.query_params.get("ebitda", 0))
    empresa = st.query_params.get("empresa", "Sua Empresa")
    valuation_final = ebitda * 6

    st.markdown(f"""
        <div class="hero-container" style="padding-top:20px;">
            <img src="https://quintes.com.br/wp-content/uploads/2023/07/Logo-Branca-Simbolo-Preto-Texto.png" class="logo-img">
        </div>
        <div class="valuation-card">
            <div style="text-transform:uppercase; color:#8b949e; letter-spacing:2px; font-size:0.8rem;">Valuation Estimado | {empresa}</div>
            <div class="valuation-value">R$ {valuation_final:,.2f}</div>
            <p style="color:#58a6ff;">Múltiplo de 6.0x aplicado sobre o EBITDA informado.</p>
        </div>
        <h3 style="text-align:center; margin-bottom:30px;">O que você deseja fazer agora?</h3>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="offer-card"><h3>📄 Relatório</h3><p>Análise detalhada em PDF para sua diretoria.</p></div>', unsafe_allow_html=True)
        st.button("Obter PDF", key="p3_1")
    with c2:
        st.markdown('<div class="offer-card"><h3>💻 Dashboard</h3><p>Acesso ao software de acompanhamento mensal.</p></div>', unsafe_allow_html=True)
        st.button("Assinar SaaS", key="p3_2")
    with c3:
        st.markdown('<div class="offer-card"><h3>🤝 M&A Advisor</h3><p>Conversar com especialista sobre venda da empresa.</p></div>', unsafe_allow_html=True)
        st.button("Falar com Consultor", key="p3_3")

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Nova Consulta"):
        st.query_params.clear()
        st.session_state.etapa = 1
        st.rerun()
