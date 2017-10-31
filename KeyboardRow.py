'''

Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]

Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.

'''


import random
import math

class Solution(object):


    # Attributed by SUNNY
    def findWords(self, words):
        res = []
        for word in words:
            if self.helper(word):
                res.append(word)
        return res

    def helper(self, word):
        row = ["QWERTYUIOP", "ASDFGHJKL","ZXCVBNM"]
        temp = word.upper()
        wo = "".join(set(temp))
        print wo
        i = 0
        while wo[0] not in row[i]:
            i += 1
        for w in wo:
            if w not in row[i]:
                return False
        return True

    def online(self, words):
        a = set("QWERTYUIOP")
        b = set("ASDFGHJKL")
        c = set("ZXCVBNM")
        ans = []
        for word in words:
            t = set(word.upper())
            if a&t == t:
                ans.append(word)
            if b&t == t:
                ans.append(word)
            if c&t == t:
                ans.append(word)
        return ans


if __name__ == "__main__":
    solu = Solution()
    input_str = ["Hello", "Alaska", "Dad", "Peace"]
    res = solu.online(input_str)
    print input_str,"ANSWER IS", res
