# -*- coding: UTF-8 -*-

# @Date    : 2020/1/2
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""
"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""


# 将两个结点移动到相同的高度，然后同时向上移动，直到移动到相同的点
# 此法用了额外空间
class Solution1:
    """
    @param: root: The root of the tree
    @param: A: node in the tree
    @param: B: node in the tree
    @return: The lowest common ancestor of A and B
    """

    def lowestCommonAncestorII(self, root, A, B):
        dic = {}
        while A is not root:
            dic[A] = True
            A = A.parent

        while B is not root:
            if B in dic:
                return B
            B = B.parent

        return root


# another method
class Solution2:
    """
    @param: root: The root of the tree
    @param: A: node in the tree
    @param: B: node in the tree
    @return: The lowest common ancestor of A and B
    """

    def lowestCommonAncestorII(self, root, A, B):
        A_len = self.get_path_len_root(A)
        B_len = self.get_path_len_root(B)

        lowest_ancestor = None
        if A_len > B_len:
            diff = A_len- B_len
            while diff:
                A = A.parent
                diff -= 1
                A_len -= 1
        if B_len > A_len:
            diff = B_len - A_len
            while diff:
                B = B.parent
                diff -= 1
                B_len -= 1

        while A_len:
            if A.parent == B.parent:
                lowest_ancestor = A.parent
                break
            A_len -= 1

        return lowest_ancestor

    def get_path_len_root(self, node):
        count = 0
        while node:
            node = node.parent
            count += 1

        return count
