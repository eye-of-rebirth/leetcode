"""
18.四数之和 / 哈希 / middle
思路:三数循环外面套一层循环
卡点: 在去重的循环过程中,要注意会不会超限
"""
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 直接在三数循环里面套一层
        nums.sort()
        n = len(nums)
        res = []

        if n<4:
            return []
        for a in range(n):
            if target>=0 and nums[a]>target:
                break
            if a>0 and nums[a]==nums[a-1]:
                continue
            b=a+1
            while b<n-2:
                left = b+1
                right = n-1
                while left<right:
                    x = nums[a]+nums[b]+nums[left]+nums[right]
                    if x<target:
                        left+=1
                    if x>target:
                        right-=1
                    if x==target:
                        res.append([nums[a],nums[b],nums[left],nums[right]])
                        right-=1
                        left+=1
                        while left < right and nums[right]==nums[right+1]:
                            right-=1
                        while left < right and nums[left]==nums[left-1]:
                            left+=1
                b+=1
                while b<n and nums[b]==nums[b-1]:
                    b+=1
        return res