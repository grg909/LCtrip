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

from collections import deque


# BFS， 此题适合训练代码结构
# Thinking process:
# 1. node -> nodes
# 2. copy nodes
# 3. copy edges
class Solution:

    def cloneGraph(self, node: 'Node') -> 'Node':
        root = node
        if node is None:
            return node

        # use bfs to traverse the graph and get all old nodes
        nodes = self.getNodes(node)

        # copy nodes, create a mapping dict from old->new
        mapping = {}
        for node in nodes:
            mapping[node] = Node(node.val, [])

        # copy edges
        for node in nodes:
            new_node = mapping[node]
            for neighbor in node.neighbors:
                new_neighbor = mapping[neighbor]
                new_node.neighbors.append(new_neighbor)

        return mapping[root]

    def getNodes(self, node: 'Node') -> 'set':
        results = set([node])
        q = deque([node])
        while q:
            head = q.popleft()
            for neighbor in head.neighbors:
                if neighbor not in results:
                    results.add(neighbor)
                    q.append(neighbor)
        return results
