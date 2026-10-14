
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for row in board:
            seen = set()
            for num in row:
                if num != ".":
                    if num in seen:
                        return False
                    seen.add(num)

        # Check columns
        j = 0
        while j < len(board[0]):
            seen = set()
            i = 0

            while i < len(board):
                num = board[i][j]

                if num != ".":
                    if num in seen:
                        return False
                    seen.add(num)

                i += 1
            j += 1

        # Check 3x3 boxes
        limit_i = 3
        limit_j = 3

        while limit_j <= len(board[0]):
            while limit_i <= len(board):
                seen1 = set()
                i = limit_i - 3

                while i < limit_i:
                    j = limit_j - 3

                    while j < limit_j:
                        num = board[i][j]

                        if num != ".":
                            if num in seen1:
                                return False
                            seen1.add(num)

                        j += 1
                    i += 1

                limit_i += 3

            limit_i = 3
            limit_j += 3

        return True
