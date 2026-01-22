import streamlit as st

# Configuração da página
st.set_page_config(page_title="Calculadora do Vitor", page_icon="🔢")

st.title("🔐 Acesso à Calculadora")

# Sistema de Login
if 'logado' not in st.session_state:
    st.session_state.logado = False

if not st.session_state.logado:
    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")
    if st.button("Entrar"):
        if usuario == "Vitor" and senha == "chg20122013":
            st.session_state.logado = True
            st.rerun()
        else:
            st.error("Usuário ou senha incorretos")
else:
    # Se estiver logado, mostra a calculadora
    st.success(f"Bem-vindo, Vitor!")
    
    operacao = st.selectbox("Escolha a operação", 
                          ["Soma", "Subtração", "Multiplicação", "Divisão", "Potenciação", "Resto"])
    
    n1 = st.number_input("Primeiro número", value=0)
    n2 = st.number_input("Segundo número", value=0)

    if st.button("Calcular"):
        if operacao == "Soma": resultado = n1 + n2
        elif operacao == "Subtração": resultado = n1 - n2
        elif operacao == "Multiplicação": resultado = n1 * n2
        elif operacao == "Divisão": 
            resultado = n1 / n2 if n2 != 0 else "Erro: Divisão por zero"
        elif operacao == "Potenciação": resultado = n1 ** n2
        elif operacao == "Resto": resultado = n1 % n2
        
        st.write(f"### Resultado: {resultado}")

    if st.button("Sair"):
        st.session_state.logado = False
        st.rerun()
