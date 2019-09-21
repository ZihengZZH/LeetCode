'''

有一个 n x m 的农田，农田的初始水位是0
现在在坐标 (a,b) 浇灌 c 的水，水会慢慢向四周渗透
每一次渗透都会降低水位直至农田边缘会水位为0

e.g. 

n=3 m=4 a=1 b=2 c=3 will form a matrix of following
0 1 2 1
1 2 3 2
0 1 2 1

n=3 m=4 a=2 b=1 c=2 will form a matrix of following
0 0 0 0 
0 1 0 0 
1 2 1 0

I/O 采用键盘输入和Case输出

'''


import sys

def get_matrix(n, m):
    # n: row
    # m: col
    matrix = []
    for _ in range(n):
        matrix.append([0]*m)
    return matrix

def get_water(a1, b1, a2, b2, c):
    # a1, b1: source point
    # a2, b2: target
    # c: water level
    distance = max(abs(a1-a2) + abs(b1-b2), 0)
    return max(c-distance, 0)

def water(matrix, a, b, c):
    # matrix: original matrix 
    # a: row_no
    # b: col_no
    # c: water level
    row = len(matrix)
    col = len(matrix[0])
    for i in range(row):
        for j in range(col):
            matrix[i][j] = get_water(i, j, a, b, c)
    return matrix

def output(matrix, no):
    print("Case #%d:" % no)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=' ')
        print()

def test():
    matrix = get_matrix(3, 4)
    water(matrix, 1, 2, 3)
    output(matrix, 1)

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    matrices = []
    for i in range(n):
        line = sys.stdin.readline().strip()
        values = list(map(int, line.split()))
        matrix = get_matrix(values[0], values[1]) # original matrix
        helper = get_matrix(values[0], values[1]) # helper matrix to identify if updated
        water(matrix, helper, values[2], values[3], values[4])
        matrices.append(matrix)
    for i in range(n):
        output(matrices[i], i+1)
