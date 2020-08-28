# -*- coding: UTF-8 -*-

# @Date    : 2020/3/1
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""

from collections import Counter


class Solution:

    def favor(self, userSongs, songGeners):
        res = {}
        d = {
            song: genres for genres in songGeners for song in songGeners[genres]
        }
        for user, song in userSongs.items():
            genresCount = Counter(d[song] for i in song)
            mxcnt = max(genresCount.values() or [0])
            res[user] = [genres for genres in genresCount if genresCount[genres] == mxcnt]\

        return res
