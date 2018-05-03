'''

You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.
Given n, find the total number of full staircase rows that can be formed.
n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:
n = 5
The coins can form the following rows:
¤
¤ ¤
¤ ¤
Because the 3rd row is incomplete, we return 2.

Example 2:
n = 8
The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤
Because the 4th row is incomplete, we return 3.

'''

import math

class Solution:
    # Complexity O(n)
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        coins, it = 0, 1
        while coins <= n:
            coins += it
            it += 1
        return (it-2)

    # ALMOST FASTEST
    # MATH MATTERS!
    def arrangeCoins_fast(self, n):
        return math.floor(math.sqrt(2*n+0.25)-0.5)
        

if __name__ == "__main__":
    solu = Solution()
    print(1, solu.arrangeCoins(1))
    print(5, solu.arrangeCoins(5))
    print(8, solu.arrangeCoins(8))
    assert solu.arrangeCoins(1) == solu.arrangeCoins_fast(1)
    assert solu.arrangeCoins(5) == solu.arrangeCoins_fast(5)
    assert solu.arrangeCoins(8) == solu.arrangeCoins_fast(8)
