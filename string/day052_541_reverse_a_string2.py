"""
541.反转字符串2 / 字符串 / easy
思路:变量阶段递增,先将字符串转换为list.再通过切片的方法来反转
卡点:字符串不可修改
"""

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # 分段反转
        # 记住字符串不可修改,此处要先转换数组再转换回字符串
        i = 0
        lst = list(s)
        while i < len(s):
            # 采用切片的方法来讲列表反转
            if i + k < len(s):
                lst[i:i + k] = lst[i:i + k][::-1]
            else:
                lst[i:len(s)] = lst[i:len(s)][::-1]
            i += 2 * k
        s = u"".join(lst)
        return s

