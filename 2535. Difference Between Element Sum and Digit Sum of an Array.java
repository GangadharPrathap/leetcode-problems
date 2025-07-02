class Solution {
    public int differenceOfSum(int[] nums) {
        int eleSum=0;
        int digitSum=0;
        for (int eachNumber:nums){
            eleSum+=eachNumber;
            int x=0;
            int temp=eachNumber;
            while(temp>0){
                x+=temp%10;
                temp/=10;
            }digitSum+=x;
        }return Math.abs(eleSum-digitSum);
    }
}
