# -*- coding: UTF-8 -*-

# @Date    : 2019/12/19
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""
    解题报告： 时间复杂度和空间复杂度
"""

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursion 1: Traverse
# 类似preorder，见前

# Recursion 2: Divide & Conquer
# 类似preorder，见前


# 反转先序遍历，非递归
class Solution1:

    def postorderTraversal(self, root: TreeNode) -> List[int]:
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

        res.reverse()

        return res


# use deque
class Solution2:

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = deque([])

        cur = root
        stack = []
        while stack or cur:
            if cur:
                stack.append(cur)
                res.appendleft(cur.val)  # reverse process of preorder
                cur = cur.right
            else:
                node = stack.pop()
                cur = node.left

        return res
