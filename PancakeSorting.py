'''

Given an array A, we can perform a pancake flip: We choose some positive integer k <= A.length, then reverse the order of the first k elements of A.  We want to perform zero or more pancake flips (doing them one after another in succession) to sort the array A.

Return the k-values corresponding to a sequence of pancake flips that sort A.  Any valid answer that sorts the array within 10 * A.length flips will be judged as correct.

Example 1:
Input: [3,2,4,1]
Output: [4,2,4,3]
Explanation: 
We perform 4 pancake flips, with k values 4, 2, 4, and 3.
Starting state: A = [3, 2, 4, 1]
After 1st flip (k=4): A = [1, 4, 2, 3]
After 2nd flip (k=2): A = [4, 1, 2, 3]
After 3rd flip (k=4): A = [3, 2, 1, 4]
After 4th flip (k=3): A = [1, 2, 3, 4], which is sorted. 

Example 2:
Input: [1,2,3]
Output: []
Explanation: The input is already sorted, so there is no need to flip anything.
Note that other answers, such as [3, 3], would also be accepted.

Note:
1 <= A.length <= 100
A[i] is a permutation of [1, 2, ..., A.length]

'''
 
 
class Solution:
    # complexity O(n^2)
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        def pancake_flip(lst, k):
            lst_copy = lst[:k]
            lst[:k] = lst_copy[::-1]
            return lst
        A_copy = A
        res = []
        # x == max number is the rest of list
        for x in range(len(A), 1, -1):
            # find the index 
            i = A.index(x)
            res.extend([i+1, x])
            # flip the list (twice)
            pancake_flip(A, i+1)
            pancake_flip(A, x)
            print(A)
        return res

'''
Find the index i of the next max number x
Reverse i+1 numbers, so that x will be at A[0]
Reverse x numbers, so that x will be at A[x-1]
Repeat this process N times
'''
        

if __name__ == "__main__":
    solu = Solution()
    input_1 = [3,2,4,1]
    input_2 = [1,2,3]
    print(input_1, solu.pancakeSort(input_1))
    print(input_2, solu.pancakeSort(input_2))