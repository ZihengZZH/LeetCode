'''

Implement int sqrt(int x).
Compute and return the square root of x.

Note that Newton's method is recommended.

'''


import random

class Solution(object):
    def mySqrt(self, x):
        r = x
        while r*r > x:
            r = (r+x/r)/2
        return r

inputs = random.sample(range(10000),10)
solu = Solution()
for ipt in inputs:
    print "Square of", ipt, "is", solu.mySqrt(ipt)
