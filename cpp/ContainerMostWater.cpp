/*

Given n non-negative integers a1, a2, ..., an, 
where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

*/

#include <vector>
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int maxArea(vector<int>& height) {
	int res = 0;
	int i = 0, j = height.size() - 1;
	while (i < j) {
		int h = min(height[i], height[j]); // The smaller height determins area 
		res = max(res, (j - i)*h); // Calculate & iterate the max area
		while (height[i] <= h && i < j) i++;
		while (height[j] <= h && i < j) j--;
		// Traverse element with single direction
		// Narrow down domain based on height and long
	}
	return res;
}

int main() {
	while (true){
		cout << "Input: \n";
		vector<int> str = {4,6,10,1,3,1,7};
		cout << "Output: " << maxArea(str) << endl;
		system("pause");
	}
}
