# -*- coding: UTF-8 -*-

# @Date    : 2020/1/18
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""

KEYBOARD = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}


class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """

    def letterCombinations(self, digits):
        if not digits:
            return []

        results = []
        self.dfs(digits, 0, '', results)

        return results

    def dfs(self, digits, index, chars, results):
        if index == len(digits):
            results.append(chars)
            return

        for letter in KEYBOARD[digits[index]]:
            self.dfs(digits, index + 1, chars + letter, results)
            # 实际和下面相同，回溯思想更明显
            # chars = chars + letter
            # self.dfs(digits, index + 1, chars, results)
            # chars = chars[:-1]
