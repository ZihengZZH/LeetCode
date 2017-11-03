'''

Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example:
For num = 5 you should return [0,1,1,2,1,2].

Follow up:
* It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
* Space complexity should be O(n).
* Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.

'''

import random

class Solution(object):
    def countBits(self,num):
        bitList = []
        for i in range(num+1):
            bitList.append(self.convertBinary(i))
        return bitList
        
    def convertBinary(self,num):
        if num == 0:
            return 0
        count = 0
        while num != 1:
            if (num % 2) == 1:
                count += 1
            num /= 2
        return count+1


if __name__ == "__main__":
    solu = Solution()
    inputNum = 5
    res = solu.countBits(inputNum)
    print inputNum, "ANSWER IS", res


