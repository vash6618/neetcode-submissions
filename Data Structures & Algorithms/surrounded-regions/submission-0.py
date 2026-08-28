class Solution:
    def edge(self, row, col, m, n):
        if row ==0 or row == m-1 or col == 0 or col == n-1:
            return True
        return False

    def dfs(self, row, col, board) -> bool:
        board[row][col] = 'Y'
        for val in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
            new_row, new_col = row + val[0], col + val[1]
            if new_row < 0 or new_col < 0 or new_row >= len(board) or new_col >= len(board[row]):
                continue
            if board[new_row][new_col] == 'O':
                print(new_row, new_col)
                self.dfs(new_row, new_col, board)


    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        vis = [[False] * n] * m
        for row in range(m):
            for col in range(n):
                if self.edge(row, col, m, n) and board[row][col] == 'O':
                    self.dfs(row, col, board)

        for row in range(m):
            for col in range(n):
                if board[row][col] == 'Y':
                    board[row][col] = 'O'
                else:
                    board[row][col] = 'X'                   
