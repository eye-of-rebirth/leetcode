"""
344.反转字符串 / 字符串 /easy
思路:左右两变量原地修改字符串
"""

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        #定义两个变量,左右两变量,相互逼近
        left = 0
        right = len(s)-1
        while left <= right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left+=1
            right-=1
        return s