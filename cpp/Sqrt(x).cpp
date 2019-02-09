/*

Implement int sqrt(int x).
Compute and return the square root of x.

Note that Newton's method is recommended.

*/


#include <vector>
#include <bitset>
#include <iostream>
#include <string>
#include <algorithm>
#include <time.h>
#include <sstream>
using namespace std;

/*
Newton's method
r is the root of f(x) = 0
First draw a tangent line with x0; y = f(x0) + f'(x0)(x-x0)
x1 = x0 - f(x0)/f'(x0) where x1 is the first approximation
then x2, x3 ... iterate until xn = r
So in this problems f(r) = r^2 - x (x is the input)
r1 = r0 - f(r0)/f'(r0) = r0 - r0^2/(2*r0)
r1 = (r0 + x/r0)/2
iterate until r = sqrt(x)
*/
int sqrt(int x) {
	long long r = x;
	while (r*r > x)
		r = (r + x / r) / 2;
	return r;
}

int main() {
	while (true) {
		clock_t start;
		clock_t stop;
		int i, output;
		
		for (int input = 100; input < 1000; input++) {
			start = clock();
			stop = start + CLOCKS_PER_SEC;
			for (i = 0; clock() < stop; i++) {
				output = sqrt(input);
			}
			start = clock() - start;
		
			cout << "The answer for " << input << " is " << output << endl;
			printf(" %f ms (%d trials)\n", 1000 * (double)start / CLOCKS_PER_SEC / i, i);
		}
		

		system("pause");
	}
}
