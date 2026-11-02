"""
239.滑动窗口求最大值 / 栈与队列 / high
思路:暴力解法下每次变化都要进行一次扫描求最大值,使用单调队列,自动维护最大值在队列顶,并且定时弹出过期队列顶
卡点:注意此处的队列要存索引,存索引可以判断什么时候要滑出
"""


#单调队列

from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        dq = deque()   # 存索引，对应值单调递减
        res = []
        for i, x in enumerate(nums):
            # 1. 队尾小于等于当前值的都弹出，只有遇到大的情况,才不弹出.保证单调递减
            while dq and nums[dq[-1]] <= x:
                dq.pop()
            dq.append(i)

            # 2. 队首索引已滑出窗口（窗口左边界是 i-k+1）
            if dq[0] <= i - k:
                dq.popleft()

            # 3. 窗口长度达到 k 后开始记录
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res