'''

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
    1
   / \
  2   2
 / \ / \
3  4 4  3

But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3

Note:
Bonus points if you could solve it both recursively and iteratively.

'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def helper_left(self, left):
        result = []
        if left is None:
            result.append('x') # Necessary for one branch empty
            return result
        result.append(left.val)
        result += self.helper_left(left.left)
        result += self.helper_left(left.right)
        return result

    def helper_right(self, right):
        result = []
        if right is None:
            result.append('x') # Necessary for one branch empty
            return result
        result.append(right.val)
        result += self.helper_right(right.right)
        result += self.helper_right(right.left)
        return result

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper_left(root) == self.helper_right(root)


if __name__ == "__main__":
    tree1 = TreeNode(1)
    tree2 = TreeNode(2)
    tree3 = TreeNode(2)
    tree4 = TreeNode(3)
    tree5 = TreeNode(3)
    tree6 = TreeNode(4)
    tree7 = TreeNode(4)
    tree1.left = tree2
    tree1.right = tree3
    tree2.left = tree4
    tree2.right = tree6
    tree3.left = tree7
    tree3.right = tree5
    solu = Solution()
    print(solu.isSymmetric(tree1))
