'''

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

'''


class Solution:
    # inspired by the integral image concept
    # but apparently, many constrictions exist
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        nums_mul = [1] * (len(nums)+1)
        for i in range(1, len(nums)+1):
            nums_mul[i] = nums_mul[i-1] * nums[i-1]
        max_num_index, min_num_index = nums_mul.index(max(nums_mul)), nums_mul.index(min(nums_mul))
        if max(nums_mul) * min(nums_mul) < 0:
            min_num_index = nums_mul.index(min(j for j in nums_mul if j > 0))
        if max_num_index > min_num_index:
            return int(nums_mul[max_num_index] / nums_mul[min_num_index])
        else:
            return 0

    # complexity: O(n); beats 19.7%
    def maxProduct_online(self, nums):
        # always keep imax > imin and possibly (imax > 0 and imin < 0)
        imin = imax = max_v = nums[0]
        for i in range(1, len(nums)):
            n = nums[i]
            # swap if negative 
            if n < 0:
                imin, imax = imax, imin
            imax = max(n, imax*n) # perhaps > 0
            imin = min(n, imin*n) # perhaps < 0
            max_v = max(max_v, imax) # update largest values
        return max_v


if __name__ == "__main__":
    solu = Solution()
    input_1 = [2, 3, -2, 4]
    input_2 = [-2, 0, -1]
    input_3 = [0, 0, 0]
    input_4 = [-2]
    input_5 = [-1, -1]
    assert solu.maxProduct_online(input_1) == 6
    assert solu.maxProduct_online(input_2) == 0
    assert solu.maxProduct_online(input_3) == 0
    assert solu.maxProduct_online(input_4) == -2
    assert solu.maxProduct_online(input_5) == 1