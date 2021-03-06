/*

Given a binary tree, find the leftmost value in the last row of the tree.

	Example 1:
	Input:
		 2
		/ \
	   1   3
	Output:
		1

	Example 2:
	Input:
		 1
		/ \
	   2   3
	  /   / \
	 4   5   6
		/
	   7
	Output:
		7

Note: You may assume the tree (i.e., the given root node) is not NULL.

*/

#include "stdafx.h"
#include <iostream>
#include <iomanip>
#include <vector>

//Definition for a binary tree node.
struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

std::vector<std::pair<int, int>> last_row;

// display the binary tree
void display(TreeNode * current, int indent)
{
	if (current != nullptr) {
		display(current->left, indent + 4);
		if (indent > 0)
			std::cout << std::setw(indent) << " ";
		std::cout << current->val << std::endl;
		display(current->right, indent + 4);
	}
}

// display the vector of pair
void display_vec(std::vector<std::pair<int, int>>& temp)
{
	for (auto t : temp)
		std::cout << t.first << " " << t.second << std::endl;
}

// help function
void helper(TreeNode* node, int level)
{
	if (node == NULL)
		return;
	else if (node->left == NULL && node->right == NULL)
		last_row.push_back(std::make_pair(node->val, level));
	helper(node->left, level+1);
	helper(node->right, level+1);
}

int findBottomLeftValue(TreeNode* root) 
{
	helper(root, 1); // LEVEL SHOULD BE 1 OTHERWISE 1-LEVEL TREE WRONG
	std::pair<int, int> result = std::make_pair(0, 0);
	for (auto item : last_row)
	{
		if (item.second > result.second)
			result = item;
	}
	display_vec(last_row);
	return result.first;
}



int main()
{
	TreeNode leaf_1 = 1;
	TreeNode leaf_2 = 2;
	TreeNode leaf_3 = 3;
	TreeNode leaf_4 = 4;
	TreeNode leaf_5 = 5;
	TreeNode leaf_6 = 6;
	TreeNode leaf_7 = 7;
	TreeNode leaf_8 = 8;
	leaf_1.left = &leaf_2;
	leaf_1.right = &leaf_3;
	leaf_2.left = &leaf_4;
	leaf_3.left = &leaf_5;
	leaf_3.right = &leaf_6;
	leaf_5.left = &leaf_7;
	leaf_7.right = &leaf_8;

	// display the tree
	display(&leaf_1, 4);

	int result = findBottomLeftValue(&leaf_1);
	std::cout << "RESULT " << result << std::endl;

	getchar();
	return 0;
}

