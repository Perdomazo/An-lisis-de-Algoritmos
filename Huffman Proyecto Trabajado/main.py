import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt
import heapq
import os
import base64
import json

# ---------------- Huffman Utilities ---------------- #

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(data):
    freq = {}
    for item in data:
        for char in item:
            freq[char] = freq.get(char, 0) + 1
    heap = [HuffmanNode(char, f) for char, f in freq.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = HuffmanNode(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        heapq.heappush(heap, merged)
    return heap[0] if heap else None

def build_huffman_codes(tree):
    codes = {}
    def encode(node, code):
        if node:
            if node.char is not None:
                codes[node.char] = code
            encode(node.left, code + "0")
            encode(node.right, code + "1")
    encode(tree, "")
    return codes

def huffman_encode(data, codes):
    out = []
    for item in data:
        encoded = ''.join([codes[char] for char in item])
        out.append(encoded)
    return out

def huffman_decode(encoded_data, tree):
    result = []
    for bits in encoded_data:
        node = tree
        decoded = ""
        i = 0
        while i < len(bits):
            while node.char is None:
                if i >= len(bits): break
                if bits[i] == "0":
                    node = node.left
                else:
                    node = node.right
                i += 1
            if node.char is not None:
                decoded += node.char
                node = tree
        result.append(decoded)
    return result

def serialize_huffman_tree(node):
    if node is None:
        return None
    # Serializa usando dicts recursivos (más robusto)
    if node.char is not None:
        return {"char": node.char}
    else:
        return {"left": serialize_huffman_tree(node.left), "right": serialize_huffman_tree(node.right)}

def deserialize_huffman_tree(obj):
    if obj is None:
        return None
    if "char" in obj:
        return HuffmanNode(obj["char"], 0)
    node = HuffmanNode(None, 0)
    node.left = deserialize_huffman_tree(obj["left"])
    node.right = deserialize_huffman_tree(obj["right"])
    return node

# -------------- Main Tkinter App ------------- #
class HuffmanApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Encriptador S&P500 y ETFs (.papus) - Algoritmo de Huffman")
        self.df = None
        self.filename = None

        lbl_title = tk.Label(root, text="Encriptador de empresas del S&P 500 y ETFs usando Huffman", font=("Arial", 13, "bold"))
        lbl_title.pack(pady=10)

        btn_load = tk.Button(root, text="Cargar archivo CSV", command=self.load_csv, width=25)
        btn_load.pack(pady=5)

        btn_encrypt = tk.Button(root, text="Encriptar a archivo .papus", command=self.encrypt_csv, width=25)
        btn_encrypt.pack(pady=5)

        btn_decrypt = tk.Button(root, text="Desencriptar archivo .papus", command=self.decrypt_papus, width=25)
        btn_decrypt.pack(pady=5)

        btn_plot = tk.Button(root, text="Graficar distribución de sectores", command=self.plot_sectors, width=25)
        btn_plot.pack(pady=5)

        self.lbl_status = tk.Label(root, text="", fg="blue", font=("Arial", 10))
        self.lbl_status.pack(pady=8)

        self.sector_context = tk.Label(root, text="", fg="darkgreen", font=("Arial", 10), wraplength=380, justify="left")
        self.sector_context.pack(pady=8)

    def load_csv(self):
        self.filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if not self.filename:
            return
        try:
            self.df = pd.read_csv(self.filename)
            symbol = next((c for c in self.df.columns if "symbol" in c.lower() or "ticker" in c.lower()), None)
            name = next((c for c in self.df.columns if "name" in c.lower()), None)
            sector = next((c for c in self.df.columns if "sector" in c.lower()), None)
            if not all([symbol, name, sector]):
                messagebox.showerror("Error", "No se detectaron columnas 'Symbol', 'Name', y 'Sector'.")
                self.df = None
                return
            self.df = self.df[[symbol, name, sector]]
            self.df = self.df.dropna()
            self.lbl_status.config(text=f"Archivo CSV cargado correctamente: {os.path.basename(self.filename)} ({self.df.shape[0]} filas)")
        except Exception as e:
            messagebox.showerror("Error al cargar el archivo", str(e))

    def encrypt_csv(self):
        if self.df is None:
            messagebox.showerror("Error", "Primero carga un archivo CSV.")
            return
        data = self.df.values.tolist()
        flattened = ["|".join(map(str, row)) for row in data]
        huff_tree = build_huffman_tree(flattened)
        codes = build_huffman_codes(huff_tree)
        encoded = huffman_encode(flattened, codes)
        tree_dict = serialize_huffman_tree(huff_tree)
        tree_serialized = json.dumps(tree_dict)
        tree_b64 = base64.b64encode(tree_serialized.encode("utf8")).decode("ascii")
        save_path = filedialog.asksaveasfilename(defaultextension=".papus", filetypes=[("Papus file", "*.papus")])
        if not save_path:
            return
        try:
            with open(save_path, "w", encoding="utf8") as f:
                # Guardamos: firma, árbol serializado base64, número de filas, cabeceras, datos codificados
                f.write("PAPUSCRYPT\n")
                f.write(tree_b64 + "\n")
                f.write(str(len(encoded)) + "\n")
                f.write(','.join(list(self.df.columns)) + "\n")
                for enc_row in encoded:
                    f.write(enc_row + "\n")
            self.lbl_status.config(text=f"Archivo .papus guardado exitosamente: {os.path.basename(save_path)}")
        except Exception as e:
            messagebox.showerror("Error al guardar archivo", str(e))

    def decrypt_papus(self):
        papus_file = filedialog.askopenfilename(filetypes=[("Papus file", "*.papus")])
        if not papus_file:
            return
        try:
            import tkinter.simpledialog as simpledialog
        except ImportError:
            messagebox.showerror("Error", "No se pudo importar simpledialog.")
            return
        pwd = simpledialog.askstring("Contraseña", "Introduce la contraseña para desencriptar:")
        if pwd != "papus":
            messagebox.showerror("Contraseña incorrecta", "La contraseña es incorrecta.")
            return
        try:
            with open(papus_file, "r", encoding="utf8") as f:
                lines = [line.strip() for line in f if line.strip()]
            if not lines[0].startswith("PAPUSCRYPT"):
                messagebox.showerror("Archivo no válido", "El archivo no es reconocido como .papus válido.")
                return
            tree_b64 = lines[1]
            tree_dict = json.loads(base64.b64decode(tree_b64.encode("ascii")).decode("utf8"))
            huff_tree = deserialize_huffman_tree(tree_dict)
            n = int(lines[2])
            columns = [c.strip() for c in lines[3].split(",")]
            encoded_data = lines[4:4+n]
            decoded = huffman_decode(encoded_data, huff_tree)
            split_decoded = [row.split("|") for row in decoded]
            df = pd.DataFrame(split_decoded, columns=columns)
            save_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
            if not save_path:
                return
            df.to_csv(save_path, index=False, encoding="utf8")
            self.lbl_status.config(text=f"Archivo CSV exportado exitosamente: {os.path.basename(save_path)}")
        except Exception as e:
            messagebox.showerror("Error al desencriptar", str(e))

    def plot_sectors(self):
        if self.df is None:
            messagebox.showerror("Error", "Primero carga un archivo CSV válido.")
            return
        sector_col = self.df.columns[2]
        data = self.df[sector_col]
        plt.figure(figsize=(7,4))
        counts = data.value_counts()
        counts.plot(kind="bar", color="teal")
        plt.title("Distribución de empresas por sector")
        plt.xlabel("Sector")
        plt.ylabel("Cantidad de empresas")
        plt.tight_layout()
        plt.show()
        major = counts.idxmax()
        percent = (counts.max() / counts.sum())*100
        resume = f"El sector con más empresas es '{major}' ({counts.max()} empresas, {percent:.1f}%).\n"
        resume += f"Total de sectores: {len(counts)}.\n"
        if percent > 40:
            resume += "Este sector domina la composición del ETF."
        else:
            resume += "Hay una distribución bastante diversa entre los sectores."
        self.sector_context.config(text=resume)

if __name__ == "__main__":
    root = tk.Tk()
    app = HuffmanApp(root)
    root.geometry("500x430")
    root.mainloop()
