# No pasa test

def check_pico(v, pivote):
    if v[pivote - 1] < v[pivote] and v[pivote] > v[pivote + 1]:
        return pivote
    else:
        return -1


def posicion_pico(v, ini, fin, pivote=0):
    if ini == fin:
        return check_pico(v, ini)

    pivote = (ini + fin) // 2

    if v[pivote - 1] < v[pivote] and v[pivote] > v[pivote + 1]:
        return pivote
    elif v[pivote - 1] < v[pivote] < v[pivote + 1]:
        return posicion_pico(v, pivote + 1, fin)
    else:
        return posicion_pico(v, ini, pivote - 1)


# Pruebas
v_1 = [1, 2, 3, 1, 0, -2]
v_2 = [1, 2, 0]
v_3 = [0, 10, 25, 15, 7, -7, -11]
v_4 = [3, 2, 1, 0, -1]

if __name__ == '__main__':
    print(posicion_pico(v_4, 0, len(v_1) - 1))  # Salida esperada: 0
    # print(posicion_pico(v_1, 0, len(v_1) - 1))  # Salida esperada: 2
    # print(posicion_pico(v_2, 0, len(v_2) - 1))  # Salida esperada: 1
    # print(posicion_pico(v_3, 0, len(v_3) - 1))  # Salida esperada: 2