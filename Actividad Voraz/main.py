import heapq
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


grafo = {
    0: [(1, 4), (2, 3)],
    1: [(0, 4), (2, 1), (3, 2)],
    2: [(0, 3), (1, 1), (3, 4), (4, 3)],
    3: [(1, 2), (2, 4), (4, 5), (5, 1)],
    4: [(2, 3), (3, 5), (5, 7)],
    5: [(3, 1), (4, 7)]
}

aristas = [
    (0, 1, 4),
    (0, 2, 3),
    (1, 2, 1),
    (1, 3, 2),
    (2, 3, 4),
    (2, 4, 3),
    (3, 4, 5),
    (3, 5, 1),
    (4, 5, 7)
]

num_nodos = 6


# Prim usando heap

def prim_mst(grafo, inicio=0):
    visitado = [False] * num_nodos
    heap = []
    # arista entre u y v
    for v, peso in grafo[inicio]:
        heapq.heappush(heap, (peso, inicio, v))
    visitado[inicio] = True

    mst_aristas = []  # mst o arbol de expansion minima
    peso_total = 0

    while heap and len(mst_aristas) < num_nodos - 1:
        peso, u, v = heapq.heappop(heap)
        if visitado[v]:
            continue
        visitado[v] = True
        mst_aristas.append((u, v, peso))
        peso_total += peso

        for w, pw in grafo[v]:
            if not visitado[w]:
                heapq.heappush(heap, (pw, v, w))

    return mst_aristas, peso_total


# Kruskal con Union-Find, es para poder usar el find() y el union()
#find() == find() se salta, find() != find() se agrega con union()

padre = list(range(num_nodos))
rango = [0] * num_nodos


def find(x):
    if padre[x] != x:
        padre[x] = find(padre[x])
    return padre[x]


def union(x, y):
    rx = find(x)
    ry = find(y)
    if rx == ry:
        return
    if rango[rx] < rango[ry]:
        padre[rx] = ry
    elif rango[rx] > rango[ry]:
        padre[ry] = rx
    else:
        padre[ry] = rx
        rango[rx] += 1


def kruskal_mst(aristas):
    # ordenar aristas por peso
    aristas_ordenadas = sorted(aristas, key=lambda x: x[2])

    mst_aristas = []
    peso_total = 0

    for u, v, w in aristas_ordenadas:
        if find(u) != find(v):  # si no forma ciclo
            union(u, v)
            mst_aristas.append((u, v, w))
            peso_total += w
            if len(mst_aristas) == num_nodos - 1:
                break

    return mst_aristas, peso_total


print("=== Algoritmo de Prim (MST) ===")
mst_prim, peso_prim = prim_mst(grafo, inicio=0)
print("Aristas en el MST (Prim):")
for u, v, w in mst_prim:
    print(f"{u} - {v} (peso {w})")
print("Peso total (Prim):", peso_prim)
print()

print("=== Algoritmo de Kruskal (MST) ===")
mst_kruskal, peso_kruskal = kruskal_mst(aristas)
print("Aristas en el MST (Kruskal):")
for u, v, w in mst_kruskal:
    print(f"{u} - {v} (peso {w})")
print("Peso total (Kruskal):", peso_kruskal)
print()

# Tkinter 

root = tk.Tk()
root.title("Comparacion MST: Prim vs Kruskal")

fig = Figure(figsize=(4, 3))
ax = fig.add_subplot(111)
algoritmos = ["Prim", "Kruskal"]
pesos = [peso_prim, peso_kruskal]
ax.bar(algoritmos, pesos, color=["skyblue", "lightgreen"])
ax.set_ylabel("Peso total del MST")
ax.set_title("Comparacion de Prim y Kruskal")
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack()

root.mainloop()
