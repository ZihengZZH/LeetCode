'''

Given the root of a tree, you are asked to find the most frequent subtree sum. 
The subtree sum of a node is defined as the sum of all the node values formed by 
the subtree rooted at that node (including the node itself). 
So what is the most frequent subtree sum value? 
If there is a tie, return all the values with the highest frequency in any order.

Examples 1
Input:
  5
 /  \
2   -3
return [2, -3, 4], since all the values happen only once, return all of them in any order.

Examples 2
Input:
  5
 /  \
2   -5
return [2], since 2 happens twice, however -5 only occur once.

Note: You may assume the sum of values in any subtree is in the range of 32-bit signed integer.

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findFrequentTreeSum(self, root):
        # count for dictionary
        def add_dic(self, value):
            if value not in dic:
                dic[value] = 1
            else:
                dic[value] += 1

        # search the binary tree
        def search(self, root):
            if root:
                temp = root.val
                if root.left:
                    temp += search(self, root.left)
                if root.right:
                    temp += search(self, root.right)
                add_dic(self, temp) # attention
                return temp
            else:
                return 0

        dic, max_, res = {}, 0, []
        search(self, root)
        for i in dic:
            if dic[i] > max_:
                max_ = dic[i]
                res = [i]
            elif dic[i] == max_:
                res.append(i)
        return res


if __name__ == "__main__":
    node0 = TreeNode(5)
    node1 = TreeNode(2)
    node2 = TreeNode(-5)
    node0.left = node1
    node0.right = node2
    solu = Solution()
    print(solu.findFrequentTreeSum(node0))
    
