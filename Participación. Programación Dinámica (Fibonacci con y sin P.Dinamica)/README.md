Comparación de tiempo y memoria en Fibonacci (iterativo vs. programación dinámica)
Este proyecto mide y grafica el tiempo de ejecución y el uso de memoria de dos formas de calcular la sucesión de Fibonacci: una versión iterativa simple y otra basada en programación dinámica que almacena los valores en una lista.​

Requisitos
Python 3.x

Librerías de Python:

matplotlib para generar las gráficas.​

memory_profiler para medir el uso de memoria con la función memory_usage.​

Instalación de dependencias:

bash
pip install matplotlib memory_profiler
Descripción del código
fib_normal(n): calcula iterativamente la sucesión de Fibonacci hasta n, actualizando dos variables (a y b) sin guardar toda la secuencia.

fib_dinamica(n): construye una lista fib y va agregando cada nuevo término como suma de los dos anteriores, representando un enfoque de programación dinámica.

tiempos_normal(n) y tiempos_dinamica(n): ejecutan cada versión hasta n y registran un arreglo con el tiempo acumulado desde el inicio de la medición en cada paso usando time.perf_counter().​

memoria_traza(func, n, interval): utiliza memory_usage de memory_profiler para obtener una traza del uso de memoria del proceso mientras se ejecuta la función indicada.​

Gráficas generadas
Al ejecutar el script se generan dos figuras:

Tiempo acumulado por N

Eje X: valor de N.

Eje Y: tiempo acumulado en segundos desde el inicio de la ejecución.

Dos curvas: una para la versión normal e iterativa y otra para la versión dinámica, dibujadas con plt.plot y personalizadas con título, etiquetas y rejilla.​

Uso de memoria

Se obtiene una lista de mediciones de memoria para cada enfoque y se grafican ambas series en una sola figura para comparar la huella de memoria entre las dos implementaciones de Fibonacci.​

Uso
Asegúrate de tener instaladas las dependencias.

Ejecuta el script:

bash
python nombre_del_archivo.py
Se abrirán dos ventanas de Matplotlib, una con la gráfica de tiempos y otra con la gráfica de memoria; puedes ajustar el valor de n en el código para probar distintos tamaños de entrada.
