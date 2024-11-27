from parte_dos import maxCoins
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
esperados = {'5.txt' : 1483, '10.txt': 2338, '20.txt': 5234,'25.txt': 7491,'50.txt': 14976,'100.txt': 28844,'1000.txt': 1401590,'2000.txt': 2869340,'5000.txt': 9939221,'10000.txt': 34107537}
obtenidos = []

for filename in os.listdir(directory):
    if filename != 'Resultados Esperados.txt' and filename.endswith(".txt"):
        path = os.path.join(directory, filename)
        resultado = maxCoins(read_test_case(path))
        print(f"{filename}:")
        print(f"Obtenido: {resultado}")
        print(f"Esperado: {esperados[filename]}")
        print("Correcto" if resultado == esperados[filename] else "Incorrecto")
        print(f"Dif: {abs(resultado - esperados[filename])}")
        print(f"{'-'*20}\n")
        obtenidos.append(resultado)