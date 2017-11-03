/*

You need to find the largest value in each row of a binary tree.

Example:
Input: 

          1
         / \
        3   2
       / \   \  
      5   3   9 

Output: [1, 3, 9]

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

vector<int> biTree;

struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

/*
void traverse(TreeNode* current, int level) {
	if (current != nullptr) {
		biTree.push_back({ current->val,level });
		traverse(current->left, level + 1);
		traverse(current->right, level + 1);
	}
}
*/

void helper(TreeNode* node, int cl) {
	if (node == NULL)
		return;
	if (biTree.size() < (cl + 1)) {
		biTree.push_back(node->val);
	}
	else {
		if (biTree[cl] < node->val)
			biTree[cl] = node->val;
	}
	helper(node->left, cl + 1);
	helper(node->right, cl + 1);
}

vector<int> largestValues(TreeNode* root) {
	if (root == NULL)
		return biTree;
	helper(root, 0);
	return biTree;

	/*
	for (vector<vector<int>>::iterator iter = biTree.begin(); iter != biTree.end(); iter++) {
		vector<int> temp_vect = *iter;
		cout << "SIZE " << temp_vect.size() << endl;
		for (vector<int>::iterator it = temp_vect.begin(); it != temp_vect.end(); it++) {
			cout << *it << " ";
		}
		cout << endl;
	}
	*/

	/*
	for (auto bitree : biTree) {
		for (auto tree : bitree) {
			cout << tree << " ";
		}
		cout << endl;
	}
	*/

}

void display(TreeNode * current, int indent)
{
	if (current != nullptr) {
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
		TreeNode leaf_5 = 5;
		TreeNode leaf_6 = 6;
		TreeNode leaf_8 = 8;
		TreeNode leaf_9 = 9;
		leaf_1.left = &leaf_3;
		leaf_1.right = &leaf_2;
		leaf_3.left = &leaf_5;
		leaf_3.right = &leaf_8;
		leaf_2.right = &leaf_9;
		// ABOVE ALL is TREE INITIALIZATION
		
		cout << "BEFORE INSERTATION\n";
		display(&leaf_1, 0);

		vector<int> outputs = largestValues(&leaf_1);

		for (auto output : outputs) {
			cout << output << " ";
		}

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
