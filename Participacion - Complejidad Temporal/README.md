Comparación de algoritmos de ordenamiento en Python
Este proyecto implementa y compara el tiempo de ejecución de tres algoritmos de ordenamiento clásicos:

Bubble Sort

Merge Sort

Quick Sort

El programa genera listas de distintos tamaños, mide el tiempo que tarda cada algoritmo en ordenarlas y muestra una gráfica con los resultados.

Requisitos
Python 3.x

Las siguientes librerías de Python:

numpy

matplotlib

Opcionalmente, el código importa tkinter, pero en esta versión no se utiliza la interfaz gráfica.

Instalación
Clona o descarga este repositorio y entra a la carpeta del proyecto:

bash
git clone <URL_DEL_REPOSITORIO>
cd <CARPETA_DEL_PROYECTO>
Instala las dependencias necesarias:

bash
pip install numpy matplotlib
Uso
Ejecuta el script principal:

bash
python nombre_del_archivo.py
Al correr el programa se generará una gráfica que muestra el tiempo de ejecución (en milisegundos) de cada algoritmo en función del tamaño de la lista.

Estructura del código
generarDatos(tamanioLista): genera un arreglo de enteros aleatorios de tamaño N.

bubblesort(datos): implementa el algoritmo de Bubble Sort.

mergesort(datos): implementa el algoritmo de Merge Sort mediante recursión.

quicksort(datos, start, end): implementa el algoritmo de Quick Sort con partición.

generar_grafica(): mide los tiempos de ejecución de cada algoritmo para distintos tamaños de lista y muestra la gráfica comparativa.
