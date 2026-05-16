class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s)-1
        letter = 'a'

        while left < right:
            letter = s[left]
            s[left] = s[right]
            s[right] = letter

            left+=1
            right-=1

        return s
