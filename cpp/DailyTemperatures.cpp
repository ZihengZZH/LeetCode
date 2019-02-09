/*

Given a list of daily temperatures, produce a list that, for each day in the input,
tells you how many days you would have to wait until a warmer temperature.
If there is no future day for which this is possible, put 0 instead.

For example, given the list temperatures = [73, 74, 75, 71, 69, 72, 76, 73],
your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000].
Each temperature will be an integer in the range [30, 100].

*/


#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <numeric>
#include <functional>
#include <algorithm>
#include <math.h>
#include <ctime>
#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

using namespace std;

void displayVec(vector<int>& vec) {
	for (auto v : vec) {
		cout << v << "\t";
	}
	cout << endl;
}

void displayStack(stack<int>& stack) {
	std::stack<int> new_stack = stack;
	while (!new_stack.empty()) {
		cout << new_stack.top() << "\t";
		new_stack.pop();
	}
	cout << endl;
}

// Mono Stack LIFO (in which some order exist)
// Complexity O(n) (each element in/out once)
vector<int> dailyTemperatures(vector<int>& temperatures) {
	vector<int> result(temperatures.size());
	stack<int> mono_stack;
	for (int i = 0; i < temperatures.size(); ++i) {
		while (!mono_stack.empty() && temperatures[mono_stack.top()] < temperatures[i]) {
			result[mono_stack.top()] = i - mono_stack.top();
			mono_stack.pop();
		}
		mono_stack.push(i);
		//displayStack(mono_stack);
	}
	return result;
}

int main() {

	vector<int> lst = vector<int>{ 73, 74, 75, 71, 69, 72, 76, 73 };
	vector<int> res;
	int i;

	cout << "INPUT ";
	displayVec(lst);
	clock_t begin_time = clock();
	clock_t end_time = begin_time + CLOCKS_PER_SEC;
	for (i = 0; clock() < end_time; i++) {
		res = dailyTemperatures(lst);
	}
	cout << "OUTPUT ";
	displayVec(res);
	printf("%f ms (%d trials)\n", 1000 * (double)begin_time / CLOCKS_PER_SEC / i, i);

	getchar();
	return 0;
}
