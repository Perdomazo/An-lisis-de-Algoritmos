
import time
import matplotlib.pyplot as plt
import random

N_DATOS = 500
ITERACIONES = 20

def generador():
    valores = []
    empresas = []
    sp = []
    for i in range(N_DATOS):
        empresas.append(i + 1)
    for i in range(N_DATOS):
        tupla_random = random.random()
        tupla_random2 = random.random()
        temp_array = []
        temp_array.append(tupla_random)
        temp_array.append(tupla_random2)
        valores.append(temp_array)
    for i in range(N_DATOS):
        temp_array = []
        temp_array.append(empresas[i])
        temp_array.append(valores[i])
        sp.append(temp_array)
    return sp

empresas_datos = generador()

def es_mejor(mitad_a, mitad_b):
    rendimiento_a, volatilidad_a = mitad_a[1]
    rendimiento_b, volatilidad_b = mitad_b[1]
    # 1. Mayor rendimiento
    if rendimiento_a > rendimiento_b:
        return True
    # 2. Si el rendimiento es igual, menor volatilidad
    if rendimiento_a == rendimiento_b and volatilidad_a < volatilidad_b:
        return True
    return False

def seleccion(empresas_evaluar):
    n = len(empresas_evaluar)
    if n <= 1:
        if n == 0:
            return None
        else:
            return empresas_evaluar[0]

    mid = n // 2
    izq = empresas_evaluar[:mid]
    der = empresas_evaluar[mid:]

    mejor_izq = seleccion(izq)
    mejor_der = seleccion(der)

    if mejor_izq is None:
        return mejor_der
    if mejor_der is None:
        return mejor_izq

    if es_mejor(mejor_izq, mejor_der):
        return mejor_izq
    else:
        return mejor_der


def seleccion_dp(empresas_evaluar):
    # Caso base
    if not empresas_evaluar:
        return None

    mejor = empresas_evaluar[0]
    for i in range(1, len(empresas_evaluar)):
        candidato = empresas_evaluar[i]
        if es_mejor(candidato, mejor):
            mejor = candidato
    return mejor


tiempos_divide = []
for _ in range(ITERACIONES):
    t0 = time.perf_counter()
    _ = seleccion(empresas_datos)
    t1 = time.perf_counter()
    tiempos_divide.append(t1 - t0)


def tiempo_promedio(func, datos, repeticiones=10):
    total = 0.0
    for _ in range(repeticiones):
        t0 = time.perf_counter()
        _ = func(datos)
        t1 = time.perf_counter()
        total += (t1 - t0)
    return total / repeticiones

Ns = list(range(50, N_DATOS + 1, 50))  
prom_divide = []
prom_dp = []

for n in Ns:
    sub = empresas_datos[:n]
    prom_divide.append(tiempo_promedio(seleccion, sub, repeticiones=20))
    prom_dp.append(tiempo_promedio(seleccion_dp, sub, repeticiones=20))

plt.figure(figsize=(7, 4))
plt.plot(Ns, prom_divide, marker='o', label='Divide y Vencerás')
plt.plot(Ns, prom_dp, marker='s', label='Programación Dinámica')
plt.title('Comparación de desempeño (n vs tiempo promedio)')
plt.xlabel('n (tamaño de la lista de empresas)')
plt.ylabel('Tiempo (segundos)')
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()
