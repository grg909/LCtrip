# -*- coding: UTF-8 -*-

# @Date    : 2019/12/24
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


class Solution:
    """
    @param root: the root of binary tree.
    @return: true if it is a mirror of itself, or false.
    """

    def isSymmetric(self, root):
        if not root:
            return True

        return self.helper(root.left, root.right)

    def helper(self, left, right):
        if not left and not right:
            return True
        if left and right and left.val == right.val:
            return self.helper(left.left, right.right) and self.helper(
                left.right, right.left)
        return False
