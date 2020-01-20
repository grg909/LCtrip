# -*- coding: UTF-8 -*-

# @Date    : 2020/1/20
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""
    解题报告：https://www.1point3acres.com/bbs/thread-564350-1-1.html 第二题
    树上的BFS + priority queue
"""
import heapq as hq


class Solution:

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


if __name__ == '__main__':
    a = Solution()
    a.find_index(7)
