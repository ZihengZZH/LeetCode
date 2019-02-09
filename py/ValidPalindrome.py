'''

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.
For the purpose of this problem, we define empty string as valid palindrome.

'''

import re

class Solution(object):
    def isPalindrome(self, s):
        if not s:
            return True
        temp = s.lower();
        alphas = re.findall('[0-9a-zA-Z]', temp)
        for alpha in alphas:
            print alpha
        count = len(alphas)
        indexL = 0
        indexR = count-1
        while indexL <= indexR:
            if alphas[indexL] != alphas[indexR]:
                return False
            indexL += 1
            indexR -= 1
        return True

pal = "A man, a plan, a canal: Panama"
pal2 = "0P";
pal3 = "1258521"
solu = Solution()
result = solu.isPalindrome(pal3)
print "The result is", result

# Regular expression is important
# Note to extract all alphanumeric characters
