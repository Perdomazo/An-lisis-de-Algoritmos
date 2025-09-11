Visualizador de Métodos de Ordenamiento (Tkinter + Matplotlib)
Aplicación en Python que visualiza y compara cuatro algoritmos de ordenamiento con animación paso a paso y gráfica del tiempo promedio acumulado por algoritmo.

Características
Visualización animada de:

Selection Sort
Bubble Sort
Merge Sort
Quick Sort

Dropdown para elegir algoritmo
Botones: Generar, Mezclar (shuffle), Limpiar
Entry para cambiar N (número de barras)
Scale para ajustar velocidad (0–200 ms)
Gráfica incrustada (Matplotlib) con promedio acumulado de tiempos “puros” (sin animación)


Requisitos
Python 3.10+
Tkinter (incluido en instalación estándar)
Matplotlib

Instalación
bash
# Clonar el repositorio
git clone https://github.com/usuario/visualizador-ordenamiento.git
cd visualizador-ordenamiento

# Crear entorno virtual (opcional)
python -m venv .venv
# Linux/Mac
source .venv/bin/activate
# Windows
.venv\Scripts\activate

# Instalar dependencias
pip install matplotlib
Ejecución
bash
python Act.-Visualizador-de-metodos-de-Ordenamiento.py

USO:
Clic en “Generar” para crear la lista aleatoria con N barras.
Elige algoritmo en el menú desplegable.
Clic en “Visualizar algoritmo seleccionado”:
Primero se mide tiempo “puro” en una copia sin animación y se actualiza la gráfica.
Luego corre la animación en el canvas.
“Mezclar” baraja la lista actual; “Limpiar” quita los resaltados.
Cambia N con el Entry + “Aplicar Cantidad”.
Ajusta la velocidad con el Scale + “Aplicar velocidad”.

Estructura del código
Algoritmos animados como generadores con yield y draw_callback para resaltar pasos.

Versiones sin animación para medir tiempos con time.perf_counter().

Gráfica Matplotlib embebida con backend TkAgg; se actualiza con el promedio acumulado por algoritmo.
