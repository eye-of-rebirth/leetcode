"""
844.比较含退格符的字符串 / 数组 / easy
思路:不需要改变原字符串,通过比较的方式来解题
卡点:执着于改变字符串

"""

class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = len(s)-1
        j = len(t)-1
        skips = 0
        skipt = 0

        while i>=0 or j>=0:
            while i>=0:
                if s[i] == "#":
                    skips+=1
                    i-=1
                elif skips > 0:
                    skips-=1
                    i-=1
                else :
                    break
            while j>=0:
                if t[j] == "#":
                    skipt +=1
                    j-=1
                elif skipt >0:
                    skipt -=1
                    j-=1
                else:
                    break
            if j>=0 and i>=0:
                if s[i] != t[j]:
                    return False
            elif j>=0 or i>=0:
                return False
            i-=1
            j-=1
        return True



# 10.23二刷
class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # 退格符,从后往前遍历
        i = len(s)-1
        j = len(t)-1
        #用于遇到退格跳过
        skips = 0
        skipt = 0

        while i>=0 or j>=0:
            # 找到s的下一位有效数字
            while i>=0 :
                if s[i] == '#':
                    skips+=1
                    i-=1
                elif skips>0:
                    skips-=1
                    i-=1
                else:
                    break
            #找到t的下一位有效数字
            while j>=0:
                if t[j] == '#':
                    skipt+=1
                    j-=1
                elif skipt>0:
                    skipt-=1
                    j-=1
                else:
                    break
            #如果条件合适就进行判断
            if i>=0 and j>=0:
                if s[i]!=t[j]:
                    return False
            #兜底(ch)
            elif i>=0 or j>=0:
                return False
            i-=1
            j-=1

        return True
