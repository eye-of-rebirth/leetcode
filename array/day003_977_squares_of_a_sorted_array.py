"""
977.有序数的平方 / 数组 / Easy /9.17

思路:双端扫描+顺序指针 --i、j 负责从两端挑出"当前最大的平方值"，pos 负责把它放到结果数组的末尾。
卡点:开始时想要使用.sort()排序,但提高了时间复杂度
复杂度:空间O(n) 时间(n)

"""
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = [0] * n  # 学会使用这种方法定义同数量的list

        i, j, pos = 0, n - 1, n - 1  # 定义一个变量pos从后往前推进从而实现排序的功能
        while i <= j:
            if nums[i] * nums[i] > nums[j] * nums[j]:
                ans[pos] = nums[i] * nums[i]
                i += 1
            else:
                ans[pos] = nums[j] * nums[j]
                j -= 1
            pos -= 1

        return ans

"""
补充一个做法,使用归并的方法
思路:求分界点,从分界点向两端推进,并且兜底最终归并
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = -1      
        for idx, num in enumerate(nums):#idx表示为索引值,num为对应元素
            if num < 0:
                i = idx 
            else:
                break
        j = i + 1
        n =len(nums)
        #此处a即为分界点
        ans = []
        while i>=0 or j<n: 
            if i <0:
                ans.append(nums[j]**2)
                j+=1
            elif j>=n:
                ans.append(nums[i]**2)
                i-=1
            elif nums[i]**2>nums[j]**2:
                ans.append(nums[j]**2)
                j+=1
            else:
                ans.append(nums[i]**2)
                i-=1
        return ans
"""