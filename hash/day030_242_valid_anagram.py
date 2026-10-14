"""
242.有效字母异位词
思路:暴力的去解,通过计数去解决,这边使用了hash表cnt,以及ord()函数表示各个字符

"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #计数数组一般就用cnt数组哈希表来
        cnt = [0]*26

        #python里面的字符编码ord()把字符转换为ascii
        for i in s:
            cnt[ord(i)-ord('a')] += 1
        for j in t:
            cnt[ord(j)-ord('a')] -= 1
        for x in range(26):
            if cnt[x]!=0:
                return False
        return True