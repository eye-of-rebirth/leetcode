"""
85.最后一个单词的长度 / 数组 / easy
思路:直接从后开始计数
卡点:注意边界,已经空格存在在最后,以及就一个单词的可能

"""



class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        js = 0
        for x in range(len(s)-1,-1,-1):
            if s[x]!=" ":
                js+=1
            elif js != 0 and s[x] == " ":
                return js
        return js