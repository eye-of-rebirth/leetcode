"""
128. 最长连续序列 / 哈希 / middle
思路:本题是不能排序的，因为排序的时间复杂度是 O(nlogn),采用set,先找开头,然后遍历后续求长度
卡点:不知道怎么求开头
"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        has = set(nums)
        m = len(has)
        js = 0

        for i in has:
            # 遍历哈希找到开头,只有找到开头才开始下一步,所以时间复杂度不会提升
            if i - 1 in has:
                continue

            # 此处j就是开头,遍历后续求长度
            j = i + 1
            while j in has:
                j += 1
            js = max(js, j - i)

            # 因为一半后没可能出现更大的连续
            if js * 2 >= m:
                break

        return js



