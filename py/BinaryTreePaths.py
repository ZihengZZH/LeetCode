'''

Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

    1
  /   \
2      3
  \
    5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3

'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root):
        self.paths = []
        self.helper(root)
        return ['->'.join(x) for x in self.paths]
    
    def helper(self, root, path=[]):
        if root is None:
            return
        if not root.left and not root.right:
            self.paths.append(path + [str(root.val)])
        
        self.helper(root.left, path + [str(root.val)])
        self.helper(root.right, path + [str(root.val)])