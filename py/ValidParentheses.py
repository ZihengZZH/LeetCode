'''

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

'''

class Solution:
    def isValid(self, s):
        s_list = list(s)
        if len(s_list) % 2 != 0:
            return False
        stack = list()
        # mapping = dict()
        # mapping['('] = ')'
        # mapping['['] = ']'
        # mapping['{'] = '}'
        for i in range(len(s_list)):
            if s_list[i] == '(' or s_list[i] == '[' or s_list[i] == '{':
                stack.append(s_list[i])
            elif len(stack) == 0:
                return False
            elif s_list[i] == ')' and stack[-1] != '(':
                return False
            elif s_list[i] == ']' and stack[-1] != '[':
                return False
            elif s_list[i] == '}' and stack[-1] != '{':
                return False
            else:
                stack = stack[:-1]
        if len(stack) != 0:
            return False
        
        return True
    
if __name__ == "__main__":
    solu = Solution()
    print(solu.isValid("()"))
    print(solu.isValid("()[]{}"))
    print(solu.isValid("(]"))
    print(solu.isValid("([)]"))
    print(solu.isValid("){"))
    print(solu.isValid("(){{{((())))[][][][]}}}"))