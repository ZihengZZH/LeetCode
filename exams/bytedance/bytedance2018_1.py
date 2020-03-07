'''

P为给定的二维平面整数点集。定义 P 中某点x，如果x满足 P 中任意点都不在 x 的右上方区域内(横纵坐标都大于x)，
则称其为“最大的”。求出所有“最大的”点的集合。(所有点的横坐标和纵坐标都不重复, 坐标轴范围在[0, 1e9) 内)

如下图：实心点为满足条件的点的集合。请实现代码找到集合 P 中的所有 ”最大“ 点的集合并输出。

'''


import sys

def get_results(points):
    points = sorted(points, key=lambda x: x[0], reverse=True)
    res = []
    maxy = -1
    for i in range(len(points)):
        if points[i][1] > maxy:
            maxy = points[i][1]
            res.append(i)
    results = [points[r] for r in res[::-1]]
    return results

def test():
    points = [
        [298498081, 747278511],
        [427131847, 460128162],
        [939984059, 817455089],
        [911902081, 683024728],
        [474941318, 6933274],
        [140954425, 607811211],
        [336122540, 629431445],
        [208240456, 458323237],
        [646203300, 469339106],
        [106410694, 436340495]
    ]
    results = get_results(points)
    for res in results:
        print("%d %d" % (res[0], res[1]))

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    points = []
    for i in range(n):
        line = sys.stdin.readline().strip()
        values = list(map(int, line.split()))
        points.append(values)
    results = get_results(points)
    for res in results:
        print("%d %d" % (res[0], res[1]))


'''
similar thinking as ContainerMostWater

|   ContainerMostWater              |   this one                    |
|   max(AREA = HEIGHT*WIDTH)        |   max(XX, YY)                 |
|   keep WIDTH starting from max    |   keep XX starting from max   |
'''