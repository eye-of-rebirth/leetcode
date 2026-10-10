"""
141.判断环形链表 / 链表 / easy
思路:同142
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        cur = head
        per =head
        while cur and cur.next:
            cur=cur.next.next
            per=per.next
            if cur==per:
                return True
        return None