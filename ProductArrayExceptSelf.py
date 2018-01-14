'''

Given an array of n integers where n > 1, nums, 
return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
Solve it without division and in O(n).
    For example, given [1,2,3,4], return [24,12,8,6].
Follow up:
Could you solve it with constant space complexity? 
(Note: The output array does not count as extra space for the purpose of space complexity analysis.)

'''

class Solution:

    # two passes O(2n)
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = [1] * n
        for i in range(1, n):
            ans[i] = ans[i-1] * nums[i-1]
        m = 1
        for i in range(n-1, -1, -1):
            ans[i] *= m
            m *= nums[i]
        return ans
    

if __name__ == "__main__": 
    input = [1,2,3,4]
    solu = Solution()
    print(input, solu.productExceptSelf(input))
