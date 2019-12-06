# -*- coding: UTF-8 -*-

# @Date    : 2019/12/6
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""

from collections import deque
"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


# 拓扑排序不是排序，而是一种基于依赖的遍历顺序(e.g.解锁课程)。Thinking process:
# 1. count and get indegree list of node
# 2. 从入度为0的点作为起始开始bfs
# 此解假定该图能够拓扑，否则需要判断再返回
class Solution1:
    """
    @param graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """

    def topSort(self, graph):
        node_to_indegree = self.get_indesgree(graph)

        # get start nodes: indegree == 0
        order = []
        start_nodes = [n for n in graph if node_to_indegree[n] == 0]
        q = deque(start_nodes)

        # bfs
        while q:
            node = q.popleft()
            order.append(node)
            for nei in node.neighbors:
                node_to_indegree[nei] -= 1
                if node_to_indegree[nei] == 0:
                    q.append(nei)

        return order

    def get_indegree(self, graph):
        node_to_indegree = {i: 0 for i in graph}

        for node in graph:
            for nei in node.neighbors:
                node_to_indegree[nei] += 1

        return node_to_indegree


# Follow up: 判断某图是否可拓扑排序（无环图都可以拓扑排序）
class Solution2:

    def isTopSort(self, graph):
        node_to_indegree = self.get_indesgree(graph)

        # get start nodes: indegree == 0
        start_nodes = [n for n in graph if node_to_indegree[n] == 0]
        count = 0
        q = deque(start_nodes)

        # bfs
        while q:
            node = q.popleft()
            count += 1
            for nei in node.neighbors:
                node_to_indegree[nei] -= 1
                if node_to_indegree[nei] == 0:
                    q.append(nei)

        return count == len(graph)

    def get_indegree(self, graph):
        node_to_indegree = {i: 0 for i in graph}

        for node in graph:
            for nei in node.neighbors:
                node_to_indegree[nei] += 1

        return node_to_indegree


# Follow up: 找出所有的拓扑排序：只能用DFS