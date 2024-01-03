import random
from time import time

def generate_numbers():
    a,b = random.randint(1,100), random.randint(1,100)
    return a,b
def calculate_mcd(a,b):
    if a<b:
        temp=a
        a=b
        b=temp
    print(a,b)
    while a%b!=0 :
        temp=b
        b=a%b
        a=temp
    return b

def main():
    t0 = time()
    a,b=generate_numbers()
    #a,b=12,6
    #a,b=5,5
    #a,b=193193814888888888888867676888888888888866878688888 ,444
    mcd= calculate_mcd(a,b)
    tf = time()
    print("Time optimum",tf - t0)
    print("MCD:",mcd)
main()