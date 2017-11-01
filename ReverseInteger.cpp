/*

Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

Note:
The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.

*/


#include <iostream>

using namespace std;

int reverse(int x) {
	int result = 0; // The result of reverse
	int carry = 0; // The reminder part
	while (x != 0) {
		carry = x % 10; // Carry part = last digit of current digit
		if (result > INT32_MAX / 10 || result < INT32_MIN / 10) {
			return 0; // If overflows, return 0 as required
		}
		result = result * 10 + carry; // Calculate result as current digit and reminder
		x /= 10; // Decrease one bit as a whole
	} // Loop until running through the integer
	return result;
}

int main() {
	cout << "Enter an integer: ";
	int integer;
	cin >> integer;
	cout << "The reversed is: " << reverse(integer) << endl;
	system("pause");
}
