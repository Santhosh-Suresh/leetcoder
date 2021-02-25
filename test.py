class Solution( object ):
    def minimumDeviation(self , nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        if len(nums) <= 1:
            return 0
        else:
            mi = min(nums)
            ma = max(nums)
