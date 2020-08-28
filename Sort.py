# -*- coding: UTF-8 -*-

# @Date    : 2020/3/11
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""
    解题报告： 各种排序算法的实现
"""


class Solution:
    # @param {int[]} A an integer array
    # @return A

    # 冒泡排序, Best O(n), Average O(n^2), Worst O(n^2)
    def bubbleSort(self, A):
        for last in range(len(A) - 1, 0, -1):
            for i in range(last):
                if A[i] > A[i + 1]:
                    A[i], A[i + 1] = A[i + 1], A[i]

        return A

    # 选择排序, Best O(n^2), Average O(n^2), Worst O(n^2)
    def selectionSort(self, A):
        for i in range(len(A)):
            minIdx = i
            for j in range(i + 1, len(A)):
                if A[j] < A[minIdx]:
                    minIdx = j
            A[i], A[minIdx] = A[minIdx], A[i]

        return A

    # 插入排序, Best O(n), Average O(n^2), Worst O(n^2) 用于近似有序的最佳
    def insertionSort(self, A):
        for i in range(1, len(A)):
            curIdx, tmp = i, A[i]
            while curIdx > 0 and A[curIdx - 1] > tmp:
                A[curIdx] = A[curIdx - 1]
                curIdx -= 1
            A[curIdx] = tmp

        return A

    # 快速排序, Best O(nlogn), Average O(nlogn), Worst O(n^2)
    def quickSort(self, A):
        self.qHelper(A, 0, len(A) - 1)
        return A

    def qHelper(self, A, start, end):
        if start >= end:
            return

        left, right = start, end
        pivot = A[(start + end) // 2]

        while left <= right:
            while left <= right and A[left] < pivot:
                left += 1
            while left <= right and A[right] > pivot:
                right -= 1
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1

        self.qHelper(A, start, right)
        self.qHelper(A, left, end)

    # 归并排序, Best O(nlogn), Average O(nlogn), Worst O(nlogn), 不太好因为需要额外空间O（n)
    def mergeSort(self, A):
        self.mHelper(A, 0, len(A) - 1, [0] * len(A))
        return A

    def mHelper(self, A, start, end, tmp):
        if start >= end:
            return

        mid = (start + end) // 2
        self.mHelper(A, start, mid, tmp)
        self.mHelper(A, mid + 1, end, tmp)
        self.mergeTwo(A, start, end, tmp)

    def mergeTwo(self, A, start, end, tmp):
        mid = (start + end) // 2
        leftIdx = start
        rightIdx = mid + 1
        idx = start

        while leftIdx <= mid and rightIdx <= end:
            if A[leftIdx] < A[rightIdx]:
                tmp[idx] = A[leftIdx]
                leftIdx += 1
            else:
                tmp[idx] = A[rightIdx]
                rightIdx += 1
            idx += 1

        while leftIdx <= mid:
            tmp[idx] = A[leftIdx]
            leftIdx, idx = leftIdx + 1, idx + 1
        while rightIdx <= end:
            tmp[idx] = A[rightIdx]
            rightIdx, idx = rightIdx + 1, idx + 1

        for i in range(start, end + 1):
            A[i] = tmp[i]


if __name__ == '__main__':
    print(Solution().bubbleSort([3, 2, 1, 4, 5]))
    print(Solution().selectionSort([3, 2, 1, 4, 5]))
    print(Solution().insertionSort([3, 2, 1, 4, 5]))
    print(Solution().quickSort([3, 2, 1, 4, 5]))
    print(Solution().mergeSort([3, 2, 1, 4, 5]))
