Optimización de cartera por fuerza bruta (Sharpe simplificado)
Este proyecto implementa un algoritmo de optimización de cartera que prueba todas las combinaciones discretas posibles de pesos entre 1 y 5 activos, buscando maximizar un índice de Sharpe simplificado (retorno menos tasa libre de riesgo entre volatilidad).​
Está pensado como una demo pedagógica para mostrar el enfoque de fuerza bruta y el costo computacional de revisar exhaustivamente muchas combinaciones de pesos.​

Requisitos
Python 3.x

No requiere librerías externas adicionales (solo se usa la librería estándar).

Uso
Ejecuta el script en una terminal:

bash
python nombre_del_archivo.py
Responde a las preguntas del programa:

Número de activos (entre 1 y 5).

Número de pasos (entre 5 y 20), que define la granularidad de los pesos (por ejemplo, pasos de 10%, 5%, etc.).

Para cada activo: rendimiento esperado (entre -1.0 y 1.0) y volatilidad (entre 0 y <1.0).

Tasa libre de riesgo (por ejemplo, 0.02 para 2%).

Al finalizar, el programa imprimirá:

Los mejores pesos por activo.

El rendimiento esperado de la cartera.

La volatilidad aproximada.

El valor del Sharpe simplificado y la tasa libre de riesgo usada.

Descripción del algoritmo
El algoritmo discretiza los pesos de la cartera en unidades que dependen del número de pasos (por ejemplo, si pasos = 10, se usan unidades de 10% que suman 100%).​

Mediante fuerza bruta, genera todas las combinaciones de pesos que suman el 100% entre los activos, calcula el retorno esperado de la cartera como suma ponderada de rendimientos y una volatilidad aproximada como suma ponderada de las volatilidades individuales.​

Para cada combinación válida con volatilidad positiva, calcula el Sharpe simplificado 


Limitaciones y notas
La volatilidad de cartera se calcula de forma simplificada sin matriz de covarianzas, por lo que no es una herramienta profesional de gestión de portafolios, sino una aproximación didáctica.​

El número de combinaciones crece rápidamente al aumentar el número de activos o al usar pasos muy finos, lo que ilustra cómo la fuerza bruta se vuelve inviable para carteras grandes o resoluciones muy detalladas.
