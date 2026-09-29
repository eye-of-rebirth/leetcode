"""
203.移除链表的元素 / 链表 / easy
思路:为了一视同仁,不用去判断是否为头节点采用虚拟头节点的作法
卡点:没写过链表
"""



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        cur = dummy = ListNode(next=head)
        while cur.next  != None:
            if cur.next.val == val:
                cur.next = cur.next.next  # 删除下一个节点
            else:
                cur = cur.next  # 继续向后遍历链表
        return dummy.next
