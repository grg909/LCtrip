# -*- coding: UTF-8 -*-

# @Date    : 2020/3/1
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""


class Solution:

    def suggestedProducts(self, products: List[str],
                          searchWord: str) -> List[List[str]]:
        if not products or not searchWord:
            return []
        products.sort()
        length = len(products)
        curInput, res = '', []

        for char in searchWord:
            tmp = []
            curInput += char
            index = self.binarySearch(products, curInput)
            for i in range(index, min(length, index + 3)):
                if products[i].startswith(curInput):
                    tmp.append(products[i])
            res.append(tmp)

        return res

    def binarySearch(self, products: List[str], curWord: str) -> int:
        start, end = 0, len(products) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if products[mid] < curWord:
                start = mid
            else:
                end = mid

        if products[start] >= curWord:
            return start

        return end
