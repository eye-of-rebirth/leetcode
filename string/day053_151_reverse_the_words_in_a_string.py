"""
151. 反转字符串中的单词 / 字符串  /middle
思路:传统上就是从后往前以空白为届反转列表,python里可以使用split把字符串切割成以单词为界限的列表,再反转一次即可
卡点:拼接字符串使用"".join(s)
"""

#传统解法
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        temp = []
        size = len(s)
        cot = size-1
        while cot >=0:
            if s[cot]!=" ":
                temp.append(s[cot])
            elif s[cot]==" " and temp :
                temp.reverse()
                res.append("".join(temp))
                temp = []
            cot-=1

        if temp:
            temp.reverse()
            res.append("".join(temp))

        return " ".join(res)

#split解法
    class Solution(object):
        def reverseWords(self, s):
            return " ".join(s.split()[::-1])#只要这一句,因为spllit会把空白元素当成切割符,把一段完整的字符串切成单词块