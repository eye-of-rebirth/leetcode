"""
383.赎金卷 / 哈希 / easy
思路:同day30.242,就是通过数组来统计出现次数
"""
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        cnt = [0]*26
        for x in magazine:
            cnt[ord(x)-ord('a')]+=1
        for y in ransomNote:
            cnt[ord(y)-ord('a')]-=1
        for i in cnt:
            if i < 0:
                return False
        return True