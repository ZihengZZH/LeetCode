/*

The gray code is a binary numeral system where two successive values differ in only one bit.
Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. 
A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:
    00 - 0
    01 - 1
    11 - 3
    10 - 2
    
Note:
For a given n, a gray code sequence is not uniquely defined.
For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.
For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.

*/



#include <vector>
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

vector<int> grayCode(int n) {
	vector<int> res(1,0); // Initialize one element as 0
	for (int j = 0; j < n; j++) {
		int curCount = res.size();
		while (curCount) {
			curCount--;
			int curNum = res[curCount];
			curNum += (1 << j); // << bitwise shift left (multiply)
			res.push_back(curNum);
		}
	}
	return res;
}

vector<int> grayCodes(int n) {
	vector<int> res(1, 0);
	for (int j = 0; j < n; j++) {
		int curCount = res.size();
		while (curCount) {
			curCount--;
			int curNum = res[curCount];
			cout << "curNum " << curNum << endl;
			int temp = 1 << j;
			cout << "temp " << temp << endl;
			curNum = curNum + temp;
			cout << "curNum " << curNum << endl;
			res.push_back(curNum);
			cout << endl;
		}
	}
	return res;
}

int main() {
	while (true) {
		cout << "Enter the integer: ";
		int intg;	cin >> intg;
		vector<int> output = grayCode(intg);
		for (int i = 0; i < output.size(); i++) cout << output[i] << " ";
		cout << endl;
		system("pause");
	}
}
