/*

Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character

*/


#include <iostream>
#include <vector>

using namespace std;

int minDistance(string word1, string word2) {

    int m = word1.length(), n = word2.length();
    vector<int> cur(m + 1, 0);
    for (int i = 0; i <= m; i++) {
        cur[i] = i;
    }
    for (int j = 1; j <= n; j++) {
        int pre = cur[0];
        cur[0] = j;
        for (int i = 1; i <= m; i++) {
            int temp = cur[i];
            if (word1[i - 1] == word2[j - 1]) cur[i] = pre;
            else cur[i] = min(pre + 1, min(cur[i] + 1, cur[i - 1] + 1));
            pre = temp;
        }
    }
    return cur[m];

}

int main(){

    string input1 = "qwerty";
    string input2 = "asdfgh";
    int output = minDistance(input1, input2);
    cout << "OUTPUT " << output << endl;

    return 0;
}


/*

Use f[i][j] to represent the shortest edit distance between word1[0,i) and word2[0, j). 
Then compare the last character of word1[0,i) and word2[0,j), 
which are c and d respectively (c == word1[i-1], d == word2[j-1]):
if c == d, then : f[i][j] = f[i-1][j-1]

Otherwise we can use three operations to convert word1 to word2:
(a) if we replaced c with d: f[i][j] = f[i-1][j-1] + 1;
(b) if we added d after c: f[i][j] = f[i][j-1] + 1;
(c) if we deleted c: f[i][j] = f[i-1][j] + 1;

Note that f[i][j] only depends on f[i-1][j-1], f[i-1][j] and f[i][j-1], 
therefore we can reduce the space to O(n) by using only the (i-1)th array 
and previous updated element(f[i][j-1]).

*/