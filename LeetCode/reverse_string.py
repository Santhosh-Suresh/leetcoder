class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        h = len(s)-1
        while h>l:
            s[h] , s[l] = s[l], s[h]
            h -= 1
            l += 1
