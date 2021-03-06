# -*- coding: UTF-8 -*-

# @Date    : 2019/12/20
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""
    解题报告：如果divide conquer实现起来不容易，
    结合traverse来实现会是更好选择。
    Traverse的特点是不直接得到结果，而是用每层得到的值去更新全局变量
"""

import sys
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


# Divide conquer + Traverse
class Solution1:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    min_sum = sys.maxsize
    subtree = None

    def findSubtree(self, root):
        # write your code here
        self.helper(root)

        return self.subtree

    def helper(self, root):
        if not root:
            return 0

        left_sum = self.helper(root.left)
        right_sum = self.helper(root.right)
        root_weight = left_sum + right_sum + root.val

        if root_weight < self.min_sum:
            self.min_sum = root_weight
            self.subtree = root

        return root_weight


# Pure divide conquer
class Solution2:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """

    def findSubtree(self, root):
        # write your code here
        sum, mini, subtree = self.helper(root)
        return subtree

    def helper(self, root):

        left_sum, left_mini, left_subtree = self.helper(root.left)
        right_sum, right_mini, right_subtree = self.helper(root.right)

        sum = left_sum + right_sum + root.val
        if left_mini == min(sum, left_mini, right_mini):
            return sum, left_mini, left_subtree
        if right_mini == min(sum, left_mini, right_mini):
            return sum, right_mini, right_subtree

        return sum, sum, root
