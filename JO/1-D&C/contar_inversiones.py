def merge(izq, der):
    merged = []
    izq_index = 0
    der_index = 0

    # Merge smaller elements first
    while izq_index < len(izq) and der_index < len(der):
        if izq[izq_index] <= der[der_index]:
            merged.append(izq[izq_index])
            izq_index += 1
        else:
            merged.append(der[der_index])
            der_index += 1

    # If there are remaining elements in izq or der half, append them to the result
    while izq_index < len(izq):
        merged.append(izq[izq_index])
        izq_index += 1

    while der_index < len(der):
        merged.append(der[der_index])
        der_index += 1

    return merged
def contar_inversiones(A, B):
    if len(B) <= 1:
        return B

    n = len(B)
    mid = n // 2
    izq = B[:mid]
    der = B[mid:]

    return merge(contar_inversiones([], izq), contar_inversiones([], der))

# Que complejidad tiene este algoritmo?
# Respuesta: O(n log n)

A = [1, 2, 3, 4, 5]
B = [2, 3, 1, 5, 4]
print(contar_inversiones(A, B))