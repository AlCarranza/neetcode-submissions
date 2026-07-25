class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Naive solution
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]+nums[j] == target:
        #             return [i,j]

        # return [-1,-1]

        # Optimized solution
        needed = {}

        for i in range(len(nums)):
            need = target - nums[i]
            
            if nums[i] in needed:
                return[needed[nums[i]], i]

            needed[need]=i
            
        return [-1,-1]


                    