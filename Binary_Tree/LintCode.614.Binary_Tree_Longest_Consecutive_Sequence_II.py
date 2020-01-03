# -*- coding: UTF-8 -*-

# @Date    : 2020/1/2
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {int} the length of the longest consecutive sequence path
    def longestConsecutive2(self, root):
        max_len, _, _ = self.helper(root)
        return max_len

    def helper(self, root):
        if not root:
            return 0, 0, 0

        left_len, left_down, left_up = self.helper(root.left)
        right_len, right_down, right_up = self.helper(root.right)

        down, up = 0, 0
        if root.left and root.left.val + 1 == root.val:
            down = left_down + 1
        if root.left and root.left.val - 1 == root.val:
            up = left_up + 1
        if root.right and root.right.val + 1 == root.val:
            down = max(down, right_down + 1)
        if root.right and root.right.val - 1 == root.val:
            up = max(up, right_up + 1)

        len = down + 1 + up
        len = max(len, left_len, right_len)

        return len, down, up
