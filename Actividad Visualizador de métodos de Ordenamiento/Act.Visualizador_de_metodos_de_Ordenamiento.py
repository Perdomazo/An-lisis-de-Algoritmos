import tkinter as tk
import random
import time
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

ANCHO = 800
ALTO = 300
N_BARRAS = 100
VAL_MIN, VAL_MAX = 5, 100
RETARDO_MS = 1

#algoritmos con animacion
def selectionsort(data, draw_callback):
    n = len(data)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            draw_callback(activos=[i, j, min_idx]); yield
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
        draw_callback(activos=[i, min_idx]); yield
    draw_callback(activos=[])

def bubblesort(data, draw_callback):
    n = len(data)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            draw_callback(activos=[j, j + 1]); yield
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    draw_callback(activos=[])

def mergesort(data, draw_callback, start, end):
    if end - start <= 1:
        return
    medio = (start + end) // 2
    yield from mergesort(data, draw_callback, start, medio)
    yield from mergesort(data, draw_callback, medio, end)

    aux = []
    i, j = start, medio
    while i < medio and j < end:
        if data[i] < data[j]:
            aux.append(data[i]); i += 1
        else:
            aux.append(data[j]); j += 1
        draw_callback(activos=list(range(i, j))); yield
    while i < medio:
        aux.append(data[i]); i += 1
        draw_callback(activos=[i - 1]); yield
    while j < end:
        aux.append(data[j]); j += 1
        draw_callback(activos=[j - 1]); yield
    for k, val in enumerate(aux):
        data[start + k] = val
        draw_callback(activos=[start + k]); yield

def quicksort(datos, start, end, draw_callback):
    if start < end:
        p_gen = particion(datos, start, end, draw_callback)
        try:
            while True:
                next(p_gen)
                yield
        except StopIteration as e:
            p = e.value
            if p is None:
                return
        yield from quicksort(datos, start, p - 1, draw_callback)
        yield from quicksort(datos, p + 1, end, draw_callback)

def particion(arr, start, end, draw_callback):
    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            draw_callback(activos=[i, j, end]); yield
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    draw_callback(activos=[i + 1, end]); yield
    return i + 1

#algoritmos sin animacion. (para medir tiempos)
def selectionsort_noanim(a):
    data = a[:]
    n = len(data)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
    return data

def bubblesort_noanim(a):
    data = a[:]
    n = len(data)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

def mergesort_noanim(a):
    data = a[:]
    def _merge_sort(lst):
        if len(lst) <= 1:
            return lst
        m = len(lst) // 2
        left = _merge_sort(lst[:m])
        right = _merge_sort(lst[m:])
        return _merge(left, right)
    def _merge(L, R):
        i = j = 0
        res = []
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                res.append(L[i]); i += 1
            else:
                res.append(R[j]); j += 1
        res.extend(L[i:]); res.extend(R[j:])
        return res
    return _merge_sort(data)

def quicksort_noanim(a):
    data = a[:]
    def _qs(lst, lo, hi):
        if lo >= hi:
            return
        p = _part(lst, lo, hi)
        _qs(lst, lo, p - 1)
        _qs(lst, p + 1, hi)
    def _part(lst, lo, hi):
        pivot = lst[hi]
        i = lo - 1
        for j in range(lo, hi):
            if lst[j] <= pivot:
                i += 1
                lst[i], lst[j] = lst[j], lst[i]
        lst[i + 1], lst[hi] = lst[hi], lst[i + 1]
        return i + 1
    _qs(data, 0, len(data) - 1)
    return data

#barras
def dibujar_barras(canvas, datos, activos=None):
    canvas.delete("all")
    if not datos:
        return
    n = len(datos)
    margen = 10
    ancho_disp = ANCHO - 2 * margen
    alto_disp = ALTO - 2 * margen
    w = ancho_disp / n
    esc = alto_disp / max(datos)
    for i, v in enumerate(datos):
        x0 = margen + i * w
        x1 = x0 + w * 0.9
        h = v * esc
        y0 = ALTO - margen - h
        y1 = ALTO - margen
        color = "#46b5f5"
        if activos and i in activos:
            color = "#fd8f00"
        canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="")
    canvas.create_text(6, 6, anchor="nw", text=f"n={len(datos)}", fill="#666")


datos = []
root = tk.Tk()
root.title("Visualizador - Algoritmos")

#canvas de barras
canvas = tk.Canvas(root, width=ANCHO, height=ALTO, bg="white")
canvas.pack(padx=10, pady=(10, 6))  # pequeño espacio inferior

def generar():
    global datos
    random.seed(time.time())
    datos = [random.randint(VAL_MIN, VAL_MAX) for _ in range(N_BARRAS)]
    dibujar_barras(canvas, datos)

#para guardar tiempos
tiempos_hist = {
    "Selection Sort": [],
    "Bubble Sort": [],
    "Merge Sort": [],
    "Quick Sort": []
}

#figuras y canvas del matplotlib
fig, ax = plt.subplots(figsize=(7, 3))
ax.set_title("Promedio acumulado de tiempos por algoritmo")
ax.set_xlabel("Ejecución (k)")
ax.set_ylabel("Tiempo promedio (segundos)")
ax.grid(True)

lineas = {
    "Selection Sort": None,
    "Bubble Sort": None,
    "Merge Sort": None,
    "Quick Sort": None
}

canvas_fig = FigureCanvasTkAgg(fig, master=root)

def _promedios_acumulados(vals):
    proms = []
    s = 0.0
    for i, v in enumerate(vals, start=1):
        s += v
        proms.append(s / i)
    return proms

