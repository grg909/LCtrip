# -*- coding: UTF-8 -*-

# @Date    : 2020/3/10
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""

from collections import defaultdict, Counter


class Solution:

    def mostVisitedPattern(self, username: List[str], timestamp: List[int],
                           website: List[str]) -> List[str]:
        peoWebList = defaultdict(list)
        seqCnt = Counter()
        for _, u, w in sorted(zip(timestamp, username, website)):
            peoWebList[u].append(w)
        for webList in peoWebList.values():
            for seq3 in self.getSeq3(webList):
                seqCnt[seq3] += 1

        return min(seqCnt, key=lambda k: [-seqCnt[k], k])

    def getSeq3(self, arr):
        res = set()
        self.dfs(arr, 0, [], res)
        return res

    def dfs(self, arr, startIndex, combination, res):
        if len(combination) == 3:
            res.add(tuple(combination))
            return

        for i in range(startIndex, len(arr)):
            combination.append(arr[i])
            self.dfs(arr, i + 1, combination, res)
            combination.pop()
