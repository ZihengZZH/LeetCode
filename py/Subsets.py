'''

Given a set of distinct integers, nums, return all possible subsets.
Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

'''


from itertools import combinations

class Solution(object):
    def subsets(self, nums):
        res = []
        i = 0
        while (i <= len(nums)):
            test = combinations(nums,i)
            for el in test:
                #print el
                res.append(el)
            i += 1
        return res

num = [1,2,3]
solu = Solution()
result = solu.subsets(num)
print "The result is", result
