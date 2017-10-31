/*

Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

For example:
Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

*/


#include <iostream>
#include <vector>
#include <numeric>
#include <functional>
#include <time.h>

using namespace std;

// Best-O(n)	Worst-O(n^2)
vector<int> singleNumber(vector<int>& nums) {
	vector<int> res;
	vector<int>::iterator it;
	bool occupy;
	for (auto num : nums) {
		occupy = false;
		it = res.begin();
		while (it != res.end()) {
			if (*it == num) {
				occupy = true;
				res.erase(it);
				break;
			}
			it++;
		}
		if (!occupy) res.insert(res.begin(), num);
	}

	return res;
}

// O(n)-time O(1)-space
vector<int> online(vector<int>& nums) {
	// Pass 1 : 
	// Get the XOR of the two numbers we need to find
	int diff = accumulate(nums.begin(), nums.end(), 0, bit_xor<int>());
	// Get its last set bit
	diff &= -diff;

	// Pass 2 :
	vector<int> rets = { 0, 0 }; // this vector stores the two numbers we will return
	for (int num : nums)
	{
		if ((num & diff) == 0) // the bit is not set
		{
			rets[0] ^= num;
		}
		else // the bit is set
		{
			rets[1] ^= num;
		}
	}
	return rets;
}

int main() {
	clock_t start;
	clock_t stop;
	int i;
	vector<int> input_num = { 11,2,1,3,2,3,5,4,10,10,1,4,100,100,5,13,32,43,43,13,32,9 }, output;


	start = clock();
	stop = start + CLOCKS_PER_SEC;
	for (i = 0; clock() < stop; i++) {
		output = singleNumber(input_num);
	}

	cout << "ANSWER IS \n";
	for (auto i : output) {
		cout << i << " ";
	}

	printf("\n%f ms (%d trials)\n", 1000 * (double)start / CLOCKS_PER_SEC / i, i);


	start = clock();
	stop = start + CLOCKS_PER_SEC;
	for (i = 0; clock() < stop; i++) {
		output = online(input_num);
	}

	cout << "ANSWER IS \n";
	for (auto i : output) {
		cout << i << " ";
	}

	printf("\n%f ms (%d trials)\n", 1000 * (double)start / CLOCKS_PER_SEC / i, i);


	system("pause");

}
