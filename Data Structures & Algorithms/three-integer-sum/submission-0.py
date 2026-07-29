class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [-4, -1, -1, 0, 1, 2]
        nums.sort()
        result = []

        for i in range(len(nums)):

            # Skip duplicate first numbers
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:

                total = nums[i] + nums[l] + nums[r]

                if total > 0:
                    r -= 1

                elif total < 0:
                    l += 1

                else:
                    result.append([nums[i], nums[l], nums[r]])

                    l += 1

                    # Skip duplicate left values
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return result