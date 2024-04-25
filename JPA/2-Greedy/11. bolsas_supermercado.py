def bolsas(capacidad, productos):
    productos.sort(reverse=True)  #Ordeno los productos de mayor a menor peso

    bolsas = [] #Lista de bolsas que se van usando

    for producto in productos:
        for bolsa in bolsas:
            if sum(bolsa) + producto <= capacidad:
                bolsa.append(producto)
                break
        else:
            bolsas.append([producto])  #Se deberá usar una nueva bolsa

    return bolsas

"""
Pueden haber casos donde este algoritmo no da la solución óptima. Si por ejemplo hay varias formas de guardas los productos en las bolsas, el algoritmo elegirá solamente una única disposición, llenando las bolsas con los productos más pesados y dejando menos espacio para los  más livianos. Potencialmente podría ocurrir que se usen más bolsas de las necesarias.
    La parte más costosa del algoritmo es la clasificación de los productos, con una complejidad de O(n log n).
    La iteración sobre los productos tiene una complejidad de O(n * m), donde m es el número de bolsas existentes en ese momento. 
"""
