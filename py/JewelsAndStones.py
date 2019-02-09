'''

You're given strings J representing the types of stones that are jewels, 
and S representing the stones you have.  
Each character in S is a type of stone you have.  
You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, 
and all characters in J and S are letters. 
Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:
Input: J = "aA", S = "aAAbbbb"
Output: 3

Example 2:
Input: J = "z", S = "ZZ"
Output: 0

Note:
S and J will consist of letters and have length at most 50.
The characters in J are distinct.

'''

class Solution:
    # 44ms
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        S_lst = list(S)
        J_lst = list(J)
        count = 0
        for j in J_lst:
            for s in S_lst:
                if j == s:
                    count += 1
                    #S_lst.remove(j)
        return count
        
    # 36ms
    def numJewelsInStones_fast(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        S_lst = list(S)
        J_lst = list(J)
        count = 0
        for j in J_lst:
            count += S_lst.count(j)
        return count
        

if __name__ == "__main__":
    solu = Solution()
    J_input = "aA"
    S_input = "aAAbbbb"
    print(J_input,S_input,solu.numJewelsInStones_fast(J_input,S_input))