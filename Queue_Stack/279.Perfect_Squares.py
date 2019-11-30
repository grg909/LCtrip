# -*- coding: UTF-8 -*-

# @Date    : 2019/12/1
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""

from collections import deque


class Solution:
    def numSquares(self, n: int) -> int:
        around = []
        for i in range(1, n + 1):
            if i**2 <= n:
                around.append(i**2)
            else:
                break

        r = 0
        seen = set()

        # ----------------BFS 开始----------------------
        q = deque([])
        q.append((n, r))

        while q:
            # 取出一个元素
            cur, step = q.popleft()

            # 放入周围元素
            for a in around:
                a = cur - a
                if a == 0:
                    return step + 1
                if a > 0 and a not in seen:
                    seen.add((a, step + 1))
                    q.append((a, step + 1))
        # ----------------------------------------------
        return 0
