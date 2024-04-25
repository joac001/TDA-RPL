# cada elemento i de la forma (valor, peso)
def mochila(elementos, W):
    elementos.sort(key=lambda x: x[0], reverse=True)
    mochila = []
    peso_actual = 0
    for elemento in elementos:
        if peso_actual + elemento[1] <= W:
            mochila.append(elemento)
            peso_actual += elemento[1]
    return mochila
