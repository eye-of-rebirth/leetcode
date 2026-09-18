"""
209.长度最小的子数组 / 数组 / Moderate /9.18
思路:滑块思维,右针先探,左针后跟收缩,注意滑块本身的变化
卡点:开始没思路,使用双while太过繁琐,使用sum导致超时
复杂度:空间O(1) 时间O(n)


"""
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # 通过一个向右的探针,满足就左边收缩
        left = 0
        sum_zi = 0
        jg = float('inf')  #定义最大值
        # 又一次犯了边界错误注意切片和range函数的边界问题,python函数和方法里基本上都是左闭右开的只有一个例外那就是random.randint(a, b)
        # for right in range(0, len(nums)):
        #     sum_zi += nums[right]
        #     while sum_zi >= target:
        #         jg = min(jg, right - left + 1)
        #         sum_zi -= nums[left]
        #         left += 1
        #
        # return jg if jg != float('inf') else 0


        # 适合直接用昨天学的enumerate()函数
        for right,x in enumerate(nums):
            sum_zi += x
            while sum_zi >= target:
                jg = min(jg,right-left+1)
                sum_zi -= nums[left]
                left += 1
        return jg if jg != float('inf') else 0   #学习这种返回方法,省下一个在循环内的if
