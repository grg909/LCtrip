# -*- coding: UTF-8 -*-

# @Date    : 2019/12/21
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""


# Valid parentheses
# 题意：输入一个只包含括号的字符串，判断括号是否匹配
# 模拟堆栈，读到左括号压栈，读到右括号判断栈顶括号是否匹配
def isValidParentheses(self, s):
    stack = []
    dic = {'{': '}', '(': ')', '[': ']'}
    for char in s:
        if char in '{[(':
            stack.append(char)
        else:
            if not stack or char != dic[stack.pop()]:
                return False

    return not stack


# Longest valid parentheses
def longestValidParentheses(self, s):
    """
    @param s: a string
    @return: return a integer
    """
    if len(s) <= 1:
        return 0

    res = 0
    dp = [0 for i in range(len(s))]
    for i in range(len(s)-2, -1, -1):
        if s[i] == '(':
            j = i + dp[i+1] +1
            if j < len(s) and s[j] == ')':
                dp[i] = dp[i+1] +2
                if j+1 < len(s):
                    dp[i] += dp[j+1]
            res = max(res, dp[i])

    return res