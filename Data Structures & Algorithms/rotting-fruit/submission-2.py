class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 2:
                    queue.append([row, col, 0])
        mins = 0
        while queue:
            row, col, level = queue.popleft()
            mins = max(mins, level)
            for dr, dc in [[-1,0], [1,0], [0,-1], [0,1]]:
                new_row, new_col = row + dr, col + dc
                if new_row < 0 or new_row >= len(grid) or new_col < 0 or new_col >= len(grid[row]):
                    continue
                elif grid[new_row][new_col] == 1:
                    grid[new_row][new_col] = 2
                    queue.append([new_row, new_col, level + 1])


        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    return -1
        return mins

        