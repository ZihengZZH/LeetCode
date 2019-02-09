'''

Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number.

'''


class Solution(object):

    def isUgly(self, num):
        for p in 2, 3, 5:
            while num % p == 0 < num:
                num /= p
        return num == 1

number = raw_input("Enter the integer: ")
numB = int(number)
solu = Solution()
result = solu.isUgly(numB)
print "The result is", result
