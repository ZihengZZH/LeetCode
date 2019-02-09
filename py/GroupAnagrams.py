'''

Given an array of strings, group anagrams together.

Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note:
All inputs will be in lowercase.
The order of your output does not matter.

'''

class Solution:
    # Amazing use of dictionary
    # Complexity O(n)
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dicti = {}
        for s in strs:
            unique = ''.join(sorted(s))
            if unique in dicti:
                dicti[unique].append(s)
            else:
                dicti[unique] = [s]
        print(dicti)
        return list(dicti.values())


if __name__ == "__main__":
    solu = Solution()
    input_lst = ["eat", "tea", "tan", "ate", "nat", "bat", "tab"]
    output_lst = solu.groupAnagrams(input_lst)
    print(input_lst, output_lst)