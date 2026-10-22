class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int i = 1, j = k, sum = 0;
        for(int x = 0; x < k; x++) sum += nums[x];
        double avg = (double) sum / k;
        for(; j < nums.length; i++, j++){
            sum -= nums[i-1];
            sum += nums[j];
            if( (double) sum/k > avg) avg = (double) sum/k;
        }
        return avg;
    }
}