import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Valuation | Quintes Capital", 
    layout="centered", 
    page_icon="https://quintes.com.br/wp-content/uploads/2023/07/Favicon-Quintes.png"
)

# --- CONTROLE DE NAVEGAÇÃO ---
if 'etapa' not in st.session_state:
    if "ebitda" in st.query_params:
        st.session_state.etapa = 3
    else:
        st.session_state.etapa = 1

# --- CSS IDENTICO AO FILLOUT (DARK MODE) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Fundo e Fonte Principal */
    .stApp { 
        background-color: #000000; 
        color: #FFFFFF; 
        font-family: 'Inter', sans-serif; 
    }
    
    /* Esconder headers e footers padrão */
    header, footer {visibility: hidden;}
    
    .main-container {
        max-width: 600px;
        margin: 0 auto;
        padding-top: 50px;
        text-align: center;
    }

    .logo-img { width: 140px; margin-bottom: 40px; filter: brightness(0) invert(1); }

    /* Headline Estilo Fillout */
    .headline {
        font-size: 2.2rem;
        font-weight: 700;
        line-height: 1.2;
        margin-bottom: 24px;
        color: #FFFFFF;
    }

    .subheadline {
        font-size: 1.1rem;
        font-weight: 400;
        line-height: 1.6;
        color: #999999;
        margin-bottom: 40px;
    }

    /* Botão Estilo Fillout (Azul Vibrante) */
    .stButton > button {
        background-color: #3182CE;
        color: #FFFFFF;
        border: none;
        padding: 12px 24px;
        border-radius: 8px;
        font-weight: 600;
        font-size: 1rem;
        width: 100%;
        transition: background 0.2s ease;
        height: 50px;
    }
    .stButton > button:hover {
        background-color: #2B6CB0;
        border: none;
        color: white;
    }

    /* Card de Resultado (Clean & Dark) */
    .res-card {
        background-color: #111111;
        border: 1px solid #333333;
        border-radius: 12px;
        padding: 40px 20px;
        margin: 20px 0;
    }
    .res-label { color: #999999; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 1px; }
    .res-value { font-size: 3.5rem; font-weight: 700; color: #FFFFFF; margin: 15px 0; }
    
    /* Grid de Ofertas */
    .offer-box {
        background-color: #111111;
        border: 1px solid #222222;
        border-radius: 12px;
        padding: 20px;
        text-align: left;
        margin-bottom: 15px;
    }
    .offer-box h3 { font-size: 1.1rem; color: #3182CE; margin-bottom: 8px; }
    .offer-box p { font-size: 0.85rem; color: #777; margin-bottom: 0; }

    </style>
""", unsafe_allow_html=True)

# --- FLUXO DE TELAS ---

with st.container():
    # PÁGINA 1: LANDING PAGE
    if st.session_state.etapa == 1:
        st.markdown('<div class="main-container">', unsafe_allow_html=True)
        st.image("https://quintes.com.br/wp-content/uploads/2023/07/Logo-Branca-Simbolo-Preto-Texto.png", width=140)
        st.markdown('<h1 class="headline">Descubra o valor da sua empresa em poucos minutos</h1>', unsafe_allow_html=True)
        st.markdown('<p class="subheadline">Tomar decisões sem saber o valor da sua empresa é como atirar no escuro. Melhore a sua visão empresarial e tenha muito mais resultado realizando o valuation do seu negócio.</p>', unsafe_allow_html=True)
        
        if st.button("Começar agora"):
            st.session_state.etapa = 2
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    # PÁGINA 2: FORMULÁRIO (FILLOUT EMBED)
    elif st.session_state.etapa == 2:
        st.markdown('<div style="text-align:center; padding-bottom:20px;">', unsafe_allow_html=True)
        st.image("https://quintes.com.br/wp-content/uploads/2023/07/Logo-Branca-Simbolo-Preto-Texto.png", width=100)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # O link do seu form real
        fillout_url = "https://forms.fillout.com/t/1qwGDDvuKKus"
        st.components.v1.iframe(fillout_url, height=600, scrolling=True)
        
        if st.button("← Voltar"):
            st.session_state.etapa = 1
            st.rerun()

    # PÁGINA 3: RESULTADO (PÓS-REDIRECIONAMENTO)
    elif st.session_state.etapa == 3:
        ebitda = float(st.query_params.get("ebitda", 0))
        empresa = st.query_params.get("empresa", "Sua Empresa")
        valuation = ebitda * 6

        st.markdown('<div class="main-container" style="padding-top:20px;">', unsafe_allow_html=True)
        st.image("https://quintes.com.br/wp-content/uploads/2023/07/Logo-Branca-Simbolo-Preto-Texto.png", width=120)
        
        st.markdown(f"""
            <div class="res-card">
                <div class="res-label">Valuation Estimado • {empresa}</div>
                <div class="res-value">R$ {valuation:,.2f}</div>
                <div style="color:#555; font-size:0.9rem;">Baseado em múltiplo de 6.0x EBITDA</div>
            </div>
            <h2 style="font-size:1.5rem; margin: 40px 0 20px 0;">Próximos Passos</h2>
        """, unsafe_allow_html=True)

        # Ofertas em formato de lista (estilo Fillout)
        st.markdown('<div class="offer-box"><h3>📄 Relatório de Indicadores</h3><p>Receba um PDF com a análise detalhada do seu valuation.</p></div>', unsafe_allow_html=True)
        st.button("Solicitar Relatório", key="opt1")
        
        st.markdown('<div class="offer-box"><h3>💻 Software M&A</h3><p>Gestão contínua do valor de mercado da sua operação.</p></div>', unsafe_allow_html=True)
        st.button("Conhecer Software", key="opt2")
        
        st.markdown('<div class="offer-box"><h3>🤝 Consultoria M&A</h3><p>Falar com um advisor para preparar a venda da empresa.</p></div>', unsafe_allow_html=True)
        st.button("Agendar Call", key="opt3")

        st.markdown('<br>', unsafe_allow_html=True)
        if st.button("Refazer Cálculo", type="secondary"):
            st.query_params.clear()
            st.session_state.etapa = 1
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
