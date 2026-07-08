class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ## Brute Force:
        # return sorted(s) == sorted(t)
        
        ## Python practical solution
        # return Counter(s) == Counter(t)

        ## Optimal solution 1
        # dic = Counter(s)

        # for w in t:
        #     dic[w] -= 1

        #     if dic[w] == 0:
        #         del(dic[w])
        
        # return len(dic) == 0

        ## Character counting solution (Optimized solution without dictionaries):
        if len(s) != len(t):
            return False

        counter = [0]*26

        for i in range(len(s)):
            counter[ord(s[i])-ord('a')] += 1
            counter[ord(t[i])-ord('a')] -= 1

        return all(c == 0 for c in counter)
