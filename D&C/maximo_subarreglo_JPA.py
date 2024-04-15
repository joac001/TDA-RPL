def max_subarray(arr):
    return get_max_subarray(arr,0,len(arr)-1)[1]

def get_max_subarray(arr, inicio, fin):
    if inicio == fin:
        return arr[inicio], [arr[inicio]]  # Devuelve la suma y el elemento

    medio = (inicio + fin) // 2

    #Voy partiendo de a mitades hasta llegar a un único elemento
    #A partir del cual se irán haciendo sumas sucesivas agregando de a un elemento
    #De esta forma puedo chequear todas las sumas posibles    
    max_izquierda_suma, max_izquierda_subsecuencia = get_max_subarray(arr, inicio, medio)
    max_derecha_suma, max_derecha_subsecuencia = get_max_subarray(arr, medio + 1, fin)

    #Ya tengo las sumas máximas de ambas mitades, pero tengo que revisar si se puede hacer una suma cruzada entre ellas
    #Es decir, si tengo [-1,1,3,4,1,-5], poder detectar que [1,3,4,1] es el subarray con máxima suma
    max_izquierda_cruzando = float('-inf')
    suma_temp = 0
    max_izquierda_index = medio
    for i in range(medio, inicio - 1, -1):
        suma_temp += arr[i]
        if suma_temp > max_izquierda_cruzando:
            max_izquierda_cruzando = suma_temp
            max_izquierda_index = i

    max_derecha_cruzando = float('-inf')
    suma_temp = 0
    max_derecha_index = medio + 1
    for i in range(medio + 1, fin + 1):
        suma_temp += arr[i]
        if suma_temp > max_derecha_cruzando:
            max_derecha_cruzando = suma_temp
            max_derecha_index = i

    #Obtengo la máxima suma entre todo lo calculados
    max_suma = max(max_izquierda_suma, max_derecha_suma, max_izquierda_cruzando + max_derecha_cruzando)

    #Condicional para controlar que subarray debe retornarse en base a que parte me dio la máxima suma
    if max_suma == max_izquierda_suma:
        return max_suma, max_izquierda_subsecuencia
    elif max_suma == max_derecha_suma:
        return max_suma, max_derecha_subsecuencia
    else:
        return max_izquierda_cruzando + max_derecha_cruzando, arr[max_izquierda_index:max_derecha_index+1]