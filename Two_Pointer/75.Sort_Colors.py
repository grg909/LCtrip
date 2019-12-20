# -*- coding: UTF-8 -*-

# @Date    : 2019/12/15
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""

from collections import Counter


# 计数排序
# use hash table, Two pass, Time O(n), Space O(n)
class Solution1:

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = Counter(nums)

        order = [0, 1, 2]
        index = 0
        for i in order:
            if i in counter:
                while counter[i]:
                    nums[index] = i
                    index += 1
                    counter[i] -= 1


# Two partition, Two pass, Time O(n), Space O(n)
# 先把0和非0分开， 然后把1和非1分开
class Solution2:

    def sortColors(self, nums: List[int]) -> None:
        index = self.partition(nums, 0, 0)
        self.partition(nums, 1, index)

    def partition(self, nums, flag, index):
        left, right = index, len(nums) - 1
        while left <= right:
            while left <= right and nums[left] == flag:
                left += 1
            while left <= right and nums[right] != flag:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left + 1, right - 1


# One partition, one pass.
# 设立三根指针:left, right, index. 假设left左侧都是0， right右侧都是2.
# index 从左到右扫描每个数，如果碰到 0 就丢给 left，碰到 2 就丢给 right。碰到 1 就跳过不管。
class Solution3:

    def sortColors(self, nums: List[int]) -> None:
        left, right, index = 0, len(nums) - 1, 0
        while index <= right:
            while index <= right and nums[index] == 1:
                index += 1
            while index <= right and nums[index] < 1:
                nums[left], nums[index] = nums[index], nums[left]
                left += 1
                index += 1
            while index <= right and nums[index] > 1:
                nums[right], nums[index] = nums[index], nums[right]
                right -= 1  # 这里不用动index， 易错，因为index还没有check交换过来的数， 而left可以动
                # index是从left开始的，已经check过所有左边的了
