def alternar(arr):
    n = len(arr)
    mid = n//2
    izq, der = arr[:mid], arr[mid:]
    arr.clear()
    for  i in range(n//2):
        arr.append(izq[i])
        arr.append(der[i])
    return arr

arr = ['c1', 'c2', 'c3', 'c4', 'd1', 'd2', 'd3', 'd4']
print(alternar(arr))