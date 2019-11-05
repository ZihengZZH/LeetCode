'''

Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
    1
      \
        2
      /
    3

Output: [1,2,3]

'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root):
        self.order_list = []
        self.preorder(root)
        return self.order_list

    def preorder(self, root):
        if not root:
            return
        self.order_list.append(root.val)
        if root.left is not None:
            self.preorder(root.left)
        if root.right is not None:
            self.preorder(root.right)


if __name__ == '__main__':
    solu = Solution()

    # build a test tree
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    print(solu.preorderTraversal(root))