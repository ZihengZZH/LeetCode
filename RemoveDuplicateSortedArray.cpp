/*

Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. 
It doesn't matter what you leave beyond the new length.

*/

#include <iostream>
#include <string>
#include <vector>

using namespace std;

//int removeDuplicates(vector<int>& nums) {
//	vector<int> res;
//	vector<int>::iterator it;
//	bool occ = false;
//	for (it = nums.begin(); it != nums.end(); it++) {
//		occ = false;
//		cout << *it << endl;
//		for (int i = 0; i < res.size(); i++) {
//			if (res[i] == *it) occ = true;
//		}
//		if (occ == false) res.push_back(*it);
//	}
//	int count = res.size();
//	return count;
//}

int removeDuplicate(vector<int>& nums) {
	int count = 0;
	for (int i = 1; i < nums.size(); i++) {
		if (nums[i] == nums[i - 1]) count++;
		else nums[i - count] = nums[i];
	}
	return nums.size() - count;
}

int main() {
	while (true){
		cout << "Input: \n";
		vector<int> nums = { 1,1,3,4,5 };
		cout << "Output: " << removeDuplicate(nums) << endl;
		vector<int>::iterator it;
		for (it = nums.begin(); it != nums.end(); it++) {
			cout << *it << endl;
		}
		system("pause");
	}
}
