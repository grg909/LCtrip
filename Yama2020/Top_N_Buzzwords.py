# -*- coding: UTF-8 -*-

# @Date    : 2020/3/1
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""

import re
import heapq as hq

class Solution:

    def topNBuzzWords(self, numToys, topToys, toys, numQuotes, quotes):
        if not quotes or not toys:
            return []

        counter = {i:[0, 0] for i in toys}

        for quote in quotes:
            wordList = re.findall(r'\w+', quote.lower())
            for word in wordList:
                if word in counter:
                    counter[word][0] += 1
            for word in counter.keys():
                if word in wordList:
                    counter[word][1] += 1

        heap = [(-freqs[0], -freqs[1], word) for word, freqs in counter.items()]
        hq.heapify(heap)

        return [hq.heappop(heap)[2] for _ in range(topToys)]


if __name__ == '__main__':
    a = Solution()
    a.topNBuzzWords(numToys = 6,
                    topToys = 2,
                    toys=["elmo", "elsa", "legos", "drone", "tablet", "warcraft"],
                    numQuotes = 6,
                    quotes=[
                        "Elmo is the hottest of the season! Elmo will be on every kid's wishlist!",
                        "The new Elmo dolls are super high quality",
                        "Expect the Elsa dolls to be very popular this year, Elsa!",
                        "Elsa and Elmo are the toys I'll be buying for my kids, Elsa is good",
                        "For parents of older kids, look into buying them a drone",
                        "Warcraft is slowly rising in popularity ahead of the holiday season"
                    ])