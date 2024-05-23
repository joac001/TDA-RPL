def operaciones(k):
    def recursividad(k, memoria):
        if k == 0:
            return []
        if memoria[k] is not None:
            return memoria[k]
        if k % 2 == 0:
            memoria[k] = recursividad(k // 2, memoria) + ["por2"]
        else:
            memoria[k] = recursividad(k - 1, memoria) + ["mas1"]
        return memoria[k]

    memoria = [None] * (k + 1)
    return recursividad(k, memoria)


"""
Indicar y justificar la complejidad del algoritmo implementado.
La complejidad del algoritmo es O(n) porque se recorre el arreglo de memoria una sola vez,
y se hace una llamada recursiva por cada valor de k, por lo que se recorre el arreglo de memoria
una sola vez, y se hace una llamada recursiva por cada valor de k, por lo que la complejidad
es lineal.
"""