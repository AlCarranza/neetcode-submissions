class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(s) < len(t):
            return ""
        
        need = Counter(t)
        window = defaultdict(int)
        best_len = float("inf")
        l = formed = best_l = 0
        required = len(need)

        for r, ch in enumerate(s):
            window[ch] += 1

            if ch in need and need[ch] == window[ch]:
                formed += 1

            while formed == required: # Valid window
                if r - l + 1 < best_len:
                    best_len = r - l + 1
                    best_l = l
                
                out = s[l]
                window[out] -= 1
                if out in need and window[out] < need[out]:
                    formed -= 1
                l += 1
        
        return "" if best_len == float("inf") else s[best_l: best_l + best_len]

        
