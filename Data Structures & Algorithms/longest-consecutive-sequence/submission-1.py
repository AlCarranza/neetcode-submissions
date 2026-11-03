class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = set(nums)
        longest = 0

        for n in dic:
            if n-1 not in dic: # then it is an start
                length = 1
                while n+length in dic:
                    length +=1
                longest = max(longest, length)
        
        return longest
