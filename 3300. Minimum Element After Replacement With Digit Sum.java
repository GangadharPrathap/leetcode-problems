import java.util.List;

class Solution {
    public int minElement(int[] nums) {
        int mn = Integer.MAX_VALUE;

        for (int eachValue : nums) {
            int sum = 0;
            int temp = Math.abs(eachValue);
            
            while (temp > 0) {
                sum += temp % 10;
                temp /= 10;
            }
            
            if (sum < mn) {
                mn = sum;
            }
        }
        return mn;
    }
}
