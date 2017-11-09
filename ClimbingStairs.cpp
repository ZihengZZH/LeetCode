/*

You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Note: Given n will be a positive integer.

*/


#include <vector>
#include <bitset>
#include <iostream>
#include <string>
#include <algorithm>
#include <time.h>
#include <sstream>

using namespace std;

/*
It is actually a  Fibonacci sequence cause every step can be 
reached from either one step or two steps ahead.
*/
int climbStairs(int n) {
	if (n == 1)
		return 1;
	int first = 1, second = 2, third;
	for (int i = 3; i <= n; i++) {
		third = first + second;
		first = second;
		second = third;
	}
	return second;
}


int main() {
	while (true) {
		clock_t start;
		clock_t stop;
		int i, input, output;
		cout << "Enter input: ";
		cin >> input;

		start = clock();
		stop = start + CLOCKS_PER_SEC;
		for (i = 0; clock() < stop; i++) {
			output = climbStairs(input);
		}
		start = clock() - start;
		cout << "The answer is as follows " << output << endl;
		printf(" %f ms (%d trials)\n", 1000 * (double)start / CLOCKS_PER_SEC / i, i);

		system("pause");
	}
}
