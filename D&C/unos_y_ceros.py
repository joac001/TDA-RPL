def indice_primer_cero(arr, pivote=0):
    if len(arr) == 1:
        return pivote if arr[0] == 0 else -1

    if len(arr) == 0 or len(arr) == sum(arr):
        return -1

    mid = len(arr)//2
    retorno = indice_primer_cero(arr[:mid], pivote)
    
    if retorno != -1:
        return retorno 

    retorno = indice_primer_cero(arr[mid:], pivote+mid)
    return retorno


a1 = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
a2 = [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
a3 = [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1]
a4 = [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1]

print(indice_primer_cero(a1))
print(indice_primer_cero(a2))
print(indice_primer_cero(a3))
print(indice_primer_cero(a4))