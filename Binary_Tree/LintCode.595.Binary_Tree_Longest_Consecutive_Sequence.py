# -*- coding: UTF-8 -*-

# @Date    : 2020/1/2
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


# Traverse + divide conquer
class Solution:
    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """

    def longestConsecutive(self, root):
        # write your code here
        return self.helper(root, None, 0)

    def helper(self, root, parent, len):
        if not root:
            return len

        if parent and root.val == parent.val + 1:
            len += 1
        else:
            len = 1

        left = self.helper(root.left, root, len)
        right = self.helper(root.right, root, len)

        return max(left, right)
