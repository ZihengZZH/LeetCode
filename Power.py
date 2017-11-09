'''

Implement pow(x, n).

Pay attention to the time complexity!!!
O(n) is not acceptable but O(logn)

'''

class Solution(object):

    def myPow(self, x, n):
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n-1)
        return self.myPow(x*x, n/2)
                
strBs = raw_input("Enter a base: ")
base = int(strBs)
strPw = raw_input("Enter a power: ")
power = int(strPw)
solu = Solution()
result = float(solu.myPow(base, power))
print "The result is %.10e" %(result)
