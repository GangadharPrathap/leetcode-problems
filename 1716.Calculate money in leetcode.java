class Solution {
    public int totalMoney(int n) {
        int fullWeeks = n / 7;
        int remainingDays = n % 7;
        int total = 0;
        for (int week = 0; week < fullWeeks; week++) {
            int weekStart = week + 1; 
            int weekSum = 0;
            for (int day = 0; day < 7; day++) {
                weekSum += weekStart + day;
            }
            total += weekSum;
        }

        
        int startDay = fullWeeks + 1; 
        for (int day = 0; day < remainingDays; day++) {
            total += startDay + day;
        }

        return total;
    }
}
