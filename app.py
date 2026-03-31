import streamlit as st

# Configuração da página
st.set_page_config(page_title="Quintes Capital - Resultado Valuation", layout="centered")

# --- ESTILIZAÇÃO CUSTOMIZADA ---
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #007BFF; color: white; }
    </style>
    """, unsafe_allow_html=True)

# --- CAPTAÇÃO DE DADOS DA URL (Vindo do Fillout) ---
query_params = st.query_params

nome = query_params.get("nome", "Investidor")
empresa = query_params.get("empresa", "sua empresa")
ebitda = float(query_params.get("ebitda", 0))
assinantes = int(query_params.get("assinantes", 0))

# Se não houver dados na URL, mostramos a Landing Page inicial
if ebitda == 0:
    st.image("https://seu-logo-aqui.com/logo.png", width=200) # Opcional: coloque seu logo
    st.title("Descubra o valor de mercado do seu Provedor")
    st.write("A Quintes Capital ajuda você a entender o real potencial da sua operação através de métricas precisas de M&A.")
    
    # BOTÃO QUE LEVA PARA O FILLOUT
    link_fillout = "https://forms.fillout.com/t/seulinkdoform" # COLOQUE SEU LINK AQUI
    st.markdown(f'<a href="{link_fillout}" target="_self"><button style="width:100%; height:50px; cursor:pointer; background-color:#007BFF; color:white; border:none; border-radius:5px; font-size:18px;">Começar Valuation Gratuito 🚀</button></a>', unsafe_allow_html=True)

else:
    # --- LÓGICA DE CÁLCULO M&A QUINTES ---
    # Usando a média: (7x EBITDA + R$2000 por assinante) / 2
    val_ebitda = ebitda * 7
    val_base = assinantes * 2000
    valuation_final = (val_ebitda + val_base) / 2 if assinantes > 0 else val_ebitda

    # --- TELA DE RESULTADO ---
    st.balloons()
    st.subheader(f"Olá, {nome}! Aqui está a análise da {empresa}:")
    
    st.markdown(f"""
        <div style="background-color: white; padding: 30px; border-radius: 10px; border-left: 10px solid #007BFF; box-shadow: 2px 2px 10px rgba(0,0,0,0.1);">
            <h4 style="color: #555;">Valuation Estimado (Cortesia)</h4>
            <h1 style="color: #007BFF;">R$ {valuation_final:,.2f}</h1>
        </div>
    """, unsafe_allow_html=True)

    st.divider()
    
    st.subheader("Escolha como deseja evoluir este resultado:")
    
    # As 4 ofertas do seu Funil
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📄 Relatório + Plano de Ação"):
            st.info("Solicitação enviada! Gerando seu PDF...")
            
    with col2:
        if st.button("💻 Plano SaaS (12 meses)"):
            st.info("Excelente! Ativando seu acesso ao software...")

    if st.button("🤝 Falar com Advisor (M&A)"):
        st.success("Prioridade máxima! Kaio ou um consultor Quintes entrará em contato em instantes.")
