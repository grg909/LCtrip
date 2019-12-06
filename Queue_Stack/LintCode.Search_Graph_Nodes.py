# -*- coding: UTF-8 -*-

# @Date    : 2019/12/5
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""

# Given a undirected graph, a node and a target, return the nearest
# node to given node which value of it is target, return NULL if you can't find.
#
# There is a mapping store the nodes' values in the given parameters.
#
# Notice
# It's guaranteed there is only one available solution
#
# Have you met this question in a real interview? Yes
#
# Example
# 2------3  5
#  \     |  |
#   \    |  |
#    \   |  |
#     \  |  |
#       1 --4
# Give a node 1, target is 50
#
# there a hash named values which is [3,4,10,50,50], represent:
# Value of node 1 is 3
# Value of node 2 is 4
# Value of node 3 is 10
# Value of node 4 is 50
# Value of node 5 is 50
#
# Return node 4

from collections import deque

class Solution:
    def searchNode(self, graph: List[Node], values: dict, node:'Node', target:int)->'Node':

        q = deque([node])
        seen = set()
        seen.add(node)

        while q:
            head = q.popleft()
            if values[head] == target:
                return head

            for nei in head.neighbors:
                if nei not in seen:
                    q.append(nei)
                    seen.add(nei)

        return None


# Follow up: 如何找到所有最近的value=target的点
# BFS分层
class Solution:
    def searchNode(self, graph: List[Node], values: dict, node:'Node', target:int)->List[Node]:

        q = deque([node])
        seen = set()
        seen.add(node)
        res = []

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if values[node] == target:
                    res.append(node)
                    for nei in node.neighbors:
                        if nei not in seen:
                            q.append(nei)
                            seen.add(nei)
            if res:
                return res

        return None


