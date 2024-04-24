"""
Se tiene un arreglo de N >= 3 elementos en forma de pico, esto es:
estrictamente creciente hasta una determinada posición p, y estrictamente decreciente a partir de ella (con 0 < p < N - 1).
Por ejemplo, en el arreglo [1, 2, 3, 1, 0, -2] la posición del pico es p = 2.
Se pide:
Implementar un algoritmo de división y conquista de orden O(log n) que encuentre la posición p del pico:
    func PosicionPico(v []int, ini, fin int) int. La función será invocada inicialmente como:
    PosicionPico(v, 0, len(v)-1), y tiene como pre-condición que el arreglo tenga forma de pico.
"""


def check_pico(arr, indice_solucion):
    return indice_solucion + 1 if arr[0] < arr[1] and arr[1] > arr[2] else -1


def posicion_pico(v, ini, fin, pivote=0):

#      Implementar un merge sort de mayor a meno


# Pruebas
v_1 = [1, 2, 3, 1, 0, -2]
v_2 = [1, 2, 0]
v_3 = [0, 10, 25, 15, 7, -7, -11]

print(posicion_pico(v_1, 0, len(v_1) - 1))  # Salida esperada: 2
print(posicion_pico(v_2, 0, len(v_2) - 1))  # Salida esperada: 1
print(posicion_pico(v_3, 0, len(v_3) - 1))  # Salida esperada: 2