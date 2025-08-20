import tkinter as tk 
import numpy as np
import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class MyGUI:

    def __init__(self):

        self.root = tk.Tk()
        self.menubar = tk.Menu(self.root)
        self.root.config(menu=self.menubar)
        self.root.title("Comparador de Algoritmos")

        self.root.geometry("800x1000")

        self.tamanio = tk.IntVar()

        self.boton = tk.Button(self.root, text="Generar Datos", font=('Arial', 16), command=self.generarDatos)
        self.boton.pack(padx=10, pady=10)

        tk.Radiobutton(self.root, text="100", font=('Arial', 16), variable=self.tamanio, value=100).pack(padx=10, pady=10)
        tk.Radiobutton(self.root, text="1000", font=('Arial', 16), variable=self.tamanio, value=1000).pack(padx=10, pady=10)
        tk.Radiobutton(self.root, text="10000", font=('Arial', 16), variable=self.tamanio, value=10000).pack(padx=10, pady=10)
        tk.Radiobutton(self.root, text="100000", font=('Arial', 16), variable=self.tamanio, value=100000).pack(padx=10, pady=10)

        self.resultados = tk.Label(self.root, text="", font=('Arial', 16), )
        self.resultados.pack(padx=10, pady=10)

        self.resultadoBusqueda = tk.Label(self.root, text="", font=('Arial', 12))
        self.resultadoBusqueda.pack()

        self.datos = []

        self.ingresaDatos = tk.Label(self.root, text="Ingresa Dato a Buscar" ,font=('Arial', 19))
        self.ingresaDatos.pack()

        self.entradaDatos = tk.Entry(self.root, font=('Arial', 12), bg = "light blue",  width=(10) )
        self.entradaDatos.pack()

        self.botonBusquedaLineal = tk.Button(self.root, text="Busqueda Lineal", font=('Arial', 12), command=self.busquedaLineal)
        self.botonBusquedaLineal.pack()

        self.botonBusquedaBinaria = tk.Button(self.root, text="Busqueda Binaria", font=('Arial', 12), command=self.busquedaBinaria)
        self.botonBusquedaBinaria.pack()

        self.graph_frame = tk.Frame(self.root)
        self.graph_frame.pack(padx=10, pady=20)


        #recuadro de arriba a la izquierda
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Generar Gráfica", menu=self.filemenu)
        self.filemenu.add_command(label="Generar Gráfica", command=self.grafica)

        self.graph_canvas = None 



        self.root.mainloop()


    def generarDatos (self):
        self.tamanioLista = self.tamanio.get()

        if self.tamanioLista > 0:
            #genera un rango de numeros que es el doble de la lista para que haya variedad de numeros.
            self.datos = np.random.randint(0, self.tamanioLista * 2, size = self.tamanioLista) 

            #ordena
            self.datos.sort()
            self.resultados.config(text=f"Lista de tamaño {self.tamanioLista} generada y ordenada.")
            print(f"Lista generada (primeros 10 elementos): {self.datos[:10]}")

        else:
            self.resultados.config(text="Seleccione un tamaño primero")
        
        print(f"Los datos son: {self.datos}")

    def busquedaLineal (self):

        self.resultadoBusqueda.config(text="")

        if len(self.datos) == 0:
            self.resultados.config(text="Genera la lista de datos primero.")
            return
        
        try:
            datoBuscar = int(self.entradaDatos.get())#de string lo paso a interger para poder == comparar
        except ValueError:
            self.resultadoBusqueda.config(text="Ingrese un numero Válido")
            return
        
        inicio = time.perf_counter()

        
        encontrado = False
        index = -1

        for i in range(len(self.datos)):    
            if self.datos[i] == datoBuscar:
                encontrado = True
                index = i #indice, puesto, lugar
                break 

        fin = time.perf_counter() 
        tiempo_ejecucion = (fin - inicio) * 1000

        if encontrado:
            self.resultadoBusqueda.config(text=f"Dato encontrado en la posición {index+1}, \nTiempo: {tiempo_ejecucion:.6f} ms.")
        else:
            self.resultadoBusqueda.config(text=f"Dato no encontrado.\nTiempo: {tiempo_ejecucion:.6f} ms.")

        

                
    def busquedaBinaria(self):
        self.resultadoBusqueda.config(text="")
        
        if len(self.datos) == 0:
            self.resultados.config(text="Genera la lista de datos primero.")
            return

        try:
            datoBuscar = int(self.entradaDatos.get())
        except ValueError:
            self.resultadoBusqueda.config(text="Ingrese un número válido.")
            return

        #medición del tiempo
        inicio = time.perf_counter() 
        
        #logica de la búsqueda binaria
        izquierda, derecha = 0, len(self.datos) - 1
        encontrado = False
        
        while izquierda <= derecha:
            medio = (izquierda + derecha) // 2
            
            if self.datos[medio] == datoBuscar:
                encontrado = True
                break
            elif self.datos[medio] < datoBuscar:
                izquierda = medio + 1
            else:
                derecha = medio - 1
        
        fin = time.perf_counter() 
        tiempo_ejecucion = (fin - inicio) * 1000 #convierte a milisegundos

        if encontrado:
            self.resultadoBusqueda.config(text=f"Dato encontrado en la posición {medio+1}.\nTiempo: {tiempo_ejecucion:.6f} ms")
        else:
            self.resultadoBusqueda.config(text=f"Dato no encontrado.\nTiempo: {tiempo_ejecucion:.6f} ms")
        
    def grafica(self):
        
        #Punto a destacar, se dividen logicas, la generacion y las busquedas ya hechas son exclusivamente para la logica de la GUI y los nuevos algoritmos
        #repetidos en esta funcion son para la logica de la grafica, atendiendo al principio fundamental de poo. =)

        tamanos = [100, 1000, 10000, 100000]
        tiemposLineal = []
        tiemposBinario = []
        repeticiones = 5
    
        #Nueva generacion de lista
        for tam in tamanos:
           
            datos_prueba = np.random.randint(0, tam * 2, size=tam)
            datos_prueba.sort()
            dato_a_buscar = datos_prueba[np.random.randint(0, tam)] 

            # listas temporales para los tiempos de esta corrida
            tiempos_corrida_lineal = []
            tiempos_corrida_binaria = []
        
            
            for _ in range(repeticiones):
                # medir y guardar tiempo para busqueda Lineal
                inicio_lineal = time.perf_counter()
                # logica del algoritmo de busqueda lineal
                for i in range(len(datos_prueba)):
                    if datos_prueba[i] == dato_a_buscar:
                        break
                fin_lineal = time.perf_counter()
                tiempos_corrida_lineal.append((fin_lineal - inicio_lineal) * 1000)

                #medir y guardar tiempo para busqueda Binaria
                inicio_binaria = time.perf_counter()
                # logica del algoritmo de búsqueda binaria
                izquierda, derecha = 0, len(datos_prueba) - 1
                while izquierda <= derecha:
                    medio = (izquierda + derecha) // 2
                    if datos_prueba[medio] == dato_a_buscar:
                        break
                    elif datos_prueba[medio] < dato_a_buscar:
                        izquierda = medio + 1
                    else:
                        derecha = medio - 1
                fin_binaria = time.perf_counter()
                tiempos_corrida_binaria.append((fin_binaria - inicio_binaria) * 1000)

            # promediado
            promedio_lineal = sum(tiempos_corrida_lineal) / repeticiones
            promedio_binario = sum(tiempos_corrida_binaria) / repeticiones

            tiemposLineal.append(promedio_lineal)
            tiemposBinario.append(promedio_binario)
    
        # dibujar la gráfica
        if self.graph_canvas:
            self.graph_canvas.get_tk_widget().destroy()

        fig, ax = plt.subplots(figsize=(7, 5), dpi=100)

        ax.plot(tamanos, tiemposLineal, marker='o', label='Búsqueda Lineal')
        ax.plot(tamanos, tiemposBinario, marker='o', label='Búsqueda Binaria')
    
        ax.set_xscale('log')
        ax.set_xticks(tamanos)
        ax.set_xticklabels([f'{t:,}' for t in tamanos])


        ax.set_title('Comparación de Tiempos de Búsqueda')
        ax.set_xlabel('Tamaño de la Lista')
        ax.set_ylabel('Tiempo Promedio (ms)')
        ax.legend()
        ax.grid(True)
    
        self.graph_canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        self.graph_canvas.draw()
        self.graph_canvas.get_tk_widget().pack()
            
MyGUI()
