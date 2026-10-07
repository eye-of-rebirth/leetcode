"""
19.删除链表倒数第n位的节点 / 链表 / middle
思路:先求链表节点个数,再使用两指针进行修改
卡点:没有事先求个数

"""



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        sz = 0
        cur = head
        while cur:
            sz += 1
            cur = cur.next

        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy.next
        per = dummy
        js = 1
        while js < sz -n+1:
            js+=1
            per = cur
            cur = cur.next
        per.next = cur.next

        return dummy.next