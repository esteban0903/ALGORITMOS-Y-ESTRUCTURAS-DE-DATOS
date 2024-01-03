from sys import stdin


def power(x, n, y):
    if x == 0 or x == y**n:
        return 1
    if x < 0 or x < y**n:
        return 0
    else:
        return power(x-y**n, n, y+1) + power(x, n, y+1)


def main():
    x = stdin.readline().strip()
    n = stdin.readline().strip()
    while x:
        print(power(int(x), int(n), 1))
        x = stdin.readline().strip()
        n = stdin.readline().strip()


main()
