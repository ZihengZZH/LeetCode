'''

Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Note:
The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.

Example 1:
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.

Example 2:
Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.

'''

import random
import math

class Solution(object):
    # complement_number + number = 1 + 2^length
    def findComplement(self,num):
        length = len(self.getBinary(num))
        return (pow(2,length)-num-1)   
    
    # Return the binary number as string
    def getBinary(self,num):
        binary = ""
        while num >= 1:
            binary = str(num%2) + binary
            num /= 2
        return binary    

if __name__ == "__main__":
    solu = Solution()
    for i in range(5):
        input_num = random.randint(1,1000)
        res = solu.findComplement(input_num)
        print input_num, "ANSWER IS", res


