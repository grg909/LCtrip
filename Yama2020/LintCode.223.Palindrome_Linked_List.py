# -*- coding: UTF-8 -*-

# @Date    : 2020/1/18
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""
    解题报告：通过找中点反转后段来间接实现
    list双指针。熟悉find_mid和reverse套路
"""
"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param head: A ListNode.
    @return: A boolean.
    """

    def isPalindrome(self, head):
        if not head or not head.next:
            return True

        mid = self.find_middle(head)
        tail = self.reverse(mid.next)

        while head and tail:
            if head.val != tail.val:
                return False
            head = head.next
            tail = tail.next

        return True

    def find_middle(self, head):
        # 1(head) -> 2 -> 3 -> 4
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse(self, head):
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre
