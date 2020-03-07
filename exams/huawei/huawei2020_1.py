'''

质量是消费者业务的生命线。用户遇到产品问题一般会拨打公司热线或通过网络求助。
公司结合商城评论、网络评论、热线等途径每小时收集用户反馈的手机问题形成每日的总数据。
形成问题解决与改进方向路标。
假定这一系列数据每行代表特别的负面舆论与当前上报数量，需要根据公司标准输出预警舆情数量。
舆情预警设定标准：单日相同负面舆情数量大于等于10例即可发起预警。
约束：   每行舆情数据中间用英文逗号隔开，逗号前面代表特定舆情为字母加数字组成的长度为4-10为字串，
        逗号后面代表上报数量范围在1～100之间；不用考虑输入内容为非法的情况，数据量不超过100

输入描述：
        舆情问题表示，反馈数量
输出描述：
        舆情预警数量

e.g.
INPUT:
    Test1,3
    Test1,7
    morale1,7
    morale3,6
    morale1,4
    hdgkshc1,5
OUTPUT:
    2

'''


import sys


if __name__ == '__main__':
    res_dict = {}
    while True:
        line = sys.stdin.readline().strip()
        if line == '':
            break
        name, level = line.split(',')
        if name in res_dict.keys():
            res_dict[name] += int(level)
        else:
            res_dict[name] = int(level)
    
    count = 0
    for val in res_dict.values():
        if val >= 10:
            count += 1
    print(count)