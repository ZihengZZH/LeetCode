/*

Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

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


int singleNumber(vector<int>& nums) {
	/*vector<int> helper;
	vector<int>::iterator iter, it, ret;
	for (iter = nums.begin(); iter != nums.end(); iter++) {
		cout << "ELEMENT " << *iter << endl;
		if (helper.empty()) {
			helper.push_back(*iter);
		}

		for (auto i : helper) {
			cout << i << "\t";
		}
		cout << endl;

		it = helper.begin();
		do {
			cout << "helper " << *it << endl;
			if (*it == *iter) {
				*it = NULL;
				//ret = remove(helper.begin(), helper.end(), *it);
				break;
			} else {
				helper.push_back(*iter);
			}
			//cout << "SIZE" << helper.size() << endl;
			it++;
		} while (it != helper.end());
	}
	cout << "SIZE" << helper.size() << endl;
	return 0;*/
	if (nums.empty()) return 0;
	int res = nums[0];
	for (int i = 1; i < nums.size(); i++) {
		res = res ^ nums[i];
		// XOR (Exclusive OR) bit manipulation
		// XOR is commutative so when two same number XOR will give 0
		// Then the result will be the single number
		cout << nums[i] << "  " << res << endl;
	}
	return res;
}

int main() {
	while (true) {
		clock_t start;
		clock_t stop;
		int i,output;
		vector<int> input = { 2,3,4,5,6,5,4,3,2,1,1 };
		

		start = clock();
		stop = start + CLOCKS_PER_SEC;
		for (i = 0; clock() < stop; i++) {
			output = singleNumber(input);
		}

		cout << "ANSWER IS " << output << endl;
		printf("%f ms (%d trials)\n", 1000 * (double)start / CLOCKS_PER_SEC / i, i);


		system("pause");
	}
}
