'''

Given a non-empty array of non-negative integers nums, 
the degree of this array is defined as the maximum frequency of any one of its elements.
Your task is to find the smallest possible length of a (contiguous) subarray of nums, 
that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.

Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6

Note:
nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.

'''


class Solution:
    def findShortestSubArray(self, nums):
        if nums == []:
            return 0
        
        freq = dict()
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        degree = max(freq.values())
        if degree == 1:
            return 1
        else:
            min_length = len(nums)
            for key in freq:
                if freq[key] == degree:
                    pos1 = nums.index(key)
                    pos2 = len(nums) - nums[::-1].index(key) - 1
                    if pos2 - pos1 + 1 < min_length:
                        min_length = pos2 - pos1 + 1
        return min_length


if __name__ == "__main__":
    solu = Solution()
    nums = [1,2,2,3,1,4,2]
    print(nums, solu.findShortestSubArray(nums))