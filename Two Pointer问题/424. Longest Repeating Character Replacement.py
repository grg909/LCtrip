# -*- coding: UTF-8 -*-

# @Date    : 2019/11/24
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        tmp = 0
        char_dict = {}
        start = 0
        for i in range(len(s)):
            if s[i] not in char_dict:
                char_dict[s[i]] = 1
            else:
                char_dict[s[i]] += 1

            tmp = max(tmp, char_dict[s[i]])
            if i - start + 1 - tmp > k:
                char_dict[start] -= 1
                start += 1
            res = max(res, i - start + 1)
        return res
