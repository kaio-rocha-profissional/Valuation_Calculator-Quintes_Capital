import streamlit as st

# 1. Configuração da página (Deve ser a primeira linha de código)
st.set_page_config(page_title="Quintes Capital - Valuation", layout="centered")

# --- CAPTAÇÃO DOS PARÂMETROS DA URL ---
# O Streamlit lê o que vem depois do '?' na URL
query_params = st.query_params

# Se a URL tiver dados, a gente calcula. Se não, mostra a página de boas-vindas.
if query_params:
    # Capturando os dados da "tripinha"
    nome = query_params.get("nome", "Investidor")
    empresa = query_params.get("empresa", "sua empresa")
    assinantes = query_params.get("assinantes", "0")
    ticket = query_params.get("ticket", "0")
    receita = query_params.get("receita", "0")

    # Tratamento de números (converte texto da URL para número real)
    try:
        n_assinantes = int(float(assinantes))
        n_ticket = float(ticket)
        n_receita = float(receita)
    except:
        n_assinantes = n_ticket = n_receita = 0

    # --- LÓGICA DE CÁLCULO QUINTES CAPITAL ---
    # Cálculo: Média entre (Receita Anual * 2.5) e (Assinantes * 2000)
    if n_receita > 0:
        val_faturamento = (n_receita * 12) * 2.5
        val_base = n_assinantes * 2000
        valuation_final = (val_faturamento + val_base) / 2
    else:
        valuation_final = 0

    # --- TELA DE RESULTADO ---
    st.balloons()
    st.title("📊 Seu Valuation está pronto!")
    st.subheader(f"Análise exclusiva para: {empresa}")
    
    st.markdown(f"""
        <div style="background-color: #ffffff; padding: 25px; border-radius: 15px; border-left: 8px solid #007BFF; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
            <p style="color: #666; margin-bottom: 5px;">Estimativa de Valor de Mercado</p>
            <h1 style="color: #007BFF; margin-top: 0;">R$ {valuation_final:,.2f}</h1>
        </div>
    """, unsafe_allow_html=True)

    st.divider()
    
    st.write(f"### Olá, {nome}! Como deseja evoluir este resultado?")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📄 Relatório + Plano de Ação"):
            st.success("Solicitação enviada! Verifique seu e-mail em instantes.")
    with col2:
        if st.button("💻 Software de Gestão (SaaS)"):
            st.info("Iniciando setup da sua conta...")

    if st.button("🤝 Falar com Advisor (M&A)"):
        st.warning("Chamando um consultor Quintes Capital agora mesmo!")

else:
    # --- PÁGINA INICIAL (Caso acessem o link sem preencher o formulário) ---
    st.image("https://images.unsplash.com/photo-1551288049-bbda48336ad9?auto=format&fit=crop&q=80&w=400", width=200) # Imagem ilustrativa
    st.title("Quintes Capital")
    st.write("Seja bem-vindo ao portal de Valuation para Provedores de Internet.")
    st.write("Para calcular o valor da sua empresa, clique no botão abaixo:")
    
    # Substitua pelo seu link real do Fillout
    link_do_fillout = "https://forms.fillout.com/t/1qwGDDvuKKus" 
    st.markdown(f'<a href="{https://forms.fillout.com/t/1qwGDDvuKKus}" target="_self"><button style="width:100%; height:50px; cursor:pointer; background-color:#007BFF; color:white; border:none; border-radius:5px; font-size:18px; font-weight:bold;">Começar Análise Gratuita 🚀</button></a>', unsafe_allow_html=True)
