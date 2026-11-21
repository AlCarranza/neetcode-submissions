class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        if n > m:
            return False

        need = [0]*26
        window = [0]*26

        for i in range(n):
            need[ord(s1[i]) - 97] += 1
            window[ord(s2[i]) - 97] += 1
        
        if need == window:
            return True


        for right in range(n, m):
            window[ord(s2[right]) - 97] += 1
            window[ord(s2[right-n]) - 97] -= 1
            
            if need == window:
                return True

        return False
