class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) - 1

        max_heap = []
        for key in count:
            heapq.heappush(max_heap, (count.get(key, 0), key))
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(max_heap)[1])
        return res