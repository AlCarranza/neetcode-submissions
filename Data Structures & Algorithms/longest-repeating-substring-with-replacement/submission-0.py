class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = 0
        l = 0
        dic = collections.defaultdict(int)
        longest = 0

        for r in range(len(s)):
            dic[s[r]] += 1

            while (r - l + 1) - max(dic.values()) > k:
                dic[s[l]] -= 1
                l+=1

            longest = max(longest, r - l + 1)

        return longest
