def hay_mas_de_dos_tercios(repeticiones, n):
    for i in range(n):
        if repeticiones[i] > (2*n)//3:
            return True

    return False


def mas_de_dos_tercios(arr):
    n = len(arr)
    repeticiones = [0]*n

    for i in range(n):
        repeticiones[arr[i] - 1] += 1

    if hay_mas_de_dos_tercios(repeticiones, n):
        return True

    return False
