"""
Se tiene un sistema monetario (ejemplo, el nuestro). Se quiere dar "cambio" de una determinada cantidad de plata. 
Implementar un algoritmo Greedy que devuelva el cambio pedido, usando la mínima cantidad de monedas/billetes. 
El algoritmo recibirá un arreglo de valores del sistema monetario, y la cantidad de cambio objetivo a dar, y 
debe devolver qué monedas/billetes deben ser utilizados para minimizar la cantidad total utilizada. 
Indicar y justificar la complejidad del algoritmo implementado. 
¿El algoritmo implementado encuentra siempre la solución óptima? Justificar si es óptimo, o dar un contraejemplo. 
¿Por qué se trata de un algoritmo Greedy? Justificar.
"""

def cambio(monedas, monto):
    monedas.sort(reverse=True)
    cambio = []
    for moneda in monedas:
        while moneda <= monto:
            cambio.append(moneda)
            monto -= moneda
        if monto == 0:
            break
    return cambio

print(cambio([1, 2, 5, 10, 20, 50, 100, 200], 1234)) # [200, 200, 200, 200, 200, 200, 50, 20, 10, 2, 2]
print(cambio([1, 2, 5, 10, 20, 50, 100, 200], 100)) # [100]
print(cambio([1, 2, 5, 10, 20, 50, 100, 200], 0)) # []
