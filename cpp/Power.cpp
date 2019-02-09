/*

Implement pow(x, n).

Pay attention to the time complexity!!!
O(n) is not acceptable but O(logn)

*/

#include <vector>
#include <iostream>
#include <string>
#include <algorithm>
#include <time.h>

using namespace std;


// Time complexity O(logn)
double myPow(double x, int n) {
	double res = x;
	if (n == 0) return 1;
	res = myPow(x, n / 2);
	if (n % 2 == 0) return res*res;
	else {
		if (n > 0) return x*res*res;
		else return (res*res)/x;
	}
}
// This approach is clever and simple to understand
// Note it includes the situation of negative power


// Time complexity O(n)
double myPowBurst(double x, int n) {
	if (n == 0) return 1;
	double res = 1;
	for (int i = 0; i < abs(n); i++) {
		res = res * x;	
	}
	if (n < 0) res = 1 / res;
	return res;
}


int main() {
	while (true) {
		clock_t start;
		clock_t stop;
		int i; // counter
		double res1, res2;
		cout << "Enter the power: ";
		int intg;	 cin >> intg;
		cout << "Enter the base: ";
		double base;	cin >> base;

		start = clock();
		stop = start + CLOCKS_PER_SEC;
		for (i = 0; clock() < stop; i++) {
			res1 = myPow(base, intg);
		}
		start = clock() - start;
		cout << base << " to the power of " << intg << " is ";
		cout << res1 << endl;
		printf(" %f ms (%d trials)\n", 1000 * (double)start / CLOCKS_PER_SEC / i, i);

		start = clock();
		stop = start + CLOCKS_PER_SEC;
		for (i = 0; clock() < stop; i++) {
			res2 = myPowBurst(base, intg);
		}
		start = clock() - start;
		cout << base << " to the power of " << intg << " is ";
		cout << res2 << endl;
		printf(" %f ms (%d trials)\n", 1000 * (double)start / CLOCKS_PER_SEC / i, i);
		
		system("pause");
	}
}
