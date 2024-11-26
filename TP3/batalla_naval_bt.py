from test_reader import *
from logic import *

def batalla_naval_bt(tablero, barcos, demanda_filas, demanda_columnas,
                     puestos, optimos, i):
    
    demanda_cumplida = sum(size * 2 for (idx, size) in puestos.keys())
    demanda_optima = sum(size * 2 for (idx, size) in optimos.keys())

    if i == len(barcos):
        if demanda_cumplida > demanda_optima:
            optimos.clear()
            optimos.update({barco: pos.copy() for barco, pos in puestos.items()})
        return

    barco = barcos[i]
    barco_idx, barco_size = barco

    alternativas = obtener_candidatos(tablero, demanda_filas, demanda_columnas, barco_size) 
    hay_alternativas = len(alternativas) > 0

    if not hay_alternativas:
        batalla_naval_bt(tablero, barcos, demanda_filas, demanda_columnas, puestos,
                         optimos, i + 1)
        return

    proyectada = demanda_proyectada(tablero, demanda_filas, demanda_columnas, barcos, i - 1)
    no_llego = demanda_cumplida + proyectada <= demanda_optima
    
    if no_llego:
        batalla_naval_bt(tablero, barcos, demanda_filas, demanda_columnas, puestos,
                         optimos, i + 1)
        return

    puestos[barco] = []
    demanda_cumplida = sum(size * 2 for (idx, size) in puestos.keys())

    for demanda, alternativa in alternativas:
        for casilleros in alternativa:
            colocar_barco(casilleros, tablero, barco_idx)
            actualizar_demandas(casilleros, demanda_filas, demanda_columnas, False)
            puestos[barco] = casilleros
            
            proyectada = demanda_proyectada(tablero, demanda_filas, demanda_columnas, barcos, i)
            buena_alternativa = demanda_cumplida + proyectada > demanda_optima
            
            if buena_alternativa:
                batalla_naval_bt(tablero, barcos, demanda_filas, demanda_columnas, 
                                 puestos, optimos, i + 1)
            
            colocar_barco(casilleros, tablero, None) # Lo sacamos del tablero. 
            actualizar_demandas(casilleros, demanda_filas, demanda_columnas, True)

    del puestos[barco]
    k =  obtener_siguiente_distinto(barcos, i)
    
    batalla_naval_bt(tablero, barcos, demanda_filas, demanda_columnas, puestos,
                     optimos, k)
    return

def batalla_naval(tablero, barcos, demanda_filas, demanda_columnas):
    barcos_ordenados = list(enumerate(barcos))
    barcos_ordenados.sort(key=lambda x: -x[1])    
    optimos = {}
    demanda_incumplida = sum(demanda_filas) + sum(demanda_columnas)
    batalla_naval_bt(tablero, barcos_ordenados, demanda_filas, demanda_columnas,
                     {}, optimos, 0)
    
    imprimir_resultados(optimos)
    demanda_cumplida = sum(size * 2 for (idx, size), pos in optimos.items())
    print(f"Demanda cumplida = {demanda_cumplida}/{demanda_incumplida}")

def imprimir_resultados(optimo):
    puestos = list(optimo.items())
    puestos.sort(key=lambda x: x[0][0])
    for (barco_idx, barco_size), pos in puestos:
        print(f"{barco_idx}: ", pos)

def main():
    dataset = read_test_case('TP3/30_25_25.txt')
    demanda_filas, demanda_columnas, barcos = dataset

    n = len(demanda_filas)
    m = len(demanda_columnas)
    
    tablero = [[None for _ in range(m)] for _ in range(n)]
    batalla_naval(tablero, barcos, demanda_filas, demanda_columnas)


# (El tiempo fue tomado así porque lo corrí desde windows)
import time
inicio = time.time()
resultado = sum(i**2 for i in range(10**7))
main()
fin = time.time()
tiempo_ejecucion = fin - inicio
horas, resto = divmod(tiempo_ejecucion, 3600)
minutos, segundos = divmod(resto, 60)
print(f"Tiempo de ejecución: {int(horas)}h {int(minutos)}m {segundos:.2f}s")