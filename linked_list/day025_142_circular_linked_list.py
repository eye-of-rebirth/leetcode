"""
142.环形链表 / 链表 / middle
思路:用快慢指针找到环内相遇点，再让头指针和相遇点指针同速前进，它们再次相遇的节点就是环的入口。
卡点:循环判断条件
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        per = head
        xyd = 0
        kt = head

        # 先进行快慢指针操作,一个是走两步一个走一步
        # 注意判断能不能下一步不需要判断下一步是不是空,而是当前是不是空
        while cur and cur.next:
            cur = cur.next.next
            per = per.next
            if per == cur:
                xyd = per
                while xyd != kt:
                    xyd = xyd.next
                    kt = kt.next
                return xyd
        return None


