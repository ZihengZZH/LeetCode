/*

Given an integer array with even length, where different numbers in this array represent different kinds of candies.
Each number means one candy of the corresponding kind.
You need to distribute these candies equally in number to brother and sister.
Return the maximum number of kinds of candies the sister could gain.

Example 1:
Input: candies = [1,1,2,2,3,3]
Output: 3
Explanation:
There are three different kinds of candies (1, 2 and 3), and two candies for each kind.
Optimal distribution: The sister has candies [1,2,3] and the brother has candies [1,2,3], too.
The sister has three different kinds of candies.

Example 2:
Input: candies = [1,1,2,3]
Output: 2
Explanation: For example, the sister has candies [2,3] and the brother has candies [1,1].
The sister has two different kinds of candies, the brother has only one kind of candies.

Note:
The length of the given array is in range [2, 10,000], and will be even.
The number in given array is in range [-100,000, 100,000].

*/


#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <map>
#include <numeric>
#include <functional>
#include <algorithm>
#include <math.h>
#include <ctime>
#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

using namespace std;


int distributeCandies(vector<int>& candies) {
	size_t kinds = 1;
	sort(candies.begin(), candies.end());
	for (int i = 1; i < candies.size(); i++) {
		kinds += candies[i] != candies[i - 1];
	}
	return min(kinds, candies.size() / 2);
}


int main() {

	vector<int> candies = { 1,1,2,2,3,3 };
	int i, output;

	cout << "INPUT ";
	for (auto candy : candies) {
		cout << candy << " ";
	}
	clock_t begin_time = clock();
	clock_t end_time = begin_time + CLOCKS_PER_SEC;
	for (i = 0; clock() < end_time; i++) {
		output = distributeCandies(candies);
	}

	cout << "\nOUTPUT " << output << endl;
	printf("%f ms (%d trials)\n", 1000 * (double)begin_time / CLOCKS_PER_SEC / i, i);

	getchar();
	return 0;
}
