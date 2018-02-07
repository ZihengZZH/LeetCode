'''
You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.

Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c. Chain of pairs can be formed in this fashion.

Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs. You can select pairs in any order.

Example 1:
Input: [[1,2], [2,3], [3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4]

Note:
The number of given pairs will be in the range [1, 1000].
'''

class Solution:
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs = sorted(pairs, key=lambda x: x[1])
        # Important to sort the array based on second element
        new_line = [pairs[0]]
        for i in range(0, len(pairs)-1):
            if new_line[len(new_line)-1][1] < pairs[i+1][0]:
                new_line.append(pairs[i+1])
        return len(new_line)
        

if __name__ == "__main__":
    solu = Solution()
    input = [[1,10],[2,3],[3,4],[5,6],[7,8]]
    print("INPUT", input)
    print("OUTPUT", solu.findLongestChain(input))