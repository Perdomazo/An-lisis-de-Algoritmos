Par de puntos más cercano en 2D (Tkinter)
Este proyecto implementa un programa en Python que, dado un conjunto de puntos en el plano 2D, encuentra el par de puntos más cercano usando la distancia euclidiana y muestra el resultado en una interfaz gráfica con Tkinter.​

Requisitos
Python 3.x

Módulos estándar de Python:

math (para calcular raíces cuadradas y potencias)​

tkinter y tkinter.messagebox (para la interfaz gráfica y cuadros de diálogo).​

No se necesitan librerías externas adicionales.

Uso
Clona o descarga este repositorio y entra a la carpeta del proyecto:

bash
git clone <URL_DEL_REPOSITORIO>
cd <CARPETA_DEL_PROYECTO>
Ejecuta el script:

bash
python nombre_del_archivo.py
En la ventana que se abre:
En la caja de texto, ingresa los puntos con el formato:
(x1,y1), (x2,y2), (x3,y3), ...

Presiona el botón "Calcular".

El programa mostrará el par de puntos más cercano y la distancia entre ellos en una etiqueta en la misma ventana.​

Descripción del programa
Dist(p1, p2): calcula la distancia euclidiana entre dos puntos p1 y p2 implementado con math.sqrt y pow.​

comparacion(puntos): recorre todos los pares posibles de puntos (algoritmo fuerza bruta  y devuelve el par con menor distancia y su valor numérico.​

ejecutar(): lee el texto ingresado en el Entry, lo convierte en una lista de tuplas, llama a comparacion y actualiza la etiqueta de resultado o muestra un messagebox.showerror si el formato es incorrecto.​

Interfaz gráfica
Se crea una ventana principal con tk.Tk() y se configura el título.​

Se utilizan:

Un Label para las instrucciones.

Un Entry para que el usuario escriba los puntos (con un ejemplo precargado).​

Un Button que ejecuta el cálculo al pulsarse.

Un Label para mostrar el resultado (par más cercano y distancia).​
