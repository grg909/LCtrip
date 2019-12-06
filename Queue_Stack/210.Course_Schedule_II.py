# -*- coding: UTF-8 -*-

# @Date    : 2019/12/6
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""

from collections import deque


# Tinking process:
# 1. no graph presentation: so build graph first
# 2. count and get the indegree of nodes
# 3. BFS topological sorting
# 4. if the graph can be topological sort, then return the order
class Solution:

    def findOrder(self, numCourses: int,
                  prerequisites: List[List[int]]) -> List[int]:

        graph = self.build_graph(numCourses, prerequisites)
        indegree = self.get_degree(numCourses, prerequisites)

        start_nodes = [n for n in graph if indegree[n] == 0]
        q = deque(start_nodes)
        order = []
        count = 0

        while q:
            node = q.popleft()
            order.append(node)
            count += 1
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        if count == numCourses:
            return order
        else:
            return []

    def get_degree(self, numCourses, prerequisites):
        indegree = [0] * numCourses

        for edge in prerequisites:
            indegree[int(edge[0])] += 1

        return indegree

    def build_graph(self, numCourses, prerequisites):
        graph = {i: [] for i in range(numCourses)}

        for edge in prerequisites:
            graph[int(edge[1])].append(edge[0])

        return graph
