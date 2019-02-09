'''

An array is monotonic if it is either monotone increasing or monotone decreasing.
An array A is monotone increasing if for all i <= j, A[i] <= A[j].  
An array A is monotone decreasing if for all i <= j, A[i] >= A[j].
Return true if and only if the given array A is monotonic.

Example 1:
Input: [1,2,2,3]
Output: true

Example 2:
Input: [6,5,4,4]
Output: true

Example 3:
Input: [1,3,2]
Output: false

Example 4:
Input: [1,2,4,5]
Output: true

Example 5:
Input: [1,1,1]
Output: true
 
Note:
1 <= A.length <= 50000
-100000 <= A[i] <= 100000

'''


class Solution:
    # Need debugging
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        equal = False
        for i in range(len(A)-2):
            equal = (A[i] == A[i+1])
            if equal:
                continue
            elif not equal and (A[i]>A[i+1]) != (A[i+1]>A[i+2]):
                return False
            elif not equal and (A[i]<A[i+1]) != (A[i+1]<A[i+2]):
                return False
        return True

    # sort the list
    def isMonotonic_online(self, A):
        a = sorted(A)
        b = a[::-1]
        return A == a or A == b
        

if __name__ == "__main__":
    input_list = [1,2,2,3]
    solu = Solution()
    print(input_list, solu.isMonotonic(input_list))
    print(input_list, solu.isMonotonic_online(input_list))

