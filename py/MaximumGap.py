'''

Given an unsorted array, find the maximum difference between 
the successive elements in its sorted form.

Try to solve it in linear time/space.
Return 0 if the array contains less than 2 elements.

You may assume all elements in the array are non-negative 
integers and fit in the 32-bit signed integer range.

'''

class Solution(object):

    # Straight-foward method
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        list_len = len(nums)
        if list_len < 2:
            return 0
        nums.sort()
        max = 0
        for i in range(0, list_len-1):
            if abs(nums[i]-nums[i + 1]) > max:
                max = abs(nums[i]-nums[i + 1])
        return max
        

if __name__ == "__main__":
    solu = Solution()
    input_lst = [1,54,21,2,1,0,4,57,4,14,30,22,10000,10,12,74]
    print(input_lst, solu.maximumGap(input_lst))