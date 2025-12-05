def fuerzaBruta():
    print("\nAlgoritmo de optimización de Cartera (Sharpe simplificado)\n")

    activos = 0
    pasos = 0
    rf = 0
    rendimiento = []  # medias esperadas por activo (por periodo consistente: p.ej. anual)
    variacion = []    # volatilidades (desviaciones estándar) por activo (mismo periodo)

    # Entradas básicas
    while activos < 1 or activos > 5:
        try:
            activos = int(input("Ingrese el número de activos (1 al 5): "))
        except ValueError:
            activos = 0
        if activos < 1 or activos > 5:
            print("Ingrese un número en el rango especificado.")

    while pasos < 5 or pasos > 20:
        try:
            pasos = int(input("Ingrese el número de pasos (5 al 20): "))
        except ValueError:
            pasos = 0
        if pasos < 5 or pasos > 20:
            print("Ingrese un número en el rango especificado.")

    print("\nIngrese el rendimiento y la variación (volatilidad) de cada activo.")
    for i in range(activos):
        while True:
            try:
                r = float(input(f"Rendimiento esperado del Activo {i+1} (entre -1.0 y 1.0): "))
                if -1.0 <= r <= 1.0:
                    rendimiento.append(r)
                    break
                else:
                    print("Rendimiento debe estar en [-1.0, 1.0]. Intente de nuevo.")
            except ValueError:
                print("Valor no válido. Intente de nuevo.")
        while True:
            try:
                v = float(input(f"Volatilidad (desv. est.) del Activo {i+1} (entre 0 y <1.0): "))
                if 0.0 <= v < 1.0:
                    variacion.append(v)
                    break
                else:
                    print("Volatilidad debe estar en [0, 1). Intente de nuevo.")
            except ValueError:
                print("Valor no válido. Intente de nuevo.")
        print()

    # Tasa libre de riesgo necesaria para Sharpe
    while True:
        try:
            rf = float(input("Ingrese la tasa libre de riesgo (por ej. 0.02 = 2%): "))
            break
        except ValueError:
            print("Valor no válido. Intente de nuevo.")

    # Discretización de pesos
    unidades = int(100 / pasos)
    total_unidades = unidades

    mejor_sharpe = float("-inf")
    mejor_pesos = None
    mejor_r = None
    mejor_sigma = None

    
    def evaluar(k_vec):
        nonlocal mejor_sharpe, mejor_pesos, mejor_r, mejor_sigma
        pesos = [k / unidades for k in k_vec]  # pesos que suman 1

        # retorno esperado de cartera: suma ponderada de retornos, sustituye convarianza
        r_port = sum(p * r for p, r in zip(pesos, rendimiento))

        # Volatilidad de cartera (simplificada): suma ponderada de volatilidades individuales
        # NOTA: Es una aproximación. La fórmula correcta usa covarianzas.
        sigma_port = sum(p * v for p, v in zip(pesos, variacion))

        if sigma_port <= 0.0:
            return

        # Sharpe: (Rp - Rf) / sigma
        sharpe = (r_port - rf) / sigma_port

        if sharpe > mejor_sharpe:
            mejor_sharpe = sharpe
            mejor_pesos = pesos[:]
            mejor_r = r_port
            mejor_sigma = sigma_port

    # Generacion de combinaciones por fuerza bruta 
    if activos == 1:
        for a in range(total_unidades + 1):
            if a == total_unidades:
                evaluar([a])
    elif activos == 2:
        for a in range(total_unidades + 1):
            b = total_unidades - a
            evaluar([a, b])
    elif activos == 3:
        for a in range(total_unidades + 1):
            for b in range(total_unidades - a + 1):
                c = total_unidades - a - b
                evaluar([a, b, c])
    elif activos == 4:
        for a in range(total_unidades + 1):
            for b in range(total_unidades - a + 1):
                for c in range(total_unidades - a - b + 1):
                    d = total_unidades - a - b - c
                    evaluar([a, b, c, d])
    elif activos == 5:
        for a in range(total_unidades + 1):
            for b in range(total_unidades - a + 1):
                for c in range(total_unidades - a - b + 1):
                    for d in range(total_unidades - a - b - c + 1):
                        e = total_unidades - a - b - c - d
                        evaluar([a, b, c, d, e])

    # Reporte
    print("\n=== RESULTADO (Fuerza Bruta con Sharpe simplificado) ===")
    if mejor_pesos is None:
        print("No se encontró ninguna combinación válida (volatilidad no positiva).")
    else:
        pesos_str = ", ".join(f"{w:.2f}" for w in mejor_pesos)
        print(f"Mejores pesos por activo (en orden ingresado): [{pesos_str}]")
        print(f"Rendimiento cartera (Rp): {mejor_r:.4f}")
        print(f"Volatilidad aprox. (sigma): {mejor_sigma:.4f}")
        print(f"Sharpe: {(mejor_r - rf) / mejor_sigma:.4f}")
        print(f"Tasa libre de riesgo (Rf): {rf:.4f}")

fuerzaBruta()
