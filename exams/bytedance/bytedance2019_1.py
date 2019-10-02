'''

给定一个长度为n的，仅包含0,1的数列。例如1,0,0,1,1,1,0。我们可以轻易算出，它的最长全1区间长度是3。从数组的第4位到第6位。

现在，你获得了k次可以将某个位置上的0变为1的机会，但可以不用完所有的机会。
请你给出，你使用了你的变化机会后，这个数列的最长全1区间最大是多少

'''


def get_results(alist, n, k):
    start = 0
    end = 0
    maxlen = []
    # until the end
    while end < n:
        # proceed to get maxlen
        while k >= 0 and end < n:
            if alist[end] == 0:
                k -= 1
            end += 1
        # possible maxlen
        maxlen.append(end - start - 1)
        print(end, start)
        # if start == 0, no need to cost k
        if alist[start] == 0:
            k += 1
        # proceed
        start += 1
    return max(maxlen)

if __name__ == '__main__':
    n, k = 10, 1
    alist = [0, 1, 1, 0, 1, 1, 0, 1, 1, 0]
    result = get_results(alist, n, k)
    print(result)