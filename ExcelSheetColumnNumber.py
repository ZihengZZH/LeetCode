'''

Given a column title as appear in an Excel sheet, 
return its corresponding column number.

For example:
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 

'''

import functools
# The reduce function, since it is not commonly used, 
# was removed from the built-in functions in Python 3. 
# It is still available in the functools module. 


class Solution:
    
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        alpha_dict = {"A":1,"B":2,"C":3,"D":4,"E":5,
        "F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,
        "N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,
        "U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}
        s_lst = list(s)
        factor = len(s) - 1
        result = 0
        for s_item in s_lst:
            result += alpha_dict[s_item] * pow(26,factor)
            factor -= 1
        return result

    def titleToNumber_online(self, s):
        return functools.reduce(lambda x,y: x*26+y, [ord(c)-64 for c in list(s)])
        

if __name__ == "__main__":
    solu = Solution()
    input_str = "ZZZZ"
    output_int = solu.titleToNumber_online(input_str)
    print(input_str,output_int)