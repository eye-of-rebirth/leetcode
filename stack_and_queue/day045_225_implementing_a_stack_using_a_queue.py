"""
225.用队列实现栈 / 栈与队列 / easy
思路:先入队的元素在后入队的元素后面,所以先入队的元素弹出的时候需要将它后面的元素都先弹出并重新入队

"""

from collections import deque


class MyStack(object):

    def __init__(self):
        self.quene = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.quene.append(x)
        for _ in range(len(self.quene) - 1):
            self.quene.append(self.quene.popleft())

    def pop(self):
        """
        :rtype: int
        """
        return self.quene.popleft()

    def top(self):
        """
        :rtype: int
        """
        return self.quene[0]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.quene

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()