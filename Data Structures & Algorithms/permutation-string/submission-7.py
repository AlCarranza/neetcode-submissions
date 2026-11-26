class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)

        if n > m:
            return False

        need = [0]*26
        window = [0]*26

        for i in range(len(s1)):
            need[ord(s1[i]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] += 1

        if need == window:
            return True

        for r in range(n,m):
            window[ord(s2[r]) - ord('a')] += 1
            window[ord(s2[r-n]) - ord('a')] -= 1
            
            if need == window:
                return True
            
        return False
            
