"""
This is a bfs-version of counting-islands problem in dfs section.
Given a 2d grid map of '1's (land) and '0's (water),
count the number of islands.
An island is surrounded by water and is formed by
connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:
11110
11010
11000
00000
Answer: 1

Example 2:
11000
11000
00100
00011
Answer: 3

Example 3:
111000
110000
100001
001101
001100
Answer: 3

Example 4:
110011
001100
000001
111100
Answer: 5
"""


def is_within_bounds(x, y, row, col):
    """Check if the coordinates are within the grid boundaries."""
    return 0 <= x < row and 0 <= y < col

def bfs(grid, start_x, start_y, visited):
    """Perform BFS to mark all parts of the current island."""
    row, col = len(grid), len(grid[0])
    queue = [(start_x, start_y)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited[start_x][start_y] = 1

    while queue:
        x, y = queue.pop(0)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_within_bounds(nx, ny, row, col) and not visited[nx][ny] and grid[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = 1

def check_and_initiate_bfs(grid, i, j, visited):
    """Initiate BFS if the current cell is an unvisited land part."""
    if grid[i][j] == 1 and not visited[i][j]:
        bfs(grid, i, j, visited)
        return 1
    return 0

def count_islands(grid):
    row, col = len(grid), len(grid[0])
    visited = [[0] * col for _ in range(row)]
    num_islands = 0

    for i in range(row):
        for j in range(col):
            num_islands += check_and_initiate_bfs(grid, i, j, visited)

    return num_islands
