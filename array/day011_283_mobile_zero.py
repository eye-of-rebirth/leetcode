"""
283.移动零 / 数组 / easy
思路:双指针原地修改,用解包组包来调换顺序
卡点:因为不知道怎么去调换顺序,使用了new数组的方法,增添了空间复杂度

"""
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = 0  # 指向下一个非零元素应该放置的位置
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        # 不需要 return
"""
原来的代码块
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #一个指针进行遍历,一个左边,一个右边
        l = 0
        r = -1 
        news = [0]* len(nums)
        for a , x in enumerate(nums):
            if x == 0:
                news[r] = x
                r -= 1
            else :
                news[l] = x
                l += 1
        for i in range(len(nums)):
            nums[i] = news[i]
        return nums
"""