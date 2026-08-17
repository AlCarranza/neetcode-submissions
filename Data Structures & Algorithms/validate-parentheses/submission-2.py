class Solution:
    def isValid(self, s: str) -> bool:
            # We'll solve this using a stack

            pairs = {"{":"}", "[":"]", "(": ")"}
            stack = []

            for c in s:
                if c in pairs: # means it is an open symbol
                    stack.append(c)
                else:
                    if not stack:
                        return False

                    latest_symbol = stack.pop()
                    if c != pairs[latest_symbol]:
                        return False
                
            return not stack
