'''

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
	[-1, 0, 1],
	[-1, -1, 2]
]

'''


class Solution:
    '''
    Find two number sums == target
    Reduce the problem to 2Sum
    '''
    def threeSum(self, nums):
        results = []
        nums = sorted(nums)
        target, front, back, total = 0,0,0,0
        
        for ii in range(len(nums)):
            target = -nums[ii]      # Find two number sums == target
            front = ii + 1
            back = len(nums) - 1
            
            while front < back:
                total = nums[front] + nums[back]
                # total + target < 0
                if total < target:
                    front += 1      # left goes right
                # total + target > 0
                elif total > target:
                    back -= 1       # right goes less
                else:
                    result = [nums[ii], nums[front], nums[back]]
                    results.append(result)
                    print(ii, front, back)
                    while front < back and nums[front] == result[1]:
                        front += 1
                    while front < back and nums[back] == result[2]:
                        back -= 1 
                    # <QUITE ODD HERE>
                    break
            while ii+1 < len(nums) and nums[ii+1] == nums[ii]:
                ii += 1
        return results


if __name__ == '__main__':
    solu = Solution()
    inputs = [0,0,0]
    print(inputs, solu.threeSum(inputs))