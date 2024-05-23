def lunatico(ganancias):
    n = len(ganancias)
    if n == 0:
        return []
    if n == 1:
        return [0]

    OPT1 = [0] * (n + 1)
    OPT1[0] = 0
    OPT1[1] = ganancias[0]
    for i in range(2, n):
        OPT1[i] = max(ganancias[i - 1] + OPT1[i - 2], OPT1[i - 1])
    OPT1[n] = OPT1[n - 1]

    OPT2 = [0] * (n + 1)
    OPT2[0] = 0
    OPT2[1] = 0
    OPT2[2] = ganancias[1]
    for i in range(3, n + 1):
        OPT2[i] = max(ganancias[i - 1] + OPT2[i - 2], OPT2[i - 1])

    OPT = []
    if OPT1[n] > OPT2[n]:
        OPT = OPT1
    else:
        OPT = OPT2

    # Reconstruccion de la solucion
    casas = []
    i = n
    while i > 0:
        if OPT[i] != OPT[i - 1]:
            casas.append(i - 1)
            i -= 2
        else:
            i -= 1

    return casas.reverse()
