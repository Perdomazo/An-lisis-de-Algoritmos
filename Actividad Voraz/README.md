Comparación de MST: Prim vs Kruskal (Tkinter + Matplotlib)
Este proyecto implementa y compara dos algoritmos clásicos para encontrar árboles de expansión mínima (MST) en un grafo no dirigido y ponderado: Prim y Kruskal.​
Además de imprimir las aristas seleccionadas y el peso total de cada MST en consola, muestra una gráfica de barras en una ventana Tkinter con el peso total obtenido por cada algoritmo.​

Requisitos
Python 3.x

Librerías:

matplotlib para la gráfica de barras embebida.​

tkinter para la interfaz gráfica.​

Instalación de Matplotlib (si no lo tienes):

bash
pip install matplotlib
Descripción del código
El grafo se define mediante:

Un diccionario de listas de adyacencia grafo (nodo → lista de (vecino, peso)).

Una lista aristas con tuplas (u, v, peso) para usar en Kruskal.​

prim_mst(grafo, inicio): usa una cola de prioridad (heapq) para seleccionar siempre la arista de menor peso que conecta el MST actual con un nuevo nodo, acumulando las aristas y el peso total.​

kruskal_mst(aristas): ordena las aristas por peso y utiliza Union-Find (find y union con compresión de caminos y unión por rango) para ir agregando aristas que no formen ciclos hasta construir el MST.​

Interfaz gráfica
Se crea una ventana Tkinter con título "Comparacion MST: Prim vs Kruskal".​

Se genera una figura de Matplotlib (Figure) con un gráfico de barras que muestra el peso total del MST de Prim y de Kruskal, y se incrusta en la ventana mediante FigureCanvasTkAgg.​

La ventana se mantiene abierta con root.mainloop() para visualizar la comparación.

Uso
Ejecuta el script:

bash
python nombre_del_archivo.py
En la terminal verás:

Las aristas que forman el MST según Prim y su peso total.

Las aristas que forman el MST según Kruskal y su peso total.

Se abrirá una ventana con una gráfica de barras comparando el peso total del MST de ambos algoritmos para el grafo definido en el código.
