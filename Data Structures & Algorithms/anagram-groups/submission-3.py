class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tracker = defaultdict(list)

        for word in strs:
            counter = [0]*26
            for l in word:
                counter[ord(l) - ord('a')] += 1
            
            key = tuple(counter)
            tracker[key].append(word)
        
        # res = []
        # for arr in tracker.values():
        #     res.append(arr)

        # return res

        return list(tracker.values())
            


