# -*- coding: UTF-8 -*-

# @Date    : 2020/1/6
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""
    解题报告：熟悉链表基本操作，把复杂问题拆解为基本操作
    可以在函数注释处写上链表的变化，避免出错
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
    @param head: a ListNode
    @param k: An integer
    @return: a ListNode
    """

    def reverseKGroup(self, head, k):
        """
        # dummy->[1->2->3]->[4->5->6]->7 (k = 3)
        # dummy->[3->2->1]->[6->5->4]->7
        """
        dummy = ListNode(-1)
        dummy.next = head

        pre = dummy
        while pre:
            pre = self.reverse_next_k_node(pre, k)

        return dummy.next

    def reverse_next_k_node(self, pre, k):
        """
        原：pre -> n1 -> n2 -> ... -> nk -> nk+1
        现：pre -> nk -> nk-1 -> ... -> n1 -> nk+1
        return n1
        """
        n1 = pre.next
        nk = self.find_kth_node(pre, k)
        if not nk:
            return None
        nk_plus = nk.next

        nk.next = None
        self.reverse(n1)
        pre.next = nk
        n1.next = nk_plus

        return n1

    def find_kth_node(self, pre, k):
        # pre -> n1 -> n2 -> ... -> nk
        cur = pre
        while k:
            cur = cur.next
            if not cur:
                return None
            k -= 1
        return cur

    def reverse(self, head):
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
