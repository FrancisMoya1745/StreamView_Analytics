import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración visual minimalista para presentaciones gerenciales
sns.set_theme(style="white")
plt.rcParams['axes.spines.top'] = False
plt.rcParams['axes.spines.right'] = False

# 1. Cargar los datos (Asegúrate de que los CSV estén en la carpeta 'data')
# df_movies = pd.read_csv('../data/netflix_movies_detailed_up_to_2025.csv')
# df_shows = pd.read_csv('../data/netflix_tv_shows_detailed_up_to_2025.csv')

def plot_evolucion_catalogo(datos_agrupados_anio):
    """
    Gráfico 1: Evolución del Catálogo: Películas vs. Series a lo largo del tiempo.
    """
    plt.figure(figsize=(10, 5))
    # Aquí iría el plot de tus datos reales. Ejemplo genérico:
    # plt.plot(datos_agrupados_anio['Anio'], datos_agrupados_anio['Peliculas'], color='#003f5c', linewidth=2.5, label='Películas')
    # plt.plot(datos_agrupados_anio['Anio'], datos_agrupados_anio['Series'], color='#ffa600', linewidth=2.5, label='Series')
    
    plt.title('Evolución de Adquisición de Contenido por Año', fontsize=14, pad=20)
    plt.xlabel('Año de Integración al Catálogo', fontsize=10)
    plt.ylabel('Cantidad de Títulos', fontsize=10)
    plt.legend(frameon=False)
    plt.grid(axis='y', linestyle='--', alpha=0.4)
    plt.tight_layout()
    plt.savefig('../images/evolucion_catalogo.png')
    plt.show()

def plot_top_generos(datos_generos):
    """
    Gráfico 2: Top 10 Géneros con Mayor Volumen de Contenido.
    """
    plt.figure(figsize=(10, 6))
    # Ejemplo genérico de gráfico de barras horizontales
    # ax = sns.barplot(x='Cantidad', y='Genero', data=datos_generos, color='#2f4b7c')
    
    plt.title('Top 10 Géneros en el Catálogo', fontsize=14, pad=20)
    plt.xlabel('') # Quitamos la etiqueta del eje X para no saturar
    plt.ylabel('')
    
    # Quitar el eje X inferior para que la vista vaya directo a las etiquetas de las barras
    plt.xticks([]) 
    
    plt.tight_layout()
    plt.savefig('../images/top_generos.png')
    plt.show()

def plot_distribucion_audiencia(datos_audiencia):
    """
    Gráfico 3: Distribución del Contenido por Audiencia Objetivo.
    """
    plt.figure(figsize=(8, 8))
    colores = ['#003f5c', '#bc5090', '#ffa600']
    
    # plt.pie(datos_audiencia['Cantidad'], labels=datos_audiencia['Clasificacion'], colors=colores, autopct='%1.1f%%', startangle=90, pctdistance=0.85, wedgeprops=dict(width=0.3))
    
    plt.title('Distribución de Contenido por Segmento de Audiencia', fontsize=14, pad=20)
    plt.tight_layout()
    plt.savefig('../images/distribucion_audiencia.png')
    plt.show()

# Llamar a las funciones (Una vez que conectes los DataFrames)
# plot_evolucion_catalogo(mis_datos)
# plot_top_generos(mis_datos)
# plot_distribucion_audiencia(mis_datos)