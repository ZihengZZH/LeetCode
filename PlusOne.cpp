/*

Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.

*/

#include <iostream>
#include <vector>
#include <numeric>
#include <functional>
#include <algorithm>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

vector<int> plusOne(vector<int>& digits) {

	bool carry = true;

	for (int i = digits.size() - 1; i >= 0 && carry; i--) {
		carry = (++digits[i] %= 10) == 0;
	}

	if (carry) digits.insert(digits.begin(), 1);

	return digits;
}


int main() {

	vector<int> input = { 9 }, output;
	
	output = plusOne(input);

	for (auto m : output) {
		cout << m << " ";
	}

	cout << endl;
	system("pause");
	return 0;
}
