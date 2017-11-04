'''

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:
Input: 16
Returns: True

Example 2:
Input: 14
Returns: False

'''

import random
import math

class Solution(object):

    def isPerfectSquare(self, num):
        if num == 1:
            return True
        index = num/2
        while index != 1:
            if index*index == num:
                return True
            index -= 1
        return False

    # Newton-Raphson method
    def online(self, num):
        r = num
        while r*r > num:
            r = (r+num/r)/2
        return r*r == num


if __name__ == "__main__":
    solu = Solution()
    for i in range(10):
        input_num = random.randint(1,100)
        res = solu.isPerfectSquare(input_num)
        res2 = solu.online(input_num)
        print input_num,"ANSWER IS", res,res2
