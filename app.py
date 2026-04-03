import streamlit as st

st.set_page_config(page_title="Aviator IA PRO", layout="centered")

st.title("🤖 Aviator IA PRO")

data = st.text_area("Ingresa multiplicadores (ej: 1.2,2.5,1.1)")

if data:
    try:
        valores = [float(x) for x in data.split(",")]

        # PROMEDIO
        prom5 = sum(valores[-5:]) / min(len(valores),5)

        # RACHAS
        racha_bajos = 0
        racha_altos = 0

        for v in reversed(valores):
            if v < 2:
                racha_bajos += 1
            else:
                break

        for v in reversed(valores):
            if v >= 2:
                racha_altos += 1
            else:
                break

        # SCORE
        score = 0

        if racha_bajos >= 3:
            score += 2
        if racha_altos >= 3:
            score -= 2
        if prom5 < 1.5:
            score += 1
        if prom5 > 2:
            score -= 1

        # DECISIÓN
        st.subheader("Señal")

        if score >= 2:
            st.success("🟢 ENTRAR BAJO (1.5x)")
        elif score <= -2:
            st.error("🔴 ENTRAR ALTO (2.2x)")
        else:
            st.warning("⏳ ESPERAR")

        # DATOS
        st.write(f"Promedio 5: {round(prom5,2)}")
        st.write(f"Racha Bajos: {racha_bajos}")
        st.write(f"Racha Altos: {racha_altos}")

        # GRÁFICA
        st.line_chart(valores)

    except:
        st.error("Error en los datos")
