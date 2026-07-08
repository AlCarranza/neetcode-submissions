class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        """
            My chosen would be number 4, but 3 also is practical and correct
            4) prevents Hash overload and also space complexity is O(1), the downside
            is that assumes 'a' <= c <= 'z'
        """
        ## 1. Brute Force:
        # return sorted(s) == sorted(t)

        ## 2. Dict solution
        # dic = Counter(s)

        # for w in t:
        #     dic[w] -= 1

        #     if dic[w] == 0:
        #         del(dic[w])
        
        # return len(dic) == 0

        ## 3. Python practical solution
        # return Counter(s) == Counter(t)

        ## 4. Character counting solution (Optimized solution without dictionaries):
        if len(s) != len(t):
            return False

        counter = [0]*26

        for i in range(len(s)):
            counter[ord(s[i])-ord('a')] += 1
            counter[ord(t[i])-ord('a')] -= 1

        return all(c == 0 for c in counter)