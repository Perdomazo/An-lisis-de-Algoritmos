Problema del Viajante (TSP) por fuerza bruta en Python
Este proyecto resuelve una versión pequeña del Problema del Viajante (Travelling Salesman Problem, TSP) usando un enfoque de fuerza bruta: se generan todas las posibles rutas que parten de una ciudad origen, visitan todas las demás una sola vez y regresan al origen, y se elige la que tiene el menor costo total.​

Requisitos
Python 3.x

Solo se usa la librería estándar (itertools), no se requieren dependencias externas.​

Descripción del código
Las ciudades se representan por índices enteros: 0, 1, 2, 3.

distancias es una matriz donde distancias[i][j] es el costo de ir de la ciudad i a la ciudad j.​

Se fija una ciudad de origen (origen = 0) y se generan todas las permutaciones posibles de las otras ciudades con itertools.permutations, construyendo rutas del tipo [origen] + perm.​

Para cada ruta:

Se suma la distancia entre ciudades consecutivas.

Se agrega el costo de regresar desde la última ciudad al origen.

Se imprime la ruta con su costo total.

Se mantiene la mejor ruta encontrada (de menor costo) y al final se muestra cuál es y su costo total.​

Uso
Ejecuta el script en una terminal:

bash
python nombre_del_archivo.py
En la salida verás:

Todas las rutas evaluadas con su costo total.

La mejor ruta encontrada y el costo total mínimo para el TSP definido por la matriz de distancias.​

Notas
El enfoque de fuerza bruta garantiza encontrar la ruta óptima, pero escala factorialmente con el número de ciudades, por lo que solo es práctico para instancias pequeñas como este ejemplo de 4 ciudades.​
