# -*- coding: UTF-8 -*-

# @Date    : 2020/3/1
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""


class Solution:

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:
            return t is None
        if s.val == t.val and self.compare(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def compare(self, s, t):
        if not s:
            return t is None
        if t is None or s.val != t.val:
            return False
        return self.compare(s.left, t.left) or self.compare(s.right, t.right)
