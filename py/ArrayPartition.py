'''

Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Example 1:
Input: [1,4,3,2]
Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).

Note:
n is a positive integer, which is in the range of [1, 10000].
All the integers in the array will be in the range of [-10000, 10000].

'''

import random

class Solution(object):
    def arrayPairSum(self,nums):
        nums_sort = sorted(nums)
        nums_len = len(nums)
        i = res = 0
        while i < nums_len:
            res += self.getMinimum(nums_sort[i],nums_sort[i+1])
            i += 2
        return res

    def getMinimum(self,num1,num2):
        if num1<num2:
            return num1
        else:
            return num2


if __name__ == "__main__":
    solu = Solution()
    inputlst = [1,4,3,2]
    res = solu.arrayPairSum(inputlst)
    print inputlst, "ANSWER IS", res


'''
THE MAIN POINT IS TO GET THE MAX SUM OF PAIRS
Given 2n integers into n pairs, return minimum of the pair
SO the worst case is to get the nums[0] to nums[n]
AND the best case is to get the nums[1], nums[3], ... nums[2n-1]
nums should be firstly sorted
'''
