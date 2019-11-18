# -*- coding: UTF-8 -*-

# @Date    : 2019/11/18
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""


class Solution:

    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k: return 0
        c = min(set(s), key=s.count)  # 按照count排序
        if s.count(c) >= k:
            return len(s)
        # 如果最小的无法满足要求，就一定不包含最小的，然后递归其他子串
        return max(self.longestSubstring(t, k) for t in s.split(c))
