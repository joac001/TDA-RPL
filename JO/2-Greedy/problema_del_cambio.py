"""
¿El algoritmo implementado encuentra siempre la solución óptima? Justificar si es óptimo, o dar un contraejemplo.
¿Por qué se trata de un algoritmo Greedy? Justificar
¿Cual es la complejidad del algoritmo implementado? Justificar por qué.

El algoritmo implementado no encuentra siempre la solución óptima. Un contraejemplo sería el siguiente:
monedas: [1, 3, 4]
monto: 6
El algoritmo devolvería [4, 1, 1] en lugar de [3, 3], que es la solución óptima.

Se trata de un algoritmo Greedy porque en cada paso se elige la moneda de mayor valor que no exceda el monto restante.

La complejidad del algoritmo implementado es O(n), donde n es la cantidad de monedas. Esto se debe a que el algoritmo
recorre todas las monedas una vez, y en cada paso realiza una operación constante (comparación y resta). Por lo tanto,
la complejidad es lineal en función de la cantidad de monedas.
"""
def cambio(monedas, monto):
    monedas.sort(reverse=True)
    cambio = []
    for moneda in monedas:
        while monto >= moneda:
            monto -= moneda
            cambio.append(moneda)
    return cambio
