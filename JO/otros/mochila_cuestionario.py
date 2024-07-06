"""
devolver el máximo valor obtenible en el problema de programacion dinamica de la mochila de tamaño
W = 15 teniendo como opciones los siguientes elementos:
v1=58,w1=7
v2=15,w2=6
v3=51,w3=12
v4=31,w4=2
v5=12,w5=12
v6=89,w6=15
v7=19,w7=9
v8=4,w8=12
v9=75,w9=8
v10=50,w10=8
"""

def knapsack(values, weights, W):
    n = len(values)
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]
if __name__ == "__main__":
    val = [58, 15, 51, 31, 12, 89, 19, 4, 75, 50]
    wt = [7, 6, 12, 2, 12, 15, 9, 12, 8, 8]
    W = 15
    print(knapsack(val, wt, W))
