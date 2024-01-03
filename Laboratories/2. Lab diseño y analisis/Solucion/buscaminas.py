from sys import stdin

# Best of the cases: empty list


def output_field(n, m, field):                              # cost(0)        times(0)        cost(omega)   Times omega()
    for i in range(n):                                          # k              n               k              0
        for j in range(m):                                      # k              n*n             k              0
            if field[i][j] == '*':                              # k              c*n             k              0
                put_numbers(i, j, n, m, field)                  # k              c*n             k              0
    return field                                                # k              1               k              0


def put_numbers(i, j, n, m, field):
    for x in range(i-1, i+2):                                   # k              c*n             k              0
        for y in range(j-1, j+2):                               # k              c*n*n           k              0
            if -1 < x < n and -1 < y < m:                       # k              c*n-1*n-1*n-1   k              0
                if field[x][y] != '*':                          # k              c*n-1*n-1*n-1   k              0
                    field[x][y] += 1                            # k              c*n-1*n-1*n-1   k              0


def numbers_field(field, n, m):
    for i in range(n):                                          # k              c*n             k              0
        for j in range(m):                                      # k              c*n*n           k              0
            if field[i][j] == '.':                              # k              c*n*n           k              0
                field[i][j] = 0                                 # k              c*n*n           k              0
    return field                                                # k              1               k              0


def print_field(field):
    for row in field:                                           # k              n               k              1
        print(''.join(map(str, row)))                           # k              n-1             k              1


def input_field(n):
    lista = []                                                  # k              1               k              1
    for i in range(n):                                          # k              n               k              1
        line = stdin.readline().strip()                         # k              n-1             k              0
        lista1 = []                                             # k              n-1             k              0
        for i in range(len(line)):                              # k              n               k              0
            lista1.append(line[i])                              # k              n-1             k              0
        lista.append(lista1)                                    # k              n-1             k              0
    return lista                                                # k              1               k              0


def main():
    stdin.readline().strip()                                    # k              1               k              1
    number = stdin.readline().strip().split()                   # k              1               k              1
    cases = 0                                                   # k              1               k              1
    while number != ['0', '0']:                                 # k              c*n             k              1
        print("\nField #{}:".format(cases+1))                      # k              c*n             k              0
        n = int(number[0])                                      # k              c*n             k              0
        m = int(number[1]) if n > 0 else 0                      # k              c*n             k              0
        print(n,m)                                              # k              c*n             k              0
        if m > 0:                                               # k              c*n             k              0
            field1 = input_field(n)                             # k*n            c*n             k*n            0
            field2 = numbers_field(field1, n, m)                # k*n            c*n             k*n            0
            field3 = output_field(n, m, field2)                 # k*n            c*n             k*n            0
            print_field(field3)                                 # k*n            c*n             k*n            0
        number = stdin.readline().strip().split()               # k              c*n             k              0
        cases = cases + 1                                       # k              c*n             k              0


main()                                                                        # O(n**3)                        omega(n)
