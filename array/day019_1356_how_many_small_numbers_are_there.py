
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        res = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            cnt = 0
            for j in range(len(nums)):
                if j == i:
                    continue
                if nums[i] > nums[j]:
                    cnt += 1
            res[i] = cnt
        return res