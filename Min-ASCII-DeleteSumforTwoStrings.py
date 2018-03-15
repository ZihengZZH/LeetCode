'''

Given two strings s1, s2, find the lowest ASCII sum of deleted characters to make two strings equal.

Example 1:
Input: s1 = "sea", s2 = "eat"
Output: 231
Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.

Example 2:
Input: s1 = "delete", s2 = "leet"
Output: 403
Explanation: Deleting "dee" from "delete" to turn the string into "let",
adds 100[d]+101[e]+101[e] to the sum.  Deleting "e" from "leet" adds 101[e] to the sum.
At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.

Note:
0 < s1.length, s2.length <= 1000.
All elements of each string will have an ASCII value in [97, 122].

'''


'''

dp[i][j] = a[i] == b[j] ? dp[i + 1][j + 1] :
	min(a[i] + dp[i + 1][j],  // delete a[i] + minimumDeleteSum(a.substr(i+1), b.substr(j))
		b[j] + dp[i][j + 1])  // delete b[j] + minimumDeleteSum(a.substr(i), b.substr(j+1))
 
'''

class Solution(object):

   def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        dp = [[0 for j in range(len(s1) + 1)] for i in range(len(s2) + 1)] # init 2d array
        # loop the circumstances
        for i, c2 in enumerate(s2):
            for j, c1 in enumerate(s1):
                # dynamic programming
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + ord(c1) if c1 == c2 else dp[i][j - 1])
        return sum(map(ord, list(s1 + s2))) - 2 * dp[len(s2) - 1][len(s1) - 1]
                    


if __name__ == "__main__":
    solu = Solution()
    input_str1 = "delete"
    input_str2 = "leet"
    print(input_str1, input_str2, solu.minimumDeleteSum(input_str1, input_str2))