# -*- coding: UTF-8 -*-

# @Date    : 2020/1/18
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""
from collections import deque


class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """

    def ladderLength(self, start, end, dict):

        dict.add(end)
        queue = deque([start])
        seen = set()
        seen.add(start)
        layer = 0

        while queue:
            layer += 1
            for i in range(len(queue)):
                cur_word = queue.popleft()
                if cur_word == end:
                    return layer
                for word in self.generate_next(cur_word):
                    if word in dict and word not in seen:
                        queue.append(word)
                        seen.add(word)
        return 0

    def generate_next(self, cur_word):
        for i in range(len(cur_word)):
            left, right = cur_word[:i], cur_word[i + 1:]
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if cur_word[i] == char:
                    continue
                yield left + char + right
