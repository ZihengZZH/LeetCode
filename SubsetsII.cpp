/*

Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

*/

#include <iostream>
#include <vector>
#include <cmath>
#include <bitset>

using namespace std;

// If we want to insert an element which is a dup, we can only insert it 
// after the newly inserted elements from last step.
vector<vector<int> > subsetsWithDup(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    vector<vector<int> > res = {{}};
    for (int i = 0; i < nums.size(); ){
        int count = 0; // # elements are the same
        while (count + i < nums.size() && nums[count+i] == nums[i])
            count++;
        int previousN = res.size();
        for (int k = 0; k < previousN; k++){
            vector<int> instance = res[k];
            for (int j = 0; j < count; j++){
                instance.push_back(nums[i]);
                res.push_back(instance);
            }
        }
        i += count;
    }
    return res;
}


int main() {

    vector<int> input;
    input.push_back(1);
    input.push_back(2);
    input.push_back(2);
    vector<vector<int> > output = subsetsWithDup(input);
    cout << "ANSWER" << endl;
    for (int m = 0; m < output.size(); m++) {
        for (int n = 0; n < output[m].size(); n++){
            cout << output[m][n] << "\t";
        }
        cout << endl;
    }

    return 0;
} 