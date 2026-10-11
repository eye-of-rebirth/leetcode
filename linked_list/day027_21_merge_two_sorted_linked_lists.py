"""
21.合并两个有序链表 / 链表 / easy
思路:双指针双循环,遍历两个链表元素
卡点:注意两链表中某一链表空的情况
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        cur1 = list1
        cur2 = list2
        per = ListNode(None)
        head = per
        # 这个限制很关键主要是为了防止出现表1不存在导致进不了循环
        if cur2 and cur1 == None:
            return cur2
        while cur1:
            while cur2 and cur2.val <= cur1.val:
                per.next = cur2
                per = per.next
                cur2 = cur2.next
            per.next = cur1
            per = per.next
            cur1 = cur1.next
            if cur2 and cur1 == None:
                # 关键在这里,如果不在这里加以限制就会在表1到底后直接结束
                per.next = cur2
        return head.next



