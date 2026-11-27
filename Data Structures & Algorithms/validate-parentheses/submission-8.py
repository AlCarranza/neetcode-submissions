class Solution:
    def isValid(self, s: str) -> bool:
        combinations = {"(":")", "[":"]", "{":"}"}
        stack = []

        for ch in s:
            if ch in combinations:
                stack.append(ch)
            else:
                if not stack:
                    return False

                out = stack.pop()
                if combinations[out] != ch:
                    return False
        
        return not stack
                
            