class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int i = 0, j = numbers.length -1;
        while(i < j){
            int result = numbers[i] + numbers[j];
            if(result == target){
                int[] ans = {i+1, j+1};
                return ans;
            }else if(result < target){
                i++;
            }else{
                j--;
            }
        }
        int[] ans = {0,0};
        return ans;
    }
}