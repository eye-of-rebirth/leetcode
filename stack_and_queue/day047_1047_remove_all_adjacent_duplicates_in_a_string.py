"""
1047.删除字符串中相邻的重复字符 / 栈与队列 / easy
思路:弹栈
卡点:学习使用join方法转化字符串
"""

class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for char in s:
            if stack and char == stack[-1]:
                stack.pop()
            else:
                stack.append(char)

        return "".join(stack)  # 使用join 把后面的序列转换为字符串
