/*

Implement strStr().
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1

*/


#include <iostream>

using namespace std;

/*
I do not really understand the logic in method strStr_1() 
because the value of j, in my opinion, cannot equal to n_len
*/

int strStr_1(string haystack, string needle) {

    int h_len = haystack.length(), n_len = needle.length();
    if (!n_len) return 0;

    for (int i = 0; i <= (h_len-n_len); i++) {
        int j = 0;
        for (; j < n_len; j++) {
            if (haystack[i+j] != needle[j]) break;
        }
        if (j == n_len) return i;
    }
    return -1;

}


int strStr_2(string haystack, string needle) {

    int h_len = haystack.length(), n_len = needle.length();
    if (!n_len) return 0;

    for (int i = 0; i <= (h_len-n_len); i++) {
        for (int j = 0; j < n_len && haystack[i+j] == needle[j]; j++) {
            if ((j+1) == n_len) return i;
        }
    }
    return -1;

}

int main() {

    string haystack = "hello"; 
    string needle = "llo"; 

    int output = strStr_1(haystack, needle);
    cout << "OUTPUT " << output << endl;

    output = strStr_2(haystack, needle);
    cout << "OUTPUT " << output << endl;

    return 0;
}