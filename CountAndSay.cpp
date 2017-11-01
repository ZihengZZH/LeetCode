/*

The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:
Input: 1
Output: "1"

Example 2:
Input: 4
Output: "1211"

*/

#include <iostream>
#include <string>

using namespace std;

string countAndSay(int n) {
	if (n == 0) return ""; // return blank for zero input
	string res = "1"; // the output corresponding to 1
	while (--n) {
		string cur = ""; // recursion string
		for (int i = 0; i < res.size(); i++) {
			int count = 1; 
			while ((i + 1 < res.size()) && (res[i] == res[i + 1])) {
				count++;
				i++;
			} // When not last digit and two digits are same
			cur += to_string(count) + res[i]; // adding #of and digit
			// Pay attention to integer_to_string
		}
		res = cur; // result string
	} // Loop until n-1 times
	return res;
}

int main() {
	cout << "Input: ";
	int integer;
	cin >> integer;
	cout << "Output: " << countAndSay(integer) << endl;
	system("pause");
}
