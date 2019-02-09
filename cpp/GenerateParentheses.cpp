/*

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

*/


#include <vector>
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;


void generate(vector<string> &parens,string p, int left, int right) {
	if (left != 0) generate(parens,p + "(", left - 1, right);
	if (right > left) generate(parens,p + ")", left, right - 1);
	if (right == 0) parens.push_back(p);
	return ;
}

vector<string> generateParenthesis(int n) {
	vector<string> res;
	generate(res,"", n, n);
	return res;
}

int main() {
	while (true){
		cout << "Input: ";
		int integ;
		cin >> integ;
		vector<string> output = generateParenthesis(integ);
		for (auto j : output) {
			cout << j << endl;
		}
		cout << endl;
		system("pause");
	}
}
