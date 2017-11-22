/*

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.

*/

#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>

using namespace std;

bool isValid(char a,char b){
    return a == '1'||(a == '2' && b <= '6');
}

bool isValid(char a){
    return a != '0';
}

/* 
Dynamic programming
dp[0] = 1
dp[i] = dp[i-1] + dp[i-2]
dp[i+1] = dp[i] + dp[i-1]
*/
int numDecodings_online(string s){

    int n = s.size();
    if(n == 0 || s[0] == '0') return 0;
    if(n == 1) return 1;
    int res = 0,fn_1 = 1,fn_2 = 1;
    for(int i = 1; i < n; i++){
        int temp = fn_1;

        if(isValid(s[i])&&isValid(s[i-1],s[i]))  res+=fn_1+fn_2;
        if(!isValid(s[i])&&isValid(s[i-1],s[i])) res+=fn_2;
        if(isValid(s[i])&&!isValid(s[i-1],s[i])) res+=fn_1;
        if(!isValid(s[i])&&!isValid(s[i-1],s[i]))  return 0;

        fn_1 = res;
        fn_2 = temp;
        res = 0;
    }
    return fn_1;
}


int main(){

    vector<string> str;
    str.push_back("123");
    str.push_back("23");
    str.push_back("4523");

    for (int k = 0; k < str.size(); k++){
        cout << str[k] << " " << numDecodings(str[k]) << endl;
    }


}