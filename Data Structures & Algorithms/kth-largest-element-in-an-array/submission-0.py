class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        # Create max heap
        for num in nums:
            negativeNumber = -1 * num
            heapq.heappush(maxHeap, negativeNumber)

        print(maxHeap)
        while k > 1:
            print(heapq.heappop(maxHeap))
            k -= 1
        
        return -1 * maxHeap[0]
