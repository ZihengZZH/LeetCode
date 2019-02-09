/*

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
Find all the elements that appear twice in this array.
Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]

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


// Actually this algorithm is equivalent to the one in Python
// However, the running time between C++ and Python is considerably different
// C++ is at least three times efficient to Python
vector<int> findDuplicates(vector<int>& nums) {
	sort(nums.begin(), nums.end());
	vector<int> res = {};
	int length = nums.size();
	for (int i = 0; i < length - 1; i++) {
		if (nums[i] == nums[i + 1])
			res.push_back(nums[i]);
	}
	return res;
}

int main() {
	while (true) {
		clock_t start;
		clock_t stop;
		int i;
		vector<int> input = { 40,3,21,7,8,2,3,1,8 };
		vector<int> outputs;
		

		start = clock();
		stop = start + CLOCKS_PER_SEC;
		for (i = 0; clock() < stop; i++) {
			outputs = findDuplicates(input);
		}

		cout << "ANSWER IS " << endl;
		for (auto output : outputs) {
			cout << output << "\t";
		}
		printf("\n%f ms (%d trials)\n", 1000 * (double)start / CLOCKS_PER_SEC / i, i);


		system("pause");
	}
}
