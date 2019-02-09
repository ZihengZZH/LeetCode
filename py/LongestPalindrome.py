'''

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example:
Input: "cbbd"
Output: "bb"

'''


class Solution(object):
    def longestPalindrome(self, s):
        if len(s) == 0:
            return 0
        maxLen = 1
        start = 0
        for i in xrange(len(s)):
            if i-maxLen >= 1 and s[i-maxLen-1:i+1] == s[i-maxLen-1:i+1][::-1]:
                start = i-maxLen-1
                maxLen += 2
                continue
            if i-maxLen >= 0 and s[i-maxLen:i+1] == s[i-maxLen:i+1][::-1]:
                start = i-maxLen
                maxLen += 1
        return s[start:start+maxLen]

strings = ["asdfdsdfdasdghds","asdewqqwezx","q9w8rewdjiv9e","qwe123ewq432","85258525852"]
solu = Solution()
for string in strings:
    print "The longest palindrome of", string, "is", solu.longestPalindrome(string)
