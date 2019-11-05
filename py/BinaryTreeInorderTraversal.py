'''

Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
    1
      \
        2
      /
    3

Output: [1,3,2]

'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root):
        self.order_list = []
        self.inorder(root)
        return self.order_list

    def inorder(self, root):
        if not root:
            return
        if root.left is not None:
            self.inorder(root.left)
        self.order_list.append(root.val)
        if root.right is not None:
            self.inorder(root.right)


if __name__ == '__main__':
    solu = Solution()

    # build a test tree
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    print(solu.inorderTraversal(root))