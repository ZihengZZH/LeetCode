'''

On a N * N grid, we place some 1 * 1 * 1 cubes.
Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).
Return the total surface area of the resulting shapes.

Example 1:
Input: [[2]]
Output: 10

Example 2:
Input: [[1,2],[3,4]]
Output: 34

Example 3:
Input: [[1,0],[0,2]]
Output: 16

Example 4:
Input: [[1,1,1],[1,0,1],[1,1,1]]
Output: 32

Example 5:
Input: [[2,2,2],[2,1,2],[2,2,2]]
Output: 46

Note:
1 <= N <= 50
0 <= grid[i][j] <= 50

'''

class Solution:
    # complexity O(n^2)
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res, low, size = 0, 0, len(grid)
        for i in range(size):
            for j in range(size):
                if grid[i][j] != 0:
                    res += grid[i][j]*4 + 2 # surface area within a tower
                if j < size-1:
                    res -= 2*min(grid[i][j], grid[i][j+1]) # horizontal common plane
                if i < size-1:
                    res -= 2*min(grid[i][j], grid[i+1][j]) # vertical common plane
        return res


if __name__ == "__main__":
    input_lst = [[2,2,2],[2,1,2],[2,2,2]]
    solu = Solution()
    print(input_lst, solu.surfaceArea(input_lst))
