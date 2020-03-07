'''

小明马上要参加期末考试，所以他特意用一段时间来做练习题，这段时间为 m 秒。
一共有序号 1～n 的 n 道题目。小明从序号 1 的题目开始做，按照序号递增的顺序开始解答。
每道题如果解答需要消耗时间 a[i] （如果剩余的时间不足 a[i] 则无法解答），
如果跳过则不消耗时间。
因为每道题都可能帮助到期末考试，小明想知道对于每一道题最少需要放弃前面几道题，才能解答完成。

e.g. 
INPUT: 
第一行是样例个数；
每个样例的第一行是 n, m, 表示n道题目和练习时长m妙
第二行是n个数字 a[i]，分别表示n道题目解答耗时为 a[i] 秒（保证所有 a[i] <= m）
OUTPUT:
每个样例输出一行，一行包括n个数字，分别n个题目如果完成需要放弃前面的最少题目数

'''


N, M = 5,5
vals = [1,2,3,4,5]

res = [0] * N
for i in range(1, N):
    if sum(vals[:i+1]) <= M:
        res[i] = 0
    else:
        tmp = vals[:i+1]
        sum_val = sum(tmp)
        count = 1
        while tmp and (sum_val - max(tmp)) > M:
            count += 1
            tmp.remove(max(tmp))
        res[i] = count

print(res)