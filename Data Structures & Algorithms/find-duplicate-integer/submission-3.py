class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: put the pointer inside the loop with
        # slow (1 step) and fast (2 steps) techinique
        slow = fast = 0
        step = 0
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # Phase 2: one pointer from the start, one from the meeting point,
        # both 1 jump at a time; they meet at the loop's entrance
        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow