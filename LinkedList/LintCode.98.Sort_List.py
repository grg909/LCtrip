# -*- coding: UTF-8 -*-

# @Date    : 2020/1/20
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""
"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


# Merge版本，因为链表的特性，所以归并链表的空间复杂度是O(1)
class Solution1:
    """
    @param head: The head of linked list.
    @return: You should return the head of the sorted linked list, using constant space complexity.
    """

    def sortList(self, head):
        if not head or not head.next:
            return head

        mid = self.find_mid(head)
        left = head
        right = mid.next
        mid.next = None

        sorted_left = self.sortList(left)
        sorted_right = self.sortList(right)

        return self.merge(sorted_left, sorted_right)

    def find_mid(self, head):
        if not head or not head.next:
            return head

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, left, right):
        dummy = ListNode(-1)
        cur = dummy

        while left and right:
            if left.val > right.val:
                cur.next = right
                right = right.next
            else:
                cur.next = left
                left = left.next
            cur = cur.next

        if left:
            cur.next = left
        if right:
            cur.next = right

        return dummy.next


# Quick sort
class Solution2:
    """
    @param head: The head of linked list.
    @return: You should return the head of the sorted linked list, using constant space complexity.
    """

    def sortList(self, head):
        if not head or not head.next:
            return head

        # 用中间节点作为pivot节点
        mid = self.find_mid(head)
        dummy_l, dummy_m, dummy_r = ListNode(-1), ListNode(-1), ListNode(-1)
        tail_l, tail_m, tail_r = dummy_l, dummy_m, dummy_r

        # 遍历链表，做partition
        while head:
            if head.val < mid.val:
                tail_l.next = head
                tail_l = tail_l.next
            if head.val > mid.val:
                tail_r.next = head
                tail_r = tail_r.next
            if head.val == mid.val:
                tail_m.next = head
                tail_m = tail_m.next
            head = head.next

        tail_l.next = None
        tail_m.next = None
        tail_r.next = None

        sorted_left = self.sortList(dummy_l.next)
        sorted_right = self.sortList(dummy_r.next)
        return self.connect(sorted_left, dummy_m.next, sorted_right)

    def find_mid(self, head):
        if not head or not head.next:
            return head

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def connect(self, left, middle, right):
        dummy = ListNode(-1)
        dummy.next = left

        while left.next:
            left = left.next

        left.next = middle

        while middle.next:
            middle = middle.next

        middle.next = right

        return dummy.next
