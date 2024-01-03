from sys import stdin
from time import time


def calculate_3nmemo(n):
    if n in memo:
        return memo[n]
    if n == 1:
        return 1
    if n % 2 == 0:
        rta = 1 + calculate_3nmemo(n//2)
    else:
        rta = 1 + calculate_3nmemo(3*n+1)

    memo[n] = rta
    return rta

memo={}
def calculate_3n(n, cases):
    if n == 1:
        return cases+1
    if n % 2 == 0:
        return calculate_3n(n//2, cases+1)
    else:
        return calculate_3n(3*n+1, cases+1)

def main():
    line = stdin.readline().strip()
    while line:
        n, m = map(int, line.split())
        # NO MEMO
        t1 = time()
        cases3 = 0
        for i in range(min(n,m), max(n,m)+1):
            cases = 0
            cases2 = calculate_3n(i, cases)
            cases3=max(cases3,cases2)
        t2=time()
        print(n, m, cases3)
        print("Time no mem:",t2-t1)

        #MEMO
        t1 = time()
        cases3 = 0
        for i in range(min(n, m), max(n, m) + 1):
            cases = 0
            cases2 = calculate_3nmemo(i)
            cases3 = max(cases3, cases2)
        t2 = time()
        print(n, m, cases3)
        print("Time mem:", t2 - t1)
        line = stdin.readline().strip()


main()
