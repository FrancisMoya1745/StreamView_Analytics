import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Asegurar que la carpeta images exista en la raíz
os.makedirs('images', exist_ok=True)

# Configuración visual minimalista
sns.set_theme(style="white")
plt.rcParams['axes.spines.top'] = False
plt.rcParams['axes.spines.right'] = False

print("Cargando datasets...")
# Rutas ajustadas para ejecución desde la raíz
df_movies = pd.read_csv('data/netflix_movies_detailed_up_to_2025.csv')
df_shows = pd.read_csv('data/netflix_tv_shows_detailed_up_to_2025.csv')

df_movies['type'] = 'Pelicula'
df_shows['type'] = 'Serie'
df_netflix = pd.concat([df_movies, df_shows], ignore_index=True)

def plot_evolucion_catalogo(df):
    plt.figure(figsize=(10, 5))
    if 'release_year' in df.columns:
        evolucion = df.groupby(['release_year', 'type']).size().unstack().fillna(0)
        evolucion = evolucion[evolucion.index >= 2000]
        
        plt.plot(evolucion.index, evolucion['Pelicula'], color='#003f5c', linewidth=2.5, label='Películas')
        if 'Serie' in evolucion.columns:
            plt.plot(evolucion.index, evolucion['Serie'], color='#ffa600', linewidth=2.5, label='Series')
        
        plt.title('Evolución de Lanzamientos por Año (2000 - 2025)', fontsize=14, pad=20)
        plt.xlabel('Año', fontsize=10)
        plt.ylabel('Cantidad de Títulos', fontsize=10)
        plt.legend(frameon=False)
        plt.grid(axis='y', linestyle='--', alpha=0.4)
        plt.tight_layout()
        plt.savefig('images/evolucion_catalogo.png')
    plt.close()

def plot_top_generos(df):
    plt.figure(figsize=(10, 6))
    col_genero = 'listed_in' if 'listed_in' in df.columns else 'genres'
    
    if col_genero in df.columns:
        generos = df[col_genero].str.split(',').explode().str.strip()
        top_10 = generos.value_counts().head(10)
        
        sns.barplot(x=top_10.values, y=top_10.index, color='#2f4b7c')
        plt.title('Top 10 Géneros en el Catálogo', fontsize=14, pad=20)
        plt.xlabel('') 
        plt.ylabel('')
        plt.xticks([]) 
        
        for i, v in enumerate(top_10.values):
            plt.text(v + 5, i, str(v), color='black', va='center')
            
        plt.tight_layout()
        plt.savefig('images/top_generos.png')
    plt.close()

def plot_distribucion_audiencia(df):
    plt.figure(figsize=(8, 8))
    if 'rating' in df.columns:
        # Llenar valores vacíos para que no rompan el cálculo
        df['rating'] = df['rating'].fillna('Desconocido')
        
        adultos = ['TV-MA', 'R', 'NC-17']
        teens = ['TV-14', 'PG-13']
        kids = ['TV-PG', 'TV-Y', 'TV-Y7', 'PG', 'G', 'TV-G']
        
        def categorizar(rating):
            if rating in adultos: return 'Adultos'
            elif rating in teens: return 'Adolescentes'
            elif rating in kids: return 'Familiar/Infantil'
            else: return 'Otros'
            
        df['Audiencia'] = df['rating'].apply(categorizar)
        conteo = df['Audiencia'].value_counts()
        
        # Colores ajustados al tamaño del conteo
        colores_base = ['#003f5c', '#bc5090', '#ffa600', '#cccccc']
        colores = colores_base[:len(conteo)]
        
        plt.pie(conteo, labels=conteo.index, colors=colores, autopct='%1.1f%%', startangle=90, pctdistance=0.85, wedgeprops=dict(width=0.3))
        
        plt.title('Distribución de Contenido por Segmento de Audiencia', fontsize=14, pad=20)
        plt.tight_layout()
        plt.savefig('images/distribucion_audiencia.png')
    plt.close()

print("Generando y guardando gráficos...")
plot_evolucion_catalogo(df_netflix)
plot_top_generos(df_netflix)
plot_distribucion_audiencia(df_netflix)
print("¡Listo! Imágenes guardadas en la carpeta 'images'.")