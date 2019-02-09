/*

Given n non-negative integers a1, a2, ..., an, 
where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

*/

package summer;

/**
 *
 * @author Ziheng
 */
public class Summer {
    
    public static int maxArea(int[] height){
        int left = 0, right = height.length - 1; // Two pivots
	int maxArea = 0;
	while (left < right) {
		maxArea = Math.max(maxArea,Math.min(height[left],height[right])*(right - left));
		if (height[left] < height[right]) left++;
                else right--;
                // Focus on height and find the largest
                // Regardless of long
        }
	return maxArea;
    }
    
    public static void main(String[] args) {
        int[] heght = {1,1,10,3,1,4,5,20,23,4,0,10};
        System.out.println(maxArea(heght));
    }
    
}
