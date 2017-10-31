/*

You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]
Answer: 16

*/

#include <vector>
#include <bitset>
#include <iostream>
#include <iomanip>
#include <string>
#include <algorithm>
#include <time.h>
#include <sstream>
using namespace std;


int islandPerimeter(vector<vector<int>>& grid) {
	int count = 0, nei = 0;
	for (int i = 0; i < grid.size(); i++) {
		for (int j = 0; j < grid[i].size(); j++) {
			if (grid[i][j] == 1) {
				count++;
				if (i < grid.size() - 1 && grid[i + 1][j] == 1) nei++; // Check the point below
				if (j < grid[i].size() - 1 && grid[i][j + 1] == 1) nei++; // Check the point on the right
			}
		}
	}
	return (4 * count - 2 * nei);
}


int main() {
	while (true) {
		clock_t start;
		clock_t stop;
		vector<vector<int>> nums = {{0,1,0,0},
		{1,1,1,0},
		{0,1,0,0},
		{1,1,0,0}};
		int input_k = 2, i;
		int output;
		

		start = clock();
		stop = start + CLOCKS_PER_SEC;
		for (i = 0; clock() < stop; i++) {
			output = islandPerimeter(nums);
		}

		cout << "ANSWER IS " << output << endl;
		printf("\n%f ms (%d trials)\n", 1000 * (double)start / CLOCKS_PER_SEC / i, i);


		system("pause");
	}
}

