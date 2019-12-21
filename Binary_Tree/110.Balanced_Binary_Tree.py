# -*- coding: UTF-8 -*-

# @Date    : 2019/12/21
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""
    解题报告： 如果D&C函数返回值不足够进行迭代
    那就用helper函数，可以返回多个值进行处理
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def isBalanced(self, root: TreeNode) -> bool:

        balanced, _ = self.validate(root)
        return balanced

    def validate(self, root):
        if not root:
            return True, 0

        balanced, left_h = self.validate(root.left)
        if not balanced:
            return False, 0
        balanced, right_h = self.validate(root.right)
        if not balanced:
            return False, 0

        return abs(left_h - right_h) <= 1, max(left_h, right_h) + 1
