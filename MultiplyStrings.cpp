/*

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.

Note:
1. The length of both num1 and num2 is < 110.
2. Both num1 and num2 contains only digits 0-9.
3. Both num1 and num2 does not contain any leading zero.
4. You must not use any built-in BigInteger library or convert the inputs to integer directly.

*/

#include <vector>
#include <iostream>
#include <string>
#include <algorithm>
#include <time.h>
#include <sstream>

using namespace std;


string multiply(string num1, string num2) {
	unsigned int n1 = num1.size(), n2 = num2.size();
	if (n1 == 0 || n2 == 0) return "0";
	vector<int> v(n1 + n2, 0); 
	// will keep the result number in vector in reverse order
	int i_n1 = 0, i_n2 = 0; // index

	// go from right to left by num1
	for (int i = n1 - 1; i >= 0; i--) {
		int carrier = 0;
		int n1 = num1[i] - '0';
		i_n2 = 0;
		// go from right to left by num2
		for (int j = n2 - 1; j >= 0; j--) {
			int n2 = num2[j] - '0';
			int sum = n1*n2 + v[i_n1 + i_n2] + carrier;
			carrier = sum / 10;
			v[i_n1 + i_n2] = sum % 10;
			i_n2++;
		}
		// store carrier in next cell
		if (carrier > 0) v[i_n1 + i_n2] += carrier;
		i_n1++;
	}
	// ignore '0's from the right
	int i = v.size() - 1;
	while (i >= 0 && v[i] == 0) i--;
	// if all '0' - means at least one of num1,num2 is '0'
	if (-1 == i) return "0";
	// generate the result string
	string s = "";
	while (i >= 0) s += to_string(v[i--]);

	return s;
}


int main() {
	while (true) {
		clock_t start;
		clock_t stop;
		int i; // counter
		string input1,input2,result;
		cout << "Enter the first string: ";
		cin >> input1;
		cout << "Enter the second string: ";
		cin >> input2;

		start = clock();
		stop = start + CLOCKS_PER_SEC;
		for (i = 0; clock() < stop; i++) {
			result = multiply(input1, input2);
		}
		start = clock() - start;
		cout << "The result is " << result << endl;
		printf(" %f ms (%d trials)\n", 1000 * (double)start / CLOCKS_PER_SEC / i, i);

		system("pause");
	}
}
