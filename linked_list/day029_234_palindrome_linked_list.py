"""
234.回文链表 / 链表 / easy
思路:快慢指针找左中点(左中点是关键，反转后半段，再逐个比较前后两段节点的值)
卡点:快慢指针必须停左中点，且最后要逐个比 val 而不是比节点对象，否则偶数长度会漏判
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        # 快慢指针中点断开
        fast = head
        slow = head
        # 注意此处的要求是fast.next和fast.next.next因为要让slow停在左边
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        # 断开操作,同样使用双指针
        cur = slow.next
        per = None
        slow.next = None
        while cur:
            temp = cur.next
            cur.next = per
            per = cur
            cur = temp
        # 很关键,==判断的依据是地址,不是具体数值所以哪怕两个链表指向完全相同也不能判断

        p1 = head
        p2 = per

        while p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True
