"""
876.链表的中间结点 / 链表 / easy
思路：快慢指针同起点，慢走 1 步、快走 2 步，fast 走不满两步就停，slow 落点就是中间节点（偶数长度落第二个）。
卡点：一开始用“走到中间右边停止”描述结果、说不清判定条件；第一次推演还拿结论反填（slow 写成 3、fast 写成 5），并误以为要从虚拟头节点起步。
套路：两个指针的落点差由循环条件控制；“fast 还能走满两步”就写 while fast and fast.next，fast 保第 1 步、fast.next 保第 2 步。
教训：同一套快慢指针，fast and fast.next 落第二个中间，fast.next and fast.next.next 落第一个——这类题先按步数推两轮，再写“应该在哪”。
"""
class Solution(object):
    def middleNode(self, head):
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow