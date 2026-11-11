"""
3.无重复字符的最大字串 / 字符串 / middle
思路:"惰性更新"维护滑动窗口，用字典记录字符最新索引，遇重复字符则将左指针跳至其上次出现位置的后一位，并实时更新最大长度
卡点:如何通过索引大小排除字典里已滑出窗口的“幽灵节点”，以及何时统一更新字典和指针
"""


# 惰性更新+滑动窗口
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 滑动窗口
        if not s:
            return 0
        n = len(s)
        left = 0
        right = 0
        res = 0
        has = {}

        while right < n:
            # 先进行向右遍历
            if s[right] in has and has[s[right]] >= left:
                left = has[s[right]] + 1
                has[s[right]] = right
            else:
                has[s[right]] = right
            res = max(res, right - left + 1)
            right += 1
        return res

# 更好的方法,只要移动左窗口就行,位置更新放到循环中,每次都会主动更新
# while right < n:
#     # 1. 遇到重复字符，且在当前窗口内，移动左指针
#     if s[right] in has and has[s[right]] >= left:
#         left = has[s[right]] + 1

#     # 2. 不管重不重复，都要把最新位置写进字典
#     has[s[right]] = right

#     # 3. 计算当前窗口长度，更新 res
#     res = max(res, right - left + 1)

#     right += 1

