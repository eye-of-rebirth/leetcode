"""
1798.你能构造最大连续数的数目 / 数组 / Moderate
思路:贪心算法,以及如果能凑出前 x 个值，并且你有一个值 v，那么就能凑出所有v+x的值
卡点:没能想到v+x这一步
"""


class Solution(object):
    def getMaximumConsecutive(self, coins):
        """
        :type coins: List[int]
        :rtype: int
        """
        coins.sort()
        reach = 0
        for v in coins:
            if v > reach + 1:
                break
            reach += v
        #因为reach得到的是连续数的大小,但要求输出的是数目所以要加1
        return reach+1