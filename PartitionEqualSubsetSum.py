'''

Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.

Example 1:
Input: [1, 5, 11, 5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
Input: [1, 2, 3, 5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.

'''


import random
import math

class Solution(object):

    def canFindSum(self, nums, target, ind, n, d):
        if target in d:
            return d[target]
        if target == 0:
            d[target] = True
        else:
            d[target] = False
            if target > 0:
                for i in xrange(ind, n):
                    if self.canFindSum(nums, target-nums[i],i+1,n,d):
                        d[target] = True
                        break
        return d[target]


    def canPartition(self, nums):
        if sum(nums) % 2 != 0:
            return False
        else:
            return self.canFindSum(nums,sum(nums)/2,0,len(nums),{})



if __name__ == "__main__":
    solu = Solution()
    input_num = [1,1,11,1,0,9]
    res = solu.canPartition(input_num)
    print "ANSWER is", res
