class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        ## Brute solution
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        
        # return [-1,-1]
        
        ## Optimal solution
        dic = {}

        for i in range(len(nums)):
            r = target - nums[i]

            if nums[i] in dic:
                return [dic.get(nums[i]), i]

            dic[r] = i

        return [-1, -1]
            