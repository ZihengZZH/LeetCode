/*

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

*/

#include <iostream> 
#include <vector>
#include <string>
#include <time.h>

using namespace std;


int maxSubArray(vector<int>& nums) {
	int ans=nums[0],sum=0,n=nums.size();
	for(int i=0;i<n;i++){
		sum+=nums[i];
		ans=max(sum,ans);
		sum=max(sum,0);
	}
	return ans;
}


int main(int argc, char** argv){
	clock_t start;
	clock_t stop;
	int i,output;
	static const int arr[] = {-2,1,-3,4,-1,2,1,-5,4};
	vector<int> input_num (arr, arr + sizeof(arr) / sizeof(arr[0]));

	start = clock();
	stop = start + CLOCKS_PER_SEC;
	for (i = 0; clock() < stop; i++) {
		output = maxSubArray(input_num);
	}

	cout << "ANSWER IS " << output;
		
	printf("\n%f ms (%d trials)\n", 1000 * (double)start / CLOCKS_PER_SEC / i, i);


	system("pause");
}


