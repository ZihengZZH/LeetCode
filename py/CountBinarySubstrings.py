'''

Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, 
and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

Example 1:
Input: "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: 
"0011", "01", "1100", "10", "0011", and "01".
Notice that some of these substrings repeat and are counted the number of times they occur.
Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.

Example 2:
Input: "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.

Note:
s.length will be between 1 and 50,000.
s will only consist of "0" or "1" characters.

'''

class Solution:
    # Complexity O(nlogn)
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        lst = list(s)
        length,count = 2,0
        while length <= len(lst):
            for i in range(0,len(lst)-length+1,1):
                sub_lst_1 = lst[i:i+int(length/2)]
                sub_lst_2 = lst[i+int(length/2):i+length]
                #print(sub_lst_1, sub_lst_2)
                if (sub_lst_1 == ['0']*int(length/2) and sub_lst_2 == ['1']*int(length/2))\
                or (sub_lst_2 == ['0']*int(length/2) and sub_lst_1 == ['1']*int(length/2)):
                    count += 1
            length += 2
        return count

    # Complexity O(n)
    def countBinarySubstrings_online(self, s):
        if (len(s) == 0 or s.count('0') == len(s)\
        or s.count('1') == len(s)):
            return 0
        counts = []
        cur = s[0]
        nc = 0
        for c in s:
            if c == cur:
                nc += 1
            else:
                counts.append(nc)
                cur = c
                nc = 1
        counts.append(nc)
        ans = 0
        for i in range(1, len(counts)):
            ans += min(counts[i], counts[i-1])
        return ans


if __name__ == "__main__":
    solu = Solution()
    str_input = "01"
    str_output = solu.countBinarySubstrings(str_input)
    str_online = solu.countBinarySubstrings_online(str_input)
    print(str_input, str_output)
    assert(str_output == str_online)