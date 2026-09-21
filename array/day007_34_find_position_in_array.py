"""
34.在排序数组中查找元素的第一个和最后一个位置 / 数组 / Moderate
思路:左右两边位置二分查找,进行两次,并且要记得左右位置返回对应的数组索引
卡点:关于结果输出的返回值
复杂度:时间复杂度O(log n ) 空间复杂度 O(1)


"""
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right =len(nums)-1
        start = -1
        end = -1
        cz = 0
        #使用二分法找两边的边界,使用昨天学的查找对应下标的方法
        #下面先找左边界
        while left <=right:
            middle = (left+right)//2
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle -1
            else :
                right = middle-1
                cz = 1
        if cz == 1 :
            start = right+1

        left = 0
        right =len(nums)-1
        cz = 0

        while left <=right:
            middle = (left+right)//2
            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else :
                left = middle+1
                cz = 1
        if cz == 1 :
            end = left -1
        jg = [start,end]
        return jg