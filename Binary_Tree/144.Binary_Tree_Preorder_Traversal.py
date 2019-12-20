# -*- coding: UTF-8 -*-

# @Date    : 2019/12/19
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""
    解题报告：非递归方法必须默写到bug free。
    分治算法，解决90%的binary tree问题
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Recursion 1: Traverse
class Solution1:

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.traverse(root, res)
        return res

    def traverse(self, root, res):
        if not root:
            return

        res.append(root.value)
        self.traverse(root.left, res)
        self.traverse(root.right, res)


# Recursion 2: Divide & Conquer
class Solution2:

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        # null or leaf
        if not root:
            return res

        # Divide
        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)

        # Conquer
        res.append(root.val)
        res.extend(left)
        res.extend(right)

        return res


# Non-recursion. Stack
class Solution3:

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        cur = root
        stack = []
        while stack or cur:
            if cur:
                stack.append(cur)
                res.append(cur.val)  # add before going to children
                cur = cur.left
            else:
                node = stack.pop()
                cur = node.right
        return res
