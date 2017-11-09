/*

Given an integer n, return 1 - n in lexicographical order.

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.

*/


#include <vector>
#include <bitset>
#include <iostream>
#include <string>
#include <algorithm>
#include <time.h>
#include <sstream>

using namespace std;


// It is important to explore the pattern in the lexicalOrder
// Maybe initializing first will be effecient than push_back
vector<int> lexicalOrder(int n) {
	vector<int> res(n); // Initialize the vector
	int cur = 1;
	for (int i = 0; i < n; i++) {
		res[i] = cur;
		if (cur * 10 <= n) {
			cur *= 10;
		} else {
			if (cur >= n)
				cur /= 10;
			cur += 1;
			while (cur % 10 == 0)
				cur /= 10;
		}
	} // Manipulate every element in the vector until enough
	return res;
}


int main() {
	while (true) {
		clock_t start;
		clock_t stop;
		int i, input = 12220;
		vector<int> output;

		start = clock();
		stop = start + CLOCKS_PER_SEC;
		for (i = 0; clock() < stop; i++) {
			output = lexicalOrder(input);
		}
		start = clock() - start;
		cout << "The answer is as follows with input " << input << endl;
		for (vector<int>::const_iterator iter = output.cbegin(); iter != output.cend(); iter++) {
			cout << (*iter) << "  ";
		}
		cout << endl;
		printf(" %f ms (%d trials)\n", 1000 * (double)start / CLOCKS_PER_SEC / i, i);

		system("pause");
	}
}
