
def posicion_valida(i,j,reinas):
    for reina in reinas:
        if i == reina[0] or j == reina[1] or abs(i - reina[0]) == abs(j - reina[1]):
            return False
    return True

"""
[0 0 0 0]
[0 0 0 0]
[0 0 0 0]
[0 0 0 0]
"""

def backtracking(tablero, fila, reinas):
    if len(reinas) == len(tablero):
        return True

    for i in range(len(tablero)): #recorro la columna
        if posicion_valida(fila,i,reinas):
            reinas.append((fila,i))
            if backtracking(tablero, fila+1, reinas): #sigo con la siguiente columna
                return True
            reinas.pop()
    return False #ningun elemento de la columna es valido

def nreinas(n):
    tablero = [[0 for _ in range(n)] for _ in range(n)]
    reinas = []
    
    backtracking(tablero, 0, reinas)

    return reinas

print(nreinas(4)) # [(1, 0), (3, 1), (0, 2), (2, 3)]

