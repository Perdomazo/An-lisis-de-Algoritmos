import itertools #para generar todas las combinaciones posibles

#ciudades representadas por índices 0, 1, 2, 3
ciudades = [0, 1, 2, 3]

# matriz de distancias
# distancias[i][j] es la distancia de la ciudad i a la j vamos adrian no es tan dificil
distancias = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

origen = 0
otras = ciudades[1:]

mejor_ruta = None
mejor_costo = float("inf")

print("Rutas evaluadas:")


#fuerza bruta para recorrer todas las combinaciones
for perm in itertools.permutations(otras):
    ruta = [origen] + list(perm)
    # calcular el costo de la ruta (incluye regreso al origen)
    costo = 0
    for i in range(len(ruta) - 1):
        costo += distancias[ruta[i]][ruta[i+1]]
    costo += distancias[ruta[-1]][ruta[0]]

    print(f"Ruta: {ruta} -> Costo total: {costo}")

     # actualizamos la mejor ruta encontrada hasta el momento
    if costo < mejor_costo:
        mejor_costo = costo
        mejor_ruta = ruta

print(" ")
print("Mejor ruta encontrada:", mejor_ruta)
print("Costo total de la mejor ruta:", mejor_costo)
