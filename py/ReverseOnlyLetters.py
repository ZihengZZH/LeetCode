'''

Given a string S, return the "reversed" string where all characters 
that are not a letter stay in the same place, and all letters reverse their positions.


Example 1:
Input: "ab-cd"
Output: "dc-ba"

Example 2:
Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

Example 3:
Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"

Note:
S.length <= 100
33 <= S[i].ASCIIcode <= 122 
S doesn't contain \ or "

'''


class Solution:
    def reverseOnlyLetters(self, S):
        icon, S_list = [], []
        for ii in range(len(S)):
            # A(65) - Z(90)
            # a(97) - z(122)
            if ord(S[ii]) in range(65, 91) or \
                ord(S[ii]) in range(97, 123):
                S_list += S[ii]
            else:
                icon.append(ii)
        # reverse letters
        S_list = S_list[::-1]
        for ic in icon:
            S_list.insert(ic, S[ic])
        return "".join(S_list)


if __name__ == "__main__":
    solu = Solution()
    input_1 = "ab-cd"
    input_2 = "a-bC-dEf-ghIj"
    input_3 = "Test1ng-Leet=code-Q!"
    print(input_1, "ANSWER IS", solu.reverseOnlyLetters(input_1))
    print(input_2, "ANSWER IS", solu.reverseOnlyLetters(input_2))
    print(input_3, "ANSWER IS", solu.reverseOnlyLetters(input_3))