/*

Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:
  *The root is the maximum number in the array.
  *The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
  *The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.

Example 1:
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    / 
     2  0   
       \
        1

Note:
The size of the given array will be in the range [1,1000].

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


struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

void display(TreeNode* current, int indent)
{
	if (current != nullptr) {
		display(current->left, indent + 4);
		if (indent > 0)
			cout << setw(indent) << " ";
		cout << current->val << endl;
		display(current->right, indent + 4);
	}
}

/*
THIS METHOD IS INCREDIBLE
Follow single direction to add nodes on a tree
While later number is bigger, keep assigning left node and poping back elements until ends
If later number is no bigger, assign right
Push back current element into vector
*/

TreeNode* constructMaximumBinaryTree(vector<int>& nums) {
	vector<TreeNode*> vec;
	for (int i = 0; i < nums.size(); i++) {
		TreeNode*cur = new TreeNode(nums[i]);
		while (!vec.empty() && vec.back()->val < nums[i]) {
			cur->left = vec.back();
			vec.pop_back();
		}
		if (!vec.empty())
			vec.back()->right = cur;
		vec.push_back(cur);
	}
	return vec.front();
	
}


int main() {
	while (true) {
		clock_t start;
		clock_t stop;
		int i;
		
		vector<int> nums = { 4,3,2,11,6,0,5,7,2,5,10 };
		TreeNode *begin = constructMaximumBinaryTree(nums);
		display(begin, 0);
		

		/*
		start = clock();
		stop = start + CLOCKS_PER_SEC;
		for (i = 0; clock() < stop; i++) {
			
		}

		cout << "AFTER INSERTATION\n";
		display(&leaf_1, 0);

		printf("%f ms (%d trials)\n", 1000 * (double)start / CLOCKS_PER_SEC / i, i);
		*/

		system("pause");
	}
}
