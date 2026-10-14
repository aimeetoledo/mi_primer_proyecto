import streamlit as st
import pandas as pd

df = pd.read_excel("YARDAS_PASOS_DATOS_TICS.xlsx")
st.title("Este es un análisis estadístico")
st.header("Base de datos de Yardas vz Pases")
st.dataframe(df.head(), use_container_width=True)

# Esta es la estadística descriptiva.
st.header("Estadística descriptiva")
st.dataframe(df.describe())

# Esto esta estandarizando las columnas.
df.columns = [c.lower().replace(' ', '_') for c in df.columns]
import matplotlib.pyplot as plt


fig, ax = plt.subplots()
ax.boxplot(df['yardas_totales'])
st.header("Diagrama de caja y bigote\nde Yardas totales")
st.pyplot(fig)
