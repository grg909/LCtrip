# -*- coding: UTF-8 -*-

# @Date    : 2019/12/15
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""

from collections import Counter

# 方法	                        Time	    Space
# 快速排序（暴力无视k）	        O(nlogn)	O(logn)
# 计数排序	                    O(n)	    O(k)
# k次partition，每次划分出一种颜色	O(nk)	    O(1)
# 分治法，logk次 partition（最优）	O(nlogk)	O(logk)


# 计数排序
class Solution1:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """

    def sortColors2(self, colors, k):
        counter = Counter(colors)
        index = 0
        for i in range(1, k + 1):
            if i in counter:
                while counter[i]:
                    colors[index] = i
                    index += 1
                    counter[i] -= 1


# k次partition
class Solution2:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """

    def sortColors2(self, colors, k):
        index = 0
        for i in range(1, k + 1):
            index = self.partition(colors, index, i)

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


# 分治，logk次partition， Rainbow Sort
class Solution3:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    """
    我理解maximum recursion depth其实由两方面综合决定：选取colorMid的方式和sort子区间的划分，题解中的(colorFrom + colorTo) / 2 划分
    对于从1开始的color种类来说，其实选取了中间偏左的颜色，偏左意味着可能就是第一种颜色，如果此时将逻辑改成 colors[l] < colorMid，
    就会造成l一直在起始位置，所有的都被划到了右侧，而[r, right]相当于整个数组没有分割又进入下一层，无限循环下去。要想换个口味，
    可以将colorMid划分成中间偏右即 (colorFrom + colorTo) / 2 + 1，对应的下层划分改为rainbowSort(colors, left, r, colorFrom, colorMid - 1); 
    和 rainbowSort(colors, l, right, colorMid, colorTo);也是ok的
    """

    def sortColors2(self, colors, k):
        self.sort(colors, 1, k, 0, len(colors)-1)

    def sort(self, colors, color_from, color_to, index_from, index_to):
        if color_from >= color_to or index_from >= index_to:
            return

        pivot = (color_from + color_to) //2 +1
        left, right = index_from, index_to
        while left <= right:
            while left <= right and colors[left] < pivot:
                left += 1
            while left <= right and colors[right] >= pivot:
                right -=1
            if left <= right:
                colors[left], colors[right] = colors[right], colors[left]
                left += 1
                right -= 1
                                    # 快排子区间划分易错
        self.sort(colors, color_from, pivot, index_from, right)
        self.sort(colors, pivot, color_to, left, index_to)