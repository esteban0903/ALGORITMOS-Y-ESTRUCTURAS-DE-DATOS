def mcd(m,n):                                           # cost            time(O)            time(omega)
    return m if n==0 else mcd(n,m%n)                    #  c1               log(n)                 1

print(mcd(0,0))                                 #  c1                1                      1