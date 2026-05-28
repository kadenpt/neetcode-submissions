class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        min_heap = []
        for num in arr:
            distance = abs(num - x)
            heapq.heappush(min_heap, (distance, num))
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(min_heap)[1])
        return sorted(res)
