"""
35. 搜索插入位置 / 数组 / easy
思路:二分搜索法
卡点:索引位置即为middle或是循环退出时的left或right
复杂度:时间复杂度O(log n) 空间复杂度O(1)


"""



class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return left
