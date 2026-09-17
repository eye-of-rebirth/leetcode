"""
704. 二分查找 | 数组 | Easy | 2026-09-15

思路：定义左闭右闭区间 [left, right]，所以 while 用 <=
卡点：一开始写成 left < right，边界处理错了
复杂度：时间 O(log n) / 空间 O(1)

同类题：35. 搜索插入位置、34. 在排序数组中查找元素的第一个和最后一个位置
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left,right = 0,len(nums)-1
        middle = left + right
        while left <=right:
            middle = (left + right)//2
            if nums[middle] == target:
                return middle
            #注意在函数中出现了return则代表着这个函数结束了输出了对应的值
            elif nums[middle] < target:
                left = middle+1
            elif nums[middle] > target:
                right = middle-1
        return -1