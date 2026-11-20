"""
88.合并两个有序数组 / 数组 / easy
思路：p1 指 nums1 有效段末尾、p2 指 nums2 末尾、p 指待填位置，每轮把两者较大值放进 p，然后各自前移。
卡点：第一版用 nums1[m:] = nums2 + sort() 直接过了，把题目唯一要练的“覆盖方向”整个绕开；被追问“从前往后填会覆盖谁”才转到从尾填。
套路：原地合并两个有序数组 → 从尾部填。空位在末尾，最大的数先落位，永远不会踩到还没比较的元素。
教训：能 AC 不等于练到了。那版 sort() 是 O((m+n)log(m+n))，力扣放你过，面试会追复杂度；先问一句“题目给的有序信息值不值得用”，再动手。
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1, p2, p = m - 1, n - 1, m + n - 1
        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
