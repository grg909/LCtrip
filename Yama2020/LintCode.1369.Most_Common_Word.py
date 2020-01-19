# -*- coding: UTF-8 -*-

# @Date    : 2020/1/19
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""
import re
from collections import Counter


class Solution:
    """
    @param paragraph:
    @param banned:
    @return: nothing
    """

    def mostCommonWord(self, paragraph, banned):
        if not paragraph:
            return None

        ban_set = set(banned)
        words = re.findall(r'\w+', paragraph.lower())
        return Counter(w for w in words if w not in ban_set).most_common()[0][0]
