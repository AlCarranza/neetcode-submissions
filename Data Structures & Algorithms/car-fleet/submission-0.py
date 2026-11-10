class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True) # closest to target first
        stack = [] # arrival time of each fleet's leader

        for p, s in cars:
            t = (target - p) / s
            if not stack or t > stack[-1]:
                stack.append(t) # slower than the fleet ahead → new fleet
            # else: catches up → joins that fleet, nothing to push
        
        return len(stack)