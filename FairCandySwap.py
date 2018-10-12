'''

Alice and Bob have candy bars of different sizes: A[i] is the size of the i-th bar of candy that Alice has, 
and B[j] is the size of the j-th bar of candy that Bob has.
Since they are friends, they would like to exchange one candy bar each so that after the exchange, 
they both have the same total amount of candy.  (The total amount of candy a person has is the sum of the sizes of candy bars they have.)
Return an integer array ans where ans[0] is the size of the candy bar that Alice must exchange,
and ans[1] is the size of the candy bar that Bob must exchange.
If there are multiple answers, you may return any one of them. 
It is guaranteed an answer exists.

Example 1:
Input: A = [1,1], B = [2,2]
Output: [1,2]

Example 2:
Input: A = [1,2], B = [2,3]
Output: [1,2]

Example 3:
Input: A = [2], B = [1,3]
Output: [2,3]

Example 4:
Input: A = [1,2,5], B = [2,4]
Output: [5,4]

Note:
1 <= A.length <= 10000
1 <= B.length <= 10000
1 <= A[i] <= 100000
1 <= B[i] <= 100000
It is guaranteed that Alice and Bob have different total amounts of candy.
It is guaranteed there exists an answer.

'''

class Solution:
    # complexity O(n^2)
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        amount = (sum(A) + sum(B)) / 2
        for i in range(len(A)):
            for j in range(len(B)):
                if sum(A)-A[i]+B[j] == amount and sum(B)-B[j]+A[i] == amount:
                    return [A[i], B[j]]

    # complexity O(n)
    # some bulit-in functions are still time-consuming
    def fairCandySwap_online(self, A, B):
        n = (sum(A) - sum(B)) // 2
        A = list(map(lambda a: a-n, A))
        b = (list(set(A) & set(B)))[0]
        return [b+n, b]
        

if __name__ == "__main__":
    input_A, input_B = [1,2,5], [2,4]
    solu = Solution()
    print(input_A, input_B, solu.fairCandySwap(input_A, input_B))
    print(input_A, input_B, solu.fairCandySwap_online(input_A, input_B))