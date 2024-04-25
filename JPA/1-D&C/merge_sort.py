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

arr = [3,4,2,5,0,9,1]
print(merge_sort(arr))