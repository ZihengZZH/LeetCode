'''

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example, 
Given s = "Hello World",
return 5.

'''


def lengthOfLastWord(s):

    s = s[::-1]
    s_list = s.split()
    #print s_list
    if len(s_list) == 0:
        return 0
    else:
        return len(s_list[0])


def online(s):
    # pointer
    length = 0
    tail = len(s)-1
    while tail >= 0 and s[tail] == ' ':
        tail-=1
    while tail >= 0 and s[tail] != ' ':
        length+=1
        tail-=1
    return length


if __name__ == "__main__":
    
    input_str = "a "
    input_strs = []
    for i in range(10):
        input_str += " "
        input_strs.append(input_str)

    for j in input_strs:
        res = lengthOfLastWord(j)
        print("Answer to",j,"is",res)
        res = online(j)
        print("Answer to",j,"is",res)