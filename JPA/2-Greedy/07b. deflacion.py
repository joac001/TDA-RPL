def precios_deflacion(R):
    precio_minimo = 0
    R.sort()
    for i in range(len(R)):
        precio_deflacionado = R[i]
        for d in range(i):
            precio_deflacionado /= 2
        precio_minimo += precio_deflacionado
    return precio_minimo
