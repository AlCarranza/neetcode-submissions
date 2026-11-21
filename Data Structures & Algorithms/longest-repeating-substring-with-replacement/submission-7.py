class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        l = max_freq = ans = 0

        for r, ch in enumerate(s):
            count[ch] += 1
            max_freq = max(max_freq, count[ch])
            while (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)

        return ans