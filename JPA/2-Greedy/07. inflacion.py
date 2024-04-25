def precios_inflacion(R):
    precio_minimo = 0
    R.sort(reverse=True)
    for i in range(len(R)):
        precio_minimo += R[i]**(i+1)
    return precio_minimo
