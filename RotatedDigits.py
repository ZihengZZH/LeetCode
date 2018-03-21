'''

X is a good number if after rotating each digit individually by 180 degrees, 
we get a valid number that is different from X.  
Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. 
0, 1, and 8 rotate to themselves; 
2 and 5 rotate to each other; 
6 and 9 rotate to each other, 
and the rest of the numbers do not rotate to any other number and become invalid.

Now given a positive number N, how many numbers X from 1 to N are good?

Example:
Input: 10
Output: 4
Explanation: 
There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.

'''


class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        counts = 0
        for num in range(1, N+1):
            number = str(num)
            # This will be an invalid number upon rotation
            if '3' in number or '7' in number or '4' in number: 
                # Skip this number and go to next iteration
                continue
            if '2' in number or '5' in number or '6' in number or '9' in number:
                counts += 1
        return counts
        

if __name__ == "__main__":
    solu = Solution()
    input_int = 10
    print(input_int, "OUTPUT", solu.rotatedDigits(input_int))