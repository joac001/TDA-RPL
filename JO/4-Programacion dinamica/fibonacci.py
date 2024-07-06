def fibonacci(n):
    n_uno = 0
    n_dos = 1
    for i in range(n):
        aux = n_dos
        n_dos = n_uno + n_dos
        n_uno = aux
    return n_dos
