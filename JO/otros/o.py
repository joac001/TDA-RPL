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

        while z != 0:
            mult = z * 2
            print(f"{z} * 2 = {mult}")
            z = mult - int(mult)
            dec_res.append(int(mult))
        return dec_res

    print(f"{x} = {"".join(map(str, int_to_bin(int(x)))) + "," + "".join(map(str, dec_to_bin(x - int(x))))}")


if __name__ == "__main__":
    float_to_bin(0.2)
