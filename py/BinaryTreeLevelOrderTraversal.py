'''

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7

return its level order traversal as:
[
    [3],
    [9,20],
    [15,7]
]

'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root):
        
        def L_child(node):
            return node.left if node.left is not None else None
        
        def R_child(node):
            return node.right if node.right is not None else None
        
        level_order = []
        if root:
            level_order.append([root])
        
        height = self.height(root)
        if height >= 1:
            for _ in range(2, height+1):
                level = []
                for node in level_order[-1]:
                    if L_child(node):
                        level.append(L_child(node))
                    if R_child(node):
                        level.append(R_child(node))
                if level:
                    level_order.append(level)
        
        for ii in range(0, height):
            for index in range(len(level_order[ii])):
                level_order[ii][index] = level_order[ii][index].val

        return level_order
    
    def height(self, root):
        if not root:
            return 0
        elif root.left is None and root.right is None:
            return 1
        elif root.left is None and root.right is not None:
            return 1 + self.height(root.right)
        elif root.left is not None and root.right is None:
            return 1 + self.height(root.left)
        else:
            return 1 + max(self.height(root.left), self.height(root.right))