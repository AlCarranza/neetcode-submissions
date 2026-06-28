class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ## Solution A:
        if len(s) != len(t):
            return False
        
        count = [0]*26
        for i in range(len(s)):
            count[ord(s[i])-ord('a')] += 1
            count[ord(t[i])-ord('a')] -= 1
        
        return all(c == 0 for c in count)

        ## Solution B:
        #return Counter(s) == Counter(t)

        ## Solution C:
        # dic = Counter(s)

        # for w in t:
        #     dic[w] -= 1
        #     if dic[w] == 0:
        #         del dic[w]
        
        # return len(dic) == 0