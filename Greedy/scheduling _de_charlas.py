# ¿Cual es la complejiodad del algoritmo en charlas(horarios) y por que?
# Respuesta:
# La complejidad del algoritmo es O(nlogn) ya que se ordena el arreglo de horarios

def charlas(horarios):

    if len(horarios) == 0:
        return []

    horarios.sort(key=lambda x: x[1])
    charlas = [horarios[0]]

    for i in range(len(horarios)):
        if charlas[-1][1] < horarios[i][0]:
            charlas.append(horarios[i])

    return charlas

if __name__ == "__main__":
    print(charlas([(5, 9), (3, 7), (1, 11), (2, 15), (6, 9), (10, 13), (12, 25), (8, 9)]))