class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(s) < len(t):
            return ""

        l = best_l = formed = 0
        best_min = float("inf")

        window = defaultdict(int)
        need = Counter(t)

        for r, ch in enumerate(s):
            window[ch] += 1
            if ch in need and window[ch] == need[ch]:
                formed += 1

            while formed == len(need):
                if r - l + 1 < best_min:
                    best_min = r - l + 1
                    best_l = l
                
                out = s[l]
                window[out] -= 1
                if out in need and window[out] < need[out]:
                    formed -= 1
                l += 1
            
        return "" if best_min == float("inf") else s[best_l: best_l + best_min]
