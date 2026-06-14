class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dic = {}

        for i in range(len(nums)):
            res = target - nums[i]
            if nums[i] in dic:
                return [dic.get(nums[i]), i]

            dic[res] = i

        return [-1,-1]



            