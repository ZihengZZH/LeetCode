'''

Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:
Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:
   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

'''


class Solution:
    ''''
    f(1) = 1; f(2) = 2; f(3) = 5;
    f(4) = 14; f(5) = 42; f(6) = 132;
    Given a sequence 1, 2, ..., n, we enumerate each number i in the seq and take it as the root to form binary trees.
    We define two functions:
    1. G(n): # unique BST for a sequence of length n (# nodes)
    2. F(i,n): # unique BST where the number i (1<=i<=n) is the root
    We construct G(n) by the sum of F(1,n)
    G(n) = \sum^n_{i=1} F(i,n) = F(1,n) + F(2,n) + ... + F(n,n)
    Notice that when we select i as a root i.e. F(i,n) we have i-1 nodes which can be used to form a left subtree; similarly we have n-i nodes to form a right subtree.
    F(i,n) = G(i-1) x G(n-i)
    Thus, F(i,n) can be calculated by the product of the number of unique BST with i-1 nodes and the number of unique BST with n-i nodes. 
    Uniqueness is guaranteed by the sizes of the left subtree and the right tree.
    Finally, we have the recurrence:
    G(n) = \sum^n_{i=1} F(i,n) = \sum^n_{i=1} G(i-1) x G(n-i) where G(0) = 1, G(1) = 1
    '''
    def numTrees(self, n):
        # TIME LIMIT EXCEEDED
        if n == 0 or n == 1:
            return 1
        total = 0
        for ii in range(n):
            total += self.numTrees(ii) * self.numTrees(n - ii - 1)
        return total
    
    def numTrees2(self, n):
        # AC w/ less than 100% py3 submission
        # store each step into a dict
        G_dict = {}
        G_dict[0] = 1
        G_dict[1] = 1
        for ii in range(2, n+1):
            G_dict[ii] = 0
            for jj in range(ii):
                G_dict[ii] += G_dict[jj] * G_dict[ii - jj - 1]
        return G_dict[n]


if __name__ == '__main__':
    solu = Solution()
    input_n = 3
    print(input_n, solu.numTrees2(input_n))
    input_n = 5
    print(input_n, solu.numTrees2(input_n))
    input_n = 6
    print(input_n, solu.numTrees2(input_n))
    input_n = 10
    print(input_n, solu.numTrees2(input_n))