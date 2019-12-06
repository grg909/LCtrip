# -*- coding: UTF-8 -*-

# @Date    : 2019/12/6
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""

from collections import deque


class Solution:

    def canFinish(self, numCourses: int,
                  prerequisites: List[List[int]]) -> bool:

        graph = self.build_graph(numCourses, prerequisites)
        indegree = self.get_degree(numCourses, prerequisites)

        start_nodes = [n for n in graph.keys() if indegree[n] == 0]
        count = 0
        q = deque(start_nodes)

        while q:
            node = q.popleft()
            count += 1
            for edge in graph[node]:
                indegree[edge] -= 1
                if indegree[edge] == 0:
                    q.append(edge)

        return count == numCourses

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
