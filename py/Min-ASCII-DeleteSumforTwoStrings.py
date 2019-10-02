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
        dp = [[0 for _ in range(len(s1) + 1)] for _ in range(len(s2) + 1)] # init 2d array
        # loop the circumstances
        for i, c2 in enumerate(s2):
            for j, c1 in enumerate(s1):
                # dynamic programming
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + ord(c1) if c1 == c2 else dp[i][j - 1])
        return sum(map(ord, list(s1 + s2))) - 2 * dp[len(s2) - 1][len(s1) - 1]
    
    def minimumDeleteSum2(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        arr = [[0]*(len(s2)+1) for i in range(len(s1)+1)]
        for i in range(1,len(s1)+1):
            arr[i][0] = arr[i-1][0] + ord(s1[i-1])
        for j in range(1,len(s2)+1):
            arr[0][j] = arr[0][j-1] + ord(s2[j-1])
        self.output(arr)
        for i in range(1,len(s1)+1):
            for j in range(1, len(s2)+1):
                if s1[i-1] == s2[j-1]:
                    arr[i][j] = arr[i-1][j-1]
                else:    
                    arr[i][j] = min(ord(s1[i-1]) + arr[i-1][j], ord(s2[j-1]) + arr[i][j-1])
        self.output(arr)
        return arr[len(s1)][len(s2)]
    
    def output(self, sss):
        for ss in sss:
            for s in ss:
                print(s, end=' ')
            print()



if __name__ == "__main__":
    solu = Solution()
    input_str1 = "sea"
    input_str2 = "eat"
    print(input_str1, input_str2, solu.minimumDeleteSum2(input_str1, input_str2))