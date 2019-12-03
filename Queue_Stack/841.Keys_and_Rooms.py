# -*- coding: UTF-8 -*-

# @Date    : 2019/12/3
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""
from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = {0}

        # 创建队列放入根节点
        q = deque([0])

        while q:
            cur = q.popleft()

            for i in set(rooms[cur]):
                if i not in seen:  # 邻剪枝
                    seen.add(i)
                    q.append(i)

        return len(seen) == len(rooms)