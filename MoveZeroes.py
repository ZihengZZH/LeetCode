'''

Given an array nums, write a function to move all 0's to the end of it 
while maintaining the relative order of the non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.

'''

import random

class Solution:
    # Complexity O(n^2)
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                for j in range(i,len(nums),1):
                    if nums[j] != 0:
                        temp = nums[i]
                        nums[i] = nums[j]
                        nums[j] = temp
                        break

    # use an attribute recording # nonZeros
    # replace nonZero elements into first nonZero_id pos
    # Complexity O(n)
    def moveZeroes_online(self, nums):
        lastNonZero_id = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[lastNonZero_id] = nums[lastNonZero_id], nums[i]
                lastNonZero_id += 1
                print("last non zero id: ", lastNonZero_id)


if __name__ == "__main__":
    solu = Solution()
    lst_input = [0,1,0,3,12,0,15,0,0,2]
    lst_input_online = lst_input
    print("Input: ", lst_input)
    solu.moveZeroes(lst_input)
    solu.moveZeroes_online(lst_input_online)
    print("Output: ", lst_input)
    assert(lst_input == lst_input_online)