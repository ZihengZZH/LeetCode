/*

Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:
n = 15,
Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]

*/


#include <vector>
#include <bitset>
#include <iostream>
#include <iomanip>
#include <string>
#include <algorithm>
#include <time.h>
#include <sstream>
using namespace std;



vector<string> fizzBuzz(int n) {
	vector<string> res;
	for (int i = 1; i <= n; i++) {
		if (i % 3 == 0 && i % 5 == 0) {
			res.push_back("FizzBuzz");
		}
		else if (i % 3 == 0) {
			res.push_back("Fizz");
		}
		else if (i % 5 == 0) {
			res.push_back("Buzz");
		}
		else {
			res.push_back(to_string(i));
		}
	}
	return res;
}



int main() {
	while (true) {
		clock_t start;
		clock_t stop;
		int i;
		int input_n;
		vector<string> output;
		
		input_n = 32;

		start = clock();
		stop = start + CLOCKS_PER_SEC;
		for (i = 0; clock() < stop; i++) {
			output = fizzBuzz(input_n);
		}

		cout << "ANSWER IS \n";
		for (auto i : output) {
			cout << i << "\n";
		}
		printf("\n%f ms (%d trials)\n", 1000 * (double)start / CLOCKS_PER_SEC / i, i);


		system("pause");
	}
}

