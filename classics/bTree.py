# import dependency
from graphviz import Digraph


class BTree(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.dot = Digraph(comment='binary tree')
    
    # 前序遍历
    def preorder(self):
        if self.data is not None:
            print(self.data, end=' ')
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()
    
    # 中序遍历
    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        if self.data is not None:
            print(self.data, end=' ')
        if self.right is not None:
            self.right.inorder()
    
    # 后序遍历
    def postorder(self):
        if self.left is not None:
            self.left.postorder()
        if self.right is not None:
            self.right.postorder()
        if self.data is not None:
            print(self.data, end=' ')
    
    # 层序遍历
    def levelorder(self):
        
        # 返回某结点左
        def L_child(node):
            return node.left if node.left is not None else None
        # 返回某节点右
        def R_child(node):
            return node.right if node.right is not None else None
        
        # 层序遍历列表
        level_order = []
        # 添加根结点数据
        if self.data is not None:
            level_order.append([self])
        
        # 树的高度
        height = self.height()
        if height >= 1:
            # 在 level_order 中添加 node 而不是 data
            for _ in range(2, height + 1):
                level = []
                for node in level_order[-1]:
                    # 若左非空，则添加左
                    if L_child(node):
                        level.append(L_child(node))
                    # 若右非空，则添加右
                    if R_child(node):
                        level.append(R_child(node))
                # 若该层非空，则添加该层
                if level:
                    level_order.append(level)
        
        # 取出每个 node 的数据
        for ii in range(0, height):
            for index in range(len(level_order[ii])):
                level_order[ii][index] = level_order[ii][index].data
        
        return level_order

    # 二叉树高度 / 深度
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
    
    # 二叉树的叶子节点
    def leaves(self):
        if self.data is None:
            return None
        elif self.left is None and self.right is None:
            print(self.data, end=' ')
        elif self.left is None and self.right is not None:
            self.right.leaves()
        elif self.left is not None and self.right is None:
            self.left.leaves()
        else:
            self.left.leaves()
            self.right.leaves()

    # 翻转二叉树
    def invert(self, node):
        if node is None:
            return None
        # 调换左右子树
        tmp = node.left
        node.left = node.right
        node.right = tmp
        # 递归左右子树
        self.invert(node.left)
        self.invert(node.right)

    # 打印二叉树
    def print_tree(self, save_path='../images/binary_tree.gv', label=False):
        # import dependencies
        import uuid
        from random import sample

        # colors for labels of nodes
        colors = ['skyblue', 
                'tomato', 
                'orange', 
                'purple', 
                'green', 
                'yellow', 
                'pink', 
                'red']

        # 绘制以某个节点为根节点的二叉树
        def print_node(node, node_tag):
            # 节点颜色
            color = sample(colors,1)[0]
            if node.left is not None:
                left_tag = str(uuid.uuid1())        # 左节点的数据
                self.dot.node(left_tag, 
                            str(node.left.data), 
                            style='filled', 
                            color=color)            # 左节点
                label_string = 'L' if label else '' # 是否在连接线上写上标签，表明为左子树
                self.dot.edge(node_tag, 
                            left_tag, 
                            label=label_string)     # 左节点与其父节点的连线
                print_node(node.left, left_tag)

            if node.right is not None:
                right_tag = str(uuid.uuid1())
                self.dot.node(right_tag, 
                            str(node.right.data), 
                            style='filled', 
                            color=color)
                label_string = 'R' if label else '' # 是否在连接线上写上标签，表明为右子树
                self.dot.edge(node_tag, 
                            right_tag, 
                            label=label_string)
                print_node(node.right, right_tag)

        # 如果树非空
        if self.data is not None:
            root_tag = str(uuid.uuid1())            # 根节点标签
            self.dot.node(root_tag, 
                        str(self.data), 
                        style='filled', 
                        color=sample(colors,1)[0])  # 创建根节点
            print_node(self, root_tag)

        self.dot.format = 'png'
        self.dot.render(save_path)                  # 保存文件为指定文件


if __name__ == '__main__':
    # build the tree from bottom to up
    left_tree = BTree(5)
    left_tree.left = BTree(1)
    left_tree.right = BTree(3)

    right_tree = BTree(6)
    right_tree.left = BTree(2)
    right_tree.right = BTree(4)

    tree = BTree(11)
    tree.left = left_tree
    tree.right = right_tree

    left_tree = BTree(7)
    left_tree.left = BTree(3)
    left_tree.right = BTree(4)

    left_tree.left.left = BTree(12)
    left_tree.left.right = BTree(13)

    right_tree = tree
    tree = BTree(18)
    tree.left = left_tree
    tree.right = right_tree

    print("pre-ordering of the B-Tree")
    tree.preorder()
    print()

    print("in-ordering of the B-Tree")
    tree.inorder()
    print()

    print("post-ordering of the B-Tree")
    tree.postorder()
    print()

    print("level-ordering of the B-Tree")
    level_order = tree.levelorder()
    print(level_order)

    print("height of the B-Tree %d" % tree.height())

    print("child nodes")
    tree.leaves()
    print()

    # tree.print_tree(label=True)
    
    tree.invert(tree)
    tree.print_tree(save_path='../images/binary_tree_invert.gv',
                    label=True)