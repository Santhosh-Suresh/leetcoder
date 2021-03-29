class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ans = {}
        n = len(cost)
        if n == 0:
            return 0
        if n == 1:
            return cost[0]
        if n == 2:
            return min(cost[0], cost[1])

        ans[n - 1] = cost[n - 1]
        ans[n - 2] = cost[n - 2]
        j = n - 3
        while (j >= 0):
            ans[j] = cost[j] + min(ans[j + 1], ans[j + 2])
            j = j - 1

        return min(ans[0], ans[1])
