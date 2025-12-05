import math
import tkinter as tk
from tkinter import messagebox


def Dist(p1, p2):
    x = (p1[0] - p2[0])
    x2 = pow(x, 2)
    y = (p1[1] - p2[1])
    y2 = pow(y, 2)
    temp = x2 + y2
    distance = math.sqrt(temp)
    return distance


def comparacion(puntos):

    if len(puntos) < 2:
        return None, None


    menor_distancia = float('inf')
    par_cercano = None

    for i in range(len(puntos)):
        p1 = puntos[i]
        for j in range(i + 1, len(puntos)):
            p2 = puntos[j]
            distancia = Dist(p1, p2)

            if distancia < menor_distancia:
                menor_distancia = distancia
                par_cercano = (p1, p2)
    
    return par_cercano, menor_distancia


def ejecutar():

    try:

        puntos = eval(f"[{entrada_puntos.get()}]")

        par_mas_cercano, distancia_menor = comparacion(puntos)
        
        if par_mas_cercano is not None:

            resultado_etiqueta.config(text=f"El par de puntos más cercano es: {par_mas_cercano}\nLa distancia es: {distancia_menor:.4f}")
        else:
            resultado_etiqueta.config(text="Ingresa al menos 2 puntos.")
            
    except (SyntaxError, IndexError, TypeError):
        messagebox.showerror("Error")


root = tk.Tk()
root.title("Par de Puntos Más Cercano")

etiqueta_instruccion = tk.Label(root, text="Ingresa los puntos: (x1,y1), (x2,y2), ...")
etiqueta_instruccion.pack(pady=5)

entrada_puntos = tk.Entry(root, width=40)
entrada_puntos.insert(0, "(8,2), (16,5), (10,20), (2,9), (1,3)")
entrada_puntos.pack(pady=5)

boton_calcular = tk.Button(root, text="Calcular", command=ejecutar)
boton_calcular.pack(pady=5)

resultado_etiqueta = tk.Label(root, text="", font=("Helvetica", 12))
resultado_etiqueta.pack(pady=10)

root.mainloop()
