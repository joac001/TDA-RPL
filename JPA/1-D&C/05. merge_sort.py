def merge(izq,der):
    resultado = []

    while (izq and der):
        if izq[0] < der[0]:
            resultado.append(izq[0])
            izq.pop(0)
        else:
            resultado.append(der[0])
            der.pop(0)

    if izq:
        resultado += izq
    if der:
        resultado += der
    
    return resultado

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    medio = len(arr) // 2
    split_izq = arr[:medio]
    split_der = arr[medio:]

    izq_ordenado = merge_sort(split_izq)
    der_ordenado = merge_sort(split_der)

    return merge(izq_ordenado,der_ordenado)

"""
Recordando al Teorema Maestro tenemos que:
aT(n/b)+O(nc)
a = cantidad de llamados recursivos
En este caso tenemos 2 llamados recursivos.
b = proporción del tamaño original con el que se trabaja recursivamente
La cantidad de parcial de elementos se divide a la mitad, por lo que b=2
c = costo de partir y juntar
El costo es lineal, por lo que c = 1.

Entonces: T(n)=2T(n/2)+O(n)
como logB(A)= log2(2) = 1 = c
Entonces -> T(n) = O(nlogn) = O(logn)

"""
