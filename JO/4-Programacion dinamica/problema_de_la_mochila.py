def reconstruccion(dp, n, W, elementos):
    i, j = n, W
    elementos_elegidos = []
    while (i != 0):
        if dp[i][j] != dp[i-1][j]:
            j -= elementos[i][1]  # W - Pi
            elementos_elegidos.append(elementos[i-1])
        i -= 1
    return elementos_elegidos

# Cada elemento i de la forma (valor, peso)c
def mochila(elementos, W):
    n = len(elementos)
    dp = [[0]*(W+1) for _ in range(n+1)]
    for i in range(1,n):
        for j in range(1,W):
            valor_actual, peso_actual = elementos[i-1]
            OPT_sin_elemento = dp[i-1][j]
            if peso_actual > j:
                dp[i][j] = OPT_sin_elemento
            else:
                OPT_con_elemento = dp[i-1][j-peso_actual] + valor_actual
                dp[i][j] = max(OPT_sin_elemento, OPT_con_elemento)

    return reconstruccion(dp, n, W, elementos)