def bodegon_dinamico(P, W):
    solution = [[0 for _ in range(W + 1)] for _ in range(len(P) + 1)]
    for n in range(1, len(P) + 1):
        for w in range(1, W + 1):
            if P[n - 1] > w:
                solution[n][w] = solution[n - 1][w]
            else:
                solution[n][w] = max(solution[n - 1][w], solution[n - 1][w - P[n - 1]] + P[n - 1])
    grupos = []
    w = W
    for i in range(len(P), 0, -1):
        if solution[i][w] != solution[i - 1][w]:
            grupos.append(P[i-1])
            w -= P[i - 1]
    return grupos[::-1]


print(bodegon_dinamico([3, 6, 2, 5, 1], 9))
