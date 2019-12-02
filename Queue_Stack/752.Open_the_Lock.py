# -*- coding: UTF-8 -*-

# @Date    : 2019/12/1
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""

from collections import deque


class Solution:

    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)  # in 操作在set中时间复杂度为O(1)
        begin = set()
        end = set()
        if '0000' in deadends:
            return -1
        if target == '0000':
            return 0

        # -------------------------------BFS 开始--------------------------------
        q = deque([])
        q.append(('0000', 0))

        while q:
            # 取出一个节点
            node, step = q.popleft()
            step += 1

            # 放入周围节点
            for i in range(4):
                for add in (1, -1):
                    cur = node[:i] + str(
                        (int(node[i]) + add) % 10) + node[i + 1:]
                    if cur == target:
                        return step
                    if cur not in deadends:
                        q.append((cur, step))
                        deadends.add(cur)  # 避免重复搜索
        # -------------------------------------------------------------------------

        return -1
