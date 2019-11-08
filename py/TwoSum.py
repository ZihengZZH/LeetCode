'''

Given an array of integers, return indices of the two numbers 
such that they add up to a specific target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''


class Solution:
    def twoSum(self, nums, target):
        sum_dict = {}
        for idx, num in enumerate(nums):
            cur = target - num
            # if cur exists, return
            if cur in sum_dict:
                return [sum_dict[cur], idx]
            # else store diff in dict
            else:
                sum_dict[num] = idx


if __name__ == '__main__':
    solu = Solution()
    input_nums = [2, 11, 7, 15]
    input_target = 9
    print(input_nums, input_target, solu.twoSum(input_nums, input_target))