"""
459.重复的子字符串 / 字符串 / easy
思路:kmp算法
"""
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        next = [0] * n
        j = 0
        for i in range(1, n):
            while j > 0 and s[j] != s[i]:
                j = next[j - 1]
            if s[j] == s[i]:
                j += 1
            next[i] = j
        # 此处要取最后一位数字,这代表了最长相等前后缀,如果用的是max只是在max值所在的下标所在的位置的最长相等前后缀
        m = next[-1]

        # m>0才能说有重复部分,有可能存在重复子集
        if m > 0 and n % (n - m) == 0:
            return True
        else:
            return False

