# -*- coding: UTF-8 -*-

# @Date    : 2019/12/6
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""
    解题报告：解法1的返回很巧妙
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution1:

    def flatten(self, root: TreeNode) -> None:
        self.helper(root)

    # restructure and return last node in preorder
    def helper(self, root):
        if not root:
            return None

        left_end = self.helper(root.left)
        right_end = self.helper(root.right)

        if left_end:
            left_end.right = root.right
            root.right = root.left
            root.left = None

        return right_end or left_end or root


# Traverse
class Solution2:

    last_node = None

    def flatten(self, root: TreeNode) -> None:
        if not root:
            return

        if self.last_node:
            self.last_node.left = None
            self.last_node.right = root

        self.last_node = root
        # 因为在进行self.flatten(root.left)的时候 root.right会发生改变
        # （在flatten root.left中 last_node是现在的root，而在flatten root.left中
        # last_node.right会变化，即对应现在的root.right也会发生变化）
        right = root.right
        self.flatten(root.left)
        self.flatten(right)
