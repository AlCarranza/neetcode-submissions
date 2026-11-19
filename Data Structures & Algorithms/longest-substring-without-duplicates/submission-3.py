class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tracking = set()
        l = 0
        ans = 0

        for r in range(len(s)):
            while s[r] in tracking:
                tracking.remove(s[l])
                l += 1
            
            tracking.add(s[r])
            ans = max(ans, r - l + 1)
        
        return ans
                
            