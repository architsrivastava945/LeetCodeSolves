class Solution {
    public int maxArea(int[] height) {
        int i = 0, j = height.length -1;
        int maxWater = 0;
        while(i < j){
            int shortWall = height[i] < height[j] ? height[i] : height[j];
            int water = shortWall * (j-i);
            if(water > maxWater) maxWater = water;
            if(height[j] > height[i]) i++;
            else j--;
        }
        return maxWater;
    }
}