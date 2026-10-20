"""
15.三数之和  / 哈希 / middle
思路:三数之和双指针一句话思路：先排序，固定第一个数 nums[i]，在它右边用 left、right 双指针向中间收缩，根据三数之和与 0 的大小移动指针，并跳过重复元素。
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 使用双指针的做法
        nums.sort()
        res = []
        if len(nums) < 3:
            return []

        for i in range(len(nums) - 2):
            # 这一步是开头元素的去重
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 双指针
            left = i + 1
            right = len(nums) - 1

            while left < right:
                if nums[i] + nums[left] + nums[right] > 0:
                    right -= 1

                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1

                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # 在找到答案后再去去重,找到之前去重无意义
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return res


#提供一个哈希解法
class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue

            seen = set()
            j = i + 1
            while j < n:
                target = -nums[i] - nums[j]
                if target in seen:
                    res.append([nums[i], target, nums[j]])
                    # 去重：跳过相同的 nums[j]
                    while j + 1 < n and nums[j] == nums[j+1]:
                        j += 1
                seen.add(nums[j])
                j += 1

        return res