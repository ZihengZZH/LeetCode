'''

Given a sorted array consisting of only integers where every element appears 
twice except for one element which appears once. 
Find this single element that appears only once.

Example 1:
Input: [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
Input: [3,3,7,7,10,11,11]
Output: 10

Note: Your solution should run in O(log n) time and O(1) space.

'''

class Solution:
    # COULD HAVE DONE THIS EARLIER
    # Complexity O(n)
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                i += 2
            else:
                return nums[i]
        return nums[i]

    # Find the only element appears twice
    # Complexity O(n) + sorting
    # Maybe improved by comparison during quicksort
    def twiceElement(self, nums):
        nums_sort = sorted(nums)
        i = 0
        while i < len(nums_sort)-1:
            if nums_sort[i] == nums_sort[i+1]:
                return nums_sort[i]
            else:
                i += 2
        return nums_sort[i]



if __name__ == "__main__":
    solu = Solution()
    nums_1 = [1,1,2,3,3,4,4,5,5]
    nums_2 = [3,3,7,7,10,10,11,11,21]
    nums_3 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,5]
    nums_4 = [12,21,22,23,24,25,26,23,11,10,9]

    print("ELEMENT APPEARS ONCE")
    print(nums_1, solu.singleNonDuplicate(nums_1))
    print(nums_2, solu.singleNonDuplicate(nums_2))
    print("ELEMENT APPEARS TWICE")
    print(nums_3, solu.twiceElement(nums_3))
    print(nums_4, solu.twiceElement(nums_4))