'''

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection 
between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.

Notes:
You may assume pattern contains only lowercase letters, 
and str contains lowercase letters separated by a single space.

'''

class Solution:
    # Using dict and comparison
    # Complexity O(n)
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str_lst = str.split(' ')
        pat_lst = list(pattern)
        if len(str_lst) != len(pat_lst):
            return False
        pat_dict = dict()
        for i in range(len(pat_lst)):
            if pat_dict.get(pat_lst[i]) is None:
                # KEYS DO NOT SHARE SAME VALUES
                for key, val in pat_dict.items():
                    if val == str_lst[i]:
                        return False
                pat_dict[pat_lst[i]] = str_lst[i]
            else:
                # ONCE NOT FOLLOW PATTERN 
                if pat_dict[pat_lst[i]] != str_lst[i]:
                    return False
        print(pat_dict)
        print(pat_dict.items())
        return True
        

if __name__ == "__main__":
    solu = Solution()
    print(solu.wordPattern("abba","dog cat cat dog"))
    print(solu.wordPattern("abba","dog cat cat fish"))
    print(solu.wordPattern("aaaa","dog cat cat dog"))
    print(solu.wordPattern("abba","dog dog dog dog"))