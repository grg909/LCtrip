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

    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return []

        res = []
        q = deque([root])
        flag = 0

        while q:
            current_layer = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    current_layer.append(node.val)

            # 插入时才改变每层顺序
            if current_layer:
                if flag:
                    current_layer = current_layer[::-1]
                res.append(current_layer)
                flag ^= 1

        return res
