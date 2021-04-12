"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):

"""


class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        n = 1000
        low = dict().fromkeys(range(1, n + 1), 1)
        high = dict().fromkeys(range(1, n + 1), 1000)
        ans = []

        for x in range(1, n + 1):
            self.binary_search(customfunction, z, ans, low, high, x)
            if x <= n:
                high[x + 1] = high[x]

        return ans

    def binary_search(self, customfunction, z, ans, low, high, x):

        if customfunction.f(x, low[x]) > z:
            high[x] = low[x]
            return
        if customfunction.f(x, high[x]) < z:
            return

        while high[x] > (low[x] + 1):
            if customfunction.f(x, high[x]) == z:
                ans.append([x, high[x]])
                return
            if customfunction.f(x, low[x]) == z:
                ans.append([x, low[x]])
                high[x] = low[x]
                return

            mid = (high[x] + low[x]) // 2

            if customfunction.f(x, mid) >= z:
                high[x] = mid
            else:
                low[x] = mid

            print(x, mid, low[x], high[x])

        else:
            if customfunction.f(x, high[x]) == z:
                ans.append([x, high[x]])
                return
            if customfunction.f(x, low[x]) == z:
                ans.append([x, low[x]])
                high[x] = low[x]
                return

        return