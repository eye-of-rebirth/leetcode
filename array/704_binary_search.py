"""
704. 二分查找 | 数组 | Easy | 2026-09-16

思路：定义左闭右闭区间 [left, right]，所以 while 用 <=
卡点：一开始写成 left < right，边界处理错了
复杂度：时间 O(log n) / 空间 O(1)
同类题：35. 搜索插入位置、34. 在排序数组中查找元素的第一个和最后一个位置
"""


def search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
