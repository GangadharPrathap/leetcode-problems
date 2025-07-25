import java.util.*;
public class Solution {

    public int reverse(int x) {
        long reversedNum = 0; 

        while (x != 0) {
            int digit = x % 10; 
            reversedNum = reversedNum * 10 + digit; 
            x /= 10;
            if (reversedNum > Integer.MAX_VALUE || reversedNum < Integer.MIN_VALUE) {
                return 0; }
        }

        return (int) reversedNum; }

}
