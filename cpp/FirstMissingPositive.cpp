/*

Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.

*/


#include <vector>
#include <iostream>
#include <string>
#include <algorithm>
#include <time.h>
#include <sstream>

using namespace std;


int firstMissingPositive(vector<int>& nums) {
	int len = nums.size();
	// Sort the array with in-place
	for (int i = 0; i < len; i++) {
		if (i + 1 == nums[i]) continue;
		int x = nums[i];
		while (x >= 1 && x <= len && x != nums[x - 1]) {
			swap(x, nums[x - 1]);
		}
	}
	// Find the missing one directly
	for (int i = 0; i < len; i++) {
		if (i + 1 != nums[i])
			return i + 1;
	}
	return len + 1;
}


int main() {
	while (true) {
		clock_t start;
		clock_t stop;
		int i,output;
		vector<int> input = {1,3,4,5,6,-3,2};
		
		start = clock();
		stop = start + CLOCKS_PER_SEC;
		for (i = 0; clock() < stop; i++) {
			output = firstMissingPositive(input);
		}
		start = clock() - start;
		cout << "The first missing positive is " << output << endl;
		printf(" %f ms (%d trials)\n", 1000 * (double)start / CLOCKS_PER_SEC / i, i);

		system("pause");
	}
}