def actualizar_grafica():
    """Genera/actualiza la gráfica comparativa bajo demanda."""
    ax.clear()
    ax.set_title("Promedio acumulado de tiempos por algoritmo")
    ax.set_xlabel("Ejecución (k)")
    ax.set_ylabel("Tiempo promedio (segundos)")
    ax.grid(True)

    hay_series = False
    for nombre, lista in tiempos_hist.items():
        if not lista:
            continue
        y = _promedios_acumulados(lista)
        x = list(range(1, len(y) + 1))
        lineas[nombre], = ax.plot(x, y, label=nombre)
        hay_series = True

    if hay_series:
        ax.legend(loc="upper right")

    fig.tight_layout()
    canvas_fig.draw()

#botones para el visualizador
panel_botones = tk.Frame(root)
panel_botones.pack(pady=4)
tk.Button(panel_botones, text="Generar", command=generar).pack(side="left", padx=5)
tk.Button(panel_botones, text="Mezclar", command=lambda: (random.shuffle(datos), dibujar_barras(canvas, datos))).pack(side="left", padx=5)
tk.Button(panel_botones, text="Limpiar", command=lambda: dibujar_barras(canvas, datos, activos=[])).pack(side="left", padx=5)

# Selección de algoritmo
panel_sel = tk.Frame(root)
panel_sel.pack(pady=4)

clicked = tk.StringVar()
clicked.set("Selection Sort")
tk.Label(panel_sel, text="Algoritmo:").pack(side="left", padx=(0, 5))
tk.OptionMenu(panel_sel, clicked, "Selection Sort", "Merge Sort", "Bubble Sort", "Quick Sort").pack(side="left", padx=5)

def medir_tiempo(algoritmo, datos_lista):
    inicio = time.perf_counter()
    if algoritmo == "Selection Sort":
        selectionsort_noanim(datos_lista)
    elif algoritmo == "Bubble Sort":
        bubblesort_noanim(datos_lista)
    elif algoritmo == "Merge Sort":
        mergesort_noanim(datos_lista)
    elif algoritmo == "Quick Sort":
        quicksort_noanim(datos_lista)
    else:
        return None
    fin = time.perf_counter()
    return fin - inicio

def ordenar_selection():
    if not datos: return
    gen = selectionsort(datos, lambda activos=None: dibujar_barras(canvas, datos, activos))
    def paso():
        try:
            next(gen); root.after(RETARDO_MS, paso)
        except StopIteration:
            pass
    paso()

def ordenar_bubble():
    if not datos: return
    gen = bubblesort(datos, lambda activos=None: dibujar_barras(canvas, datos, activos))
    def paso():
        try:
            next(gen); root.after(RETARDO_MS, paso)
        except StopIteration:
            pass
    paso()

def ordenar_mergesort():
    if not datos: return
    gen = mergesort(datos, lambda activos=None: dibujar_barras(canvas, datos, activos), 0, len(datos))
    def paso():
        try:
            next(gen); root.after(RETARDO_MS, paso)
        except StopIteration:
            pass
    paso()

def ordenar_quicksort():
    if not datos: return
    gen = quicksort(datos, 0, len(datos) - 1, lambda activos=None: dibujar_barras(canvas, datos, activos))
    def paso():
        try:
            next(gen); root.after(RETARDO_MS, paso)
        except StopIteration:
            pass
    paso()

def visualizar_algoritmo():
    algoritmo = clicked.get()
    if not datos:
        return
    t = medir_tiempo(algoritmo, datos[:]) 
    if t is not None:
        tiempos_hist[algoritmo].append(t)
    # Solo animación
    if algoritmo == "Selection Sort":
        ordenar_selection()
    elif algoritmo == "Merge Sort":
        ordenar_mergesort()
    elif algoritmo == "Bubble Sort":
        ordenar_bubble()
    elif algoritmo == "Quick Sort":
        ordenar_quicksort()

tk.Button(panel_sel, text="Visualizar algoritmo seleccionado", command=visualizar_algoritmo).pack(side="left", padx=8)

# Controles de cantidad y velocidad
panel_ctrl = tk.Frame(root)
panel_ctrl.pack(pady=4)

tk.Label(panel_ctrl, text="Cantidad de barras:").pack(side="left", padx=(0,5))
entry_n_barras = tk.Entry(panel_ctrl, width=6)
entry_n_barras.insert(0, str(N_BARRAS))
entry_n_barras.pack(side="left", padx=5)

def aplicar_n_barras():
    global N_BARRAS
    try:
        n = int(entry_n_barras.get())
        if n > 0:
            N_BARRAS = n
            generar()
        else:
            print("Ingresa un número positivo")
    except ValueError:
        print("Ingresa un número válido")

tk.Button(panel_ctrl, text="Aplicar Cantidad", command=aplicar_n_barras).pack(side="left", padx=8)

escala = tk.Scale(panel_ctrl, from_=0, to=200, orient="horizontal", label="Velocidad (ms)", length=150)
escala.set(RETARDO_MS)
escala.pack(side="left", padx=5)

def aplicar_ms():
    global RETARDO_MS
    try:
        RETARDO_MS = int(escala.get())
        print("Velocidad aplicada")
    except ValueError:
        print("Ingresa un número válido")

tk.Button(panel_ctrl, text="Aplicar velocidad", command=aplicar_ms).pack(side="left", padx=8)

#grafica
canvas_fig.get_tk_widget().pack(padx=10, pady=(8, 6), fill="x")
fig.tight_layout()
canvas_fig.draw()  # ejes listos; no se grafica nada hasta que lo pidas

#boton grafica comparativa
panel_graf = tk.Frame(root)
panel_graf.pack(pady=(2, 10))
tk.Button(panel_graf, text="Generar gráfica comparativa", command=actualizar_grafica)\
  .pack(side="left", padx=5)

generar()
root.mainloop()
