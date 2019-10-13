'''

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:
Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.

Example:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

'''


class Solution:
    def twoSum(self, numbers, target):
        front, back = 0, len(numbers) - 1
        
        while front < back:
            total = numbers[front] + numbers[back]
            if total < target:
                front += 1
            elif total > target:
                back -= 1
            else:
                break
        return [front+1, back+1]


if __name__ == '__main__':
    solu = Solution()
    inputs = [2, 7, 11, 15]
    target = 26
    print(inputs, target, solu.twoSum(inputs, target))
    