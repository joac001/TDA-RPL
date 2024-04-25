def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)


def fib_memorioso(n):
    M_FIB = [None] * (n + 1)
    return fib_rec_memorioso(n, M_FIB)


def fib_rec_memorioso(n, M_FIB):
    if n == 0:
        return 0
    if n == 1:
        return 1

    if M_FIB[n - 1] is None:
        M_FIB[n] = fib_rec_memorioso(n - 1, M_FIB)
    if M_FIB[n - 2] is None:
        M_FIB[n] = fib_rec_memorioso(n - 2, M_FIB)
    M_FIB[n] = M_FIB[n - 1] + M_FIB[n - 2]

    return M_FIB[n]

def fib_iterativo(n):
    M_FIB = [None] * (n + 1)
    # noinspection PyTypeChecker
    M_FIB[0], M_FIB[1] = 0, 1

    for i in range(2, n + 1):
        # noinspection PyUnresolvedReferences
        M_FIB[i] = M_FIB[i - 1] + M_FIB[i - 2]

    return M_FIB[n]

def fib_dinamico(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    anterior, actual = 0, 1

    for i in range(1, n):
        nuevo, anterior = actual + anterior, actual
        actual = nuevo
    return actual