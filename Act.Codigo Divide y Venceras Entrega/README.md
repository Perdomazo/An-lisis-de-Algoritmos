Supuesta seleccion de mejor empresa S&P500

Este script genera datos simulados de empresas con rendimiento y volatilidad, selecciona la mejor empresa según reglas simples y grafica el tiempo de ejecución de la función `seleccion` 
en múltiples iteraciones usando `time.perf_counter` para medición precisa en segundos 

# Requisitos

- Python 3.8+ con `pip` disponible en tu sistema  
- Paquetes de Python:
  - matplotlib para graficar 
  - memory-profiler 
  
# Instalación

Se recomienda usar un entorno virtual e instalar las dependencias con `pip` 
python -m venv venv

Windows
venv\Scripts\activate
Linux/macOS
source venv/bin/activate
pip install matplotlib memory-profiler

text
`matplotlib` provee `pyplot` para crear y mostrar la gráfica, y `memory-profiler` satisface el import presente en el archivo aunque no se utilice en esta versión 

# Cómo ejecutar

Ejecuta el script directamente con Python desde el directorio del proyecto 
python main.py

text
Se abrirá una ventana con la figura de Matplotlib mostrando el tiempo por iteración; cierra la ventana para terminar el script si estás en modo interactivo  

# ¿Qué hace el script?

- Genera `N_DATOS` empresas como pares `[id, [rendimiento, volatilidad]]` con valores aleatorios uniformes en 0–1 para simular una fuente de datos 
- Define `es_mejor(a, b)` que prioriza mayor rendimiento y, en caso de empate, menor volatilidad para decidir entre dos empresas
- Implementa `seleccion(lista)` con división recursiva de la lista, comparando los mejores de cada mitad para retornar un único candidato óptimo según las reglas anteriores  
- Mide `ITERACIONES` veces la ejecución de `seleccion(empresas_datos)` usando `time.perf_counter()` antes y después de cada llamada, acumulando la diferencia como tiempo de ejecución en segundos de alta resolución
- Grafica con `matplotlib.pyplot.plot` el tiempo de cada iteración, agrega etiquetas de ejes y cuadrícula, y muestra la figura con `plt.show()` 

# Detalles de medición

`time.perf_counter()` es un contador de alto rendimiento.

# Notas

- Si no deseas instalar `memory-profiler`, elimina la línea `from memory_profiler import memory_usage` del script, ya que no se usa en la gráfica actual
