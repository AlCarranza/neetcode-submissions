class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tracking = set()
        l = ans = 0

        for r, ch in enumerate(s):
            while ch in tracking:
                tracking.remove(s[l])
                l += 1

            tracking.add(ch)
            ans = max(ans, r - l + 1)
        
        return ans