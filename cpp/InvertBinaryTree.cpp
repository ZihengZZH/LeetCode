/*

Invert a binary tree.
     4
   /   \
  2     7
 / \   / \
1   3 6   9

to
     4
   /   \
  7     2
 / \   / \
9   6 3   1

Trivia:
This problem was inspired by this original tweet by Max Howell:
Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so fuck off.

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

TreeNode* invertTree(TreeNode* root) {
	if (root->right == NULL || root->left == NULL) {
		return 0;
	} // MAYBE something is wrong here

	invertTree(root->left);
	invertTree(root->right);

	TreeNode *leaf_temp = nullptr;
	leaf_temp = root->left;
	root->left = root->right;
	root->right = leaf_temp;
	
}

TreeNode* invertTree2(TreeNode* root) {
	if (root) {
		invertTree(root->left);
		invertTree(root->right);
		swap(root->left, root->right);
	}
	return root;
}

void display(TreeNode *current, int indent)
{
	if (current != nullptr)
	{
		display(current->left, indent + 4);
		if (indent > 0)
			cout << setw(indent) << " ";
		cout << current->val << endl;
		display(current->right, indent + 4);
	}
}


int main() {
	while (true) {
		clock_t start;
		clock_t stop;
		int i;
		TreeNode leaf_1 = 1;
		TreeNode leaf_2 = 2;
		TreeNode leaf_3 = 3;
		TreeNode leaf_4 = 4;
		TreeNode leaf_6 = 6;
		TreeNode leaf_7 = 7;
		TreeNode leaf_9 = 9;
		leaf_4.left = &leaf_2;
		leaf_4.right = &leaf_7;
		leaf_2.left = &leaf_1;
		leaf_2.right = &leaf_3;
		leaf_7.left = &leaf_6;
		leaf_7.right = &leaf_9;
		// ABOVE ALL is TREE INITIALIZATION
		

		cout << "BEFORE INSERTATION\n";
		display(&leaf_4,0);
		start = clock();
		stop = start + CLOCKS_PER_SEC;
		for (i = 0; clock() < stop; i++) {
			invertTree(&leaf_4);
		}
		cout << "AFTER INSERTATION\n";
		display(&leaf_4, 0);
		printf(" %f ms (%d trials)\n", 1000 * (double)start / CLOCKS_PER_SEC / i, i);
		

		cout << "BEFORE INSERTATION\n";
		display(&leaf_4, 0);
		start = clock();
		stop = start + CLOCKS_PER_SEC;
		for (i = 0; clock() < stop; i++) {
			invertTree2(&leaf_4);
		}
		cout << "AFTER INSERTATION\n";
		display(&leaf_4, 0);
		printf(" %f ms (%d trials)\n", 1000 * (double)start / CLOCKS_PER_SEC / i, i);

		system("pause");
	}
}
