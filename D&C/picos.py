"""
Este algoritmo no pasa test de volumen para O(log n)
"""


def check_pico(arr, indice_solucion):
    return indice_solucion + 1 if arr[0] < arr[1] and arr[1] > arr[2] else -1


def posicion_pico(v, ini, fin, pivote=0):
    v_len = len(v)

    maximo_pico_local = 0
    maximo_pico = 0
    for i in range(0, v_len - 1):

        arr = v[i:i + 3]
        if len(arr) < 3:
            break

        maximo_pico_local = check_pico(arr, pivote)
        if maximo_pico_local == -1:
            maximo_pico_local = maximo_pico

        if v[maximo_pico_local] >= v[maximo_pico]:
            maximo_pico = maximo_pico_local
        pivote += 1

    return maximo_pico


# Pruebas
v_1 = [1, 2, 3, 1, 0, -2]
v_2 = [1, 2, 0]
v_3 = [0, 10, 25, 15, 7, -7, -11]

print(posicion_pico(v_1, 0, len(v_1) - 1))  # Salida esperada: 2
print(posicion_pico(v_2, 0, len(v_2) - 1))  # Salida esperada: 1
print(posicion_pico(v_3, 0, len(v_3) - 1))  # Salida esperada: 2