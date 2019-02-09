'''

We are given the head node root of a binary tree, 
where additionally every node's value is either a 0 or a 1.
Return the same tree where every subtree (of the given tree) not containing a 1 has been removed.
(Recall that the subtree of a node X is X, plus every node that is a descendant of X.)

Example 1:
Input: [1,null,0,0,1]
Output: [1,null,0,null,1]
Explanation: Only the red nodes satisfy the property "every subtree not containing a 1".

Example 2:
Input: [1,0,1,0,0,0,1]
Output: [1,null,1,null,1]

Example 3:
Input: [1,1,0,1,1,0,1,0]
Output: [1,1,0,1,1,null,1]

Note:
The binary tree will have at most 100 nodes.
The value of each node will only be 0 or 1.

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return root
        root.left = self.pruneTree(root.left) 
        root.right = self.pruneTree(root.right) 
        # key criterion
        if root.val == 0 and root.left == None and root.right == None:
            return None
        return root


def display_tree(root, tree_lst):
    if root == None:
        return
    tree_lst.append(root.val)
    if root.left != None:
        display_tree(root.left, tree_lst)
    if root.right != None:
        display_tree(root.right, tree_lst)


if __name__ == "__main__":
    Node0 = TreeNode(1)
    Node0.left = TreeNode(0)
    Node0.left.left = TreeNode(0)
    Node0.left.right = TreeNode(0)
    Node0.right = TreeNode(1)
    Node0.right.left = TreeNode(0)
    Node0.right.right = TreeNode(1)

    tree_lst = []
    display_tree(Node0, tree_lst)
    print(tree_lst)

    solu = Solution()
    solu.pruneTree(Node0)

    tree_lst = []
    display_tree(Node0, tree_lst)
    print(tree_lst)