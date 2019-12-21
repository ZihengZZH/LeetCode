'''

INTERVIEW - 2.2

给定一棵二叉树，判定其是否对称 (Symmetric Tree)

二叉树 [1,2,2,3,4,4,3] 对称
      1
  2       2
3   4   4   3

二叉树 [1,2,2,null,3,null,3] 非对称
           1
     2           2
null    3   null    3

'''


class BTree(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    
    def height(self):
        if self.data is None:
            return 0 
        elif self.left is None and self.right is None:
            return 1
        elif self.left is None and self.right is not None:
            return 1 + self.right.height()
        elif self.left is not None and self.right is None:
            return 1 + self.left.height()
        else:
            return 1 + max(self.left.height(), self.right.height())
    
    def level_order(self):
        level_order = []
        if self.data is not None:
            level_order.append([self])
        height = self.height()
        if height >= 1:
            for _ in range(2, height + 1):
                level = []
                for node in level_order[-1]:
                    if node.left is not None:
                        level.append(node.left)
                    if node.right is not None:
                        level.append(node.right)
                if level:
                    level_order.append(level)
        for ii in range(0, height):
            for index in range(len(level_order[ii])):
                level_order[ii][index] = level_order[ii][index].data
        return level_order


def check_symmetric_tree(root):
    level_order = root.level_order()
    # print(level_order)
    for level in level_order:
        if level != level[::-1]:
            return False
    return True


if __name__ == "__main__":
    # build the tree from bottom to up
    left_tree = BTree(2)
    left_tree.left = BTree(3)
    left_tree.right = BTree(4)

    right_tree = BTree(2)
    right_tree.left = BTree(4)
    right_tree.right = BTree(3)

    tree = BTree(11)
    tree.left = left_tree
    tree.right = right_tree

    if check_symmetric_tree(tree):
        print("THE TREE IS SYMMETRIC")
    else:
        print("THE TREE IS NOT SYMMETRIC")