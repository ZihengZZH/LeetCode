'''

Given an integer, return its base 7 string representation.

Example 1:
Input: 100
Output: "202"

Example 2:
Input: -7
Output: "-10"

Note: The input will be in range of [-1e7, 1e7].

'''

class Solution:
    def convertToBase7(self, num):
        if num < 0:
            return "-" + self.convertToBase7(-num)
        res = ""
        while (num/7 != 0):
            res = str(num%7) + res
            num /= 7
        res = str(num%7) + res
        return res

    def convertToBase7_online(self, num):
        if num == 0: return '0'
        n, res = abs(num), ''
        while n:
            res = str(n % 7) + res
            n //= 7
        return res if num > 0 else '-' + res

    def convertToBase7_fast(self, num):
        if num < 0: return '-' + self.convertToBase7_fast(-num)
        if num < 7: return str(num)
        return self.convertToBase7_fast(num // 7) + str(num % 7)


if __name__ == "__main__":
    input_num = range(-100,101)
    solu = Solution()
    for num in input_num:
        print(num, solu.convertToBase7(num))
        print(num, solu.convertToBase7_online(num))
        print(num, solu.convertToBase7_fast(num))
