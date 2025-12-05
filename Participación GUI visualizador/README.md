Visualizador de Selection Sort y Bubble Sort en Tkinter
Este proyecto muestra una visualización gráfica de dos algoritmos de ordenamiento: Selection Sort y Bubble Sort, usando barras dibujadas en un Canvas de Tkinter que se actualizan paso a paso durante la ejecución del algoritmo.​

Requisitos
Python 3.x

Tkinter (viene incluido con la mayoría de instalaciones estándar de Python)

No requiere librerías externas adicionales

Uso
Clona o descarga este repositorio y entra a la carpeta del proyecto:

bash
git clone <URL_DEL_REPOSITORIO>
cd <CARPETA_DEL_PROYECTO>
Ejecuta el script:

bash
python nombre_del_archivo.py
En la ventana que se abre:

Pulsa "Generar" para crear un nuevo conjunto de barras aleatorias.

Pulsa "Ordenar (Selection)" para ver la animación del Selection Sort.

Pulsa "Ordenar (Bubble)" para ver la animación del Bubble Sort.

Descripción del programa
Se generan N_BARRAS valores aleatorios en un rango definido, que se representan como barras verticales en un Canvas de tamaño fijo.​

Cada algoritmo está implementado como un generador que va rindiendo pasos de la animación mediante yield, permitiendo actualizar el dibujo con root.after(RETARDO_MS, paso) para controlar la velocidad.​

Las barras activas (elementos comparados o intercambiados) se destacan con un color diferente para facilitar la comprensión visual del proceso de ordenamiento.​

Estructura principal del código
selection_sort_steps(data, draw_callback): implementación paso a paso del Selection Sort, llamando a draw_callback en cada comparación e intercambio.

bubble_sort_steps(data, draw_callback): implementación paso a paso del Bubble Sort, también animada con yield.

dibujar_barras(canvas, datos, activos=None): redibuja todas las barras en el Canvas, resaltando los índices activos.

Funciones generar(), ordenar_selection() y ordenar_bubble() controlan la generación de datos y el inicio de cada animación.

La interfaz gráfica se construye con Tk(), un Canvas para las barras y un Frame con botones para controlar la visualización.
