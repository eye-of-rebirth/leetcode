"""
347.前k个高频元素 / 栈与队列 / middle
思路:小顶堆,会自动排序,把根节点pop掉,根节点必定小于左右孩子
卡点:元组的排序,return的循环解包写法
"""

import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #先用字典来记录数量
        r_dict = {}
        for x in nums:
            r_dict[x] = r_dict.get(x, 0) + 1
        # 2. 小顶堆，按频率排序，只留 k 个
        heap = []
        for key, value in r_dict.items():
            heapq.heappush(heap, (value, key))
            if len(heap) > k:
                heapq.heappop(heap)
        return [x for _, x in heap]