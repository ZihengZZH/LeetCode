'''

计算 C = (((A^T) * B) * B^T)^T
其中 T 是转置, * 是矩阵乘法(外积)
计算结果对指数1009取模

e.g. 
A =         B =         C = 
| 1 2 |     | 4 3 |        | 58 94 |
| 3 4 |     | 2 1 |        | 26 42 |

I/O 采用键盘输入和Case输出

'''


import sys

def get_matrix(n, m):
    matrix = []
    for _ in range(n):
        matrix.append([0]*m)
    return matrix

def transpose(matrix):
    # transpose matrixes (2D list py)
    row = len(matrix)
    col = len(matrix[0])
    matrix_T = get_matrix(col, row)
    for i in range(row):
        for j in range(col):
            matrix_T[j][i] = matrix[i][j]
    return matrix_T

def element(list_1, list_2):
    # get multiplication of two equal-length lists
    if len(list_1) != len(list_2):
        return
    res = [list_1[i] * list_2[i] for i in range(len(list_1))]
    return sum(res) % 1009 # get mod 1009

def multiply(matrix_1, matrix_2):
    row = len(matrix_1)
    col = len(matrix_2[0])
    # transpose to both row-wise for simpler use
    matrix_2_T = transpose(matrix_2)
    res = get_matrix(row, col)
    for i in range(row):
        for j in range(col):
            res[i][j] = element(matrix_1[i], matrix_2_T[j])
    return res

def output(matrix):
    row = len(matrix)
    col = len(matrix[0])
    print("%d %d" % (row, col))
    for i in range(row):
        for j in range(col):
            print(matrix[i][j], end=' ')
        print()

def test():
    A = [[1,2],[3,4]]
    B = [[4,3],[2,1]]
    B_T = transpose(B)
    A_T = transpose(A)
    C = multiply(A_T, B)
    C = transpose(multiply(C, B_T))
    output(C)

if __name__ == "__main__":
    values = list(map(int, sys.stdin.readline().strip().split()))
    n, m = values[0], values[1]
    A, B = [], []
    for i in range(n):
        line = sys.stdin.readline().strip()
        values = list(map(int, line.split()))
        A.append(values)
    for i in range(n):
        line = sys.stdin.readline().strip()
        values = list(map(int, line.split()))
        B.append(values)
    B_T = transpose(B)
    A_T = transpose(A)
    C = multiply(A_T, B)
    C = transpose(multiply(C, B_T))
    output(C)



