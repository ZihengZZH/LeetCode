'''

Suppose you have N integers from 1 to N. 
We define a beautiful arrangement as an array that is constructed by these N numbers successfully 
if one of the following is true for the ith position (1 <= i <= N) in this array:
The number at the ith position is divisible by i.
i is divisible by the number at the ith position.
Now given N, how many beautiful arrangements can you construct?

Example 1:
Input: 2
Output: 2
Explanation: 

The first beautiful arrangement is [1, 2]:
Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).
Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).
The second beautiful arrangement is [2, 1]:
Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).
Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.
Note:
N is a positive integer and will not exceed 15.

'''


import itertools

class Solution:
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        res = 0
        # TIME CONSUMING
        arrays = list(itertools.permutations(list(range(1,N+1))))
        for array in arrays:
            res += 1
            for i in range(len(array)):
                if (i+1)%array[i] != 0 and array[i]%(i+1) != 0:
                    res -= 1
                    break
        return res

    def countArrangement_online(self, N):
        def count(i, X):
            if i == 1:
                return 1
            return sum(count(i-1, X-{x}) for x in X if x%i == 0 or i%x == 0)
        return count(N, set(range(1, N+1)))


if __name__ == "__main__":
    input_N = list(range(1,15))
    solu = Solution()
    for i in range(len(input_N)):
        # when 12, BREAK DOWN
        if solu.countArrangement(input_N[i]) == solu.countArrangement_online(input_N[i]):
            print(input_N[i], "OK")

        