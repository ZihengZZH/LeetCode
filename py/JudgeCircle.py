'''

Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.

Example 1:
Input: "UD"
Output: true
Example 2:
Input: "LL"
Output: false

'''


import random
import math

class Solution(object):


    # Attributed by SUNNY
    def judgeCircle(self, moves):
        print moves
        r = moves.count("R")
        l = moves.count("L")
        u = moves.count("U")
        d = moves.count("D")
        print r,l,u,d
        if r == l and u == d:
            return True
        else:
            return False


if __name__ == "__main__":
    solu = Solution()
    input_str = "RLUDDURRL"
    res = solu.ziheng(input_str)
    print input_str,"ANSWER IS", res
