#OPCION 1

def lunatico(ganancias):
    # Manejo de casos base
    if len(ganancias) == 0:
        return []
    if len(ganancias) == 1:
        return [0]
    if len(ganancias) == 2:
        return [0] if ganancias[0] >= ganancias[1] else [1]

    # Considerar ambos casos: sin la última casa y sin la primera casa
    primer_caso = lunatico_acortado(ganancias[:-1])
    segundo_caso = lunatico_acortado(ganancias[1:])

    # Determinar cuál opción da mayor ganancia y reconstruir el camino
    if primer_caso[-1] >= segundo_caso[-1]:
        camino = reconstruir_camino(primer_caso, ganancias[:-1])
        return camino
    else:
        camino = reconstruir_camino(segundo_caso, ganancias[1:])
        return [x + 1 for x in camino]


def lunatico_acortado(ganancias):
    OPT = [0] * (len(ganancias))
    OPT[0] = ganancias[0]
    OPT[1] = max(ganancias[0], ganancias[1])
    for n in range(2, len(ganancias)):
        OPT[n] = max(OPT[n - 1], OPT[n - 2] + ganancias[n])
    return OPT


def reconstruir_camino(OPT, ganancias):
    camino = []
    n = len(OPT) - 1

    while n >= 0:
        if n == 0:
            camino.append(0)
            break
        
        if n == 1: #No uso n-2 para no excederme del index
            if OPT[n] > OPT[n-1]:
                camino.append(n)
                break
            n -= 1
        
        elif OPT[n - 1] >= OPT[n - 2] + ganancias[n]:
                # No se roba esta casa
                n -= 1
        else:
            # Se roba
            camino.append(n)
            n -= 2
    camino.reverse()
    return camino

#OPCION 2

def lunatico(ganancias):
    n = len(ganancias)
    if n == 0:
        return []
    if n == 1:
        return [0]
    
    OPT1 = [0] * (n+1)
    OPT1[0] = 0
    OPT1[1] = ganancias[0]
    for i in range(2, n):
        OPT1[i] = max(ganancias[i-1] + OPT1[i-2], OPT1[i-1])
    OPT1[n] = OPT1[n-1]
    
    OPT2 = [0] * (n+1)
    OPT2[0] = 0
    OPT2[1] = 0
    OPT2[2] = ganancias[1]
    for i in range(3, n+1):
        OPT2[i] = max(ganancias[i-1] + OPT2[i-2], OPT2[i-1])
    
    OPT = []
    if OPT1[n] > OPT2[n]:
        OPT = OPT1
    else:
        OPT = OPT2
    
    # Reconstruccion de la solucion
    casas = []
    i = n
    while i > 0:
        if OPT[i] != OPT[i-1]:
            casas.append(i-1)
            i -= 2
        else:
            i -= 1

    casas.reverse()
    return casas

#OPCION 3

def lunatico(ganancias):
    if not ganancias:
        return []
        
    if len(ganancias)==1:
        return [0]

    op1, total1 = _lunatico(ganancias[1:])
    
    for i in range(len(op1)):
        op1[i] = op1[i]+1

    op2, total2 = _lunatico(ganancias[:-1])
    
    if total1 >= total2:
        return op1
    else:
        return op2

def _lunatico(ganancias):
    dias = len(ganancias)

    M_SCHE = [0] * dias
    M_SCHE[0] = ganancias[0]

    if dias > 1:
        M_SCHE[1] = max(ganancias[0], ganancias[1])

    for d in range(2, dias):
        M_SCHE[d] = max(ganancias[d] + M_SCHE[d - 2], M_SCHE[d - 1])

    return construir_elecciones(M_SCHE , ganancias), M_SCHE[-1]

def construir_elecciones(M_SCHE, ganancias):
    elecciones = []
    d = len(M_SCHE) - 1
    while d >= 0:
        ayer = M_SCHE[d - 1] if d > 0 else 0
        anteayer = M_SCHE[d - 2] if d > 1 else 0
        hoy = ganancias[d]

        if hoy + anteayer >= ayer:
            elecciones.append(d)
            d -= 2
        else:
            d -= 1
    elecciones.reverse()
    return elecciones