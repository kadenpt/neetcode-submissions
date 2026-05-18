class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        def backtrack(total, i):
            # 1 step away
            if i == n - 1 or i == n - 2:
                return total + cost[i]

            return min(
                backtrack(total + cost[i], i + 1),
                backtrack(total + cost[i], i + 2)
            )

        return min(backtrack(0, 0), backtrack(0, 1))
        