"""
5.最小回文子集 / 字符串 / middle
思路:左右扩展
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) < 1:
            return ""

        start, end = 0, 0  # 记录最长回文子串的起始和结束索引

        for i in range(len(s)):
            # 情况1：以单个字符为中心（奇数长度），例如 "aba"
            len1 = self.expandAroundCenter(s, i, i)
            # 情况2：以两个字符之间的空隙为中心（偶数长度），例如 "abba"
            len2 = self.expandAroundCenter(s, i, i + 1)

            max_len = max(len1, len2)

            # 如果找到了更长的回文串，更新起始和结束位置
            if max_len > end - start:
                # 这里的计算需要稍微推导一下：
                # 如果是奇数长度 (len=5, i=2)，起点是 i - len//2 = 2 - 2 = 0
                # 如果是偶数长度 (len=4, i=1)，起点是 i - (len-1)//2 = 1 - 1 = 0
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start:end + 1]

    def expandAroundCenter(self, s, left, right):
        # 只要左右不越界，且字符相等，就继续向外扩展
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # 退出循环时，right - left - 1 就是当前回文串的长度
        return right - left - 1