from sys import stdin
# phrase is an array of strings
# best of the cases: empty str


def decode_phrase(word):                                        # cost(0)  times(0)  cost(omega)  Times omega()
    result, letter_index = "", 0                                   # k       1           k              1
    for letter in word:                                            # k       n-1         k              1
        if len(letter) > letter_index:                             # k       n           k              1
            result += letter[letter_index]                           # k       c*n         k              0
            letter_index += 1                                        # k       c*n         k              0
    return result                                                  # k       n           k              1


def read_paragraph():
    line = stdin.readline().strip()                                # k       n-1         k              1
    while line:                                                    # k       n-1         k              1
        words = line.split()                                       # k       n-1         k              1
        print(decode_phrase(words))                                 # k       n-1         k              1
        line = stdin.readline().strip()                            # k       n-1         k              1


def main():
    paragraphs = stdin.readline().strip()                          # k       1           k              1
    stdin.readline().strip()                                       # k       1           k              1
    if paragraphs != "":                                           # k        1           k              1
        for case in range(int(paragraphs)):                        # k       n           k              1
            print("Case #{}:".format(case+1))                      # k       n-1         k              1
            read_paragraph()                                       # k       n-1         k              1
    else:
        print("No message")


main()                                                                   # 0(n**2)                 omega (n)
