/*

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)

*/


#include <vector>
#include <iostream>
#include <string>
#include <algorithm>
#include <time.h>
#include <sstream>

using namespace std;

// Test input: 25525511135

template <class T>
void convertFromString(T &value, const string &s) {
	  stringstream ss(s);
	  ss >> value;
}

string getStr(const int n) {
	stringstream ss;
	ss << n;
	return ss.str();
}

vector<string> restoreIpAddress(string s) {
	vector<string> res = {};
	int len = s.length();
	for (int i = 1; i <= 3; i++) {
		if (len - i > 9) continue;
		for (int j = i + 1; j <= i + 3; j++) {
			if (len - j > 6) continue;
			for (int k = j + 1; k <= j + 3 && k < len; k++) {
				int a, b, c, d;
				convertFromString(a, s.substr(0, i));
				convertFromString(b, s.substr(i, j-i));
				convertFromString(c, s.substr(j, k-j));
				convertFromString(d, s.substr(k));
				//cout << a << "\t" << b << "\t" << c << "\t" << d << endl;
				//cout << getStr(a) << "\t" << getStr(b) << "\t" << c << "\t" << d << endl;
				if (a > 255 || b > 255 || c > 255 || d > 255) continue;
				string tempIP = getStr(a) + "." + getStr(b) + "." + getStr(c) + "." + getStr(d);
				cout << "tempIP " << tempIP << endl;
				if (tempIP.length() < len + 3) continue;
				res.push_back(tempIP);
			}
		}
	}
	return res;
}

vector<string> restoreIP(string s) {
	vector<string> res;
	string ans;
	for (int a = 1; a <= 3; a++)
	for (int b = 1; b <= 3; b++)
	for (int c = 1; c <= 3; c++)
	for (int d = 1; d <= 3; d++)
		if (a + b + c + d == s.length()) {
			int A = stoi(s.substr(0, a));
			int B = stoi(s.substr(a, b));
			int C = stoi(s.substr(a + b, c));
			int D = stoi(s.substr(a + b + c, d));
			if (A <= 255 && B <= 255 && C <= 255 && D <= 255) {
				if ((ans = to_string(A) + "." + to_string(B) + "." + to_string(C) + "." + to_string(D)).length() == s.length() + 3)
					res.push_back(ans);
			}
		}
	return res;
}

// restoreIP() is quite faster than restoreIpAddress()
int main() {
	while (true) {
		clock_t start;
		clock_t stop;
		int i; // counter
		string input;
		cout << "Enter the address: ";
		cin >> input;
		if (input.length() < 3) break;
		cout << "IP address (only digits) " << input << endl;
		vector<string> output = {};

		start = clock();
		stop = start + CLOCKS_PER_SEC;
		for (i = 0; clock() < stop; i++) {
			output = restoreIpAddress(input);
		}
		start = clock() - start;
		for (int m = 0; m < output.size(); m++) {
			cout << "IP address could be " << output[m] << endl;
		}
		printf(" %f ms (%d trials)\n", 1000 * (double)start / CLOCKS_PER_SEC / i, i);

		start = clock();
		stop = start + CLOCKS_PER_SEC;
		for (i = 0; clock() < stop; i++) {
			output = restoreIP(input);
		}
		start = clock() - start;
		for (int m = 0; m < output.size(); m++) {
			cout << "IP address could be " << output[m] << endl;
		}
		printf(" %f ms (%d trials)\n", 1000 * (double)start / CLOCKS_PER_SEC / i, i);
		
		system("pause");
	}
}
