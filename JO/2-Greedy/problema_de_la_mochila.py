"""
El algoritmo implementado no encuentra siempre la solución óptima porque se basa en la elección de los elementos que
tienen la mejor relación valor/peso, sin embargo, esto no garantiza que la solución sea la óptima.

Un contraejemplo sería el siguiente:
elementos = [(60, 10), (100, 20), (120, 30)]
W = 50
La solución óptima sería tomar los elementos (60, 10) y (120, 30), con un valor total de 180 y un peso total de 40.
El algoritmo greedy tomaría los elementos (100, 20) y (60, 10), con un valor total de 160 y un peso total de 30.

El algoritmo es greedy porque en cada paso toma la mejor decisión local, es decir,
elige el elemento con la mejor relación valor/peso en cada iteración.
Sin embargo, no considera el impacto de esta decisión en las siguientes iteraciones, lo que
puede llevar a una solución subóptima.
"""


def mochila(elementos, W):
    # cada elemento i de la forma (valor, peso)
    elementos.sort(key=lambda x: x[0]/x[1], reverse=True)
    peso_actual = 0
    solucion = []

    for elemento in elementos:
        if peso_actual + elemento[1] <= W:
            peso_actual += elemento[1]
            solucion.append(elemento)

    return solucion
