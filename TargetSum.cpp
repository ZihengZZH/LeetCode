/*

You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. 
Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.
Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 
-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
There are 5 ways to assign symbols to make the sum of nums be target 3.

Note:
The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.

*/

#include <vector>
#include <bitset>
#include <iostream>
#include <string>
#include <algorithm>
#include <time.h>
#include <sstream>

using namespace std;

int subsetSum(vector<int>& nums, int S) {
	vector<int> dp(S + 1, 0);
	dp[0] = 1;
	for (int n : nums) {
		for (int i = S; i >= n; i--) {
			dp[i] += dp[i - n];
		}
	}
	return dp[S];
}

int findTargetSumWays(vector<int>& nums, int S) {
	int sum = 0;
	for (int i : nums) sum += i;

	return sum < S || (S + sum) & 1 ? 0 : subsetSum(nums, (S + sum) >> 1);
}

int findTargetSumWay(vector<int>& nums, int S) {
	int sum = 0, count;
	for (int i : nums) sum += i;
	int subSum = subsetSum(nums, (S + sum) / 2);
	if (sum < S || (S + sum) % 2 != 0)
		count = 0;
	else
		count = subSum;
	return count;
}

int main() {
	while (true) {
		clock_t start;
		clock_t stop;
		int i, input, output;
		vector<int> vec = { 1,2,7,9,981 };
		input = 1000000000;

		start = clock();
		stop = start + CLOCKS_PER_SEC;
		for (i = 0; clock() < stop; i++) {
			output = findTargetSumWay(vec, input);
		}
		start = clock() - start;
		cout << "The answer is as follows " << output << endl;
		printf(" %f ms (%d trials)\n", 1000 * (double)start / CLOCKS_PER_SEC / i, i);

		system("pause");
	}
}
