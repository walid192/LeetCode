class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows, cols = len(board), len(board[0])

        # Check rows
        for i in range(rows):
            s = set()
            for j in range(cols):
                if board[i][j] != ".":
                    if board[i][j] in s:
                        return False
                    s.add(board[i][j])

        # Check columns
        for i in range(cols):
            s = set()
            for j in range(rows):
                if board[j][i] != ".":
                    if board[j][i] in s:
                        return False
                    s.add(board[j][i])

        # Check 3x3 subgrids
        def isValidNine(r, c):
            s = set()
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    if board[i][j] != ".":
                        if board[i][j] in s:
                            return False
                        s.add(board[i][j])
            return True

        for i in range(0, rows, 3):
            for j in range(0, cols, 3):
                if not isValidNine(i, j):
                    return False

        return True
