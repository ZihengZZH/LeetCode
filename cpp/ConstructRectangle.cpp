/*

For a web developer, it is very important to know how to design a web page's size. So, given a specific rectangular web page’s area, your job by now is to design a rectangular web page, whose length L and width W satisfy the following requirements:

1. The area of the rectangular web page you designed must equal to the given target area.
2. The width W should not be larger than the length L, which means L >= W.
3. The difference between length L and width W should be as small as possible.

You need to output the length L and the width W of the web page you designed in sequence.

Example:
Input: 4
Output: [2, 2]
Explanation: The target area is 4, and all the possible ways to construct it are [1,4], [2,2], [4,1]. 
But according to requirement 2, [1,4] is illegal; according to requirement 3,  [4,1] is not optimal compared to [2,2]. So the length L is 2, and the width W is 2.

Note:
The given area won't exceed 10,000,000 and is a positive integer
The web page's width and length you designed must be positive integers.

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


vector<int> constructRectangle(int area) {

	vector<vector<int>> pairs;

	for (int i = 1; i <= sqrt(area); i++) {
		vector<int> pair;
		if (area % i == 0) {
			pair.push_back(i);
			pair.push_back(area / i);
			pairs.push_back(pair);
		}
	}

	sort(pairs.begin(), pairs.end(), [](vector<int> a, vector<int> b) 
	{return abs(a[0] - a[1]) < abs(b[0] - b[1]); });

	if (pairs[0][0] < pairs[0][1]) {
		int temp = pairs[0][0];
		pairs[0][0] = pairs[0][1];
		pairs[0][1] = temp;
	}

	return pairs[0];
}

int main() {

	vector<int> output;

	for (int j = 0; j < 10; j++) {
		int input = rand() % 1000;
		output = constructRectangle(input);
		cout << "To input " << input << " the output is "
			<< "[" << output[0] << "," << output[1] << "]\n";

	}
	

	system("pause");
	return 0;
}
