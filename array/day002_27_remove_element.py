"""
27.移除元素 / 数组 / Easy /9.16

思路:读写双指针,a（for 变量）是读指针，扫过所有元素；k是写指针，指向下一个合法元素该放的位置。
卡点:看到移除想到的是直接删除
复杂度:时间 O(n)，空间 O(1)

"""
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        for a in nums :
            if a != val:
                nums[k] = a
                k +=1
        return k
