'''

给定一个M行N列的矩阵（M*N个格子），每个格子中放着一定数量的平安果。
你从左上角的各自开始，只能向下或者向右走，目的地是右下角的格子。
每走过一个格子，就把格子上的平安果都收集起来。求你最多能收集到多少平安果。
注意：当经过一个格子时，需要一次性把格子里的平安果都拿走。
限制条件：1<N,M<=50；每个格子里的平安果数量是0到1000（包含0和1000）.

输入描述：
输入包含两部分：
第一行M, N
接下来M行，包含N个平安果数量
输出描述：
一个整数
最多拿走的平安果的数量

示例：
输入
2 4
1 2 3 40
6 7 8 90
输出
136

'''


def get_results(matrix):
    dp_matrix = [[0] * (len(matrix[0])+1) for _ in range(len(matrix)+1)]
    for ii in range(len(dp_matrix)):
        for jj in range(len(dp_matrix[ii])):
            if ii == 0 or jj == 0:
                continue
            dp_matrix[ii][jj] = max(dp_matrix[ii-1][jj], dp_matrix[ii][jj-1]) + matrix[ii-1][jj-1]
    return dp_matrix[-1][-1]


matrix = [
    [1,2,3,40],
    [6,7,8,90]
]
print(get_results(matrix))