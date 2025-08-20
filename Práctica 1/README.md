Proyecto: Comparador de Algoritmos de Búsqueda
Este proyecto implementa una aplicación de escritorio con Python para comparar el rendimiento de los algoritmos de búsqueda lineal y binaria. La interfaz gráfica de usuario (GUI) permite generar listas de diferentes tamaños, buscar un elemento en ellas y visualizar una gráfica comparativa de los tiempos de ejecución.

Requisitos
Para ejecutar el programa, necesitarás tener instalado:

Python 3.10 o superior 
Las siguientes librerías de Python: tkinter, numpy, y matplotlib.
El proyecto fue desarrollado en un entorno virtual para asegurar la portabilidad de las dependencias.
Instrucciones de Ejecución
Sigue estos pasos para instalar las dependencias y ejecutar la aplicación desde la terminal.

Clonar el repositorio:
Bash
git clone https://www.youtube.com/watch?v=3GymExBkKjE
cd Practica1

Crear y activar el entorno virtual:
Bash
python3 -m venv venv
source venv/bin/activate

Instalar las librerías necesarias:
Bash
pip install -r requirements.txt

Ejecutar el programa:
Bash
python3 main.py

Funcionalidades de la GUI 
Generación de datos: Un botón y opciones para crear listas de 100, 1000, 10,000 o 100,000 elementos aleatorios y ordenados.
Búsqueda: Campos para ingresar un valor y botones para realizar la búsqueda lineal y binaria. El resultado y el tiempo de ejecución se muestran en milisegundos.
Comparación Gráfica: Un botón para generar una gráfica de líneas que compara los tiempos promedio de ambos algoritmos. La gráfica se actualiza en la misma ventana. Para los promedios, se realizan 5 repeticiones por cada tamaño de lista.


Estructura de Archivos 
El proyecto contiene la siguiente estructura de archivos:
main.py: El punto de entrada de la aplicación.
requirements.txt: Archivo que lista las dependencias del proyecto.
README.md: Este archivo.

