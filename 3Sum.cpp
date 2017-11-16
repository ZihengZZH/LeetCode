/*

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
	[-1, 0, 1],
	[-1, -1, 2]
]

*/


#include <iostream>
#include <vector>
#include <numeric>
#include <functional>
#include <algorithm>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

vector<vector<int> > threeSum(vector<int> &nums) {

	vector<vector<int> > res;
	std::sort(nums.begin(), nums.end());
	int target, front, back, sum;

	for (int i = 0; i < nums.size(); i++) {
		target = -nums[i];
		front = i + 1;
		back = nums.size() - 1;

		while (front < back) {
			sum = nums[front] + nums[back];
			// Finding answer which start from number num[i]
			if (sum < target)
				front++;
			else if (sum > target)
				back--;
			else {
				vector<int> triplet(3, 0);
				triplet[0] = nums[i];
				triplet[1] = nums[front];
				triplet[2] = nums[back];
				res.push_back(triplet);
				// Processing duplicates of Number 2
				// Rolling the front pointer to the next different number forwards
				while (front < back && nums[front] == triplet[1]) front++;
				// Processing duplicates of Number 3
				// Rolling the back pointer to the next different number backwards
				while (front < back && nums[back] == triplet[2]) back--;
			}
		}

		// Processing duplicates of Number 1
		while (i + 1 < nums.size() && nums[i + 1] == nums[i]) i++;

	}

	return res;

}


int main() {

	vector<int> input_vec = { -1,0,1,2,-1,-4,-3,3,2,5,-1 };
	vector<vector<int>> output_vec = threeSum(input_vec);

	cout << "ANSWER IS " << endl;
	for (auto i : output_vec) {
		for (auto j : i) {
			cout << j << ", ";
		}
		cout << endl;
	}

	system("pause");
	return 0;
	
}