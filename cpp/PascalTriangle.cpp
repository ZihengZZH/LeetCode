/*

Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

*/


#include <vector>
#include <bitset>
#include <iostream>
#include <string>
#include <algorithm>
#include <time.h>
#include <sstream>

using namespace std;


vector<int> iter(vector<int>& lst) {
	vector<int> res = {};
	int len = lst.size() + 1;
	for (int i = 0; i < len; i++) {
		if (i == 0 || i == len - 1) {
			res.push_back(1);
		}
		else {
			res.push_back(lst[i - 1] + lst[i]);
		}
	}
	return res;
}

vector<vector<int>> generate(int numRows) {
	vector<vector<int>> res;
	vector<int> temp = { 1 };
	for (int i = 0; i < numRows; i++) {
		res.push_back(temp);
		temp = iter(temp);
	}
	return res;
}


int main() {
	while (true) {
		clock_t start;
		clock_t stop;
		int i, input = 10;
		vector<vector<int>> output = {};
		vector<int>::iterator it;
		vector<vector<int>>::iterator iter;
		vector<int> vec_tmp;

		start = clock();
		stop = start + CLOCKS_PER_SEC;
		for (i = 0; clock() < stop; i++) {
			output = generate(input);
		}
		start = clock() - start;
		cout << "All the non-duplicate subsets are as follows " << endl;
		cout << "Use iterator : " << endl;
		
		for (iter = output.begin(); iter != output.end(); iter++){
			vec_tmp = *iter;
			cout << " [";
			for (it = vec_tmp.begin(); it != vec_tmp.end(); it++)
				cout << *it << ",";
			cout << "] " << endl;
		}

		printf(" %f ms (%d trials)\n", 1000 * (double)start / CLOCKS_PER_SEC / i, i);

		system("pause");
	}
}

/*
[], [], [], [], [], [], [], []
[], [1], [], [1], [], [1], [], [1]
[], [1], [2], [1, 2], [], [1], [2], [1, 2]
[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]
*/
