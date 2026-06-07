class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        res = 0
        my_set = set()

        for right in range(len(s)):
            while s[right] in my_set:
                my_set.remove(s[left])
                left += 1

            my_set.add(s[right])
            res = max(res, right - left + 1)

        return res