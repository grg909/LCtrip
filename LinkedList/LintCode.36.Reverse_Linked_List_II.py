# -*- coding: UTF-8 -*-

# @Date    : 2020/1/7
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


# One-pass, my solution
class Solution1:
    """
    @param head: ListNode head is the head of the linked list
    @param m: An integer
    @param n: An integer
    @return: The head of the reversed ListNode
    """

    def reverseBetween(self, head, m, n):
        # pre -> n1 -> nm -> ... -> nn -> nn+1
        # pre -> n1 -> nn -> ... -> nm -> nn+1
        dummy = ListNode(-1)
        dummy.next = head

        nm_pre = self.find_kth_node(dummy, m - 1)
        nm = nm_pre.next

        # 举例子可以发现不是n-m, 而是n-m+1
        nn, nn_plus = self.reverse_k_times(nm, n - m + 1)

        nm_pre.next = nn
        nm.next = nn_plus

        return dummy.next

    def find_kth_node(self, pre, k):
        cur = pre
        while k:
            cur = cur.next
            if not cur:
                return None
            k -= 1
        return cur

    def reverse_k_times(self, head, k):
        pre = None
        cur = head

        while k:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
            k -= 1

        return pre, cur


# Not one pass
class Solution2:
    def reverseBetween(self, head, m, n):
        # pre -> n1 -> nm -> ... -> nn -> nn+1
        # pre -> n1 -> nn -> ... -> nm -> nn+1
        dummy = ListNode(-1)
        dummy.next = head

        nm_pre = self.find_kth_node(dummy, m - 1)
        nm = nm_pre.next
        nn = self.find_kth_node(dummy, n)
        nn_plus = nn.next

        nn.next = None
        self.reverse(nm)
        nm_pre.next = nn
        nm.next = nn_plus

        return dummy.next

    def find_kth_node(self, pre, k):
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