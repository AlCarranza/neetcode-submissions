class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        maximum = 0

        while l < r:
            area = (r - l)*min(heights[r],heights[l])
            maximum = max(maximum, area)

            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1

        return maximum