/*

Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].

*/


#include <vector>
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

// equal_range是C++ STL中的一种二分查找的算法，试图在已排序的[first, last)中寻找value，
// 它返回一对迭代器i和j，其中i是在不破坏次序的前提下，value可插入的第一个位置（亦即lower_bound），
// j则是在不破坏次序的前提下，value可插入的最后一个位置（亦即upper_bound），
// 因此，[i, j)内的每个元素都等同于value，而且[i, j)是[first, last)之中符合此一性质的最大子区间
// 如果以稍许不同的角度来思考equal_range, 我们可把它想成是[first, last)内"与value等同"之所有元素形成的区间A，
// 由于[fist, last)有序（sorted），所以我们知道"与value等同"之所有元素一定都相邻，
// 于是，算法lower_bound返回区间A的第一个迭代器，算法upper_bound返回区间A的最后一个元素的下一个位置，
// 算法equal_range则是以pair的形式将两者都返回
// 即使[fist, last)并未含有"与value等同"之任何元素，以上叙述仍然合理，
// 这种情况下，"与value等同"之所有元素形成的，其实是一个空区间，在不破坏次序的情况下，
// 只有一个位置可以插入value，而equal_range所返回的pair，其第一和第二（都是迭代器）皆指向该位置。

// auto关键字用于两种情况：声明变量时根据初始化表达式自动推断该变量的类型、声明函数时函数返回值的占位符。

vector<int> searchRange(vector<int>& nums, int target) {
	auto bounds = equal_range(nums.begin(), nums.end(), target);
	if (bounds.first == bounds.second) return{ -1,-1 };
	return{ bounds.first - nums.begin(), bounds.second - nums.begin() - 1 };
}

int main() {
	while (true) {
		cout << "Enter the target: ";
		int tagt;	cin >> tagt;
		vector<int> input = { 5,7,7,8,8,10 };
		vector<int> output = searchRange(input, tagt);
		cout << output[0] << endl;
		cout << output[1] << endl;
		system("pause");
	}
}
