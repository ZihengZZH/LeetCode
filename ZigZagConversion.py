'''

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

'''

def convert(s, numRows):
    if numRows == 1 or numRows >= len(s):
            return s

    L = [''] * numRows
    index, step = 0, 1

    for x in s:
        L[index] += x
        if index == 0:
            step = 1
        elif index == numRows -1:
            step = -1
        index += step

    return ''.join(L)


if __name__ == "__main__":
    input_str = "QWERTYUIOPASDFGHJKL"
    input_num = 4
    output_str = convert(input_str,input_num)
    print("OUTPUT STRING IS",output_str)