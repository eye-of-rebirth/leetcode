"""
1.两数之和 / 哈希表  /  easy
思路:遍历数组时，用字典记住"每个值出现过的索引"，对当前数只需 O(1) 查一下"它的补数（target - 当前数）之前是否出现过"，出现过就返回两个索引。
"""
#自我想出的方法,使用暴力解法,时间复杂度为O(n2)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        jg = []
        found = False
        has = set(nums)
        for x,i in enumerate(nums):
            temp = target - i
            if temp in has:
                for y,j in enumerate(nums):
                    if j == temp and y!=x:
                        jg.append(x)
                        jg.append(y)
                        found = True
                        break
                if found:
                    break
        return jg

# 使用字典的方法,通过字典记录一遍数组,后续查询的时候可以顺带返回下标
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}  # value -> index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []
