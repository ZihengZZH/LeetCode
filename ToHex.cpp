/*

Given an integer, write an algorithm to convert it to hexadecimal. 
For negative integer, two's complement method is used.

*/

#include <iostream>
#include <string>
#include <vector>
#include <utility>

using namespace std;

const string HEX = "0123456789abcdef";

class Solution {
public:

	string toHex(int num) {
		vector<pair<int, string>> hexDigit;
		hexDigit.push_back(pair<int, string>(10, "a"));
		hexDigit.push_back(pair<int, string>(11, "b"));
		hexDigit.push_back(pair<int, string>(12, "c"));
		hexDigit.push_back(pair<int, string>(13, "d"));
		hexDigit.push_back(pair<int, string>(14, "e"));
		hexDigit.push_back(pair<int, string>(15, "f"));
		string res;
		int count = 0;
		bool neg = num >= 0 ? false : true;
		num = abs(num);
		while (num && count++ < 8)  {
			int digit = num % 16;
			if (digit < 10)
				res = to_string(digit) + res;
			else
				for (auto dig : hexDigit) {
					if (dig.first == digit)
						res = dig.second + res;
				}
			num /= 16;
		}
		if (neg) {
			// TO DO 2's complement
		}

		return res;

	}

	string toHex_online(int num) {
		if (num == 0) return "0";
		string result;
		int count = 0;
		while (num && count++ < 8) {
			result = HEX[(num & 0xf)] + result;
			num >>= 4;
		}
		return result;
	}
};


int main() {

	Solution *solu = new Solution();
	for (int i = -100; i < 100; i++) {
		cout << i << " " << solu->toHex(i) << endl;
	}
	getchar();

}