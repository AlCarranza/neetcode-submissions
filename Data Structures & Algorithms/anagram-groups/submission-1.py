from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # We'll track the frequency of each str, using the pattern
        # character counting, mapping each word
        anagrams = defaultdict(list)

        for s in strs:
            count = [0]*26

            for c in s:
                count[ord(c)-ord('a')] += 1

            key = tuple(count)

            anagrams[key].append(s)

        return list(anagrams.values())