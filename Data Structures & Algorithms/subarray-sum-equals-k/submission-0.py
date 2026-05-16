class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Prefix sum and hashmap pattern
        dic = {0:1}
        prefix = 0
        count = 0

        for num in nums:
            prefix += num

            if prefix - k in dic:
                count += dic[prefix-k]

            dic[prefix] = (dic.get(prefix,0)+1)

        return count