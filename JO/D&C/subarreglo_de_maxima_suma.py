def max_subarray(arr):
    return obtener_max_subarray(arr,0,len(arr)-1)[1]

def obtener_max_subarray(arr, inicio, fin):
    if inicio == fin:
        return arr[inicio], [arr[inicio]]

    medio = (inicio + fin) // 2

    suma_maxima_izq, subsecuencia_maxima_izq = obtener_max_subarray(arr, inicio, medio)
    suma_maxima_der, subsecuencia_maxima_der = obtener_max_subarray(arr, medio + 1, fin)

    izq_max_cruzado = float('-inf')
    suma_temp = 0
    index_max_izq = medio
    for i in range(medio, inicio - 1, -1):
        suma_temp += arr[i]
        if suma_temp > izq_max_cruzado:
            izq_max_cruzado = suma_temp
            index_max_izq = i

    der_max_cruzado = float('-inf')
    suma_temp = 0
    index_max_der = medio + 1
    for i in range(medio + 1, fin + 1):
        suma_temp += arr[i]
        if suma_temp > der_max_cruzado:
            der_max_cruzado = suma_temp
            index_max_der = i

    suma_maxima = max(suma_maxima_izq, suma_maxima_der, izq_max_cruzado + der_max_cruzado)

    if suma_maxima == suma_maxima_izq:
        return suma_maxima, subsecuencia_maxima_izq
    elif suma_maxima == suma_maxima_der:
        return suma_maxima, subsecuencia_maxima_der
    else:
        return izq_max_cruzado + der_max_cruzado, arr[index_max_izq:index_max_der+1]