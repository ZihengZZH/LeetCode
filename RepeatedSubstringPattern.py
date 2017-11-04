'''

Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

Example 1:
Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.

Example 2:
Input: "aba"
Output: False

Example 3:
Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)

'''


import random
import math

class Solution(object):

    def repeatedSubstringPattern(self, s):
        if len(s) == 1:
            return False
        i = 1
        while i != len(s):
            sub_str = s[0:i]
            if self.helper(s, sub_str):
                return True
            i += 1
        return False

    def helper(self, s, sub):
        if len(s)%len(sub) == 0:
            if s == sub*(len(s)/len(sub)):
                return True
        return False

    def online(self, s):
        if not s:
            return False

        ss = (s + s)[1:-1]
        return ss.find(s) != -1




if __name__ == "__main__":
    solu = Solution()
    input_str = "aabcdaabcdaabcdaabcd"

    res = solu.repeatedSubstringPattern(input_str)
    res2 = solu.online(input_str)
    print input_str,"ANSWER IS", res
    print input_str,"ANSWER IS", res2



'''
1. First char of input string is first char of repeated substring
2. Last char of input string is last char of repeated substring
3. Let S1 = S + S (where S in input string)
4. Remove 1 and last char of S1. Let this be S2
5. If S exists in S2 then return true else false
6. Let i be index in S2 where S starts then repeated substring length i + 1 and repeated substring S[0: i+1]
'''
