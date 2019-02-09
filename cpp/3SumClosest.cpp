/*

Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. 
Return the sum of the three integers. You may assume that each input would have exactly one solution.

For example, given array S = {-1 2 1 -4}, and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

*/

#include <vector>
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int threeSumClosest(vector<int>& nums, int target) {
	if (nums.size() < 3) return 0;
	int res = nums[0] + nums[1] + nums[2]; // Initiate res value
	sort(nums.begin(),nums.end()); // Sort the vector first
	for (int start = 0; start < nums.size() -2; start++) {
		if (start > 0 && nums[start] == nums[start - 1]) continue;
		int mid = start + 1, last = nums.size() - 1; // Reset with every start
		while (mid < last) {
			int sum = nums[start] + nums[mid] + nums[last];
			if (sum == target) return sum; // If equals, return sum immediately
			if (abs(target - sum) < abs(target - res)) res = sum; // Assign the smaller
			if (sum > target) last--; // Reduce the sum
			else mid++; // Increase the sum
		}
		cout << start << "\t" << mid << "\t" << last << endl;
	} // Iterate all combinations of three numbers
	return res;
}

int main() {
	while (true){
		cout << "Input: ";
		int integer;
		cin >> integer;
		vector<int> str = {-1,2,1,-4,6,30,9,-10};
		cout << "Output: " << threeSumClosest(str, integer) << endl;
		system("pause");
	}
}
