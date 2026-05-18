class Solution:

    # [["Q", ".", ".", "."],
    #  [".", ".", ".", "Q"]
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        # [[".", ".", ".", "."], ... ]
        state = []

        if n == 1:
            return [["Q"]]

        for i in range(n):
            # add empty list
            state.append([])
            for j in range(n):
                state[i].append(".")
    
        # helper function to check if a queen placed at x y is valid
        def isLegal(x: int, y: int, board: List[List[str]]) -> bool:
            # Check if queen already there:
            if board[y][x] == "Q":
                return False

            for i in range(n):
                if board[i][x] == "Q":
                    return False
                if board[y][i] == "Q":
                    return False

            i = 1
            while i < n:
                # top left, both decrease
                if x - i >= 0 and y - i >= 0:
                    if board[y-i][x-i] == "Q":
                        return False
                # top right, x increases, y decreases
                if x + i < n and y - i >= 0:
                    if board[y-i][x+i] == "Q":
                        return False
                # bottom left, x deceases, y increases
                if x - i >= 0 and y + i < n:
                    if board[y+i][x-i] == "Q":
                        return False
                if x + i < n and y + i < n:
                    if board[y+i][x+i] == "Q":
                        return False
                i += 1

            return True
        
        # Incoming board in form [[".", ".", ".", "."], ...]
        # Return board in form ["....", "...."]
        def formatBoard(board: List[List[str]]) ->List[str]:
            newBoard = []
            currentString = ""
            for i in range(n):
                for j in range(n):
                    currentString += board[i][j]

                newBoard.append(currentString)
                currentString = ""
            return newBoard

        
        def dfs(row, current: List[List[str]]):
            if row == n:
                res.append(formatBoard(current).copy())
                return

            for i in range(n):
                if isLegal(i, row, current):
                    current[row][i] = "Q"
                    dfs(row + 1, current)
                    current[row][i] = "."


        dfs(0, state)
            
        return res


