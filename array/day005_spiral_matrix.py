"""
59.螺旋矩阵 / 数组 / Moderate / 9.19
思路:四方边界法,遍历后边界收缩,直到收缩完毕/或者多次循环迭代并且特殊考虑
卡点:不知道数组矩阵怎么定义和纯储,以及边界处理不干净



"""
#四方边界法(推荐)
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0] * n for _ in range(n)]
        top, bottom, left, right = 0, n - 1, 0, n - 1
        num = 1

        while top <= bottom and left <= right:
            # 上边
            for j in range(left, right + 1):
                matrix[top][j] = num
                num += 1
            top += 1

            # 右边
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1

            # 下边
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    matrix[bottom][j] = num
                    num += 1
                bottom -= 1

            # 左边
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    matrix[i][left] = num
                    num += 1
                left += 1

        return matrix


#多层迭代型(循环)
"""
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0] * n for _ in range(n)]
        num = 1

        for layer in range(n // 2 + 1):
            start = layer
            end = n - layer - 1

            for j in range(start, end):
                matrix[start][j] = num
                num += 1
            for i in range(start, end):
                matrix[i][end] = num
                num += 1
            for j in range(end, start, -1):
                matrix[end][j] = num
                num += 1
            for i in range(end, start, -1):
                matrix[i][start] = num
                num += 1

        if n % 2 == 1:
            matrix[n // 2][n // 2] = n ** 2
        return matrix
"""