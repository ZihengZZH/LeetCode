'''

找出每个坐标点在多少个坐标区间内 left <= target <= right
输入坐标点数量和坐标区间数量，之后输入具体坐标点和坐标区间

e.g.
INPUT:
10 5
0 1 2 3 4 5 6 7 8 9
0 5
10 20
-5 -3
7 7
100 105
OUTPUT:
1 1 1 1 1 1 0 1 0 0

INPUT:
5 1
1 1 1 1 1
0 2
1 1 1 1 1
'''


import sys

def include(target, lists):
    # check if target is in each list (in lists)
    count = 0
    for lst in lists:
        if lst[0] <= target and target <= lst[1]:
            count += 1
    return count

def get_result(Ns, Ms):
    res = []
    for n in Ns:
        res.append(include(n, Ms))
    return res

def output(results, no):
    print("Case #%d:" % no)
    for res in results:
        print(res)

def test():
    Ns = [0,1,2,3,4,5,6,7,8,9]
    Ms = [[0, 5],
        [10, 20],
        [-5, -3],
        [7, 7],
        [100, 105]]
    res = get_result(Ns, Ms)
    output(res, 1)

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    Ns_n, Ms_n = [], []
    for i in range(n):
        values = list(map(int, sys.stdin.readline().strip().split()))
        _, m = values[0], values[1]
        Ns = list(map(int, sys.stdin.readline().strip().split()))
        Ms = []
        for j in range(m):
            ms = list(map(int, sys.stdin.readline().strip().split()))
            Ms.append(ms)
        Ns_n.append(Ns)
        Ms_n.append(Ms)
    for i in range(n):
        res = get_result(Ns_n[i], Ms_n[i])
        output(res, i+1)

