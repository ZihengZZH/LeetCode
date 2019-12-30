'''

You have a list of points in the plane. 
Return the area of the largest triangle that can be formed by any 3 of the points.

Example:
Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2
Explanation: 
The five points are show in the figure below. 
The red triangle is the largest.

Notes:
3 <= points.length <= 50.
No points will be duplicated.
-50 <= points[i][j] <= 50.
Answers within 10^-6 of the true value will be accepted as correct.

'''


import itertools


class Solution:
    def largestTriangleArea(self, points):
        max_area = 0
        for ii, jj, kk in itertools.combinations(points, 3):
            max_area = max(max_area, 0.5 * abs(ii[0] * kk[1] + \
                                                jj[0] * ii[1] + \
                                                kk[0] * jj[1] - \
                                                ii[0] * jj[1] - \
                                                jj[0] * kk[1] - \
                                                kk[0] * ii[1]))
        return max_area


if __name__ == "__main__":
    solu = Solution()
    input_1 = [[0,0],[0,1],[1,0],[0,2],[2,0]]
    input_2 = [[0,0],[0,1],[1,5],[0,2],[2,0]]
    print(input_1, solu.largestTriangleArea(input_1))
    print(input_2, solu.largestTriangleArea(input_2))