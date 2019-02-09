#! python3
# -*- coding: utf-8 -*-

'''

Given four lists A, B, C, D of integer values,
compute how many tuples (i, j, k, l) there are such that
A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D
have same length of N where 0 ≤ N ≤ 500.
All integers are in the range of -228 to 228 - 1
and the result is guaranteed to be at most 231 - 1.

Example:
Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]
Output:
2
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0

'''

import collections
import timeit

class Solution:

    # MUCH FASTER
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        AB = collections.Counter(a+b for a in A for b in B)
        return sum(AB[-c-d] for c in C for d in D)

    # SIMPLE BUT SLOW!!
    def fourSumCountSlow(self, A, B, C, D):

        lst_1, lst_2 = [], []
        count = 0
        for a in A:
            for b in B:
                lst_1.append(a+b)
        for c in C:
            for d in D:
                lst_2.append(c+d)
        for item1 in lst_1:
            for item2 in lst_2:
                if item1 + item2 == 0:
                    count += 1
        return count


# MAIN FUNCTION
if __name__ == "__main__":
    solu = Solution()
    A = [1,2,1,2,3,4,5,6,2,2,-1]
    B = [-2,-1,4,5,6,7,5,-1,-3,-4,2]
    C = [-1,2,0,-4,-3,2,1,2,-1,-5,-10]
    D = [0,2,-9,1,2,3,4,5,2,4,2]
    if len(A) == len(B) and len(B) == len(C) and len(C) == len(D):
        start_time = timeit.default_timer()
        res_1 = solu.fourSumCount(A,B,C,D)
        time_1 = timeit.default_timer() - start_time
        start_time = timeit.default_timer()
        res_2 = solu.fourSumCountSlow(A,B,C,D)
        time_2 = timeit.default_timer() - start_time
        print(A,B,C,D,res_1,time_1, sep='  ')
        print(A,B,C,D,res_2,time_2, sep='  ')


'''
    NICE TUTORIAL http://www.zlovezl.cn/articles/collections-in-python/
'''
