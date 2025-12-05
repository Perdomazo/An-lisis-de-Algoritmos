Compresión de texto con Huffman (Tkinter)
Este proyecto implementa el algoritmo de compresión de Huffman usando una estrategia voraz y muestra su funcionamiento en una interfaz gráfica desarrollada con Tkinter.​
La aplicación permite cargar un archivo de texto, codificarlo con Huffman, ver el tamaño antes y después de la compresión y decodificar el resultado para verificar que el texto original se recupera correctamente.​

Requisitos
Python 3.x

Módulos estándar:

collections.Counter para calcular frecuencias de caracteres.​

heapq para manejar la cola de prioridad (min-heap) al construir el árbol de Huffman.​

tkinter, filedialog y messagebox para la interfaz gráfica y selección de archivos.​

No se necesitan librerías externas adicionales.

Uso
Ejecuta el script:

bash
python nombre_del_archivo.py
En la ventana de la aplicación:

Haz clic en “Cargar archivo” y selecciona un archivo .txt.​

Haz clic en “Codificar” para:

Construir la tabla de frecuencias.

Generar el árbol y los códigos de Huffman.

Codificar el texto y mostrar:

Tamaño original (en bits).

Tamaño codificado (en bits).

Porcentaje de compresión lograda.

Haz clic en “Decodificar” para reconstruir el texto original a partir del binario y mostrarlo en el área de salida.​

Descripción del algoritmo
Se construye una tabla de frecuencias de caracteres con Counter(texto).​

Con esas frecuencias se arma un árbol de Huffman usando un min-heap (heapq), combinando siempre los dos nodos de menor frecuencia hasta quedar un solo árbol.​

A cada hoja (carácter) se le asigna un código binario según el camino en el árbol: ir a la izquierda agrega 0 y a la derecha 1, lo que produce códigos de longitud variable más cortos para caracteres más frecuentes.​

El texto se codifica concatenando los códigos de cada carácter y se decodifica recorriendo el árbol bit a bit hasta llegar de nuevo a las hojas.​

Interfaz gráfica
Se utiliza una clase AplicacionHuffman que encapsula la ventana principal, botones y área de texto.​

filedialog.askopenfilename se usa para seleccionar el archivo de entrada y Text sirve como zona de salida para mensajes, tamaños y texto decodificado.​
