def distance(p1,p2):
    dx = abs(p1[0]-p2[0])
    dy = abs(p1[1]-p2[1])
    return max(dx, dy)
def numCells(p1, p2):
    return distance(p1,p2) + 1
def wonderSquare(n):
    size = 2*n-1
    center = (n-1, n-1)
    mat = [[numCells((i,j), center) for j in range(size)] for i in range(size)]
    return mat
def printMat(mat):
    for row in mat:
        print(''.join(map(str, row)))

def main():
    for i in range(1,3):
        print(i, "======================")
        printMat(wonderSquare(i))
        print("======================")

main()