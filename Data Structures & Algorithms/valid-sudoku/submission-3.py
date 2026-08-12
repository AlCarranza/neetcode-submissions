class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Solution that involves only 1 set to maintain
        seen = set()

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                
                if num == ".":
                    continue
                # The heart of this solution using tupples which are immutable
                row = ("row",r,num)
                col = ("col",c,num)
                box = ("box",r // 3,c // 3,num)

                if row in seen or col in seen or box in seen:
                    return False

                seen.add(row)
                seen.add(col)
                seen.add(box)

        return True