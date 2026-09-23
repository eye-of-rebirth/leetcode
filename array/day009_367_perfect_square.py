"""
367.有效的完全平方数 / 数组 / easy
思路: 使用二分查找
卡点: 无


"""


class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left = 0
        right = num
        while left <= right:
            middle = (left + right) // 2
            if middle * middle == num:
                return True
            elif middle * middle < num:
                left = middle + 1
            elif middle * middle > num:
                right = middle - 1
        return False

