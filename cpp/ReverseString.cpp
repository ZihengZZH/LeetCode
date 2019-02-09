/*

Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".

NOTE: Try to avoid running-time-exceeded

*/

#include <vector>
#include <bitset>
#include <iostream>
#include <iomanip>
#include <string>
#include <algorithm>
#include <time.h>
#include <sstream>
using namespace std;


string reverseString(string s) {
	string res = "";
	for (int i = s.length()-1; i >= 0; i--) {
		res += s[i];
	}
	return res;
}

int main() {
	while (true) {
		clock_t start;
		clock_t stop;
		int i;
		string input = "hello";
		string output;
		

		start = clock();
		stop = start + CLOCKS_PER_SEC;
		for (i = 0; clock() < stop; i++) {
			output = reverseString(input);
		}

		cout << "ANSWER IS " << output << endl;
		printf("%f ms (%d trials)\n", 1000 * (double)start / CLOCKS_PER_SEC / i, i);


		system("pause");
	}
}
