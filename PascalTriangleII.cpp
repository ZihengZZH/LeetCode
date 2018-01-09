/*

Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?

*/

/*

The rows of Pascal's triangle are conventionally enumerated starting with row n = 0 
at the top (the 0th row). The entries in each row are numbered from the left beginning with k = 0 
and are usually staggered relative to the numbers in the adjacent rows. 
The triangle may be constructed in the following manner: In row 0 (the topmost row), 
there is a unique nonzero entry 1. Each entry of each subsequent row is constructed 
by adding the number above and to the left with the number above and to the right, 
treating blank entries as 0. For example, the initial number in the first (or any other) row is 1 (the sum of 0 and 1), 
whereas the numbers 1 and 3 in the third row are added to produce the number 4 in the fourth row.

			1
		1		1
	1		2		1
1		3		3		1

(n,k) = (n-1,k-1) + (n-1,k)

*/


#include <iostream>
#include <vector>
#include <numeric>
#include <functional>
#include <algorithm>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctime>


using namespace std;



// Nested vector is time-consuming
vector<int> getRow(int rowIndex) {

	vector<vector<int>> triangle;
	triangle.push_back({ 1 });
	triangle.push_back({ 1,1 });
	for (int i = 2; i <= rowIndex; i++) {
		vector<int> row(i + 1);
		row[0] = 1;
		row[i] = 1;
		for (int j = 1; j < i; j++) {
			row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j];
		}
		triangle.push_back(row);
	}
	if (rowIndex < 3)
		return triangle[rowIndex];
	else
		return triangle.back();

}


// A bit faster
vector<int> getRow_online(int rowIndex) {

	vector<int> vi(rowIndex + 1);
	vi[0] = 1;
	for (int i = 0; i <= rowIndex; i++) {
		for(int j = i; j > 0; --j) {
			vi[j] = vi[j] + vi[j - 1];
		}
	}
	return vi;
}


void displayVec(vector<int>& vec) {

	for (auto i : vec) {
		cout << i << "\t";
	}
	cout << endl;

}


int main() {

	/*COMPARISON OF TWO APPOARCHES*/

	clock_t begin = clock();
	for (int index = 0; index < 500; index++) {
		vector<int> result = getRow(index);
		//displayVec(result);
	}
	clock_t end = clock();
	double elapased_secs = double(end - begin) / CLOCKS_PER_SEC;
	cout << "RUNNING TIME " << elapased_secs << endl;

	begin = clock();
	for (int index = 0; index < 500; index++) {
		vector<int> result = getRow_online(index);
		//displayVec(result);
	}
	end = clock();
	elapased_secs = double(end - begin) / CLOCKS_PER_SEC;
	cout << "RUNNING TIME " << elapased_secs << endl;

	getchar();
	return 0;
	
}