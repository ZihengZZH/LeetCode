'''

Given a string, you need to reverse the order of characters in each word 
within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space 
and there will not be any extra space in the string.

'''


class Solution:
    # complexity O(n) beats 13.9%
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_res = ""
        s_lst = s.split(" ")
        for word in s_lst:
            #print(word)
            for i in range(len(word)):
                s_res += word[len(word)-i-1]
            s_res += " "
        return s_res[:-1]

    # complexity O(n) beats 13.9%
    def reverseWords_fast(self, s):
        s_res, temp = "", ""
        for i in range(len(s)):
            #print(s[i])
            if s[i] == " ":
                s_res += temp + " "
                temp = ""
            else:
                temp = s[i] + temp
        s_res += temp
        return s_res

    # complexity O(n) beats 42.7%
    def reverseWords_faster(self, s):
        s_res = ""
        for i,v in enumerate(s.split(" ")):
            #print(i, v)
            s_res += v[::-1] + " "
        return s_res.rstrip()


if __name__ == "__main__":
    input_str = "Let's take LeetCode contest"
    solu = Solution()    
    print(input_str, solu.reverseWords_faster(input_str))