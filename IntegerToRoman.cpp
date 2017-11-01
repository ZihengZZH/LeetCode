/*

Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.

Symbol	  I	  V	  X	  L	  C	  D	  M
Value	  1	  5	  10	  50	  100	  500	  1,000s

*/

#include <iostream>
#include <string>

using namespace std;

string intToRoman(int num) {
	string res;
	int count,div,rem;
	int numb[13] = { 1000,900,500,400,100,90,50,40,10,9,5,4,1 };
	string roman[13] = { "M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I" };
	for (int i = 0; i < 13; i++) {
		div = num / numb[i];
		rem = num % numb[i];
		if (div == 0) continue; // If divider is 0 (no current digit)
		while (div--) {
			res = res + roman[i]; // # character
		}
		num = rem; // Assign the value and continue
	}
	return res;
}

int main() {
	while (true){
		cout << "Input: ";
		int integer;
		cin >> integer;
		cout << "Output: " << intToRoman(integer) << endl;
		system("pause");
	}
}
