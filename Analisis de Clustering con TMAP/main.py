import pandas as pd
import numpy as np
import tmap
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min


RUTA_CSV = "/home/adrian/Desktop/Analisis de Algoritmos/TMAP/fashion-mnist_test.csv"

# Cargar datos 
tabla = pd.read_csv(RUTA_CSV)
pixeles = tabla.drop(columns=["label"]).values.astype(np.uint8)
etiquetas = tabla["label"].values

#  binarizar (0/1) para TMAP
pixeles_bin = (pixeles > 0).astype(np.uint8)
n_total = pixeles_bin.shape[0]

# firmas Minhash global con perm=516
perm = 516
lista_vectores = []
for i in range(n_total):
    indices_activos = np.where(pixeles_bin[i] == 1)[0].astype(np.uint32)
    lista_vectores.append(tmap.VectorUint(indices_activos.tolist()))

encoder = tmap.Minhash(perm)
firmas = encoder.batch_from_sparse_binary_array(lista_vectores)

# indice LSHForest + layout TMAP global
bosque = tmap.LSHForest(perm, 128)
bosque.batch_add(firmas)
bosque.index()

cfg = tmap.LayoutConfiguration()
cfg.k = 10
cfg.kc = 30

x, y2, s, t, _ = tmap.layout_from_lsh_forest(
    lsh_forest=bosque, config=cfg, keep_knn=False, create_mst=True, clear_lsh_forest=False
)

# A NumPy para máscaras
x_np = np.array(list(x), dtype=np.float32)
y_np = np.array(list(y2), dtype=np.float32)

# 5) Elegir clase objetivo (Sandals=5) y crear una semilla ampliable en el layout global
clase_objetivo = 5
mask_clase = (etiquetas == clase_objetivo)
idx_clase = np.where(mask_clase)[0]
x_clase = x_np[idx_clase]
y_clase = y_np[idx_clase]

centro_x, centro_y = np.median(x_clase), np.median(y_clase)
rango_x = np.max(x_clase) - np.min(x_clase)
rango_y = np.max(y_clase) - np.min(y_clase)

m_objetivo = 400
fraccion_ventana = 0.30
fraccion_maxima = 1.00
m_semilla = 0
idx_semilla_global = np.array([], dtype=int)

while (m_semilla < m_objetivo) and (fraccion_ventana <= fraccion_maxima):
    medio_x = (rango_x * fraccion_ventana) / 2.0
    medio_y = (rango_y * fraccion_ventana) / 2.0
    xmin, xmax = centro_x - medio_x, centro_x + medio_x
    ymin, ymax = centro_y - medio_y, centro_y + medio_y
    dentro = (x_clase >= xmin) & (x_clase <= xmax) & (y_clase >= ymin) & (y_clase <= ymax)
    idx_local = np.where(dentro)[0]
    idx_semilla_global = idx_clase[idx_local]
    m_semilla = idx_semilla_global.shape[0]
    if m_semilla < m_objetivo:
        fraccion_ventana *= 1.25

print(f"Semilla 'Sandals' seleccionada: m={m_semilla} (fracción final ~{min(fraccion_ventana, fraccion_maxima):.2f})")

# Visual de referencia (restaurada)
plt.figure(figsize=(7,7))
plt.scatter(x_np, y_np, s=1, c="lightgray")
plt.scatter(x_np[idx_clase], y_np[idx_clase], s=2, c="tab:blue", label="Sandals (5)")
plt.scatter(x_np[idx_semilla_global], y_np[idx_semilla_global], s=6, c="tab:red", label="Semilla")
plt.legend(loc="lower right")
plt.title("Subcluster Sandals (global)")
plt.axis("off")
plt.tight_layout()
plt.show()

#  Reaplicar TMAP solo al (subcluster)
X_semilla = pixeles[idx_semilla_global]
Xb_semilla = pixeles_bin[idx_semilla_global]

lista_vectores_semilla = []
for i in range(m_semilla):
    idx_on = np.where(Xb_semilla[i] == 1)[0].astype(np.uint32)
    lista_vectores_semilla.append(tmap.VectorUint(idx_on.tolist()))

encoder2 = tmap.Minhash(perm)
firmas_semilla = encoder2.batch_from_sparse_binary_array(lista_vectores_semilla)

bosque2 = tmap.LSHForest(perm, 128)
bosque2.batch_add(firmas_semilla)
bosque2.index()

cfg2 = tmap.LayoutConfiguration()
cfg2.k = 10
cfg2.kc = 30

x2, y2_local, s2, t2, _ = tmap.layout_from_lsh_forest(
    lsh_forest=bosque2, config=cfg2, keep_knn=False, create_mst=True, clear_lsh_forest=False
)

x2_np = np.array(list(x2), dtype=np.float32)
y2_np = np.array(list(y2_local), dtype=np.float32)

# Visual de plantilla local (restaurada)
plt.figure(figsize=(6,6))
plt.scatter(x2_np, y2_np, s=6, c=np.zeros(m_semilla), cmap="tab10")
plt.title(f"Plantilla de subcluster (m={m_semilla})")
plt.axis("off")
plt.tight_layout()
plt.show()

# 7) k automático simple (heurística): k = redondear(sqrt(m)/3), acotado a [2, 10] para evitar el poderoso harcodeo
k_auto = int(max(2, min(10, round(np.sqrt(max(m_semilla, 1))/3))))
print(f"k automático (heurística) = {k_auto}")

# Subclusters con k
coords_locales = np.vstack([x2_np, y2_np]).T
kmeans = KMeans(n_clusters=k_auto, n_init=10, random_state=0)
sub_etiquetas = kmeans.fit_predict(coords_locales)

plt.figure(figsize=(6,6))
plt.scatter(x2_np, y2_np, s=8, c=sub_etiquetas, cmap="tab10")
plt.title(f"Subclusters internos en Sandals (k={k_auto})")
plt.axis("off")
plt.tight_layout()
plt.show()

# 8) 1 imagen representativa por subcluster (más cercana al centro de c/u)
idx_repr, _ = pairwise_distances_argmin_min(kmeans.cluster_centers_, coords_locales)

plt.figure(figsize=(2.6*k_auto, 3.0))
for c in range(k_auto):
    ix = idx_repr[c]
    plt.subplot(1, k_auto, c+1)
    plt.imshow(X_semilla[ix].reshape(28,28), cmap="gray")
    plt.title(f"Subcl {c}")
    plt.axis("off")
plt.suptitle("Imágenes representativas por subcluster (Sandals)")
plt.tight_layout()
plt.show()
