from collections import deque
from typing import List
# https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        seen = set()
        q = deque()

        # Queue up all the zero values 
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    q.append((r, c))
                    seen.add((r, c))

    # Traverse level order wise and for each level and update distance
        coords = [(0,1), (1,0), (0,-1), (-1,0)]
        distance = 1
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                for rc, cc in coords:
                    r = row + rc
                    c = col + cc
                    # Add such element to back of queue also for next level traversal. In this way those who are not reachable to any zero in first attempt (i.e.first level), the new level is checked and hence length counter will increased by 1
                    if r >= 0 and r < rows and c >= 0 and c < cols and (r, c) not in seen:
                        mat[r][c] = distance
                        q.append((r, c))
                        seen.add((r, c))

            distance += 1
        return mat
    
matrixSol = Solution()
print(matrixSol.updateMatrix([[0,0,0],[0,1,0],[0,0,0]]))