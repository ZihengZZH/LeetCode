'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''

class Solution:

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        perms = [[]]
        for n in nums:
            new_perms = []
            l = len(perms[-1])
            for perm in perms:
                for i in range(l,-1,-1):
                    if i < l and perm[i] == n:
                        break
                    new_perms.append(perm[:i] + [n] + perm[i:])
            perms = new_perms
        return perms



if __name__ == "__main__":
    solu = Solution()
    input = [1,1,2]
    output = solu.permuteUnique(input)
    print(input, output)
    