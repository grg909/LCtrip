# -*- coding: UTF-8 -*-

# @Date    : 2019/12/1
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""

# BFS， 此题非常好的训练代码结构
# Thinking process:
# 1. node -> nodes
# 2. copy nodes
# 3. copy edges
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':


# DFS
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        d = {}

        def dfs(old):
            if old not in d:
                # 每遍历一个新节点就创建一个副本到哈希表
                d[old] = new = Node(old.val, None)
                new.neighbors = [*map(dfs, old.neighbors)]
            return d[old]

        return dfs(node)
