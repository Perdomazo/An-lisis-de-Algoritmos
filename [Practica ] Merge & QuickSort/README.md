# Algoritmos de Ordenamiento: Quick Sort y Merge Sort

Este repositorio contiene implementaciones en Python de dos algoritmos de ordenamiento fundamentales: **Quick Sort** y **Merge Sort**.

---

## Estructura del Proyecto

El archivo principal (`[main.py]`) incluye las siguientes funciones:

### 1. Quick Sort

La función `quick_sort(arr)` implementa el algoritmo de ordenamiento rápido utilizando una estrategia recursiva de **Divide y Vencerás**. Se selecciona el elemento central como **pivote** y se particiona la lista en sublistas menores, iguales y mayores al pivote.

* **Función:** `quick_sort(arr)`
* **Complejidad:** O(n log n) en promedio.

### 2. Merge Sort

Implementación del algoritmo de ordenamiento por mezcla. Este algoritmo garantiza una complejidad de tiempo estable.

* **Función de División y Llamada Recursiva:** `merge_sort(arr)`
* **Función de Mezcla y Ordenación:** `merge(arr, left_half, right_half)`
* **Complejidad:** O(n log n) en el peor caso.

---

## Requisitos y Uso

### Requisitos

Necesitas tener **Python 3.x** instalado.

### Instalación y Ejecución

1.  Clona el repositorio en tu máquina local:

2.  Navega al directorio del proyecto.
3.  Ejecuta el script. El programa solicitará el tamaño de la lista y sus elementos para realizar el ordenamiento.
    ```bash
    python [main.py]
    ```

Lista ingresada antes de quicksort y mergesort:  ['1', '3', '4', '6', '9', '2', '12', '29', '32', '5', '7', '16', '23', '23', '46']
Arreglo ordenado por QuickSort: ['1', '12', '16', '2', '23', '23', '29', '3', '32', '4', '46', '5', '6', '7', '9']
Arreglo ordenado por QuickSort: ['1', '12', '16', '2', '23', '23', '29', '3', '32', '4', '46', '5', '6', '7', '9']
