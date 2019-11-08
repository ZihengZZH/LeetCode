'''

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:
Input: n = 4, k = 2
Output:
[
    [2,4],
    [3,4],
    [2,3],
    [1,2],
    [1,3],
    [1,4],
]

'''


class Solution:
    def combine(self, n, k):
        self.n = n  # range
        self.k = k  # number
        result = []
        self.helper(1, 0, [], result)
        return result

    def helper(self, this_n, this_k, subset, result):
        # this_n starts from 1
        # this_k starts from 0
        if this_k == self.k:
            result.append(subset)   # append subset if number equals
        else:
            for ii in range(this_n, self.n + 1):
                subset_tmp = subset + [ii]  # append value [ii]
                self.helper(ii + 1, this_k + 1, subset_tmp, result)


if __name__ == '__main__':
    solu = Solution()
    n, k = 4, 1
    print(n, k, solu.combine(n, k))