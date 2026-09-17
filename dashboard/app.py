import streamlit as st
import pandas as pd
from PIL import Image
import os

st.set_page_config(page_title="StreamView Analytics", layout="wide")

st.title("📊 StreamView Analytics - Panel Gerencial")
st.markdown("Análisis de contenido para apoyar la toma de decisiones basada en datos.")

# Cargar datos para calcular los KPIs reales
@st.cache_data
def load_data():
    try:
        df_m = pd.read_csv('data/netflix_movies_detailed_up_to_2025.csv')
        df_s = pd.read_csv('data/netflix_tv_shows_detailed_up_to_2025.csv')
        return df_m, df_s
    except:
        return None, None

df_movies, df_shows = load_data()

# Mostrar KPIs si los datos cargaron correctamente
if df_movies is not None and df_shows is not None:
    col1, col2, col3 = st.columns(3)
    col1.metric("Total de Películas", f"{len(df_movies):,}")
    col2.metric("Total de Series", f"{len(df_shows):,}")
    col3.metric("Volumen Total del Catálogo", f"{len(df_movies) + len(df_shows):,}")
else:
    st.warning("Verifica que los archivos CSV estén en la carpeta 'data/'.")

st.markdown("---")
st.subheader("Análisis Exploratorio de Datos (EDA)")

# Usar pestañas para organizar la narrativa visual sin saturar la pantalla
tab1, tab2, tab3 = st.tabs(["Evolución del Catálogo", "Top Géneros", "Distribución por Audiencia"])

def mostrar_imagen(ruta, tab):
    if os.path.exists(ruta):
        image = Image.open(ruta)
        tab.image(image, use_container_width=True)
    else:
        tab.info(f"Falta el gráfico. Ejecuta primero: python notebooks/analisis_exploratorio.py")

# Pestaña 1
mostrar_imagen('images/evolucion_catalogo.png', tab1)
tab1.markdown("**Justificación y Toma de Decisiones:** Visualiza el ritmo de producción histórico. Crucial para definir el presupuesto futuro y evaluar si la adquisición de series acompaña el nivel de interacción de los clientes.")

# Pestaña 2
mostrar_imagen('images/top_generos.png', tab2)
tab2.markdown("**Justificación y Toma de Decisiones:** Identifica las categorías dominantes en el catálogo. Permite orientar las campañas de marketing hacia los géneros de mayor volumen y evaluar reasignaciones de recursos financieros.")

# Pestaña 3
mostrar_imagen('images/distribucion_audiencia.png', tab3)
tab3.markdown("**Justificación y Toma de Decisiones:** Define la identidad demográfica de la plataforma. Fundamental para campañas de expansión de mercado y suscripciones conjuntas enfocadas en segmentos específicos.")