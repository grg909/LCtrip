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
    @return: a list of lists of string
    """

    def findLadders(self, start, end, dict):
        dict.add(start)
        dict.add(end)
        distance = {}

        self.bfs(end, distance, dict)

        result = []
        self.dfs(start, end, distance, dict, [], result)

    def bfs(self, start, distance, dict):
        distance[start] = 0
        queue = deque([start])
        while queue:
            word = queue.popleft()
            for next_word in self.generate_next(word):
                if next_word in dict and next_word not in distance:
                    distance[next_word] = distance[word] + 1
                    queue.append(next_word)

    def generate_next(self, cur_word):
        for i in range(len(cur_word)):
            left, right = cur_word[:i], cur_word[i + 1:]
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if cur_word[i] == char:
                    continue
                yield left + char + right

    def dfs(self, cur, target, distance, dict, path, result):
        path.append(cur)
        if cur == target:
            result.append(list(path))
            return

        for word in self.generate_next(cur):
            if word not in dict or distance[word] != distance[cur] - 1:
                continue
            self.dfs(word, target, distance, dict, path, result)
            path.pop()
