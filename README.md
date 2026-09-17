# StreamView Analytics - Visualización de Datos

## Descripción del Proyecto
Este proyecto fue desarrollado como una solución integral de visualización de datos para **StreamView Analytics**, una plataforma internacional de streaming digital. El objetivo principal es analizar el comportamiento de los usuarios, las preferencias de consumo de contenido y la retención de clientes para apoyar la toma de decisiones gerenciales.

## Estructura del Repositorio
El proyecto sigue una estructura estructurada y profesional:
* `data/`: Contiene las fuentes de datos corporativas (películas y series).
* `notebooks/`: Scripts y cuadernos de análisis exploratorio.
* `dashboard/`: Código fuente para el dashboard interactivo.
* `images/`: Gráficos exportados y recursos visuales.
* `src/`: Funciones auxiliares y procesamiento de datos.

## Fuentes de Datos
Los análisis se basan en los conjuntos de datos corporativos hasta 2025:
- `netflix_movies_detailed_up_to_2025.csv`
- `netflix_tv_shows_detailed_up_to_2025.csv`

## Herramientas Utilizadas
- **Lenguaje:** Python
- **Librerías de Análisis:** Pandas, NumPy
- **Visualización:** Matplotlib, Seaborn, Plotly (Dashboard)

## Instalación y Ejecución
Para evitar problemas de entorno o variables de sistema (PATH) al momento de levantar el proyecto en diferentes equipos, sigue estos pasos desde tu terminal, asegurándote de estar posicionado en la carpeta raíz del proyecto:

1. **Instalar dependencias necesarias:**
   ```bash
   pip install streamlit pandas matplotlib seaborn plotly