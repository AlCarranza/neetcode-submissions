from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        buckets = [[] for _ in range(len(nums)+1)]

        for n,v in count.items():
            buckets[v].append(n)
        
        res = []
        for bucket in range(len(buckets)-1, 0, -1):
            for num in buckets[bucket]:
                res.append(num)

                if len(res) == k:
                    return res
            