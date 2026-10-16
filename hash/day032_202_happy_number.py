"""
202.快乐数 / 哈希表 / easy
思路:建一个set去存储过程中产生的值,如果出现不在set的值就储存,如果在set就直接返回错误值
"""

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        has = set()
        has.add(n)
        m=n
        x=0
        while m!=1:
            #通过一个循环去求各个位置的平方和
            x=0
            while m!=0:
                x=x+(m%10)**2
                m=m/10
            if x not in has:
                has.add(x)
                m=x
            elif x in has:
                return False
        return True