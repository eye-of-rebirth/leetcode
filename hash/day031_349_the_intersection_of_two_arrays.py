"""
349.两不同集合的交点
思路:只关心“元素是否存在”“是否重复”，而不需要存储键值对、计数或顺序时，就用 set
卡点:开始的时候用双list时间复杂度高
"""
#第一遍使用的方法效率低下
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        has =[]
        for i in nums1:
            if i not in has and i in nums2:
                has.append(i)
        return has

#采用集合,set会自动去重
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s1 = set(nums1)
        res = set()
        for num in nums2:
            if num in s1:
                res.add(num)
        return list(res)