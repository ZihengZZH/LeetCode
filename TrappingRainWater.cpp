/*

Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
http://www.leetcode.com/static/images/problemset/rainwatertrap.png

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

*/


#include <iostream> 
#include <string>
#include <vector>

using namespace std;

int trap(vector<int>& height) {
    int secHeight=0, left=0, right=height.size()-1, area=0;
    while (left < right){
        if (height[left] < height[right]){
            secHeight = max(height[left],secHeight);
            area += secHeight - height[left];
            left++;
        }else{
            secHeight = max(height[right],secHeight);
            area += secHeight - height[right];
            right--;
        }
    } // check all elements from two-ended-point
    // calculate the area with secHeight subtracting current height
    return area;
}


int main(){
    cout << "Enter xxx ";
        clock_t start;
		clock_t stop;
		int i, output;
        vector<int> input = {0,1,2,2,1,0,1,3,2,1,2,1};
		
		start = clock();
		stop = start + CLOCKS_PER_SEC;
		for (i = 0; clock() < stop; i++) {
            output = trap(input);
		}
		start = clock() - start;
		cout << "The result is " << output << endl;
		printf(" %f ms (%d trials)\n", 1000 * (double)start / CLOCKS_PER_SEC / i, i);
}
