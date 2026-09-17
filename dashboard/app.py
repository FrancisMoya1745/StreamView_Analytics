import streamlit as st
import pandas as pd
# import plotly.express as px

# Configuración de la página
st.set_page_config(page_title="StreamView Analytics", layout="wide")

st.title("📊 StreamView Analytics - Panel Gerencial")
st.markdown("Bienvenido al panel interactivo de análisis de contenido. Seleccione los filtros en el menú lateral para explorar los datos.")

# Barra lateral para filtros
st.sidebar.header("Filtros de Búsqueda")
tipo_contenido = st.sidebar.selectbox("Tipo de Contenido", ["Todos", "Películas", "Series"])
# anio_lanzamiento = st.sidebar.slider("Año de Lanzamiento", 1990, 2025, (2010, 2025))

# KPIs Principales
col1, col2, col3 = st.columns(3)
col1.metric("Total de Películas", "A calcular...")
col2.metric("Total de Series", "A calcular...")
col3.metric("Género Principal", "A calcular...")

st.markdown("---")

# Espacio para los gráficos interactivos
st.subheader("Tendencias de Contenido")
st.markdown("*Aquí se integrarán los gráficos generados con Plotly o Matplotlib basados en los datasets corporativos.*")
