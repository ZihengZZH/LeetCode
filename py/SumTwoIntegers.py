'''

Calculate the sum of two integers a and b, 
but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.

'''

# Exclusive OR like digital calculator
# Python does not use 8-bit numbers. (unlike C++ Jaca)
# It used however many bits were native to your machine.

class Solution:
    
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MOD     = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF
        while b != 0:
            a, b = (a^b) & MOD, ((a&b) << 1) & MOD
        return a if a <= MAX_INT else ~(a&MAX_INT)^MAX_INT

    def getSumPos(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        a_lst = [0]*a
        b_lst = [0]*b
        all_lst = sum([a_lst, b_lst], [])
        return len(all_lst)

if __name__ == "__main__":
    a, b = 10, 100
    solu = Solution()
    print(a,b,solu.getSum(a,b))
        