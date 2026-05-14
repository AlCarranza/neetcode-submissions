from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # We can track the frequency and then apply the bucket sort strategy
        # then we filter for the top K
        frequency = defaultdict(int)

        for num in nums:
            frequency[num] += 1

        buckets = [[] for _ in range(len(nums)+1)]

        for val, freq in frequency.items():
            buckets[freq].append(val)

        res = []
        for freq in range(len(buckets)-1, -1, -1):
            for n in buckets[freq]:
                res.append(n)

                if len(res) == k:
                    return res
        
