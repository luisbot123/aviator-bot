import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Aviator PRO IA", layout="wide")

st.title("🚀 Aviator PRO IA")

# -------- SESSION STATE --------
if "data" not in st.session_state:
    st.session_state.data = []

if "soportes" not in st.session_state:
    st.session_state.soportes = []

if "resistencias" not in st.session_state:
    st.session_state.resistencias = []

# -------- BOTONES DE CUOTAS --------
st.subheader("🎯 Registrar Cuotas")

col1, col2, col3, col4, col5 = st.columns(5)

if col1.button("1.00 - 1.50 🔵"):
    st.session_state.data.append(1.3)

if col2.button("1.51 - 1.99 🔷"):
    st.session_state.data.append(1.7)

if col3.button("2.00 - 4.99 🟢"):
    st.session_state.data.append(2.5)

if col4.button("5.00 - 9.99 🟡"):
    st.session_state.data.append(6)

if col5.button("10+ 🌸"):
    st.session_state.data.append(10)

# -------- CONTROLES --------
colA, colB, colC = st.columns(3)

if colA.button("❌ Borrar última"):
    if st.session_state.data:
        st.session_state.data.pop()

if colB.button("🧹 Reset"):
    st.session_state.data = []

if colC.button("📉 Soporte"):
    if st.session_state.data:
        st.session_state.soportes.append(st.session_state.data[-1])

colD, colE = st.columns(2)

if colD.button("📈 Resistencia"):
    if st.session_state.data:
        st.session_state.resistencias.append(st.session_state.data[-1])

if colE.button("🧽 Borrar líneas"):
    st.session_state.soportes = []
    st.session_state.resistencias = []

# -------- IA --------
def analizar(data):
    if len(data) < 5:
        return "Esperar", 50

    ultimos = data[-5:]
    promedio = sum(ultimos)/5

    bajos = sum(1 for x in ultimos if x < 2)
    altos = sum(1 for x in ultimos if x >= 2)

    score = 0

    if bajos >= 3:
        score += 2
    if altos >= 3:
        score -= 2
    if promedio < 1.5:
        score += 1
    if promedio > 2:
        score -= 1

    if score >= 2:
        return "Entrada BAJA (1.5x)", 75
    elif score <= -2:
        return "Entrada ALTA (2.0x+)", 75
    else:
        return "Esperar", 55

# -------- RESULTADO IA --------
if st.session_state.data:
    decision, conf = analizar(st.session_state.data)

    st.subheader("🧠 IA")
    st.write(f"Señal: {decision}")
    st.write(f"Confianza: {conf}%")

# -------- GRÁFICO --------
if st.session_state.data:

    colores = []
    for x in st.session_state.data:
        if x <= 1.5:
            colores.append("red")
        elif x < 2:
            colores.append("gray")
        elif x < 5:
            colores.append("green")
        elif x < 10:
            colores.append("gold")
        else:
            colores.append("pink")

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        y=st.session_state.data,
        mode='lines+markers',
        marker=dict(color=colores, size=10),
        line=dict(color="white")
    ))

    # soportes
    for s in st.session_state.soportes:
        fig.add_hline(y=s, line_color="green")

    # resistencias
    for r in st.session_state.resistencias:
        fig.add_hline(y=r, line_color="red")

    st.plotly_chart(fig, use_container_width=True)
