# Asumo que el arreglo tiene por lo menos 3 elementos
def elemento_desordenado(arr):
    if len(arr) == 2:
        if arr[0] > arr[1]: 
            return arr[0]
        else: 
            return None

    for indice in range(0, len(arr)):
        retorno = None
        if indice != len(arr)-1:
            retorno = elemento_desordenado([arr[indice], arr[indice + 1]])
        if retorno is not None:
            return retorno


if __name__=='__main__':
    array = [1, 2, 3, 4]
    print(elemento_desordenado(array))