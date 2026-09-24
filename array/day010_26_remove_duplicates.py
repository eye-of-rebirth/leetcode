"""
26.移除有序数组的重复项 / 数组 / easy
思路:看到原地移除,想到快慢指针的方法,和enumerate()
卡点:无


"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=0
        for a , x in enumerate(nums):
            if a == 0:
                nums[k] = x
                k += 1
            elif a != 0 and x != nums[a-1]:
                nums[k] = x
                k += 1
        return k