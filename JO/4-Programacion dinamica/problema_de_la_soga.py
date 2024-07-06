def problema_soga(n):
    prod = [0] * (n + 1)
    prod[0] = 0
    prod[1] = 0
    prod[2] = 1

    for i in range(3, n + 1):
        for j in range(1, i):
            prod[i] = max(prod[i], j * max(i - j, prod[i - j]))
    return prod[n]

"""
Indicar y justificar la complejidad del algoritmo
La complejidad del algoritmo es O(n^2) ya que se recorre un ciclo de tamaño n y en cada iteración se recorre otro ciclo
de tamaño n. Por lo tanto, la complejidad es cuadrática.
"""