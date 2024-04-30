def cambio(monedas, monto):
    monedas.sort(reverse=True)
    cambio = []
    for moneda in monedas:
        while monto >= moneda:
            monto -= moneda
            cambio.append(moneda)
    return cambio
