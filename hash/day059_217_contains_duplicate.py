"""
217.存在重复元素 / 哈希表 / easy
思路:使用set(遇到查找时用set速度快,时间复杂度低)
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        set1 = set()
        for i in nums:
            if i not in set1:
                set1.add(i)
            else :
                return True
        return False