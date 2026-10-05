"""
206.反转链表 / 链表 / easy
思路:通过两个指针去反转,同时创建一个临时指针temp去储存
卡点:没能明白循环结束后cur已经为空了,应该返回pre

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        cur = head
        pre = None
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre          #此处循环结束cur已经成为None了