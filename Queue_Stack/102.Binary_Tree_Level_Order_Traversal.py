# -*- coding: UTF-8 -*-

# @Date    : 2019/12/4
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

    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        res = []
        if not root:
            return []

        q = deque([])
        q.append(root)

        while q:
            current_level = []
            for i in range(len(q)):
                head = q.popleft()
                current_level.append(head.val)
                if head.left:
                    q.append(head.left)
                if head.right:
                    q.append(head.right)

            res.append(current_level)

        return res
