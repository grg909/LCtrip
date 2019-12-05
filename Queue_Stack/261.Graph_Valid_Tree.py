# -*- coding: UTF-8 -*-

# @Date    : 2019/12/5
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""
    证明树的充要条件：1. n node, edge = n -1 2. 所有点联通
"""

# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a
# pair of nodes), write a function to check whether these edges make up a valid tree.
#
# For example:
#
# Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.
# Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.
#
# Hint:
#
# Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], what should your return? Is this case a valid tree?
# According to the definition of tree on Wikipedia: “a tree is an undirected graph in which any two vertices
# are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.”
# Note: you can assume that no duplicate edges will appear in edges. Since all edges are
# undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

# BFS
from collections import defaultdict, deque


class Solution(object):

    def validTree(self, n, edges):

        if len(edges) != n - 1:
            return False

        # 好的代码结构是代码自我解释，而不是靠注释
        neighbors = self.initialisGraph(edges)

        seen = set()
        q = deque([0])

        while q:
            curr = q.popleft()
            seen.add(curr)
            for node in neighbors[curr]:
                if node not in seen:
                    q.append(node)
                    seen.add(node)

        return len(seen) == n

    def initialisGraph(self, edges):
        """创建了邻接表（图的表现形式）"""
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        return graph
