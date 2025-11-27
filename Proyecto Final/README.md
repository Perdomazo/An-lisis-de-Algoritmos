# Herramienta de Análisis de Portafolios ETF (S&P 500)

Proyecto final de la materia **Ingeniería de Algoritmos**.  
Desarrollamos una aplicación de escritorio en Python que permite analizar un ETF del S&P 500 usando diferentes técnicas algorítmicas (Fuerza Bruta, Divide y Vencerás, Programación Dinámica, Árboles de Expansión Mínima y un algoritmo Greedy de diversificación). [attached_file:6]

La idea es mostrar cómo los algoritmos que vemos en clase pueden aplicarse a un problema real: **armar y analizar portafolios de inversión** de forma interactiva.

---

##  Descripción general del proyecto

La herramienta carga un archivo CSV con las empresas del S&P 500 (símbolo, nombre y sector) y ofrece cuatro módulos principales:

1. **Fuerza Bruta (Portafolio)**  
   - Prueba muchas combinaciones posibles de pesos entre 1 y 5 activos.  
   - Calcula rendimiento, “riesgo” aproximado y un Sharpe simplificado.  
   - Muestra qué combinación de pesos tiene mejor relación ganancia/riesgo.

2. **Mejor Empresa (Divide y Vencerás vs Programación Dinámica)**  
   - Descarga datos históricos de cada empresa.  
   - Calcula rendimiento anual, volatilidad y ratio de Sharpe.  
   - Compara dos algoritmos (DyV y DP) para encontrar la mejor empresa y grafica tiempos de ejecución en función del número de empresas. 

3. **Prim/Kruskal AEM (Árbol de Expansión Mínima)**  
   - Calcula correlaciones entre los rendimientos de las empresas.  
   - Transforma correlaciones en distancias y construye el Árbol de Expansión Mínima con Prim y Kruskal.  
   - Muestra grafos donde los nodos son empresas y el color representa el sector (clusters por comportamiento similar).

4. **Greedy Correlación Mínima**  
   - Construye un portafolio seleccionando iterativamente la empresa menos correlacionada con las ya elegidas.  
   - Busca maximizar la diversificación (correlación promedio baja).  
   - Muestra lista ordenada de empresas y gráficos de evolución de la correlación y distribución por sectores.

La interfaz gráfica está hecha con **CustomTkinter** y usa **matplotlib** para las visualizaciones. 

---

##  Tecnologías y dependencias

Lenguaje principal: **Python 3.10+**

Dependencias principales del proyecto:

- `customtkinter`
- `tkinter` (viene con Python estándar)
- `pandas`
- `numpy`
- `yfinance`
- `matplotlib`
- `networkx`
- `threading` y `time` (módulos estándar)
- `warnings` (módulo estándar)
- `scipy`


##  Uso rápido de la aplicación / Ejecucion

1. **Cargar CSV del S&P 500**
   - Haz clic en el botón **“Cargar CSV S&P500”**.
   - Selecciona un archivo `.csv` que contenga columnas al menos: `Symbol, Name, Sector`.
   - Si todo sale bien, en el menú lateral verás el mensaje **“Archivo cargado y listo.”**.

2. **Módulo Fuerza Bruta (Portafolio)**
   - Ingresa número de activos (1–5), pasos de discretización y tasa libre de riesgo.
   - Especifica rendimiento esperado y volatilidad de cada activo.
   - Presiona **“Optimizar”** para ver:
     - Pesos óptimos por activo.
     - Rendimiento y volatilidad aproximada de la cartera.
     - Sharpe simplificado.

3. **Módulo Mejor Empresa (DV || DP)**
   - Requiere tener cargado el CSV.
   - Haz clic en **“Analizar empresas”**.
   - El módulo descargará precios, calculará métricas y mostrará:
     - Mejor empresa para Divide y Vencerás.
     - Mejor empresa para Programación Dinámica.
     - Gráfica comparando tiempo de ejecución de ambos algoritmos según el número de empresas. [attached_file:6]

4. **Módulo Prim/Kruskal AEM**
   - Clic en **“Generar Grafo AEM”**.
   - Se descargan precios de las empresas y se calcula la matriz de correlaciones. [attached_file:6]
   - Se construyen los árboles con Prim y Kruskal y se muestran en ventanas de matplotlib:
     - Nodos = empresas.
     - Color = sector.
     - Aristas = relaciones más fuertes (distancia mínima).

5. **Módulo Greedy Correlación Mín.**
   - Elige el número de activos que quieres en el portafolio (10, 20, 30, etc.).
   - Clic en **“Analizar portafolio”**.
   - Verás:
     - Lista ordenada de empresas seleccionadas, su sector y correlación promedio al momento de ser añadidas.
     - Gráfico de cómo aumenta la correlación al añadir más activos.
     - Gráfico de barras con número de empresas por sector.

---

##  Objetivs

Este proyecto busca:

- Aplicar en contexto real los algoritmos vistos en clase (Fuerza Bruta, Divide y Vencerás, Programación Dinámica, Prim, Kruskal y Greedy).  
- Entender en la práctica temas como complejidad, rendimiento vs exactitud y visualización de datos.  
- Mostrar que conceptos de teoría de algoritmos pueden usarse para problemas reales de finanzas y manejo de portafolios.

---

##  Autores

- Estudiante(s): Adrian Perdomo y Abraham Garcia
- Universidad: CUCEI





