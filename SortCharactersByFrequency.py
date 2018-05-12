'''

Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:
Input:  "tree"
Output: "eert"
Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:
Input:  "cccaaa"
Output: "cccaaa"
Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:
Input:  "Aabb"
Output: "bbAa"
Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

'''

# High-performance container datatypes
import collections


class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_set = set(list(s))
        freq, res = [], ""
        for element in s_set:
            freq.append((element,s.count(element)))
        freq.sort(key=lambda f: f[1], reverse=True)
        for f in freq:
            res += f[0] * f[1]
        return res

    def frequencySort_online(self, s):
        return ''.join(c * i for c, i in collections.Counter(s).most_common())


if __name__ == "__main__":
    solu = Solution()
    input_str = "tree"
    print(input_str, solu.frequencySort(input_str))
    print(input_str, solu.frequencySort_online(input_str))
