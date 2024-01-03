from sys import stdin
from time import time
memo = {}

def super_digit(number):
    if len(number) == 1:
        return int(number)
    else:
        suma = sum(int(digit) for digit in number)
        return super_digit(str(suma))
def super_digitmemo(number):
    if number in memo:
        return memo[number]
    if len(number) == 1:
        return int(number)
    else:
        suma = sum(int(digit) for digit in number)
        memo[number] = suma
        return super_digitmemo(str(suma))


def main():
    line = stdin.readline().strip()
    while line:
        n, k = line.split()
        t1 = time()
        print(super_digit(n * int(k)))
        t2 = time()
        print("Time no memo", t2 - t1)

        t1 = time()
        print(super_digitmemo(n * int(k)))
        t2 = time()
        print("Time memo",t2-t1)
        line = stdin.readline().strip()


main()
