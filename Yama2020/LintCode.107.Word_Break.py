# -*- coding: UTF-8 -*-

# @Date    : 2020/1/18
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""
    解题报告：由于大问题可以转化为小问题，所有可以使用dp，
    字符串分割，序列型dp，状态为'前' i个字符能不能拼出来，看最后一步写出状态方程
"""


# 内循环需要优化，去除不必要验证（常用技巧）
# state: dp[i] represent previous i chars can be break into words or not, True or False
# transfer function, dp[i] = OR(dp[j] and s[j:i]) in dict for all j < i, i - j <= maxlen
# init: dp[0] = True; empty string
# return: dp[n] where n = len(s)
class Solution:
    """
    wordBreak('leet') = wordBreak('lee') && inDict('t')
    || wordBreak('le') && inDict('et')
    || wordBreak('l') && inDict('eet')
    || wordBreak('') && inDict('leet')
    """

    def wordBreak(self, s, dict):
        if not dict:
            return len(s) == 0

        n = len(s)
        f = [False] * (n + 1)
        f[0] = True

        maxLength = max([len(j) for j in dict])
        for i in range(1, n + 1):
            for j in range(1, min(i, maxLength) + 1):  # 此处min是为了优化
                if not f[i - j]:
                    continue
                if s[i - j:i] in dict:
                    f[i] = True
                    break

        return f[n]
