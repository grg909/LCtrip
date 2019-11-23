# -*- coding: UTF-8 -*-

# @Date    : 2019/11/24
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""


# Greedy and slide window
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = {c: i for i, c in enumerate(S)}
        j = left = 0
        ans = []
        for i in range(len(S)):
            j = max(j, last[S[i]])

            if i == j:
                ans.append(i - left + 1)
                left = i + 1

        return ans
