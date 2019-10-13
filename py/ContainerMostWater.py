'''

Given n non-negative integers a1, a2, ..., an, 
where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

'''


class Solution:
    '''
    AREA = HEIGHT * WIDTH
    target to find the max AREA
    keep WIDTH starting from the max
    only care HEIGHT in each loop
    '''
    def maxArea(self, height):
        result = 0
        ii, jj = 0, len(height) - 1
        while ii < jj:
            hh = min(height[ii], height[jj])
            result = max(result, (jj-ii)*hh)
            # area still max when left moving right
            while height[ii] <= hh and ii < jj:
                ii += 1
            # area still max when right moving left
            while height[jj] <= hh and ii < jj:
                jj -= 1
        return result

if __name__ == '__main__':
    solu = Solution()
    inputs = [4,6,10,1,3,1,7]
    print(inputs, solu.maxArea(inputs))