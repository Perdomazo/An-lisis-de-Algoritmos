import time
import matplotlib.pyplot as plt
from memory_profiler import memory_usage  


def fib_normal(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b

def fib_dinamica(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[-1] if n > 0 else 0

def tiempos_normal(n):
    a, b = 0, 1
    t0 = time.perf_counter()
    ts = []
    for _ in range(n):
        a, b = b, a + b
        ts.append(time.perf_counter() - t0)
    return ts

def tiempos_dinamica(n):
    fib = [0, 1]
    t0 = time.perf_counter()
    ts = [0, 0]  
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
        ts.append(time.perf_counter() - t0)
    return ts


def memoria_traza(func, n, interval=0.01):
    return memory_usage((func, (n,)), interval=interval)

if __name__ == "__main__":
    n = 10000

    t_norm = tiempos_normal(n)
    t_din = tiempos_dinamica(n)

    plt.figure(figsize=(11, 4))
    plt.plot(range(len(t_norm)), t_norm, label="Normal")
    plt.plot(range(len(t_din)), t_din, label="Dinámica")
    plt.title("Tiempo acumulado por N")
    plt.xlabel("N")
    plt.ylabel("Segundos")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

    # Memoria
    m_norm = memoria_traza(fib_normal, n, interval=0.01)
    m_din = memoria_traza(fib_dinamica, n, interval=0.01)

    plt.figure(figsize=(11, 4))
    plt.plot(m_norm, label="Normal")
    plt.plot(m_din, label="Dinámica")
    plt.title("Uso de memoria (traza del proceso)")
    plt.xlabel("N")
    plt.ylabel("MB")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
