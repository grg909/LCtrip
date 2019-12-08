# -*- coding: UTF-8 -*-

# @Date    : 2019/12/8
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""


# hashmap
class Solution3:

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        res = []
        map = {}

        for i in nums1:
            map[i] = map[i] + 1 if i in map else 1

        for i in nums2:
            if i in map and map[i] > 0:
                map[i] -= 1
                if i not in res:
                    res.append(i)

        return res


# Sort + merge
class Solution2:

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        res = []

        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                if not res:
                    res.append(nums1[i])
                elif res[-1] != nums1[i]:
                    res.append(nums1[i])
                i += 1
                j += 1

        return res


# brute-force searching + binary acceleration
class Solution3:

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        nums2.sort()
        for i in nums1:
            if i not in res and self.search(nums2, i):
                res.append(i)

        return res

    def search(self, nums2, target):

        start, end = 0, len(nums2) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums2[mid] == target:
                start = mid
            if nums2[mid] > target:
                end = mid
            if nums2[mid] < target:
                start = mid

        if nums2[end] == target:
            return True
        if nums2[start] == target:
            return True

        return False
