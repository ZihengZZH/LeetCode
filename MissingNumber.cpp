/*

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, 
find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. 
Could you implement it using only constant extra space complexity?

*/

#include <vector>
#include <bitset>
#include <iostream>
#include <string>
#include <algorithm>
#include <time.h>
#include <sstream>
using namespace std;

// Traditional way to traverse the array
int missingNumber(vector<int>& nums) {
	sort(nums.begin(), nums.end());
	int missing = 0, i;
	for (i = 0; i < nums.size(); i++) {
		if (nums[i] != i) {
			return i;
		}
	}
	return i;
}

// Faster with arithmetics
int missingNumber_2(vector<int>& nums) {
	int sum = 0;
	for (int num : nums)
		sum += num;
	return ((nums.size() + 1)*nums.size() / 2 - sum);
}


int main() {
	while (true) {
		clock_t start;
		clock_t stop;
		int i, output;
		vector<int> vec = { 0,1,2,7,6,5,4,3,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24 };

		start = clock();
		stop = start + CLOCKS_PER_SEC;
		for (i = 0; clock() < stop; i++) {
			output = missingNumber(vec);
		}
		start = clock() - start;
		cout << "The answer is as follows " << output << endl;
		printf(" %f ms (%d trials)\n", 1000 * (double)start / CLOCKS_PER_SEC / i, i);

		start = clock();
		stop = start + CLOCKS_PER_SEC;
		for (i = 0; clock() < stop; i++) {
			output = missingNumber_2(vec);
		}
		start = clock() - start;
		cout << "The answer is as follows " << output << endl;
		printf(" %f ms (%d trials)\n", 1000 * (double)start / CLOCKS_PER_SEC / i, i);

		system("pause");
	}
}
