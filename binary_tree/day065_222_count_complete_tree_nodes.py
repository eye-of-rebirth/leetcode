"""
222.完全二叉树的节点个数 / 二叉树 / medium
思路：基础版递归累加左右子树和当前节点；进阶版直接算出上面各层的节点数，再二分找最底层最后一个有节点的位置
卡点：外层二分缩小的是候选编号范围；检查某个编号时，目标固定，当前节点和它覆盖的范围一起更新。
套路：遇到从左到右呈现“有节点 → 空位”的单调分布，可以二分找边界。
教训：每次检查新编号都从根和完整范围出发，递归用参数传递下一步要检查的节点，用 return 把检查结果传回来。
"""
class Solution(object):
    def countNodes(self, root):
        if root is None:
            return 0

        # 沿最左路径数层数，根节点算第 1 层
        height = 0
        node = root
        while node is not None:
            height += 1
            node = node.left

        last_level_size = 2 ** (height - 1)

        def exists(node, start, end, target):
            if node is None:
                return False
            if start == end:
                return True

            mid = (start + end) // 2
            if target <= mid:
                return exists(node.left, start, mid, target)
            return exists(node.right, mid + 1, end, target)

        left, right = 1, last_level_size
        last_present = 0

        while left <= right:
            mid = (left + right) // 2
            if exists(root, 1, last_level_size, mid):
                last_present = mid
                left = mid + 1
            else:
                right = mid - 1

        return (last_level_size - 1) + last_present