from typing import List
# https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # keep track of row and column lengths of grid to access later
        m = len(grid)
        n = len(grid[0])

        def destroyIsland(r,c): # recursive DFS helper
            grid[r][c] = "2" # set this spot to a different value to avoid infinite loops
            for (row,col) in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]: # 4-dimensionally adjacent locations
                if 0 <= row < m and 0 <= col < n and grid[row][col] == "1": # if not out of bounds and part of the island
                    destroyIsland(row,col) # destroy the rest of the island (set to "2")

        ans = 0 # answer
        for i, row in enumerate(grid): # get rows from grid
            for j, element in enumerate(row): # go through the row
                if element == "1": # if we hid land
                    destroyIsland(i,j) # destroy this island
                    ans += 1 # we found an island
        return ans
        