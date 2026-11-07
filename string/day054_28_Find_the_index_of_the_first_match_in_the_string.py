"""
28.找出字符串中第一个匹配的下标 / 字符串 / easy
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        i = 0
        while i <= len(haystack) - len(needle):
            j = 0
            while j < len(needle) and haystack[i + j] == needle[j]:
                j += 1
            if j == len(needle):  # 全部匹配
                return i
            i += 1  # 失败从下一个起点重来
        return -1