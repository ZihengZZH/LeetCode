/*

Determine whether an integer is a palindrome. Do this without extra space.

*/

#include <iostream>

using namespace std;

bool isPalindrome(int x) {
	int integer = x;
	if (x < 0) { return false; }
	int result = 0; // The result of reverse
	int carry = 0; // The reminder part
	while (x != 0) {
		carry = x % 10; // Carry part = last digit of current digit
		result = result * 10 + carry; // Calculate result as current digit and reminder
		x /= 10; // Decrease one bit as a whole
	} // Loop until running through the integer
	cout << "The result is " << result << endl;
	if (result == integer) {
		return true;
	}
	else {
		return false;
	}
}

int main() {
	cout << "Enter an integer: ";
	int integer;
	cin >> integer;
	if (isPalindrome(integer)) {
		cout << "It is a palindrome \n";
	}
	else {
		cout << "It is not a palindrome \n";
	}
	system("pause");
}
