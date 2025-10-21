# Comparación de selección de empresa: Divide y Vencerás vs Programación Dinámica

Este proyecto genera datos simulados de empresas y compara el tiempo de ejecución de dos enfoques para elegir la “mejor” empresa:
- Divide y Vencerás (`seleccion`), que divide recursivamente la lista y compara los mejores de cada mitad.
- Recorrido lineal tipo “programación dinámica” (`seleccion_dp`), que itera una sola vez actualizando el mejor candidato.

La medición se realiza con `time.perf_counter()` para precisión de alta resolución, y la visualización se hace con Matplotlib en una gráfica de líneas de tiempo promedio vs tamaño de entrada \(n\) 

# Reglas de selección
Entre dos empresas \(A\) y \(B\):
1) Gana la de mayor rendimiento.  
2) Si empatan en rendimiento, gana la de menor volatilidad.  

Estas reglas se aplican tanto en el proceso recursivo como en el recorrido lineal.

# Requisitos

- Python 3.8+  
- Paquetes:
  - matplotlib (para graficar) 

Instalación recomendada en entorno virtual:
python -m venv venv

Windows
venv\Scripts\activate

Linux/macOS
source venv/bin/activate
pip install matplotlib


# Estructura del script

- `generador()`: crea `N_DATOS` empresas como `[id, [rendimiento, volatilidad]]` con valores aleatorios uniformes en 0–1.  
- `es_mejor(a, b)`: aplica las reglas de comparación descritas.  
- `seleccion(lista)`: estrategia recursiva “divide y vencerás” que retorna el mejor elemento.  
- `seleccion_dp(lista)`: recorrido lineal que mantiene el mejor candidato al pasar por la lista.  
- `tiempo_promedio(func, datos, repeticiones)`: mide el tiempo promedio de ejecutar `func(datos)` repitiendo varias veces usando `time.perf_counter()`  
- Bucle de benchmarking: para tamaños `n` desde 50 hasta `N_DATOS` en pasos de 50, calcula el tiempo promedio de ambas funciones y las grafica.

# Cómo ejecutar

Desde el directorio del proyecto:
python main.py

Se abrirá una ventana con una figura donde:
- Eje X: tamaño de la lista de empresas \(n\).
- Eje Y: tiempo promedio en segundos de la función correspondiente.
- Dos líneas: “Divide y Vencerás” vs “Programación Dinámica”, con leyenda y cuadrícula.

# Detalles de medición

- `time.perf_counter()` es un contador monotónico de alta resolución; el punto de referencia es indefinido, por lo que solo deben usarse diferencias \(t_1 - t_0\) para medir duraciones cortas con precisión [web:6][web:28].  
- Para reducir ruido, se repite cada medición varias veces y se promedia, una práctica estándar para obtener estimaciones más estables en microbenchmarks

# Personalización

- Cambia `N_DATOS` para ajustar el tamaño máximo de los datos generados.  
- Modifica `ITERACIONES` y el argumento `repeticiones` de `tiempo_promedio` para más estabilidad a costa de mayor tiempo total de benchmarking.  
- Ajusta el estilo del gráfico con Matplotlib (marcadores, colores, leyenda) conforme a tus necesidades 
# Referencias

- `time.perf_counter`: temporizador de mayor resolución para benchmarks, monotónico y adecuado para medir duraciones cortas 
- Matplotlib Pyplot: creación de gráficas de líneas y leyendas en una figura simple 
