class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"(":")","[":"]","{":"}"}

        stack = []

        for c in s:
            if c in pairs:
                stack.append(c)
            else:
                if not stack:
                    return False
                
                latest = stack.pop()

                if pairs[latest] != c:
                    return False
        
        return not stack