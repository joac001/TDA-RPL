from parte_dos import maxCoins
from termcolor import colored

def test(coins, expectedAnswer):
    got = maxCoins(coins)
    if got != expectedAnswer:

        print(colored(f"\u2717 Coins: {coins}, expected: {expectedAnswer}, got: {got}", "red"))
        return

    print(colored(f"\u2713 Coins: {coins}, expected: {expectedAnswer}", "green"))

    return

# coins, expectedAnswer
test([1, 10, 5], 6)
test([3, 7, 2, 8, 5], 10)
test([1, 2, 3, 4, 5, 6], 12)
test([8, 15, 3, 7], 22)
test([2, 2, 2], 4)
test([1, 2, 3, 4, 5, 6, 7, 8], 20)
test([20, 30, 2, 10], 40)
test([1, 2, 3, 4, 5, 6, 7], 16)
test([1, 2, 5, 10, 7], 13)
test([1, 5, 10, 20], 25)
test([1, 5, 10, 6, 2, 50], 61)
test([1, 1, 1, 1, 1, 1], 3)
test([5, 5, 5, 5], 10)
test([10, 20, 30, 40], 60)
test([2, 4, 6, 8, 10], 18)
test([1, 3, 5, 7, 9], 15)
test([1, 2, 4, 8, 16], 21)
test([3, 6, 9, 12], 18)
test([7, 14, 21, 28], 42)
test([2, 3, 5, 7, 11], 18)
test([1, 4, 9, 16, 25], 35)