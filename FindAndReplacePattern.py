'''

You have a list of words and a pattern, and you want to know which words in words matches the pattern.
A word matches the pattern if there exists a permutation of letters p 
so that after replacing every letter x in the pattern with p(x), we get the desired word.
(Recall that a permutation of letters is a bijection from letters to letters: 
every letter maps to another letter, and no two letters map to the same letter.)
Return a list of the words in words that match the given pattern. 
You may return the answer in any order.

Example 1:
Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
since a and b map to the same letter.

Note:
1 <= words.length <= 50
1 <= pattern.length = words[i].length <= 20

'''

class Solution:
    # BEATS 99.73% OF SUBMISSIONS
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        help_map, res = dict(), []
        valid = True
        for word in words:
            if len(pattern) != len(word):
                continue
            for i in range(len(word)):
                if pattern[i] in help_map and help_map[pattern[i]] != word[i]:
                        valid = False
                        break
                if pattern[i] not in help_map and word[i] in help_map.values():
                        valid = False
                        break
                else:
                    help_map[pattern[i]] = word[i]
            if valid:
                res.append(word)
            valid = True
            help_map = dict()
        return res


if __name__ == "__main__":
    input_list = ["abc","deq","mee","aqq","dkd","ccc"]
    input_pattern = "abb"
    solu = Solution()
    print(input_list, solu.findAndReplacePattern(input_list,input_pattern))
    