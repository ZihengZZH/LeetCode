/*

Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

1 == ""
2 == "abc"
3 == "def"
4 == "ghi"
5 == "jkl"
6 == "mno"
7 == "pqrs"
8 == "tuv"
9 == "wxyz"

*/

#include <vector>
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

// Do not use switch case: low and not efficient
// All combinations for fixed size characters
vector<string> letterCombinations(string digits) {
	vector<string> res;
	vector<string> dig = { " ","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz" };
	res.push_back(""); // Add a seed for initial case
	if (digits.empty()) return vector<string>();
	for (int i = 0; i < digits.size(); i++) {
		int num = digits[i] - '0'; // Get the number
		if (num < 0 || num > 9) break; // Invalid input
		string& candid = dig[num];
		if (candid.empty()) continue; // Empty input
		vector<string> temp; // Initialize at every loop
		for (int j = 0; j < candid.size(); j++) {
			for (int k = 0; k < res.size(); k++) {
				temp.push_back(res[k] + candid[j]);
			} // res.size * candid.size = all combinations
		} // Every combn in res append a character in candid
		res.swap(temp); // Vector assignmenet (my opinion)
	}
	return res;
}

int main() {
	while (true){
		cout << "Input: ";
		string str;
		cin >> str;
		if (str == "quit") break;
		vector<string> output = letterCombinations(str);
		int count = 0;
		for (int q = 0; q < output.size(); q++) {
			cout << output[q] << "\t";
			count++;
			if (count % 5 == 0) cout << endl;
 		}
		cout << endl;
		system("pause");
	}
}
