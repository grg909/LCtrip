# -*- coding: UTF-8 -*-

# @Date    : 2019/12/21
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""
    解题报告：Traverse的特点是不直接得到结果，
    而是用每层得到的值去更新全局变量
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
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """

    max_average = 0
    subtree = None

    def findSubtree2(self, root):
        self.helper(root)

        return self.subtree

    def helper(self, node):

        left_sum, left_num = self.helper(node.left)
        right_sum, right_num = self.helper(node.right)

        cur_sum = node.val + left_sum + right_sum
        num = left_num + right_num + 1
        average = cur_sum * 1.0 / num

        # 由于max_average初始化为0，不是极小值，所以第一次需要单独考虑
        if not self.subtree or average > self.max_average:
            self.max_average = average
            self.subtree = node

        return cur_sum, num
