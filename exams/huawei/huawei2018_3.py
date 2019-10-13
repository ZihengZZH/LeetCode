'''

写出一个程序，接受一个十六进制的数，输出该数值的十进制表示。（多组同时输入）

输入描述:
输入一个十六进制的数值字符串。
输出描述:
输出该数值的十进制字符串。

输入例子1:
0xA
输出例子1:
10

'''


import sys


def hex2dec(dec_string):
    hex2dec_dict = {
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15
    }
    for ii in range(10):
        hex2dec_dict[str(ii)] = ii

    dec_list = dec_string.split('x')
    assert len(dec_list) == 2

    total = 0
    for jj in range(len(dec_list[1])):
        total += hex2dec_dict[
                    dec_list[1][jj]] * (
                    16**(len(dec_list[1]) - jj - 1))
    return total


if __name__ == "__main__":
    input_string = sys.stdin.readline().strip()
    result = hex2dec(input_string)
    print(result)
