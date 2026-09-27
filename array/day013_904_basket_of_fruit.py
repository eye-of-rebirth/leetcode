"""
904.水果成篮 / 数组 /. Moderate
思路:滑块思维.并且把篮子作为储存的容器
卡点:不知道篮子怎么处理

"""




class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        # 初始化两个篮子及它们最后一次出现的索引
        basket1 = fruits[0]
        basket2 = -1
        last1 = 0
        last2 = -1

        left = 0
        max_fruits = 0

        for right, f in enumerate(fruits):
            if f == basket1:
                # 属于篮子1，更新最后出现的位置
                last1 = right
            elif basket2 == -1 or f == basket2:
                # 属于篮子2，更新最后出现的位置
                basket2 = f
                last2 = right
            else:
                # 遇到了第三种水果，必须丢弃一个篮子
                if last1 < last2:
                    # 篮子1的水果更早断档，丢弃篮子1
                    left = last1 + 1
                    basket1 = f
                    last1 = right
                else:
                    # 篮子2的水果更早断档，丢弃篮子2
                    left = last2 + 1
                    basket2 = f
                    last2 = right

            # 更新最大收集数量
            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits