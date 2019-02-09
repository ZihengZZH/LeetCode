/*

Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number.

*/


#include <vector>
#include <bitset>
#include <iostream>
#include <string>
#include <algorithm>
#include <time.h>
#include <sstream>

using namespace std;

vector<int> isPrime(int num) {
	vector<int> prime = {};
	for (int i = 2; i <= num; i++) {
		while (num != i) {
			if (num % i != 0) break;
			prime.push_back(i);
			num = num / i;
		}
	}
	prime.push_back(num);
	/*for (int j = 0; j < prime.size(); j++) {
	cout << "Prime " << j << " " << prime[j] << endl;
	}*/
	return prime;
}

bool isUglyB(int num) {
	if (num == 1) return true;
	vector<int> primes = isPrime(num);
	for (int i = 0; i < primes.size(); i++) {
		if (primes[i] != 2 && primes[i] != 3 && primes[i] != 5) return false;
	}
	return true;
}

bool isUgly(int num) {
	if (num == 1) return true;
	for (int i = 2; i < 6 && num; i++) {
		while (num % i == 0) {
			num = num / i;
		}
	}
	return num == 1;
}

int main() {
	while (true) {
		clock_t start;
		clock_t stop;
		int i, input;
		bool output = true;
		cout << "Enter the number ";
		cin >> input;

		start = clock();
		stop = start + CLOCKS_PER_SEC;
		for (i = 0; clock() < stop; i++) {
			output = isUgly(input);
		}
		start = clock() - start;
		cout << "The given number is ugly number " << boolalpha << output << endl;
		printf(" %f ms (%d trials)\n", 1000 * (double)start / CLOCKS_PER_SEC / i, i);

		start = clock();
		stop = start + CLOCKS_PER_SEC;
		for (i = 0; clock() < stop; i++) {
			output = isUglyB(input);
		}
		start = clock() - start;
		cout << "The given number is ugly number " << boolalpha << output << endl;
		printf(" %f ms (%d trials)\n", 1000 * (double)start / CLOCKS_PER_SEC / i, i);

		system("pause");
	}
}
