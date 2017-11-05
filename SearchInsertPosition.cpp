/*

Given a sorted array and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0

*/

#include <vector>
#include <iostream>
#include <string>

using namespace std;

int searchInsert(vector<int>& nums, int target) {
	int res = 0;
	for (int i = 0; i < nums.size(); i++) {
		if (nums[i] == target) {
			res = i; 
		} // Found return position
		if (i + 1 < nums.size() && nums[i] < target && nums[i + 1] > target) {
			cout << "Not found" << endl;
			res = i + 1;
		} // Not found return insert position
	}
	if (target > nums[nums.size() - 1]) res = nums.size();
	// If largr than all elements, return size index
	return res;
}

int main() {
	while (true){
		cout << "Input: ";
		vector<int> num = {1,3,5,6,9,20,34};
		int integer;
		cin >> integer;
		cout << "Output: "  << searchInsert(num,integer) << endl;
		system("pause");
	}
}
