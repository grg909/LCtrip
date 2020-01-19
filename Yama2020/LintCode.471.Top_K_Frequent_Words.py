# -*- coding: UTF-8 -*-

# @Date    : 2020/1/19
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""
    解题报告：1. python heapq默认为最小堆，可以
    同过加负号转换为最大堆
    2. heapq排序规则是按照依次按照维度排序，比如这里
    先按-freq从小到大，相同-freq再按word从小到大排
"""
from collections import Counter
import heapq as hq


class Solution:
    """
    @param words: an array of string
    @param k: An integer
    @return: an array of string
    """

    def topKFrequentWords(self, words, k):
        if not words or not k:
            return []

        counter = Counter(words)
        heap = [(-freq, word) for word, freq in counter.items()]
        hq.heapify(heap)

        return [hq.heappop(heap)[1] for _ in range(k)]
