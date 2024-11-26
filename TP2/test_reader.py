from parte_dos import maxCoins2
import os



def read_test_case(path):

    numbers = []
    
    with open(path, 'r') as file:
        for line in file:
            line = line.strip()
            
            if line.startswith('#'):
                continue
            else:
                numbers = list(map(int, line.split(';')))
    
    return numbers


directory = "./TP2/TP2/"
esperados = [1483, 2338, 5234, 7491, 14976, 28844, 1401590, 2869340, 9939221, 34107537]
obtenidos = []

for filename in os.listdir(directory):
    if filename != 'Resultados Esperados.txt' and filename.endswith(".txt"):
        path = os.path.join(directory, filename)
        resultado = maxCoins2(read_test_case(path))
        print(f"Resultado para {filename}: {resultado}")
        obtenidos.append(resultado)

'''
Resultado para 5.txt:       1483 - 1483                 :esperado 
Resultado para 10.txt:      2338 - 2338                 :esperado
Resultado para 20.txt:      5034 - 5234                 :esperado X
Resultado para 25.txt:      7058 - 7491                 :esperado X
Resultado para 50.txt:      14976 - 14976               :esperado
Resultado para 100.txt:     26448 - 28844               :esperado X
Resultado para 1000.txt:    1241330 - 1401590           :esperado X
Resultado para 2000.txt:    2529302 - 2869340           :esperado X
Resultado para 5000.txt:    8876453 - 9939221           :esperado X
Resultado para 10000.txt:   30205265 - 34107537         :esperado X

Resultado para 5.txt: 1483
Resultado para 10.txt: 2357
Resultado para 20.txt: 5067
Resultado para 25.txt: 7058
Resultado para 50.txt: 15011
Resultado para 100.txt: 26475
Resultado para 1000.txt: 1241345
Resultado para 2000.txt: 2529316
Resultado para 5000.txt: 8876467
Resultado para 10000.txt: 30205289
'''