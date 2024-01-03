import math
from time import time
from random import randint
SIZE = 1000
TESTS = 2
def maxCharOcurrence(S):
    max_ocurr, max_char = -math.inf, None
    ascii_tb = {}
    for c in S:
        if c in ascii_tb.keys():
            ascii_tb[c]= ascii_tb[c]+1
        else:
            ascii_tb[c]=1
        if max_ocurr <= ascii_tb[c]:
            if max_ocurr == ascii_tb[c]:
                max_ocurr, max_char = ascii_tb[c], min(c, max_char)
            else:
                max_ocurr, max_char = ascii_tb[c], c

    return (max_ocurr, max_char)
def stringBuilder(size):
    s = ""
    for i in range(size):
        s+=chr(randint(33,165))
    return s
def main():
    for test in range(TESTS):
        s = stringBuilder(int(SIZE))
        t0 = time()
        out = maxCharOcurrence(s)
        tf = time()
        print(s)
        print("Time optimum", out, tf-t0)
main()