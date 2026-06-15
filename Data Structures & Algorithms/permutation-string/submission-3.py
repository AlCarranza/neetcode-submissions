class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        need = Counter(s1)
        have = Counter(s2[:len(s1)])

        if need == have:
            return True
        
        l = 0

        for r in range(len(s1), len(s2)):

            have[s2[r]] += 1
            have[s2[l]] -= 1

            if have[s2[l]] == 0:
                del have[s2[l]]

            l += 1

            if need == have:
                return True

        return False