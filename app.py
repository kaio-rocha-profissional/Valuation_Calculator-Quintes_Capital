import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import datetime

# 1. SEMPRE a primeira configuração do Streamlit
st.set_page_config(page_title="Valuation Telecom - Cortesia", layout="centered")

# 2. Conexão com o Google Sheets
conn = st.connection("gsheets", type=GSheetsConnection)

# --- SESSÃO DE CONTROLE ---
if 'etapa' not in st.session_state:
    st.session_state.etapa = 1

# --- ETAPA 1: CAPTAÇÃO E CÁLCULO ---
if st.session_state.etapa == 1:
    st.title("Análise de Mercado: Setor Telecom")
    st.write("Descubra o Valuation da sua operação de forma gratuita.")

    with st.form("form_captacao"):
        st.subheader("Dados da Operação")
        col1, col2 = st.columns(2)
        
        with col1:
            nome = st.text_input("Seu Nome *")
            email = st.text_input("E-mail Corporativo *")
            empresa = st.text_input("Nome do Provedor *")
        with col2:
            whatsapp = st.text_input("WhatsApp (com DDD) *")
            uf = st.selectbox("Estado", ["SP", "RJ", "MG", "PR", "SC", "RS", "Outro"])
            assinantes = st.number_input("Número de Assinantes", min_value=0)

        st.divider()
        
        col3, col4 = st.columns(2)
        with col3:
            ebitda_anual = st.number_input("EBITDA Anual (R$)", min_value=0.0)
            churn = st.slider("Churn Rate Mensal (%)", 0.0, 10.0, 1.5)
        with col4:
            mrr = st.number_input("Receita Mensal (MRR)", min_value=0.0)
            ticket_medio = st.number_input("Ticket Médio (ARPU)", min_value=0.0)

        submit = st.form_submit_button("Gerar meu Valuation 🚀")

        if submit:
            if not nome or not email or ebitda_anual == 0:
                st.error("Por favor, preencha os dados essenciais para o cálculo.")
            else:
                # LÓGICA DE CÁLCULO (Ajustada para a média que sugerimos)
                val_ebitda = ebitda_anual * 6
                valuation_estimado = val_ebitda
                
                # --- PROSPECÇÃO INVERSA: GRAVANDO NO GOOGLE SHEETS ---
                try:
                    novo_lead = pd.DataFrame([{
                        "Data": datetime.now().strftime("%d/%m/%Y %H:%M"),
                        "Nome": nome,
                        "WhatsApp": whatsapp,
                        "Empresa": empresa,
                        "UF": uf,
                        "EBITDA": ebitda_anual,
                        "Valuation": valuation_estimado,
                        "Interesse": "Acessou Resultado"
                    }])
                    
                    # Lê os dados existentes e concatena (Ajuste o nome da worksheet se necessário)
                    dados_existentes = conn.read(worksheet="Página1")
                    dados_atualizados = pd.concat([dados_existentes, novo_lead], ignore_index=True)
                    conn.update(worksheet="Página1", data=atualizados)
                except:
                    # Se o Sheets ainda não estiver configurado nas Secrets, o app não trava
                    pass

                # SALVANDO NA SESSÃO PARA A ETAPA 2
                st.session_state.dados_cliente = {
                    "nome": nome, "empresa": empresa, "whatsapp": whatsapp,
                    "ebitda": ebitda_anual, "valuation": valuation_estimado
                }
                st.session_state.etapa = 2
                st.rerun()

# --- ETAPA 2: RESULTADO E CONVERSÃO ---
elif st.session_state.etapa == 2:
    dados = st.session_state.dados_cliente
    
    st.balloons()
    st.success(f"### Valuation Estimado da {dados['empresa']}:")
    st.metric(label="Valor de Mercado (Estimativa Estática)", value=f"R$ {dados['valuation']:,.2f}")
    
    st.info("💡 Este valor é uma estimativa baseada em múltiplos de mercado atuais para o setor de Telecom.")
    
    st.divider()
    st.subheader("📈 Como você deseja prosseguir com este resultado?")
    
    escolha = st.radio("Selecione uma opção para detalhamento:", [
        "Quero o Plano Básico: Relatório Completo + Plano de Ação",
        "Quero o Plano Avançado: Aplicativo Calculadora + Mentoria particular",
        "Quero falar com um Consultor Quintes Capital"
    ])
    
    if st.button("Confirmar Interesse"):
        # Aqui você pode adicionar um segundo conn.update para registrar qual plano ele escolheu!
        st.write(f"Excelente escolha, {dados['nome']}! Nossa equipe entrará em contato via WhatsApp ({dados['whatsapp']}) em breve.")
    
    if st.button("Refazer Cálculo"):
        st.session_state.etapa = 1
        st.rerun()
