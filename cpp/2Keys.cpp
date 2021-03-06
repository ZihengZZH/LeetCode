/*

Initially on a notepad only one character 'A' is present. You can perform two operations on this notepad for each step:

Copy All: You can copy all the characters present on the notepad (partial copy is not allowed).
Paste: You can paste the characters which are copied last time.
Given a number n. You have to get exactly n 'A' on the notepad by performing the minimum number of steps permitted. Output the minimum number of steps to get n 'A'.

Example 1:
Input: 3
Output: 3
Explanation:
Intitally, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.

Note:
The n will be in the range [1, 1000].

*/


#include <iostream>
#include <vector>
#include <numeric>
#include <functional>
#include <algorithm>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

/*
It takes 2 op to double, 3 op to triple, ...
If n % 2 == 0, then f(n) = f(n/2) + 2
If n % 3 == 0, then f(n) = f(n/3) + 3
2*2 = 2+2, 2*3 > 2+3, 4*4 > 4+4, so it is always better to divide whenever possible
Now it becomes a problem for finding all possible factors.
*/

int minSteps(int n) {

	if (n == 1) return 0;
	for (int i = 2; i < n; i++) {
		if (n % i == 0) return i + minSteps(n / i);
	}
	return n;

}


int main() {

	int input = 1;
	for (; input <= 100; input++) {
		cout << "INPUT " << input << " OUTPUT " << minSteps(input) << endl;
	}

	system("pause");
	return 0;
	
}