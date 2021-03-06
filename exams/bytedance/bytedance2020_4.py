'''

给定一个字符串 s，我们定义一个循环节是这个字符串中最短的重复出现的片段，
循环节的长度为 k，字符串首尾两端的循环节可以不完整，即只需满足 s[i] = s[i%k]
举例：
ABAABAA 的循环节是 ABA，长度为 3
AAAA 的循环节是 A，长度为 1
AABBB 的循环节是 AABBB，长度为 5

假设 s 有 a 个字母 A 和 b 个字母 B 组成，问 s 可能形成的循环节长度 k 有多少中可能？
注意是 k 的取值可能，而非循环节本身的可能

e.g.
INPUT:
输入仅有一行，为两个正整数，用空格分开，分别代表 a 和 b (a, b in [1, 10^9])
OUTPUT:
一个正数，代表循环节长度 k 的可能取值有多少种

'''