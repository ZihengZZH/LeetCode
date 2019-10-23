'''

最短路径问题，在一个制定地图里行走，求可能的最短距离

'''


matrix = [
    [1,0,1,1,1],
    [1,1,1,0,1],
    [1,1,0,0,1],
    [1,0,1,1,1],
    [1,1,1,0,1]
]

n = len(matrix)

dp_matrix = [[0]*(n+1) for _ in range(n+1)]

for ii in range(1, n+1):
    for jj in range(1, n+1):
        if ii == 1 and jj == 1:
            dp_matrix[ii][jj] = 1
        elif matrix[ii-1][jj-1] == 1:
            if matrix[ii-2][jj-1] != 0:
                dp_matrix[ii][jj] = min(dp_matrix[ii-1][jj] + 1, dp_matrix[ii][jj])
            elif matrix[ii-1][jj-2] != 0:
                dp_matrix[ii][jj] = min(dp_matrix[ii][jj-1] + 1, dp_matrix[ii][jj])
            elif matrix[ii][jj-1] != 0:
                dp_matrix[ii][jj] = min(dp_matrix[ii+1][jj] + 1, dp_matrix[ii][jj])
            elif matrix[ii-1][jj] != 0:
                dp_matrix[ii][jj] = min(dp_matrix[ii][jj+1] + 1, dp_matrix[ii][jj])

def print_new(matrix):
    for ii in range(len(matrix)):
        for jj in range(len(matrix[ii])):
            print(dp_matrix[ii][jj], end=' ')
        print()

print_new(dp_matrix)
print(dp_matrix[-1][-1])