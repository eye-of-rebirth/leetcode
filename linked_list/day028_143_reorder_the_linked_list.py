"""
143.重排链表 / 链表 / middle
思路:快慢指针找中点，反转后半段，再把前半段和反转后的后半段交替合并。
卡点:忘记前面的反转指针的内容

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # 使用快慢指针法把数据拆分成为两部分,找中点
        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 断开两部分
        cur = slow.next
        per = None
        slow.next = None

        # 反转链表
        while cur:
            temp = cur.next
            cur.next = per
            per = cur
            cur = temp

        # 接下来交替进行
        tp1 = head
        tp2 = per
        while tp2:
            nxt1 = tp1.next
            nxt2 = tp2.next

            tp1.next = tp2
            tp2.next = nxt1

            tp1 = nxt1
            tp2 = nxt2
        return head

