class Solution:
    def maxArea(self, height: list[int]) -> int:
        l = 0
        r = len(height) - 1
        max = 0
        while l <= r:
            if height[l] <= height[r]:
                s = height[l] * (r-l)
                if s > max :
                    max = s
                l = l + 1
            else:
                s = height [r] * (r-l)
                if s > max:
                    max = s
                r = r -1
        return max
