# -*- coding: UTF-8 -*-

# @Date    : 2019/12/20
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""
    解题报告： 分治更简单直接，traverse需要维护全局变量
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Divide & Conquer, 数字是写代码时思考逻辑的顺序
class Solution1:

    def maxDepth(self, root: TreeNode) -> int:
        # 3. Edge case
        if not root:
            return 0

        # 1. Divide
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        # 2. Conquer
        return max(left, right) + 1


# Traverse, 需要维护全局变量
class Solution2:

    depth = 0

    def maxDepth(self, root: TreeNode) -> int:
        self.traverse(root, 1)
        return self.depth

    def traverse(self, node, curtDepth):
        if not node:
            return 0

        if curtDepth > self.depth:
            self.depth = curtDepth

        self.traverse(node.left, curtDepth + 1)
        self.traverse(node.right, curtDepth + 1)
