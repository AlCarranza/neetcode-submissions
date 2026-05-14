from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Easy but not optimal solution
        # return sorted(s) == sorted(t)

        # Optimal but more complex is Character counting
        if len(s) != len(t):
            return False

        count = [0]*26
        for i in range(len(s)):
            count[ord(s[i])-ord('a')] += 1
            count[ord(t[i])-ord('a')] -= 1
        
        return all(c == 0 for c in count)
