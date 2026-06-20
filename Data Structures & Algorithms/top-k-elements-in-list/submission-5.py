class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        buckets = [[] for _ in range(len(nums)+1)]
        
        for n, f in freq.items():
            buckets[f].append(n)

        res = []
        for bucket in range(len(buckets)-1, 0, -1):
            for num in buckets[bucket]:
                res.append(num)

                if len(res) == k:
                    return res
