/*

You are playing a simplified Pacman game. You start at the point (0, 0), and your destination is (target[0], target[1]).
There are several ghosts on the map, the i-th ghost starts at (ghosts[i][0], ghosts[i][1]).

Each turn, you and all ghosts simultaneously *may* move in one of 4 cardinal directions:
north, east, west, or south, going from the previous point to a new point 1 unit of distance away.

You escape if and only if you can reach the target before any ghost reaches you (for any given moves the ghosts may take.)
If you reach any square (including the target) at the same time as a ghost, it doesn't count as an escape.

Return True if and only if it is possible to escape.

Example 1:
Input:
ghosts = [[1, 0], [0, 3]]
target = [0, 1]
Output: true
Explanation:
You can directly reach the destination (0, 1) at time 1, while the ghosts located at (1, 0) or (0, 3) have no way to catch up with you.

Example 2:
Input:
ghosts = [[1, 0]]
target = [2, 0]
Output: false
Explanation:
You need to reach the destination (2, 0), but the ghost at (1, 0) lies between you and the destination.

Example 3:
Input:
ghosts = [[2, 0]]
target = [1, 0]
Output: false
Explanation:
The ghost can reach the target at the same time as you.

Note:
All points have coordinates with absolute value <= 10000.
The number of ghosts will not exceed 100.

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

using namespace std;


void displayVec(vector<int>& vec) {
	for (auto v : vec) {
		cout << v << "\t";
	}
	cout << endl;
}

/* Original solution 6ms */

int distanceBetween(vector<int> ghost, vector<int> target) {
	if (ghost.size() != 2 || target.size() != 2)
		return INT_MAX;
	int dist = 0;
	for (int i = 0; i < 2; ++i) {
		dist += abs(ghost[i] - target[i]);
	}
	return dist;
}

bool escapeGhosts(vector<vector<int>>& ghosts, vector<int>& target) {
	int dist_ghost = INT_MAX;
	for (vector<vector<int>>::iterator iter = ghosts.begin(); iter != ghosts.end(); ++iter) {
		//displayVec(*iter);
		int dist = distanceBetween(*iter, target);
		if (dist < dist_ghost)
			dist_ghost = dist;
	}
	int dist_user = distanceBetween(vector<int>{0, 0}, target);
	if (dist_user < dist_ghost) {
		return true;
	}
	else {
		return false;
	}
}

/* Optimised solution 7ms */
/* However slower than original one*/

void distanceBetween_fast(vector<int> ghost, vector<int> target, int &dist) {
	if (ghost.size() != 2 || target.size() != 2)
		dist = INT_MAX;
	dist = 0;
	for (int i = 0; i < 2; ++i) {
		dist += abs(ghost[i] - target[i]);
	}
}

bool escapeGhosts_fast(vector<vector<int>>& ghosts, vector<int>& target) {
	int dist_user, dist_ghost;
	distanceBetween_fast(vector<int>{0, 0}, target, dist_user);
	for (vector<vector<int>>::iterator iter = ghosts.begin(); iter != ghosts.end(); ++iter) {
		distanceBetween_fast(*iter, target, dist_ghost);
		if (dist_ghost <= dist_user)
			return false;
	}
	return true;
}


int main() {
	vector<vector<int>> ghosts;
	ghosts.push_back(vector<int>{2, 0});
	ghosts.push_back(vector<int>{0, 3});
	vector<int> target = vector<int>{ 1, 0 };
	cout << "IT IS POSSIBLE TO ESCAPE " << boolalpha << escapeGhosts_fast(ghosts, target) << endl;

	getchar();
	return 0;
}
