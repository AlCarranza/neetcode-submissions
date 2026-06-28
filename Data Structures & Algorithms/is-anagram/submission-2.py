class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

        # dic = Counter(s)

        # for w in t:
        #     dic[w] -= 1
        #     if dic[w] == 0:
        #         del dic[w]
        
        # return len(dic) == 0