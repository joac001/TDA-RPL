def escalones(n):
    E = [0]*(n+1)

    if n == 0 or n == 1:
        return 1
    if n == 2:
        return 2

    E[0], E[1], E[2] = 1, 1, 2

    for i in range(3, n+1):
        E[i] = E[i-1] + E[i-2] + E[i-3]
    return E, E[n]

print(escalones(5))