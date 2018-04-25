/*

There are N students in a class. Some of them are friends, while some are not. 
Their friendship is transitive in nature. For example, if A is a direct friend of B, 
and B is a direct friend of C, then A is an indirect friend of C. 
And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. 
If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. 
And you have to output the total number of friend circles among all the students.

Example 1:
Input:
[[1,1,0],
[1,1,0],
[0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle.
The 2nd student himself is in a friend circle. So return 2.

Example 2:
Input:
[[1,1,0],
[1,1,1],
[0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends,
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.

Note:
N is in range [1,200].
M[i][i] = 1 for all students.
If M[i][j] = 1, then M[j][i] = 1.

*/


#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <numeric>
#include <functional>
#include <algorithm>
#include <math.h>
#include <ctime>
#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

using namespace std;

// Depth-first-search
void dfs(vector<vector<int>>& M, vector<int>& visited, int i) {
	for (int j = 0; j < M.size(); ++j) {
		if (M[i][j] == 1 && visited[j] == 0) {
			visited[j] = 1;
			dfs(M, visited, j);
		}
	}
}

// Similar as finding connected components in un-directed graph
// Traverse half the matrix and record the visited element
int findCircleNum(vector<vector<int>>& M) {
	vector<int> visited = vector<int>(M.size());
	int count = 0;
	for (int i = 0; i < M.size(); ++i) {
		// Only check un-visited
		if (visited[i] == 0) {
			dfs(M, visited, i);
			count++;
		}
	}
	return count;
}

int main() {

	vector<vector<int>> lst;
	lst.push_back({ 1,0,0,0 });
	lst.push_back({ 0,1,0,0 });
	lst.push_back({ 0,0,1,0 });
	lst.push_back({ 0,0,0,1 });

	int i, output;

	cout << "INPUT ";
	clock_t begin_time = clock();
	clock_t end_time = begin_time + CLOCKS_PER_SEC;
	for (i = 0; clock() < end_time; i++) {
		output = findCircleNum(lst);
	}
	cout << "OUTPUT " << output << endl;
	printf("%f ms (%d trials)\n", 1000 * (double)begin_time / CLOCKS_PER_SEC / i, i);

	getchar();
	return 0;
}
