'''

Given a binary tree and a sum, 
determine if the tree has a root-to-leaf path 
such that adding up all the values along the path 
equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        if not root:
            return False
        if not root.left and not root.right and root.val == sum:
            return True
        sum -= root.val
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)


if __name__ == "__main__":
    node0 = TreeNode(5)
    node1 = TreeNode(4)
    node2 = TreeNode(8)
    node3 = TreeNode(11)
    node4 = TreeNode(13)
    node5 = TreeNode(4)
    node6 = TreeNode(7)
    node7 = TreeNode(2)
    node8 = TreeNode(1)
    node0.left = node1
    node0.right = node2
    node1.left = node3
    node3.left = node6
    node3.right = node7
    node2.left = node4
    node2.right = node5
    node5.right = node8
    solu = Solution()
    print("ANSWER",solu.hasPathSum(node0, 22))
    # 22 -> True; 23 -> False
