/*

Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

*/


#include <vector>
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

bool isSameTree(TreeNode* p, TreeNode* q) {
	if (p == NULL || q == NULL) return (p == q);
	return (p->val == q->val && isSameTree(p->left, q->left) && isSameTree(p->right, q->right));
	// Recursive method to check all the nodes inside a tree
}

int main() {
	cout << "Begin\n";

	TreeNode first1(1);
	TreeNode first2(1);
	TreeNode first3(1);
	first1.left = &first2;
	first1.right = &first3;
	TreeNode secnd1(1);
	TreeNode secnd2(1);
	TreeNode secnd3(1);
	secnd1.left = &secnd2;
	secnd1.right = &secnd3;
	cout << "Result: " << isSameTree(&first1,&secnd1) << endl;

	system("pause");
}
