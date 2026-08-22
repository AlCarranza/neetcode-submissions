class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        dq = deque()

        for r in range(len(nums)):
            # Remove small values
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()

            # Add current index
            dq.append(r)

            # Remove values outside the window
            if dq[0] < r - k + 1:
                dq.popleft()
            
            # Window has reach the size k:
            if r >= k - 1:
                result.append(nums[dq[0]])

        return result

