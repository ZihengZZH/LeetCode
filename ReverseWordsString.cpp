/*

Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

*/


#include <iostream>
#include <string>
#include <vector>
#include <numeric>
#include <functional>
#include <algorithm>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctime>


using namespace std;


void reverseWord(string &s, int i, int j) {
	while (i < j) {
		char t = s[i];
		s[i++] = s[j];
		s[j--] = t;
	}
}

void reverseWords(string &s) {
	int i = 0, j = 0, l = 0;
	int len = s.length();
	int wordcount = 0;

	while (true) {
		while (i < len&&s[i] == ' ')
			i++;
		if (i == len)
			break;
		if (wordcount)
			s[j++] = ' ';
		l = j;
		while (i < len&&s[i] != ' ') {
			s[j] = s[i];
			j++;
			i++;
		}
		reverseWord(s, l, j - 1);
		wordcount++;
	}

	s.resize(j);
	reverseWord(s, 0, j - 1);
}



int main() {

	string input = "haha is always late for the class";
	cout << "INPUT " << input << endl;

	reverseWords(input);
	cout << "OUTPUT " << input << endl;

	getchar();
	return 0;
	
}