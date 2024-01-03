from sys import stdin

# Best case: n=1


def compare_elements(mat, n):                                # cost(0)       times(0)       cost(omega)   Times omega()
    hadamard = calculate_pow(n)                                 # k*n            1               k              1
    if hadamard == "Hadamard" and n != 1:                       # k              1               k              0
        band = True
        while band:
            for i in range(0, n, 2):                            # k              n/2             k              0
                equal = 0
                for j in range(n):                              # k              n               k              0
                    if mat[i][j] == mat[i+1][j]:                # k              n-1             k              0
                        equal += 1                              # k              n-1             k              0
                if equal != n/2:                                # k              1               k              0
                    hadamard = "No Hadamard"                    # k              1               k              0
                    band = False
            band = False
    return hadamard                                             # k              1               k              1


def calculate_pow(x):
    i = 0                                                       # k              1               k              1
    rta = "Impossible"                                          # k              1               k              1
    band = True                                                 # k              1               k              1
    while band:                                                 # k              n               k              1
        if 2**i == x:                                           # k              n               k              1
            band = False                                        # k              n               k              1
            rta = "Hadamard"                                    # k              n               k              1
        elif 2**i > x:                                          # k              n               k              1
            band = False                                        # k              1               k              0
        i = i+1                                                 # k              n               k              1
    return rta                                                  # k              1               k              1


def print_mat(mat):
    for row in mat:                                             # k              n               k              1
        print(''.join(map(str, row)))                           # k              n-1             k              1


def create_mat(n, spaces):
    lista = []                                                  # k              1               k              1
    if n >= 2:                                                  # k              1               k              1
        for i in range(1, n+1):                                 # k              n               k              0
            sublist = []                                        # k              n-1             k              0
            for j in range((i-1)*n, n*i):                       # k              n*n-1           k              0
                sublist.append(spaces[j])                       # k              n-1*n-1*n       k              0
            lista.append(sublist)                               # k              n-1             k              0
    elif n == 1:                                                # k              1               k              0
        lista.append(spaces[0])                                 # k              1               k              1
    return lista                                                # k              1               k              1


def main():
    stdin.readline().strip()                                    # k              1               k              1
    n = int(stdin.readline().strip())                           # k              1               k              1
    spaces = stdin.readline().strip().replace(" ", "")  # k          1               k              1
    mat = create_mat(n, spaces)                                 # k*n            n-1             k*n            1
    print_mat(mat)                                              # k              1               k              1
    print(compare_elements(mat, n))                             # k*n            1               k*n            1


main()                                                                         # 0(n**3)                       omega(n)
