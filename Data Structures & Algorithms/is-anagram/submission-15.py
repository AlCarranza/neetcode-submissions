from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        counter = defaultdict(int)

        for i in range(len(s)):
            counter[s[i]] += 1
            counter[t[i]] -= 1
        
        return all(v == 0 for v in counter.values())
        