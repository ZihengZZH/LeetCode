'''

Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:
The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

'''


import random

class Solution(object):
    def addStrings(self, num1, num2):
        if len(num1) <= len(num2):
            for i in range(len(num2)-len(num1)):
                num1 = "0"+num1
        else:
            for i in range(len(num1)-len(num2)):
                num2 = "0"+num2
        length = len(num1)
        print "NUM1",num1,"NUM2",num2
        carry = False
        res = ""
        for i in range(0, length):
            if carry:
                temp = int(num1[length-i-1]) + int(num2[length-i-1]) + 1
            else:
                temp = int(num1[length-i-1]) + int(num2[length-i-1])
            if temp > 9:
                res = str(temp-10) + res
                carry = True
            else:
                res = str(temp) + res
                carry = False
        if carry:
            res = "1" + res
        return res


if __name__ == "__main__":
    solu = Solution()
    for i in xrange(5):
        inputnum1 = random.randint(100,1000000)
        inputnum2 = random.randint(100,1000)
        inputstr1 = str(inputnum1)
        inputstr2 = str(inputnum2)
        output = solu.addStrings(inputstr1, inputstr2)
        print "OUTPUT",output
