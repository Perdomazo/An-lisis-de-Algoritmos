import tkinter as tk 
import numpy as np
import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from random import sample 

def generarDatos (tamanioLista):
        

        if tamanioLista > 0:
            #genera un rango de numeros que es el doble de la lista para que haya variedad de numeros.
            datos = np.random.randint(0, tamanioLista * 2, size = tamanioLista) 


            return datos

def bubblesort(datos):
    """Esta función ordenara el vector que le pases como argumento con el Método de Bubble Sort"""

    


    n = len(datos) # Establecemos un contador del largo del vector
    
    inicio = time.perf_counter()
    for i in range(n-1): 
    # Le damos un rango n para que complete el proceso. 
        for j in range(0, n-i-1): 
            # Revisa la matriz de 0 hasta n-i-1
            if datos[j] > datos[j+1] :
                datos[j], datos[j+1] = datos[j+1], datos[j]
            # Se intercambian si el elemento encontrado es mayor 
            # Luego pasa al siguiente
    fin = time.perf_counter() 
    tiempo_ejecucion = (fin - inicio) * 1000



def mergesort(datos):


    
    
    if len(datos) <= 1:
        return datos
    
    medio = len(datos) // 2
    izq = datos[:medio]
    der = datos[medio:]
    

    izq = mergesort(izq)
    der = mergesort(der)
    

    i = j = k = 0
    while i < len(izq) and j < len(der):
        if izq[i] < der[j]:
            datos[k] = izq[i]
            i += 1
        else:
            datos[k] = der[j]
            j += 1
        k += 1
    
    while i < len(izq):
        datos[k] = izq[i]
        i += 1
        k += 1
    
    while j < len(der):
        datos[k] = der[j]
        j += 1
        k += 1
    

    return datos


def quicksort(datos, start, end): #fue acomoadado porq el original estaba mal
    """Función principal y recursiva para Quick Sort."""
    def particion(arr, start, end):
        pivot = arr[end]
        i = start - 1
        for j in range(start, end):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[end] = arr[end], arr[i + 1]
        return i + 1

    if start < end:
        p = particion(datos, start, end)
        quicksort(datos, start, p - 1)
        quicksort(datos, p + 1, end)

def generar_grafica():
    """Mide y grafica el tiempo de ejecución de los algoritmos."""
    # Define los tamaños de lista a probar
    tamanos = list(range(50, 1001, 50))
    tiempos_bubble = []
    tiempos_merge = []
    tiempos_quick = []
    
    for tam in tamanos:

        
        # --- Medir tiempo de Bubble Sort ---
        datos_bubble = generarDatos(tam)
        inicio = time.perf_counter()
        bubblesort(datos_bubble)
        fin = time.perf_counter()
        tiempos_bubble.append((fin - inicio) * 1000)
        
        # --- Medir tiempo de Merge Sort ---
        datos_merge = generarDatos(tam)
        inicio = time.perf_counter()
        mergesort(datos_merge)
        fin = time.perf_counter()
        tiempos_merge.append((fin - inicio) * 1000)
        
        # --- Medir tiempo de Quick Sort ---
        datos_quick = generarDatos(tam)
        inicio = time.perf_counter()
        quicksort(datos_quick, 0, len(datos_quick) - 1)
        fin = time.perf_counter()
        tiempos_quick.append((fin - inicio) * 1000)

    # --- Generar la gráfica ---
    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(tamanos, tiempos_bubble, marker='o', label='Bubble Sort')
    ax.plot(tamanos, tiempos_merge, marker='o', label='Merge Sort')
    ax.plot(tamanos, tiempos_quick, marker='o', label='Quick Sort')

    ax.set_title('Comparación de Tiempos de Algoritmos de Ordenamiento')
    ax.set_xlabel('Tamaño de la Lista (N)')
    ax.set_ylabel('Tiempo de Ejecución (ms)')
    ax.legend()
    ax.grid(True, which="both", ls="--")
    
    plt.tight_layout()
    plt.show()

# --- Llamada a la función principal para generar la gráfica ---
if __name__ == "__main__":
    generar_grafica()
