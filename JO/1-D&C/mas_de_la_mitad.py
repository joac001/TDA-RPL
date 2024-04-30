# Cual es la complejiodad del algoritmo en mas_de_la_mitad(arr) y por que?
# La complejidad es O(n) porque se recorre el arreglo una vez para contar las repeticiones de cada elemento y luego se
# recorre el arreglo de repeticiones para verificar si alguna repeticion es mayor a la mitad del tamaño del arreglo.

def mas_de_la_mitad(arr):
    n = len(arr)
    repeticiones = [0]*n

    for i in range(n):
        repeticiones[arr[i] - 1] += 1

    if max(repeticiones) > n//2:
        return True

    return False