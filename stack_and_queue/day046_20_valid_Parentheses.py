"""
20 有效的括号 / 栈与队列 / easy
思路:相同弹栈思维,用字典去做映射操作
卡点:栈的初始化,栈的弹出操作,栈的判断操作
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # 建立右括号到左括号的映射
        mapping = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            # 如果是右括号
            if char in mapping:
                # 如果栈为空，或者栈顶元素与当前右括号不匹配
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()  # 匹配成功，弹出栈顶
            else:
                # 如果是左括号，压入栈
                stack.append(char)

        # 最后判断栈是否为空
        return not stack