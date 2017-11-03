'''

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
Find all the elements that appear twice in this array.
Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]

'''

import random
import math

class Solution(object):
    
    # O(n) complexity based on python built-in sort()
    def findDuplicates(self,nums):
        nums.sort()
        length = len(nums)
        dupli = []
        for i in range(length-1):
            if nums[i] == nums[i+1]:
                dupli.append(nums[i])
        return dupli
    
    
    '''
    traverse the list for i= 0 to n-1 elements
    {
        check for sign of A[abs(A[i])] ;
        if positive then
            make it negative by   A[abs(A[i])]=-A[abs(A[i])];
        else  // i.e., A[abs(A[i])] is negative
            this element (ith element of list) is a repetition
    }
    '''
    # Elements should be 0 to n-1 to fit this algorithm
    def onlineAnswer(self,nums):
        res = []
        for x in nums:
            if nums[abs(x)-1] < 0:
                res.append(abs(x))
            else:
                nums[abs(x)-1] *= -1
        return res
           
    
    

if __name__ == "__main__":
    solu = Solution()
    
    for i in range(5):
        input_nums = []
        for j in range(10):
            temp = random.randint(1,20)
            input_nums.append(temp)
        res = solu.findDuplicates(input_nums)
        print input_nums, "ANSWER IS", res


