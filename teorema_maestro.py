from math import log

# Teorema maestro para calcular complejidad de algoritmos de 1-D&C
def teorema_maestro_dc():
    print('Ingrese a: Cantidad de llamados recursivos.')
    input_a = input()

    print('Ingrese b: El factor por el cual se divide el problema.')
    input_b = input()

    print('Ingrese c: El costo de partir y juntar (todo lo que no son llamados recursivos).')
    input_c = input()
    
    a,b,c = int(input_a), float(input_b), int(input_c)

    z = log(a, b)
    if z < c:
        return f'n^{c} ==> O(n)'
    elif z == c:
        return f'n^({c})log(n) ==> O(log(n))'
    else:
        return f'n^({log(a,b)}) ==> O(n)'

print(f'O({teorema_maestro_dc()})')

if __name__ == "__main__":
    teorema_maestro_dc()