'''

N couples sit in 2N seats arranged in a row and want to hold hands. 
We want to know the minimum number of swaps so that every couple is sitting side by side. 
A swap consists of choosing any two people, then they stand up and switch seats.

The people and seats are represented by an integer from 0 to 2N-1, 
the couples are numbered in order, the first couple being (0, 1), 
the second couple being (2, 3), and so on with the last couple being (2N-2, 2N-1).

The couples' initial seating is given by row[i] being the value of the person 
who is initially sitting in the i-th seat.

Example 1:
Input: row = [0, 2, 1, 3]
Output: 1
Explanation: We only need to swap the second (row[1]) and third (row[2]) person.

Example 2:
Input: row = [3, 2, 0, 1]
Output: 0
Explanation: All couples are already seated side by side.

Note:
len(row) is even and in the range of [4, 60].
row is guaranteed to be a permutation of 0...len(row)-1.

'''

import math

class Solution:
    # scan row list from left to the right and two by two
    # if the current couple is seated, do nothing
    # else, person at left side (p) stays, and his right neighbour
    # will be exchanged with the legitimate partner q of p
    '''Beats 100% of Python submission'''
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        count = 0
        person2pos = [0]*len(row)
        for i, person in enumerate(row):
            person2pos[person] = i
        for i in range(0, len(row), 2):
            if int(row[i]/2) == int(row[i+1]/2):
                continue
            else:
                q = int(row[i]/2)*2*2+1 - row[i]
                q_pos = person2pos[q]
                # q exchange with row[i+1]
                r = row[i+1]
                row[i+1] = q
                row[q_pos] = r
                person2pos[r] = q_pos
                person2pos[q] = i+1
                count += 1
        return count

        
        

if __name__ == "__main__":
    row_1 = [3,2,0,1]
    row_2 = [0,2,1,3]
    row_3 = [0,2,1,4,3,5]
    row_4 = [0,2,4,6,7,1,3,5]
    solu = Solution()
    print(row_1, solu.minSwapsCouples(row_1))
    print(row_2, solu.minSwapsCouples(row_2))
    print(row_3, solu.minSwapsCouples(row_3))
    print(row_4, solu.minSwapsCouples(row_4))