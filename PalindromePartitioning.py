'''

Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return
[
  ["aa","b"],
  ["a","a","b"]
]

'''


# Divide the string to check whether two parts are palindrome
# Further check if each part contains two palindromes
# Note the default output
class Solution:
    def partition(self, s):
        result = []
        for i in range(1, len(s)+1):
            if s[:i] == s[i-1::-1]:
                for rest in self.partition(s[i:]):
                    result.append([s[:i]]+rest)
        if not result:
            return [[]]
        return result

if __name__ == "__main__":
    s1 = "aabb"
    s2 = "aasssd"
    solu = Solution()
    print(s1, solu.partition(s1))
    print(s2, solu.partition(s2))