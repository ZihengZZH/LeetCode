'''

There are 1000 buckets, one and only one of them contains poison, the rest are filled with water. 
They all look the same. 
If a pig drinks that poison it will die within 15 minutes. 
What is the minimum amount of pigs you need to figure out which bucket contains the poison within one hour.

Answer this question, and write an algorithm for the follow-up general case.

Follow-up:
If there are n buckets and a pig drinking poison will die within m minutes, 
how many pigs (x) you need to figure out the "poison" bucket within p minutes? 
There is exact one bucket with poison.

'''

import math

class Solution(object):
    # If one attempts 2^x => #bucket
    # If more attempts (t+1)^x => #bucket
    # May refer to https://leetcode.com/problems/poor-pigs/discuss/94273/Solution-with-detailed-explanation
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        q, r1 = divmod(minutesToTest, minutesToDie)
        return int(math.ceil(math.log(buckets, q+1)))


if __name__ == "__main__":
    buckets = 1000
    minutesToDie = 15
    minutesToTest = 60
    solu = Solution()
    print(solu.poorPigs(buckets,minutesToDie,minutesToTest))