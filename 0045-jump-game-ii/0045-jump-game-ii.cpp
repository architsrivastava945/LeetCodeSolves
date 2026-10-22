class Solution {
public:
    int jump(vector<int>& nums) {
        int n = nums.size();
        if(n < 2) return 0;
        int range = nums[0];
        int big = 1;
        int i = 1;
        int steps = 1;
        for(;range < n-1; i++){
            if(i+nums[i]>=big+nums[big]) big = i;
            if(i == range){
                range = big + nums[big];
                i = big;
                big++;
                steps++;
            } 
        }
        return steps;
    }
};