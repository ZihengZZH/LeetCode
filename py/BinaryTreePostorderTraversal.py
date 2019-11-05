'''

Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
    1
      \
        2
      /
    3

Output: [3,2,1]

'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root):
        self.order_list = []
        self.postorder(root)
        return self.order_list

    def postorder(self, root):
        if not root:
            return
        if root.left is not None:
            self.postorder(root.left)
        if root.right is not None:
            self.postorder(root.right)
        self.order_list.append(root.val)


if __name__ == '__main__':
    solu = Solution()

    # build a test tree
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    print(solu.postorderTraversal(root))