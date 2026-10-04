"""
707.设计链表 / 链表  /  Middle
思路:虚拟头节点,以及赋值先后再前
卡点:虚拟头节点上处理没对,要在__init__里定义并且调用

"""


class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList(object):

    def __init__(self):
        self.dummy = ListNode(0)
        self.size = 0

    # 调用这里面的dummy和size要记得把self带上

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1
        cur = self.dummy.next  # 因为是定位到当前位置的所以要先next一下
        for _ in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < 0 or index > self.size:
            return
        self.size += 1
        cur = self.dummy  # 因为是定位到当前位置之前的所以不用next
        newcode = ListNode(val)
        for _ in range(index):
            cur = cur.next
        newcode.next = cur.next
        cur.next = newcode

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            return
        self.size -= 1
        cur = self.dummy
        for _ in range(index):
            cur = cur.next
        cur.next = cur.next.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)