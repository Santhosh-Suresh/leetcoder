#Problem statement: Minimize deviation in array
"""
https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/583/week-5-january-29th-january-31st/3622/
Problem type: Hard
"""
import bisect

class Solution( object ):

    #Instinct is to apply recursion here

    def odderize(self, nums):
        new_nums = []
        for item in nums:
            if item %2 == 0:
                new_nums.append(item//2)
            else:
                return nums
        return new_nums
    def minimumDeviation(self , nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(list(set(nums)))
        nums = self.odderize( nums )
        mi = nums[0]
        ma = nums [-1]
        one_odd_set = set()
        return self.minDeviation(nums, one_odd_set ,mi, ma)

    def minDeviation(self, nums, one_odd_set, mi, ma):
        """
        :params
            nums: list
            one_odd_set: set
            mi: int
            ma: int
        :return: int
        """
        #Trivial case: if there is 1 or 0 elements in the set, then the diff is 0.
        if len(nums) <= 1:
            return 0
        else:
            diff = ma - mi
            if (ma % 2 == 1) and (mi % 2 == 0) :
                return diff
            if (ma % 2 == 0) and (ma not in one_odd_set):
                nums.remove(ma)
                mid = ma//2
                mid_added= False
                if mid not in nums:
                    mid_added= True
                    bisect.insort(nums, mid)
                diff = min(diff, self.minDeviation(nums, one_odd_set, nums[0], nums[-1]))
                if mid_added:
                    nums.remove(mid)
                bisect.insort(nums, ma)

            if (mi %2 == 1):
                nums.remove(mi)
                mid  = 2*mi
                mid_added= False
                if mid not in nums:
                    mid_added = True
                    bisect.insort(nums,mid)
                one_odd_set.add(mid)
                diff = min(diff, self.minDeviation(nums, one_odd_set, nums[0], nums[-1]))
                if mid_added:
                    nums.remove(mid)
                one_odd_set.remove(mid)
                bisect.insort(nums, mi)
            return diff
