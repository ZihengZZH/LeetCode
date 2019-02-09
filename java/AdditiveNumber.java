/*

Additive number is a string whose digits can form additive sequence.
A valid additive sequence should contain at least three numbers. 
Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

For example:
"112358" is an additive number because the digits can form an additive sequence: 1, 1, 2, 3, 5, 8.
1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8

"199100199" is also an additive number, the additive sequence is: 1, 99, 100, 199.
1 + 99 = 100, 99 + 100 = 199

Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.
Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

Follow up:
How would you handle overflow for very large input integers?

*/

package summer;

import java.util.*;

/**
 *
 * @author Ziheng
 */


public class Summer {
    
    public boolean isValid(Long x1, Long x2, String num, int start) {
    //当可以走到后面没有和了的时候，说明这个string满足条件
        if (start == num.length()) return true;
        x2 = x1 + x2;
        x1 = x2 - x1;
        String sum = x2.toString();
        //string.startsWith()直接可以知道这个sum是不是存在于num中
        return num.startsWith(sum, start) && isValid(x1, x2, num, start + sum.length());
    }

    public boolean isAdditiveNumber(String num) {
        int len = num.length();
        for (int i = 1; i <= len / 2; i++) {
            if (num.charAt(0) == '0' && i > 1) return false;
            Long x1 = Long.parseLong(num.substring(0, i));
            for (int j = 1; Math.max(i, j) <= len - i - j; j++) {
                if (num.charAt(i) == '0' && j > 1) break;
                Long x2 = Long.parseLong(num.substring(i, i + j));
                if (isValid(x1, x2, num, i + j)) return true;
            }
        }
        return false;
    }
    
    public String createData(int length){
        StringBuilder sb = new StringBuilder();
        Random rand = new Random();
        for (int i = 0; i < length; i++){
            sb.append(rand.nextInt(10));
        }
        String data = sb.toString();
       // System.out.println("Random data: " + data);
        return data;
    }
    
    public static void main(String []args){
        for (int i = 0 ; i < 15; i++){
            Summer test = new Summer();
            String input = test.createData(15);
            boolean output = test.isAdditiveNumber(input);
            System.out.println("No" + (i+1) + " INPUT " + input + " OUTPUT " +output);
        }
    }
    
}
