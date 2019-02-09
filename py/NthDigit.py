'''

Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:
Input:  3
Output: 3

Example 2:
Input:  11
Output: 0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the numbe

'''


class Solution:
    # 1 digit: #9
    # 2 digit: #90
    # 3 digit: #900
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        base, digit, ranGe = 9, 1, 9
        # calculate n's length
        while (ranGe < n):
            base *= 10
            digit += 1
            ranGe += base*digit
        print("range", int(ranGe), end=" ")
        # calculate n's offset
        offset = n - ranGe + base*digit
        # calculate nth digit belongs to which number
        number = pow(10, digit-1) + (offset-1)/digit
        print("number", int(number), end=" ")
        # calculate nth digit at which digit
        inner_offset = (offset-1) % digit
        # extract the number
        for i in range(digit-1-inner_offset):
            number /= 10
        return int(number%10)


if __name__ == "__main__":
    solu = Solution()
    print(30, solu.findNthDigit(30))
    print(111, solu.findNthDigit(111))