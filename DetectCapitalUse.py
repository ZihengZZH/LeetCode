'''

Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:
* All letters in this word are capitals, like "USA".
* All letters in this word are not capitals, like "leetcode".
* Only the first letter in this word is capital if it has more than one letter, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.

Example 1:
Input: "USA"
Output: True

Example 2:
Input: "FlaG"
Output: False

Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.

'''

import random
import math

class Solution(object):
    
    def detectCapitalUse(self,word):
        all_cap = word.upper()
        all_lit = word.lower()
        if word == all_cap or word == all_lit:
            return True
        if word[0] == all_cap[0] and word[1:] == all_lit[1:]:
            return True
        return False
    
    def detectCapital(self,word):
        return word.isupper() or word.islower() or word.istitle()
    

if __name__ == "__main__":
    solu = Solution()
    input_str = "Flaglaglaglaglaglaglag"
    res = solu.detectCapitalUse(input_str)
    res2 = solu.detectCapital(input_str)
    print input_str, "ANSWER IS", res, res2


