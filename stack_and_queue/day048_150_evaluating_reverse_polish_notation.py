"""
150.逆波兰表达式求值 / 栈与队列 / middle
思路:弹栈
卡点:注意使用python3,还有注意虽然是数组,但在字符串里面的都是字符,记得进行一步转换
"""
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i in tokens:
            if i not in ('+', '-', '*', '/'):#此函数用于 判断数据类型
                stack.append(int(i))
            else:
                a = stack.pop()
                b = stack.pop()
                if i=='+':
                    c=a+b
                elif i=='-':
                    c=b-a
                elif i=='/':
                    c=int(b/a)
                elif i=='*':
                    c=a*b
                stack.append(c)
        return stack[-1] if stack else None