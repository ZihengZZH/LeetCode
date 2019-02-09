/*

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example, 
Given s = "Hello World",
return 5.

*/


#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

int online (string s){

    int len = 0, tail = s.length()-1;
    while (tail >= 0 && s[tail] == ' ') tail--;
    while (tail >= 0 && s[tail] != ' ') {
        len++;
        tail--;
    }
    return len;

}

int lengthOfLastWord(string s){

    if (s.empty()) return 0;
    string copy(s);
    reverse(copy.begin(), copy.end());
    int space = copy.find(" ");
    if (space == -1) return s.length();
    else return space;

}


int main(){

    string input_str = "Hi World Nice to meet you";

    int output_int = lengthOfLastWord(input_str);

    cout << "The answer is " << output_int;

    return 0;
}