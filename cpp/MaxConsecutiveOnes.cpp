/*

Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Note:
The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000

*/


#include <iostream>
#include <vector>
#include <time.h>

using namespace std;

// Time complexity O(n)
int findMaxConsecutiveOnes(vector<int>& nums) {
	int sum = 0, count = 0;
	for (auto num : nums) {
		if (num == 1) {
			count++;
		}
		else {
			if (sum < count) sum = count;
			count = 0;
		}
	}
	if (sum < count) sum = count;
	return sum;
}


int main() {
	clock_t start;
	clock_t stop;
	int i, output;
	vector<int> input_num = { 1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,0,0,1,1,0,1,1,1 };

	start = clock();
	stop = start + CLOCKS_PER_SEC;
	for (i = 0; clock() < stop; i++) {
		output = findMaxConsecutiveOnes(input_num);
	}

	cout << "ANSWER IS " << output;

	printf("\n%f ms (%d trials)\n", 1000 * (double)start / CLOCKS_PER_SEC / i, i);


	system("pause");

}
