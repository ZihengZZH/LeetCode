'''

Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

'''


import random
import math

class Solution(object):

    def isAnagram(self, s, t):
        lst1 = list(s)
        lst2 = list(t)
        lst1.sort()
        lst2.sort()
        return lst1 == lst2


if __name__ == "__main__":
    solu = Solution()
    input_str1 = "rat"
    input_str2 = "car"

    res = solu.isAnagram(input_str1,input_str2)
    print input_str1,input_str2,"ANSWER IS", res
