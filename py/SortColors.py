'''

Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.

'''

import random
import math

class Solution(object):

    def sortColors(self, nums):
        num_0 = nums.count(0)
        num_1 = nums.count(1)
        num_2 = nums.count(2)
        for i in xrange(len(nums)):
            if i < num_0:
                nums[i] = 0
            elif i < (num_0+num_1):
                nums[i] = 1
            else:
                nums[i] = 2
        print nums
    
    # Like quick sort algorithm
    # Keep a loop invariant that [0,i)[i,j)[j,k) are 0s, 1s and 2s 
    def sortColor(self, nums):
        i = j = 0
        for k in xrange(len(nums)):
            v = nums[k]
            nums[k] = 2
            if v < 2:
                nums[j] = 1
                j += 1
            if v == 0:
                nums[i] = 0
                i += 1
        print nums
                
        


if __name__ == "__main__":
    solu = Solution()
    input_nums = [0,1,1,0,0,1,2,2,2,0,1,0,2,1,0]

    solu.sortColors(input_nums)
    solu.sortColor(input_nums)
    #print input_nums,"ANSWER IS", res
