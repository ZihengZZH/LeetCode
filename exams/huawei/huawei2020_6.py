'''

多规则排序问题，规则较为复杂。
输入为: 姓名<space>语文分数<space>数学分数<space>英语分数
一共输入 10 组这样的数据
首先，合格学生需要没有不及格的科目 (>=60)
在所有合格学生中，排序出总分排名前三名学生录取
排序规则如下:
1. 总分 (从大到小))
2. 语文 (从大到小))
3. 数学 (从大到小)
4. 英语 (从大到小)
5. 姓名 ASCII 码数值 (从小到大)
排序后，先输出所有合格学生，再输出排名前三的录取学生

'''


import sys


def get_first_final(alines):
    inputs_int = []
    max_len = 0
    for inp in alines:
        alist = inp.split(' ')
        max_len = max(0, len(alist[0]))
        alist[1] = int(alist[1])
        alist[2] = int(alist[2])
        alist[3] = int(alist[3])
        if alist[1] < 60 or alist[2] < 60 or alist[3] < 60:
            continue
        inputs_int.append(alist)

    for input_int in inputs_int:
        input_int[0] += ' '*(max_len - len(input_int[0]))

    inputs_int_sort = sorted(inputs_int, key=lambda x: (
        x[1]+x[2]+x[3], 
        x[1], 
        x[2], 
        x[3], 
        [-ord(x[0][ii]) for ii in range(max_len)]), 
        reverse=True)

    scores = []
    final_list = []
    for names in inputs_int_sort:
        score = names[1]+names[2]+names[3]
        if score not in scores and len(scores) < 3:
            scores.append(score)
            if names[1] >= 60 and names[2] >= 60 and names[3] >= 60:
                final_list.append(names)
        elif score in scores and len(scores) <= 3:
            if names[1] >= 60 and names[2] >= 60 and names[3] >= 60:
                final_list.append(names)
    return inputs_int_sort, final_list

def print_new(alist):
    for aa in alist:
        for a in aa:
            print(a, end=' ')
        print()

if __name__ == '__main__':
    inputs = []
    for _ in range(10):
        line = sys.stdin.readline().strip()
        inputs.append(line)
    inputs_int_sort, final_list = get_first_final(inputs)
    print_new(inputs_int_sort)
    print()
    print_new(final_list)

    # testcase = [
    #     "goudan2 80 60 40",
    #     "zhaowu 70 60 40",
    #     "zhangsan 90 40 80",
    #     "yatou 90 90 40",
    #     "goudan1 80 40 80",
    #     "gousheng 40 60 60",
    #     "lilei 40 70 60",
    #     "hanmingmei 80 90 60",
    #     "liutao 80 90 60",
    #     "SimonYin 70 60 60"
    # ]

