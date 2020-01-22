# -*- coding: UTF-8 -*-

# @Date    : 2020/1/20
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""
    解题报告：https://www.1point3acres.com/bbs/thread-564350-1-1.html 第二题
    解法1，树上的BFS + priority queue
    解法2，https://stackoverflow.com/questions/25344313/generating-ascending-sequence-2p3q
"""

import heapq as hq


class Solution1:

    def find_index(self, index):

        pqueue = []
        hq.heappush(pqueue, 1)
        seen = set()
        count = 0

        while pqueue:
            num = hq.heappop(pqueue)
            if count == index:
                return num
            count += 1

            for i in (2, 3):
                new_num = num * i
                if new_num not in seen:
                    seen.add(new_num)
                    hq.heappush(pqueue, new_num)

        return -1


class Solution2:

    def find_index(self, index):
        S = [1]
        i2 = 0  # current index in 2S
        i3 = 0  # current index in 3S
        count = 0
        while True:
            if count == index:
                return S[-1]
            count += 1

            n2 = 2 * S[i2]
            n3 = 3 * S[i3]
            S.append(min(n2, n3))
            # 如果上面取小的是n2，2s的index就加1
            i2 += n2 <= n3
            # 如果上面取小的是n3，3s的index就加1
            i3 += n2 >= n3


if __name__ == '__main__':
    a = Solution2()
    a.find_index(1)
