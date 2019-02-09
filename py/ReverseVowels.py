'''

Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".

'''


import random
import math

class Solution(object):

    # Traverse the string twice, verbose
    def reverseVowels(self, s):
        vowels = []
        res = ""
        for j in s:
            if j in "aeiouAEIOU":
                print "GET", j
                vowels.append(j)
        for k in s:
            if k in "aeiouAEIOU":
                res += vowels.pop()
            else:
                res += k
        return res

    # Two pointers method (Traverse string from two sides)
    def online(self, s):
        vowel = 'AEIOUaeiou'
        s = list(s)
        i,j = 0, len(s)-1
        while i<j:
            while s[i] not in vowel and i<j:
                i = i + 1
            while s[j] not in vowel and i<j:
                j = j - 1
            s[i], s[j] = s[j], s[i] # Exchange
            i, j = i + 1, j - 1 # Move to the middle
        return ''.join(s)

if __name__ == "__main__":
    solu = Solution()
    input_str = "asidqwezzaasd"
    res = solu.online(input_str)
    print input_str,"ANSWER IS", res
