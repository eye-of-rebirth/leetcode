"""
49.异位字母词的分组 / 哈希  / middle
思路:将每个字符串中26个字母的出现次数构造成元组作为哈希表的键,相同键的字符串归入同一组。
卡点:1.字母出现的次数列表边做元组,作为字典的键
    2.字典的值是列表,需要通过setdefault实现对应值的初始化
"""
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        #这道题的做法是把每个词字母出现的次数列表边做元组,作为字典的键,然后把对应的单词加入值的列表中(通过setdefault实现对应值的初始化)
        n = len(strs)
        res = dict()
        x = []

        for i in range(n):
            cut = [0]*26
            for j in strs[i]:
                cut[ord(j)-ord('a')]+=1
            res.setdefault(tuple(cut), []).append(strs[i])
            #setdefault的作用:这个签名第一次出现就建个空 list，然后把当前词塞进去；已经出现过就直接往原 list 里塞
        return res.values()