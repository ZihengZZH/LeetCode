'''

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:
Input: x = 1, y = 4
Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ?   ?
The above arrows point to positions where the corresponding bits are different.

'''


class Solution(object):
    def intToBinary(self,z):
        s = ""
        while (z != 0):
            if (z % 2 == 0):
                s = "0" + s
            else:
                s = "1" + s
            z = z/2
        return s

    def supplement(self, x, num):
        for i in range(0,num):
            x = "0" + x
        return x

    def hammingDistance(self, x, y):
        hamDis = 0
        dif = 0
        xB = self.intToBinary(x)
        yB = self.intToBinary(y)
        if len(xB) < len(yB):
            dif = len(yB) - len(xB)
            xB = self.supplement(xB, dif)
        if len(xB) > len(yB):
            dif = len(xB) - len(yB)
            yB = self.supplement(yB, dif)
        for i in range(0,len(xB)):
            if xB[i] != yB[i]:
                hamDis += 1
        return hamDis



FR = raw_input("Enter first integer: ")
first = int(FR)
SC = raw_input("Enter second integer: ")
second = int(SC)
solu = Solution()
result = solu.hammingDistance(first,second)
print "The result is", result
