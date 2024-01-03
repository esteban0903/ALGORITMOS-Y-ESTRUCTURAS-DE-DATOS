from time import time
from random import randint

size=1000
def analyze_str(str1):
    size=len(str1)-1
    band=True
    x="yes"
    while band:
        for i in str1:
            if i!=str1[size]:
                band=False
                x="no"
            size=size-1
        band=False
    if x=="yes":
        answer="Es palindromo"
    else:
        answer="No es palindromo"
    return answer
def stringBuilder(size):
    s = ""
    for i in range(size):
        s+=chr(randint(65,90))
    return s
def main():
    t0 = time()
    #str1=""
    #str1="somos"
    str1=stringBuilder(int(size))
    print(str1)
    out = analyze_str(str1)
    tf = time()
    print("Time optimum", out, "time:",tf - t0)
main()


