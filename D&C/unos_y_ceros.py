def indice_primer_cero(arr, pivote=0):
    len_arr = len(arr)

    if len_arr == 0 or len_arr == sum(arr):
        return -1
    elif len_arr == 1:
        return pivote if arr[0] == 0 else -1

    mid = len_arr // 2
    retorno = indice_primer_cero(arr[:mid], pivote)

    if retorno != -1:
        return retorno

    retorno = indice_primer_cero(arr[mid:], pivote + mid)
    return retorno


# Pruebas
a1 = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
a2 = [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
a3 = [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1]
a4 = [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1]
a5 = []
a6 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
a7 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0]

if __name__ == "__main__":
    print(indice_primer_cero(a1))
    print(indice_primer_cero(a2))
    print(indice_primer_cero(a3))
    print(indice_primer_cero(a4))
    print(indice_primer_cero(a5))
    print(indice_primer_cero(a6))
    print(indice_primer_cero(a7))

