/*

Given an array of integers that is already sorted in ascending order, 
find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that 
they add up to the target, where index1 must be less than index2. 
Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution and you may not use the same element twice.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2

*/

#include <vector>
#include <bitset>
#include <iostream>
#include <string>
#include <algorithm>
#include <time.h>
#include <sstream>

using namespace std;

int binarySearch(vector<int>& nums, int left, int right, int target) {
	if (right >= left) {
		int mid = left + (right - left) / 2;
		if (nums[mid] == target) {
			return mid;
		}
		else if (nums[mid] < target) {
			return binarySearch(nums, mid+1, right, target);
		}
		else {
			return binarySearch(nums, left, mid-1, target);
		} 
	}
	return -1;
}


vector<int> twoSum(vector<int>& numbers, int target) {
	sort(numbers.begin(), numbers.end());
	vector<int> res(2);
	int temp, secIndex = 0, firstIndex = 0;
	while (firstIndex <= (numbers.size() - 1)) {
		temp = numbers[firstIndex];
		secIndex = binarySearch(numbers, 0, numbers.size()-1, target - temp);
		cout << "first index " << firstIndex << " second index " << secIndex << endl;
		if (secIndex != -1 && firstIndex != secIndex) {
			res[0] = firstIndex + 1;
			res[1] = secIndex + 1;
		}
		firstIndex++;
	}
	if (res[0] > res[1]) {
		int tempo = res[0];
		res[0] = res[1];
		res[1] = tempo;
	}
	return res;
}

int main() {
	while (true) {
		clock_t start;
		clock_t stop;
		int target = 0, i;
		vector<int> input = { 0,0,3,4 };
		// 2,4,6,10,13,14,19,26,40,67
		vector<int> output = twoSum(input, target);
		
		
		start = clock();
		stop = start + CLOCKS_PER_SEC;
		for (i = 0; clock() < stop; i++) {
			output = twoSum(input, target);
		}
		start = clock() - start;
		
		
		cout << "The answer is as follows " << endl;
		for (vector<int>::const_iterator iter = output.cbegin(); iter != output.cend(); iter++) {
			cout << (*iter) << " ";
		}
		cout << endl;
		printf(" %f ms (%d trials)\n", 1000 * (double)start / CLOCKS_PER_SEC / i, i);
		

		system("pause");
	}
}
