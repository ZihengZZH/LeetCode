/*

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.

*/


#include <iostream>
#include <string>
#include <vector>
#include <numeric>
#include <functional>
#include <algorithm>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctime>


using namespace std;

class MinStack {
public:
	vector<int> stack;

	/** initialize your data structure here. */
	MinStack() {
		stack.clear();
	}

	void push(int x) {
		stack.push_back(x);
	}

	void pop() {
		if (stack.size() >= 1)
			stack.pop_back();
	}

	int top() {
		vector<int>::iterator iter = stack.end() - 1;
		return *iter;
	}

	int getMin() {
		int min = INT_MAX;
		for (auto s : stack)
		{
			if (s < min)
				min = s;
		}
		return min;
	}

	void display() {
		for (auto s : stack)
		{
			cout << s << "\t";
		}
		cout << endl;
	}
};

/**
* Your MinStack object will be instantiated and called as such:
* MinStack obj = new MinStack();
* obj.push(x);
* obj.pop();
* int param_3 = obj.top();
* int param_4 = obj.getMin();
*/

int main() {

	int x = 10, y = 1, z = 4;
	MinStack obj;
	obj.push(x);
	obj.display();
	obj.push(y);
	obj.display();
	obj.push(z);
	obj.display();
	obj.pop();
	obj.display();
	int param_3 = obj.top();
	cout << "param_3 " << param_3 << endl;
	int param_4 = obj.getMin();
	cout << "param_4 " << param_4 << endl;

	getchar();
	return 0;
	
}