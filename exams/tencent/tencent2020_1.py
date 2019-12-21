'''

INTERVIEW - 1

Given a sorted list
[1, 1, 2, 3, 4, 4, 4, 4, 8, 10, 20]
return max count 4

'''


import sys


def get_max_count(alist):
    count,  max_count = 0, 0
    cur_idx = 0
    for ii in range(len(alist)):
        if alist[ii] == alist[cur_idx]:
            count += 1
        else:
            max_count = max(count, max_count)
            count = 1
            cur_idx = ii
    max_count = max(count, max_count)
    return max_count


if __name__ == "__main__":
    test_list = [1, 1, 2, 3, 4, 4, 4, 4, 4, 8, 10, 20]
    print(test_list, get_max_count(test_list))
    test_list = [1, 1, 2, 3, 8, 10, 20, 4, 4, 4, 4, 4]
    print(test_list, get_max_count(test_list))