# -*- coding: UTF-8 -*-

# @Date    : 2019/12/5
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

from collections import deque


class Solution:

    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return []

        res = deque([])
        q = deque([root])

        while q:
            current_layer = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    current_layer.append(node.val)
            if current_layer:
                res.appendleft(current_layer)

        return res
