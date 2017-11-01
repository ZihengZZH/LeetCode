/*

Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

{ 'I',1 },{ 'V',5 },{ 'X',10 },{ 'L',50 },{ 'C',100 },{ 'D',500 },{ 'M',1000 }

*/

#include <unordered_map>
#include <iostream>
#include <string>

using namespace std;


// I(1) V(5) X(10) L(50) C(100) D(500) M(1000)
int romanToInt(string s) {
	int res = 0;
	if (s.empty()) return 0; // None input
	unordered_map<char, int> ht({ { 'I',1 },{ 'V',5 },{ 'X',10 },{ 'L',50 },{ 'C',100 },{ 'D',500 },{ 'M',1000 } });
	// Key-value pair, which is useful and powerful
	for (int i = 0; i < s.size(); i++) {
		if (ht.count(s[i]) == 0) return 0;
		res += ht[s[i]]; // Add corresponding value
		if (i != 0 && ht[s[i]] > ht[s[i - 1]])
			res -= 2 * ht[s[i - 1]]; // If order reversed, subtract twice
	}
	return res;
}

int main() {
	while (true){
		cout << "Input: ";
		string romn;
		cin >> romn;
		cout << "Output: " << romanToInt(romn) << endl;
		system("pause");
	}
}
