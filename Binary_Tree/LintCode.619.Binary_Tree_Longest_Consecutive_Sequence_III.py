# -*- coding: UTF-8 -*-

# @Date    : 2020/1/2
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""
"""
Definition for a multi tree node.
class MultiTreeNode(object):
    def __init__(self, x):
        self.val = x
        children = [] # children is a list of MultiTreeNode
"""


class Solution:
    # @param {MultiTreeNode} root the root of k-ary tree
    # @return {int} the length of the longest consecutive sequence path
    def longestConsecutive3(self, root):
        _, _, max_len = self.helper(root)
        return max_len

    def helper(self, root):
        if not root:
            return 0, 0, 0

        up, down, max_len = 0, 0, 0
        for child in root.children:
            result = self.helper(child)
            max_len = max(max_len, result[0])
            if child and child.val + 1 == root.val:
                down = max(down, result[1] + 1)
            if child and child.val - 1 == root.val:
                up = max(up, result[2] + 1)

        max_len = max(down + 1 + up, max_len)

        return max_len, down, up
