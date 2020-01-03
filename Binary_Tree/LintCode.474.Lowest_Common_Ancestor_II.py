# -*- coding: UTF-8 -*-

# @Date    : 2020/1/2
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""
"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""


# 将两个结点移动到相同的高度，然后同时向上移动，直到移动到相同的点
class Solution:
    """
    @param: root: The root of the tree
    @param: A: node in the tree
    @param: B: node in the tree
    @return: The lowest common ancestor of A and B
    """

    def lowestCommonAncestorII(self, root, A, B):
        dic = {}
        while A is not root:
            dic[A] = True
            A = A.parent

        while B is not root:
            if B in dic:
                return B
            B = B.parent

        return root
