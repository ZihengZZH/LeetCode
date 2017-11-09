/*

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: 
Starting with any positive integer, replace the number by the sum of the squares of its digits, 
and repeat the process until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1. 
Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

*/


#include <vector>
#include <bitset>
#include <iostream>
#include <string>
#include <algorithm>
#include <time.h>
#include <sstream>

using namespace std;

int sumOfSquare(int n) {
	int res = 0;
	while (n >= 1) {
		res += (n % 10) * (n % 10);
		n /= 10;
	}
	return res;
}

bool isIn(vector<int> temp, int n) {
	for (int i = 0; i < temp.size(); i++) {
		if (n == temp[i])
			return true;
	}
	return false;
}

bool isHappy(int n) {
	vector<int> occupy = {};
	bool isHp = true;
	while (n != 1) {
		occupy.push_back(n);
		n = sumOfSquare(n);
		//cout << "n " << n << endl;
		if (isIn(occupy, n)) {
			isHp = false;
			break;
		}
	}
	return isHp;
}

int main() {
	while (true) {
		clock_t start;
		clock_t stop;
		int i, input;
		bool output = true;
		cout << "Enter the number ";
		cin >> input;

		start = clock();
		stop = start + CLOCKS_PER_SEC;
		for (i = 0; clock() < stop; i++) {
			output = isHappy(input);
		}
		start = clock() - start;
		cout << "The given number is happy number " << boolalpha << output << endl;
		printf(" %f ms (%d trials)\n", 1000 * (double)start / CLOCKS_PER_SEC / i, i);


		system("pause");
	}
}
