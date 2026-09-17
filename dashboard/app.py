import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración profesional de la página
st.set_page_config(page_title="StreamView Analytics", page_icon="📊", layout="wide")

# Encabezado corporativo
st.markdown("<h1 style='text-align: center; color: #E50914;'>StreamView Analytics</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Panel Gerencial de Toma de Decisiones</p>", unsafe_allow_html=True)
st.markdown("---")

# Carga e integración de datos
@st.cache_data
def load_data():
    df_m = pd.read_csv('data/netflix_movies_detailed_up_to_2025.csv')
    df_s = pd.read_csv('data/netflix_tv_shows_detailed_up_to_2025.csv')
    df_m['type'] = 'Película'
    df_s['type'] = 'Serie'
    df = pd.concat([df_m, df_s], ignore_index=True)
    df['rating'] = df['rating'].fillna('Desconocido')
    return df

df = load_data()

# ----------------- FILTROS INTERACTIVOS -----------------
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/0/08/Netflix_2015_logo.svg", width=150)
st.sidebar.header("⚙️ Filtros Globales")
st.sidebar.markdown("Ajuste los parámetros para actualizar el dashboard en tiempo real.")

rango_anios = st.sidebar.slider(
    "Seleccione Rango de Años de Lanzamiento", 
    min_value=2000, 
    max_value=2025, 
    value=(2015, 2025)
)

# Aplicar filtro
df_filt = df[(df['release_year'] >= rango_anios[0]) & (df['release_year'] <= rango_anios[1])]

# ----------------- KPIs -----------------
col1, col2, col3 = st.columns(3)
col1.metric("🎬 Total de Títulos", f"{len(df_filt):,}")
col2.metric("🎥 Películas vs Series", f"{len(df_filt[df_filt['type']=='Película'])} / {len(df_filt[df_filt['type']=='Serie'])}")
col3.metric("📅 Rango Analizado", f"{rango_anios[0]} - {rango_anios[1]}")

st.markdown("<br>", unsafe_allow_html=True)

# ----------------- NARRATIVA VISUAL (TABS) -----------------
tab1, tab2, tab3 = st.tabs(["📈 Evolución del Catálogo", "🏆 Top Géneros", "🎯 Distribución de Audiencia"])

# ----- PESTAÑA 1: EVOLUCIÓN -----
with tab1:
    col_grafico, col_texto = st.columns([7, 3]) # 70% gráfico, 30% texto
    
    with col_grafico:
        evolucion = df_filt.groupby(['release_year', 'type']).size().reset_index(name='count')
        fig1 = px.line(evolucion, x='release_year', y='count', color='type',
                       color_discrete_map={'Película': '#E50914', 'Serie': '#221f1f'},
                       title='Tendencia de Producción Anual',
                       labels={'release_year': 'Año', 'count': 'Volumen de Títulos', 'type': 'Formato'})
        fig1.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig1, use_container_width=True)
        
    with col_texto:
        st.markdown("### 📊 Propósito del Gráfico")
        st.write("Este gráfico actúa como el pulso histórico de la plataforma, mostrando hacia dónde se inclina la estrategia de producción.")
        st.markdown("### 💡 Apoyo a la Decisión")
        st.info("Visualizar el cruce entre formatos permite a la gerencia auditar la asignación de presupuestos. Si el engagement demanda series, pero la producción muestra una tendencia a la baja, se deben redirigir los recursos de licencias inmediatamente.")

# ----- PESTAÑA 2: GÉNEROS -----
with tab2:
    col_grafico, col_texto = st.columns([7, 3])
    
    with col_grafico:
        col_genero = 'listed_in' if 'listed_in' in df_filt.columns else 'genres'
        generos = df_filt[col_genero].str.split(',').explode().str.strip().value_counts().head(10).reset_index()
        generos.columns = ['Género', 'Cantidad']
        
        fig2 = px.bar(generos, x='Cantidad', y='Género', orientation='h',
                      color='Cantidad', color_continuous_scale='Reds',
                      title='Top 10 Géneros Más Ofertados')
        fig2.update_layout(yaxis={'categoryorder':'total ascending'}, plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig2, use_container_width=True)
        
    with col_texto:
        st.markdown("### 📊 Propósito del Gráfico")
        st.write("Muestra la identidad actual del catálogo ordenando de mayor a menor el volumen de contenido por categoría, minimizando la carga cognitiva con un formato de ranking intuitivo.")
        st.markdown("### 💡 Apoyo a la Decisión")
        st.success("Esencial para los departamentos de Marketing y Adquisiciones. Permite detectar si existe un desbalance entre lo que más cuesta producir frente a lo que más volumen ocupa en el servidor, optimizando la compra de derechos.")

# ----- PESTAÑA 3: AUDIENCIA -----
with tab3:
    col_grafico, col_texto = st.columns([6, 4])
    
    with col_grafico:
        adultos = ['TV-MA', 'R', 'NC-17']
        teens = ['TV-14', 'PG-13']
        kids = ['TV-PG', 'TV-Y', 'TV-Y7', 'PG', 'G', 'TV-G']
        
        def categorizar(rating):
            if rating in adultos: return 'Adultos (+18)'
            elif rating in teens: return 'Adolescentes'
            elif rating in kids: return 'Familiar/Infantil'
            else: return 'Otros'
            
        df_filt_copy = df_filt.copy()
        df_filt_copy['Audiencia'] = df_filt_copy['rating'].apply(categorizar)
        conteo = df_filt_copy[df_filt_copy['Audiencia'] != 'Otros']['Audiencia'].value_counts().reset_index()
        conteo.columns = ['Segmento', 'Total']
        
        fig3 = px.pie(conteo, values='Total', names='Segmento', hole=0.4,
                      color='Segmento', color_discrete_map={'Adultos (+18)':'#E50914', 'Adolescentes':'#564d4d', 'Familiar/Infantil':'#f5f5f1'},
                      title='Distribución Demográfica del Catálogo')
        st.plotly_chart(fig3, use_container_width=True)
        
    with col_texto:
        st.markdown("### 📊 Propósito del Gráfico")
        st.write("Agrupa decenas de clasificaciones complejas en tres macrogrupos fáciles de interpretar mediante un gráfico de anillo.")
        st.markdown("### 💡 Apoyo a la Decisión")
        st.warning("Define la viabilidad de nuevas campañas. Si la gerencia desea lanzar suscripciones familiares, este panel muestra instantáneamente si el volumen de contenido 'Familiar/Infantil' respalda la estrategia o si requiere inversión previa.")