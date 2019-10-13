'''

明明想在学校中请一些同学一起做一项问卷调查，为了实验的客观性，
他先用计算机生成了N个1到1000之间的随机整数（N≤1000），
对于其中重复的数字，只保留一个，把其余相同的数去掉，
不同的数对应着不同的学生的学号。然后再把这些数从小到大排序，
按照排好的顺序去找同学做调查。请你协助明明完成“去重”与“排序”的工作
(同一个测试用例里可能会有多组数据，希望大家能正确处理)。


Input Value
n               输入随机数的个数
inputArray      n个随机整数组成的数组

Return Value
OutputArray    输出处理后的随机整数


注：测试用例保证输入参数的正确性，答题者无需验证。测试用例不止一组。

输入描述:
输入多行，先输入随机整数的个数，再输入相应个数的整数
输出描述:
返回多行，处理后的结果


输入例子1:
11
10
20
40
32
67
40
20
89
300
400
15

输出例子1:
10
15
20
32
40
67
89
300
400

'''


import sys


def partion(inputs, left, right):
    pivot = inputs[left]
    while left < right:
        while left < right and inputs[right] > pivot:
            right -= 1
        if left < right:
            inputs[left] = inputs[right]
        
        while left < right and inputs[left] < pivot:
            left += 1
        if left < right:
            inputs[right] = inputs[left]

    inputs[left] = pivot
    return left

def quick_sort(inputs, left, right):
    if left < right:
        pivot_index = partion(inputs, left, right)
        quick_sort(inputs, left, pivot_index)
        quick_sort(inputs, pivot_index+1, right)

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    input_list = []
    for _ in range(n):
        value = int(sys.stdin.readline().strip())
        input_list.append(value)
    quick_sort(input_list, 0, len(input_list) - 1)
    output_list = input_list
    for output in output_list:
        print(output)
