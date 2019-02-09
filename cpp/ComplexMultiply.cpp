/*

Given two strings representing two complex numbers.
You need to return a string representing their multiplication. Note i2 = -1 according to the definition.

Example 1:
Input: "1+1i", "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.

Example 2:
Input: "1+-1i", "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.

Note:
The input strings will not have extra blank.
The input strings will be given in the form of a+bi, where the integer a and b will both belong to the range of [-100, 100]. 
And the output should be also in this form.

*/

#include <vector>
#include <bitset>
#include <iostream>
#include <string>
#include <algorithm>
#include <time.h>
#include <sstream>

using namespace std;

int split(string a) {
	int i, pos = 0;
	string temp;
	for (i = 0; i < a.length(); i++) {
		temp = a[i];
		pos = temp == "+" ? i : pos;
	}
	return pos;
}

string complexMultiply(string a, string b) {
	string realA = a.substr(0, split(a));
	string compA = a.substr(split(a) + 1, a.length() - 1);
	string realB = b.substr(0, split(b));
	string compB = b.substr(split(b) + 1,b.length() - 1);
	//cout << realA << "\t" << compA << "\t" << realB << "\t" << compB << endl;
	int real_a = stoi(realA, nullptr, 10);
	int comp_a = stoi(compA, nullptr, 10);
	int real_b = stoi(realB, nullptr, 10);
	int comp_b = stoi(compB, nullptr, 10);
	//cout << real_a << "\t" << comp_a << "\t" << real_b << "\t" << comp_b << endl;

	int real_mul = real_a * real_b - comp_a * comp_b;
	int comp_mul = real_a * comp_b + real_b * comp_a;
	string res = to_string(real_mul) + "+" + to_string(comp_mul) + "i";
	return res;
}


int main() {
	while (true) {
		clock_t start;
		clock_t stop;
		int i;
		string input1, input2, output;
		cout << "Enter first ";
		cin >> input1;
		cout << "Enter second ";
		cin >> input2;

		start = clock();
		stop = start + CLOCKS_PER_SEC;
		for (i = 0; clock() < stop; i++) {
			output = complexMultiply(input1, input2);
		}
		start = clock() - start;
		cout << "The complex multiplication is " << output << endl;
		printf(" %f ms (%d trials)\n", 1000 * (double)start / CLOCKS_PER_SEC / i, i);

		system("pause");
	}
}
