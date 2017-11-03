'''

Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".

NOTE: Try to avoid running-time-exceeded

'''

class Solution(object):
    def reverseString(self,s):
        res = ""
        i = len(s)-1
        while i >= 0:
            res += s[i]
            i-=1
        return res
        
        '''
        res = ""
        for char in s:
            res = char + res
        return res
        '''

if __name__ == "__main__":
    solu = Solution()
    inputStr = "My name is Ziheng ZHANG, an undergraduate"
    res = solu.reverseString(inputStr)
    print inputStr, "ANSWER IS", res


