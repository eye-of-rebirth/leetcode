"""
69 . x的平方根 / 数组 / easy
思路:二分搜索查找,和34.很像
卡点:边界处理


"""

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        #中间数的平方和x做比较,如果小于x则数变中间
        #舍却小数部分
        l = 0
        r = x
        #什么时候停止循环
        while l <= r :
            m = (l + r ) // 2
            if m*m < x:
                l = m+1
            elif m*m > x:
                r = m-1
            else :
                return m
        return l-1
