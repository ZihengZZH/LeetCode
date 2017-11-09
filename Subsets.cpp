/*

Given a set of distinct integers, nums, return all possible subsets.
Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

*/


#include <vector>
#include <bitset>
#include <iostream>
#include <string>
#include <algorithm>
#include <time.h>
#include <sstream>

using namespace std;


vector<vector<int>> subsets(vector<int>& nums) {
	sort(nums.begin(), nums.end());
	int num_subset = pow(2, nums.size());
	vector<vector<int>> res(num_subset, vector<int>());
	for (int i = 0; i < nums.size(); i++) {
		for (int j = 0; j < num_subset; j++) {
			if ((j >> i) & 1) {
				res[j].push_back(nums[i]);
			} // The shift operators bitwise shift the value 
			// on their left by the number of bits on their right
			// 2 << 4 is 32  && -8 >> 3 is -1
		}
	}
	return res;
}

int factor(int i, int j) {
	int numer = 1, deno = 1;
	while (j != 0) {
		numer *= i;
		deno *= j;
		i -= 1;
		j -= 1;
	}
	return (numer / deno);
}

int main() {
	while (true) {
		clock_t start;
		clock_t stop;
		int i;
		vector<int> input = { 5,2,1,3,4 };
		vector<vector<int>> output = {};
		vector<int>::iterator it;
		vector<vector<int>>::iterator iter;
		vector<int> vec_tmp;

		start = clock();
		stop = start + CLOCKS_PER_SEC;
		for (i = 0; clock() < stop; i++) {
			output = subsets(input);
		}
		start = clock() - start;
		cout << "All the non-duplicate subsets are as follows " << endl;
		cout << "Use iterator : " << endl;
		for (iter = output.begin(); iter != output.end(); iter++){
			vec_tmp = *iter;
			cout << " [";
			for (it = vec_tmp.begin(); it != vec_tmp.end(); it++)
				cout << *it << ",";
			cout << "] " << endl;
		}

		printf(" %f ms (%d trials)\n", 1000 * (double)start / CLOCKS_PER_SEC / i, i);

		system("pause");
	}
}

/*
[], [], [], [], [], [], [], []
[], [1], [], [1], [], [1], [], [1]
[], [1], [2], [1, 2], [], [1], [2], [1, 2]
[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]
*/
