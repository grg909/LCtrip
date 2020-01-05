# -*- coding: UTF-8 -*-

# @Date    : 2019/12/21
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 如果找到了就返回这个LCA
        # 如果只找到node1， 就返回node1
        # 如果只找到node2， 就返回node2
        # 如果都没有，就返回None
        if not root or root == p or root == q:
            return root

        # divide
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # conquer
        if left and right:
            return root
        if left:
            return left
        if right:
            return right

        return None