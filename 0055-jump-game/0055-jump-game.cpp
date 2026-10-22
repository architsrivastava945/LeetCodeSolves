class Solution {
public:
    bool canJump(vector<int>& nums) {
        if(nums.size() < 2) return true;
        int j,i = 0;
        for(;i<nums.size()-1; i++){
            if(nums[i] == 0){
                for(j = i-1; j>=0;j--){
                    if(nums[j] > i-j) break;
                }
                if(j < 0) return false;
            }
        }
        return true;
    }
};