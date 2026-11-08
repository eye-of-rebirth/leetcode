"""
14. 最长公共前缀 / 字符串 /easy
思路 : 切片法比较
卡点: 切片左闭右开
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        temp = ""
        cot = 0
        if not strs:
            return res

        while True:
            temp = strs[0][0:cot + 1]
            for i in range(len(strs)):
                if cot == len(strs[i]):
                    return res
                if strs[i][0:cot + 1] != temp:
                    return res
            res = temp
            cot += 1
