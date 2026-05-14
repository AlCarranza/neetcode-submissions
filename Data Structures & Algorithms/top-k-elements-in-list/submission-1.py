from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # We'll use the pattern of bucket sort and store in the dic the 
        # frequency of each number
        frequency = defaultdict(int)

        for num in nums:
            frequency[num] += 1

        buckets = [[] for _ in range(len(nums)+1)]

        for val, freq in frequency.items():
            buckets[freq].append(val)

        result = []
        for freq in range(len(buckets)-1, 0, -1):
            for num in buckets[freq]:
                result.append(num)

                if len(result) == k:
                    return result