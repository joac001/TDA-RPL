def reconstruccion(dp, n, m):
    # Reconstruccion de la solucion
    path = []
    i, j = n-1, m-1
    while i > 0 and j > 0:
        path.append((i, j))
        if dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    path.append((0, 0))
    return path

def laberinto(matriz):
    if not matriz or not matriz[0]:
        return 0

    n = len(matriz)
    m = len(matriz[0])

    # Inicializo la matriz que va a guardar la maxima ganancia para llegar del
    # inicio al final
    dp = [0] * n
    for i in range(n):
        dp[i] = [0] * m

    dp[0][0] = matriz[0][0]

    # Armo los casos base
    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + matriz[i][0]
    for j in range(1, m):
        dp[0][j] = dp[0][j - 1] + matriz[0][j]

    # Recorro la matriz (laberinto) y calculo el maximo y lo guardo en la
    # matriz dp
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + matriz[i][j]

    path = reconstruccion(dp, n, m)

    return dp[-1][-1], path[::-1]
