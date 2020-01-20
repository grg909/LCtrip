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

Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: head: The first node of linked list.
    @return: a tree node
    """
    def sortedListToBST(self, head):
        if not head:
            return None

        if not head.next:
            return TreeNode(head.val)

        mid = self.find_mid(head)
        temp = mid.next
        mid.next = None
        parent = TreeNode(temp.val)

        parent.left = self.sortedListToBST(head)
        parent.right = self.sortedListToBST(temp.next)

        return parent

    # 此题用到了dummy head
    def find_mid(self, head):
        dummy = ListNode(-1)
        dummy.next = head

        slow, fast = dummy, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
