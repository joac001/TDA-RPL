import math


def float_to_bin(x):
    def int_to_bin(y):
        int_res = list()
        while y > 0:
            division = y // 2
            rest = y % 2
            print(f"{y} // 2 = {division} || {y} % 2 = {rest}")
            int_res.append(rest)
            y = division
        if len(int_res) == 0:
            int_res.append(0)
        return int_res[::-1]

    def dec_to_bin(z):
        dec_res = list()
        original = z
        contador = 0

        def es_parecido():
            # Analizar si un numero flotante es parecido a otro
            # Por ejemplo 0.2 debe ser parecido a 0.20000000000000018
            return math.isclose(original, z, rel_tol=1e-9, abs_tol=1e-9)

        while z != 0:
            if es_parecido() and contador > 0:
                print(f"Se repite el número en el paso {contador}")
                break
            contador += 1
            mult = z * 2
            print(f"{z} * 2 = {mult}")
            z = mult - int(mult)
            dec_res.append(int(mult))
        return dec_res

    # Simplemente une la lista de soluciones de la parte entera y decimal para que se imprima de forma legible.
    print(f"{x} = {"".join(map(str, int_to_bin(int(x)))) + "," + "".join(map(str, dec_to_bin(x - int(x))))}")


if __name__ == "__main__":
    float_to_bin(0.2)
