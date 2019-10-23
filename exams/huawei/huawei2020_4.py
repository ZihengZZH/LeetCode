'''

计算一个字符串中所有的闭合区间个数
例如 4 有一个闭合区间，8 有两个
注意字符串包含 [0-9] [a-z] [A-Z]

e.g.
INPUT:  asdqwe14
OUTPUT: 5

'''


import sys


helper = {
    '0': 1, '4': 1, '6': 1,
    '8': 2, '9': 1, 'a': 1,
    'b': 1, 'd': 1, 'e': 1,
    'g': 1, 'o': 1, 'p': 1,
    'q': 1, 'A': 1, 'B': 2,
    'D': 1, 'O': 1, 'P': 1,
    'Q': 1, 'R': 1
}

def get_number(astring):
    count = 0
    for ii in range(len(astring)):
        char = astring[ii]
        if char in helper.keys():
            count += helper[char]
    return count

if __name__ == '__main__':
    aline = sys.stdin.readline().strip()
    print(get_number(aline))