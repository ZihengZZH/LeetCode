'''

Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path 
from the root node down to the farthest leaf node.

'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):
        depth = 1
        if root.left is not None:
            depth += self.maxDepth(root.left)
        elif root.right is not None:
            depth += self.maxDepth(root.right)
        elif root.left is None and root.right is None:
            return depth
        return depth

    def maxDepth_online(self, root):
        if root is None:
            return 0
        leftDepth = self.maxDepth_online(root.left)
        rightDepth = self.maxDepth_online(root.right)
        return (max(leftDepth, rightDepth)+1)


if __name__ == "__main__":
    node0 = TreeNode(0)
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node0.left = node1
    node0.right = node2
    node1.left = node3
    node3.right = node4
    node2.left = node4
    node4.right = node5
    solu = Solution()
    max_1 = solu.maxDepth(node0)
    print("MAX DEPTH", max_1)
    max_online = solu.maxDepth_online(node0)
    print("MAX DEPTH", max_online)