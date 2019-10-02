'''

给定一个数组序列, 需要求选出一个区间, 使得该区间是所有区间中经过如下计算的值最大的一个：
区间中的最小数 * 区间所有数的和最后程序输出经过计算后的最大值即可，不需要输出具体的区间。
如给定序列  [6 2 1]则根据上述公式, 可得到所有可以选定各个区间的计算值:

[6] = 6 * 6 = 36;
[2] = 2 * 2 = 4;
[1] = 1 * 1 = 1;
[6,2] = 2 * 8 = 16;
[2,1] = 1 * 3 = 3;
[6, 2, 1] = 1 * 9 = 9;

从上述计算可见选定区间 [6] ，计算值为 36， 则程序输出为 36。
区间内的所有数字都在[0, 100]的范围内;

'''


import sys

def max_value(points):
    max_val = []
    for i in range(len(points)):
        j = i
        k = i - 1
        subsum = 0
        while points[i] <= points[j] and j < len(points)-1:
            subsum += points[j]
            j += 1
        while points[i] <= points[k] and k >= 0:
            subsum += points[k]
            k -= 1
        max_val.append(points[i] * subsum)
    return max(max_val)

def test():
    points = [81, 87, 47, 59, 81, 18, 25, 40, 56, 0]   
    print(points)
    res = max_value(points)
    print(res)
    
if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    points = list(map(int, line.split())) 
    res = max_value(points)
    print(res)