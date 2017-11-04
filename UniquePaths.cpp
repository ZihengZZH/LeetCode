/*

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Note: m and n will be at most 100.

*/

#include <vector>
#include <bitset>
#include <iostream>
#include <iomanip>
#include <string>
#include <algorithm>
#include <time.h>
#include <sstream>

using namespace std;



int uniquePaths(int m, int n) {
	if (m > n) return uniquePaths(n, m);
	vector<int> cur(m, 1);
	for (int j = 1; j < n; j++) {
		for (int i = 1; i < m; i++) {
			cur[i] += cur[i - 1];
		}
	}
	return cur[m - 1];
}


// Dynamic programming
int uniquePath(int m, int n) {
	vector<vector<int>> path(m, vector<int>(n, 1));
	for (int i = 1; i < m; i++) {
		for (int j = 1; j < n; j++) {
			path[i][j] = path[i - 1][j] + path[i][j - 1];
		}
	}
	return path[m - 1][n - 1];
}


int main() {
	while (true) {
		clock_t start;
		clock_t stop;
		int i;
		int input_m, input_n, output1,output2;
		
		input_m = 10;
		input_n = 32;

		start = clock();
		stop = start + CLOCKS_PER_SEC;
		for (i = 0; clock() < stop; i++) {
			output1 = uniquePaths(input_m, input_n);
		}

		cout << "ANSWER IS " << output1;
		
		printf("\n%f ms (%d trials)\n", 1000 * (double)start / CLOCKS_PER_SEC / i, i);

		cout << endl;


		start = clock();
		stop = start + CLOCKS_PER_SEC;
		for (i = 0; clock() < stop; i++) {
			output2 = uniquePath(input_m, input_n);
		}

		cout << "ANSWER IS " << output2;

		printf("\n%f ms (%d trials)\n", 1000 * (double)start / CLOCKS_PER_SEC / i, i);

		system("pause");
	}
}

