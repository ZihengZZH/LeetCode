'''

字节跳动大街上有许多商铺，其中只有一部分有为顾客开放厕所。
街道办想提供一项便民服务，在每家店铺门口放一个标志，写明距离当前店铺
最近的厕所有几个店铺的距离。如果当前店铺就有厕所，则标志为0。
请帮助街道办的同志完成这项工作。
PS: 已知整条街上至少有一个厕所

e.g.
INPUT:  9 \n XX0X00XXX ('O'表示有厕所，'X'表示没有)
OUTPUT: 2 1 0 1 0 0 1 2 3

'''


alist = 'XXOXXXOOXXX'

values = [0] * len(alist)
firstX = 0

def reverse_values(start, end):
    tmp = values[start:end]
    if start == 0:
        values[start:end] = tmp[::-1]
    else:
        internal = (end - start) // 2
        values[(end-internal):end] = tmp[:internal][::-1]


for i in range(len(alist)):
    if alist[i] == 'X' and firstX == i:
        firstX = i
        values[i] = 1
    elif alist[i] == 'X' and firstX != i:
        values[i] = values[i-1] + 1
    elif alist[i] == 'O':
        reverse_values(firstX, i)
        firstX = i+1
