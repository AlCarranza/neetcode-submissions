class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Brute force
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True

        # return False

        # Optimized algorightm
        my_set = set()

        for num in nums:
            if num in my_set:
                return True
            my_set.add(num)
        return False
