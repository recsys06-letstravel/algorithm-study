# graph = {
#     (0,1): [(0,1),(1,0)],
#     (1,0): [(1,1),(2,0)]
# }
# print(graph[(0,1)])
#
# graph = {
#     (0, 1): [(0, 1), (1, 0)],
#     (2, 2):
# }
import collections


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        def dfs(i,j):
            if i < 0 or i >= len(grid) or \
                j < 0 or j >= len(grid[0]) or \
                grid[i][j] != '1':
                return

            grid[i][j] = 0

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i,j)
                    result += 1

        return result


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
grid3 = [["1","1","1"],["0","1","0"],["1","1","1"]]

sol = Solution()
print(sol.numIslands(grid3))