"""
155.最小栈 / 栈与队列 / medium
思路：普通栈保存元素，辅助栈保存最小值的历史。
卡点：重复的最小值也要入辅助栈，避免弹出后丢失记录。
套路：需要随弹出恢复历史状态时，考虑使用辅助栈。
教训：把“相等”的边界落实到代码，不能只在思路里记住。
"""
class MinStack(object):

    def __init__(self):
        self.list = []
        self.limlist = []

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.list.append(value)
        if not self.limlist or self.limlist[-1] >= value:
            self.limlist.append(value)

    def pop(self):
        """
        :rtype: None
        """
        value = self.list.pop()
        if self.limlist[-1] == value:
            self.limlist.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.list[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.limlist[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()