/*

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:
Input: x = 1, y = 4
Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ?   ?
The above arrows point to positions where the corresponding bits are different.

*/


#include <vector>
#include <bitset>
#include <iostream>
#include <string>
#include <algorithm>
#include <time.h>
#include <sstream>

using namespace std;

string intToBinary(int z) {
	string res = "";
	while (z != 0) {
		res = (z % 2 == 0 ? "0" : "1") + res;
		z /= 2;
	}
	return res;
}

string supplement(string x, int num) {
	for (int i = 0; i < num; i++) {
		x = "0" + x;
	}
	return x;
}


int hammingDistance(int x, int y) {
	int hamDis = 0;
	string xB = intToBinary(x);
	string yB = intToBinary(y);
	if (xB.length() < yB.length()) {
		int dif = yB.length() - xB.length();
		xB = supplement(xB, dif);
	}
	else if (xB.length() > yB.length()) {
		int dif = xB.length() - yB.length();
		yB = supplement(yB, dif);
	}
	
	for (int i = 0; i < xB.length(); i++) {
		if (xB[i] != yB[i]) {
			hamDis++;
		}
	}
	return hamDis;
}


int main() {
	while (true) {
		clock_t start;
		clock_t stop;
		int i,output;
		int input1, input2;
		cout << "Enter first ";
		cin >> input1;
		cout << "Enter second ";
		cin >> input2;
		cout << intToBinary(input1) << endl;
		cout << intToBinary(input2) << endl;

		
		start = clock();
		stop = start + CLOCKS_PER_SEC;
		for (i = 0; clock() < stop; i++) {
			output = hammingDistance(input1, input2);
		}
		start = clock() - start;
		cout << "The hamming distance is " << output << endl;
		printf(" %f ms (%d trials)\n", 1000 * (double)start / CLOCKS_PER_SEC / i, i);

		system("pause");
	}
}
