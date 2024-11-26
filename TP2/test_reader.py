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
                break
    
    return numbers


directory = "./TP2/TP2/"
esperados = [1483, 2338, 5234, 7491, 14976, 28844, 1401590, 2869340, 9939221, 34107537]
obtenidos = []

for filename in os.listdir(directory):
    if filename != 'Resultados Esperados.txt' and filename.endswith(".txt"):
        path = os.path.join(directory, filename)
        resultado = maxCoins(read_test_case(path))
        print(f"Resultado para {filename}: {resultado}")
        obtenidos.append(resultado)

if obtenidos == esperados:
    print("Todos los tests pasaron correctamente")
else:
    print("Algun test fallo")
    print(f"Esperados: {esperados}")
    print(f"Obtenidos: {obtenidos}")