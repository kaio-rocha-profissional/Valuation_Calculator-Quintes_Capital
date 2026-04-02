import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Valuation Cortesia | Quintes Capital", 
    layout="centered", 
    page_icon="https://quintes.com.br/wp-content/uploads/2023/07/Favicon-Quintes.png"
)

# --- TODO O LAYOUT HTML/CSS AQUI ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');
    
    /* Reset Geral */
    .stApp { background-color: #ffffff; font-family: 'Poppins', sans-serif; }
    
    /* Hero Section */
    .hero-container { text-align: center; padding: 40px 0 20px 0; }
    .logo-img { width: 180px; margin-bottom: 15px; }
    .hero-title { color: #007bff; font-weight: 700; font-size: 2.8rem; margin-bottom: 5px; }
    .hero-subtitle { color: #666; font-size: 1.1rem; margin-bottom: 30px; }

    /* Card de Valuation (Resultado) */
    .valuation-card {
        background: #fdfdfd;
        border: 2px solid #007bff;
        border-radius: 20px;
        padding: 50px 20px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,123,255,0.1);
        margin-bottom: 40px;
    }
    .valuation-label { text-transform: uppercase; letter-spacing: 2px; color: #888; font-size: 0.9rem; font-weight: 600; }
    .valuation-value { font-size: 4rem; font-weight: 800; color: #1a1a1a; margin: 10px 0; }
    .valuation-multiplo { color: #007bff; font-weight: 600; font-size: 1rem; }

    /* Grid de Ofertas */
    .offer-grid-title { text-align: center; font-weight: 700; font-size: 1.8rem; margin-bottom: 30px; color: #1a1a1a; }
    
    .offer-card {
        background: white;
        border: 1px solid #eee;
        border-radius: 15px;
        padding: 25px;
        text-align: center;
        height: 280px;
        transition: all 0.3s ease;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .offer-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(0,0,0,0.08);
        border-color: #007bff;
    }
    .offer-card h3 { color: #007bff; font-size: 1.3rem; margin-bottom: 10px; font-weight: 700; }
    .offer-card p { font-size: 0.9rem; color: #555; line-height: 1.4; }

    /* Ajuste Iframe */
    iframe { border-radius: 15px; border: 1px solid #eee !important; }
    </style>
""", unsafe_allow_html=True)

# --- LÓGICA DE NAVEGAÇÃO ---
query_params = st.query_params

# Se o Fillout mandou o EBITDA via URL, mostramos o Layout de Resultado
if "ebitda" in query_params:
    ebitda = float(query_params.get("ebitda", 0))
    empresa = query_params.get("empresa", "Sua Empresa")
    
    # Cálculo: 6x EBITDA (Podemos ajustar essa regra depois)
    valuation_final = ebitda * 6

    # HEADER DO RESULTADO
    st.markdown(f"""
        <div class="hero-container">
            <img src="https://quintes.com.br/wp-content/uploads/2023/07/Logo-Branca-Simbolo-Preto-Texto.png" class="logo-img">
        </div>
        <div class="valuation-card">
            <div class="valuation-label">Valuation Estimado de {empresa}</div>
            <div class="valuation-value">R$ {valuation_final:,.2f}</div>
            <div class="valuation-multiplo">Múltiplo de Mercado Aplicado: 6.0x EBITDA</div>
        </div>
        <h2 class="offer-grid-title">Como deseja evoluir este resultado?</h2>
    """, unsafe_allow_html=True)

    # COLUNAS DE OFERTA COM HTML + BOTÕES STREAMLIT
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div class="offer-card">
                <div>
                    <h3>📄 Relatório Detalhado</h3>
                    <p>PDF completo com análise de KPIs, comparativo regional e plano de ação imediato.</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Quero PDF", key="btn_pdf", use_container_width=True):
            st.info("Preparando seu relatório...")

    with col2:
        st.markdown("""
            <div class="offer-card">
                <div>
                    <h3>💻 Software M&A</h3>
                    <p>Acompanhe seu valuation em tempo real e simule cenários de venda mensalmente.</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Assinar SaaS", key="btn_saas", use_container_width=True):
            st.info("Abrindo checkout...")

    with col3:
        st.markdown("""
            <div class="offer-card">
                <div>
                    <h3>🤝 Advisor Quintes</h3>
                    <p>Mentoria particular com nossos especialistas para preparar sua saída (exit).</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Falar com Advisor", key="btn_adv", use_container_width=True):
            st.success("Chamando no WhatsApp...")

    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("Refazer Análise"):
        st.query_params.clear()
        st.rerun()

else:
    # --- TELA INICIAL (EMBED DO FILLOUT) ---
    st.markdown("""
        <div class="hero-container">
            <img src="https://quintes.com.br/wp-content/uploads/2023/07/Logo-Branca-Simbolo-Preto-Texto.png" class="logo-img">
            <h1 class="hero-title">Calculadora <span>M&A</span></h1>
            <p class="hero-subtitle">Descubra o valor da sua operação de Telecom em segundos.</p>
        </div>
    """, unsafe_allow_html=True)

    # Link do Fillout que você enviou
    fillout_url = "https://forms.fillout.com/t/1qwGDDvuKKus"
    
    # Exibindo o formulário dentro do site
    st.components.v1.iframe(fillout_url, height=700, scrolling=True)
