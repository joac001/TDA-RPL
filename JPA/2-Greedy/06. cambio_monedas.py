def cambio(monedas, monto):
    monedas.sort(reverse=True)
    cambio = []
    for moneda in monedas:
        while moneda <= monto:
            cambio.append(moneda)
            monto -= moneda
        if monto == 0:
            break
    return cambio

print(cambio([1, 2, 5, 10, 20, 50, 100, 200], 1234)) # [200, 200, 200, 200, 200, 200, 50, 20, 10, 2, 2]
print(cambio([1, 2, 5, 10, 20, 50, 100, 200], 100)) # [100]
print(cambio([1, 2, 5, 10, 20, 50, 100, 200], 0)) # []
