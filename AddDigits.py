'''

Given a non-negative integer num, 
repeatedly add all its digits until the result has only one digit.

For example:
Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. 
Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?

'''

import random

class Solution:

    def addDigits(self, num):
        while len(str(num)) != 1:
            num_lst = list(str(num))
            res = 0
            for item in num_lst:
                res += int(item)
            num = res
        return num
        

if __name__ == "__main__":
    solu = Solution()
    for i in range(10):
        input = random.randint(1,1000)
        print(input, solu.addDigits(input))