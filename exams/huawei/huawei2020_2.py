'''

一组工人搬运一批水果，用一维数组存储工人编号和水果名称以及搬运重量，
要求先按水果分组，然后按照搬运重量排序输出。

输入描述：
        输入的第一行包括一个整数 N (1<=N<=100)，代表工人的个数。接下来的 N 行
        每行包括两个正整数 p 和 q，分表代表每个工人的标号和搬运数量，以及一个字符串 m，
        代表水果名称。
输出描述：
        先按照水果分组，然后按照工人的搬运重量从小到达进行排序，并将排序后的信息打印出来。
        如果工人的搬运重量相同，则按照编号的大小进行从小到达排序，并且要求水果输出的次序同输入次序

e.g.
INPUT:
    Apple 1 80
    Apple 2 62
    Apple 4 73
    Orange 4 65
    Orange 1 90
    Apple 3 91
    Orange 3 88
    Orange 5 90
OUTPUT:
    Apple 2 62
    Apple 4 73
    Apple 1 80
    Apple 3 91
    Orange 4 65
    Orange 3 88
    Orange 1 90
    Orange 5 90

'''


import sys


def sub_rank(values):
    return sorted(values, key=lambda x: (x[2], x[1]))


def rank(values, names):
    result = []
    for name in names:
        result.extend(sub_rank([val for val in values if val[0] == name]))
    return result

def sub_rank2(values):
    return sorted(values, key=lambda x: (x[0], x[2], x[1]))

def rank2(values, names):
    fruit_dict, inverse_dict = {}, {}
    for val, key in enumerate(names):
        fruit_dict[key] = int(val)
        inverse_dict[int(val)] = key
    new_values = [[fruit_dict[val[0]], val[1], val[2]] for val in values]
    sorted_values = sub_rank2(new_values)
    return [[inverse_dict[val[0]], val[1], val[2]] for val in sorted_values]


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    names = []          # [name1, name2, ...]
    ids = []            # [id1, id1, ...]
    values = []         # [[name, ID, wright]]
    while True:
        line = sys.stdin.readline().strip()
        value = line.split()
        if value[0] not in names:
            names.append(value[0])
        if value[1] not in ids:
            ids.append(value[1])
        values.append([value[0], int(value[1]), int(value[2])])
        if len(ids) == n:
            break
    
    # values = [
    #     ['Apple', 2, 62],
    #     ['Apple', 10, 62],
    #     ['Apple', 7, 100],
    #     ['Orange', 2, 62],
    #     ['Apple', 4, 62],
    #     ['Orange', 5, 90],
    #     ['Orange', 2, 90]
    # ]
    # names = ['Apple', 'Orange']

    results = rank2(values, names)
    
    for ii in range(len(results)):
        print("%s %d %d" % (results[ii][0], results[ii][1], results[ii][2]))
