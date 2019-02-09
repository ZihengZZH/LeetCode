'''

Given two strings representing two complex numbers.
You need to return a string representing their multiplication. Note i2 = -1 according to the definition.

Example 1:
Input: "1+1i", "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.

Example 2:
Input: "1+-1i", "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.

Note:
The input strings will not have extra blank.
The input strings will be given in the form of a+bi, where the integer a and b will both belong to the range of [-100, 100]. 
And the output should be also in this form.

'''


class Solution(object):

    def complexMultiply(self, a, b):
        lstA = a.split("+")
        lstB = b.split("+")
        realA = int(lstA[0])
        compA = int(lstA[1][:-1])
        realB = int(lstB[0])
        compB = int(lstB[1][:-1])
        print realA, compA, realB, compB
        real_mul = realA*realB - compA*compB
        comp_mul = realA*compB + realB*compA
        res = str(real_mul) + "+" + str(comp_mul) + "i"
        return res

FR = raw_input("Enter first integer: ")
SC = raw_input("Enter second integer: ")
solu = Solution()
result = solu.complexMultiply(FR,SC)
print "The result is", result
