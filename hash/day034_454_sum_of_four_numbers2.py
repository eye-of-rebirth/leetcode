"""
454.四数相加2 / 哈希表 / middle
思路:先用两数相加进入字典,再通过遍历后两个数组count值
"""

class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        hashmap = dict()
        for x in nums1:
            for y in nums2:
                if x+y in hashmap:
                    hashmap[x+y]+=1
                else:
                    hashmap[x+y]=1
        count = 0
        for i in nums3:
            for j in nums4:
                if 0-i-j in hashmap:
                    count+=hashmap[0-i-j]
        return count