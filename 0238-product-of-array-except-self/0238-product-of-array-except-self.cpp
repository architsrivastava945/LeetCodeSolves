class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int numlen = nums.size();
        std::vector<int> answer(numlen,1);
        int ans = 1;
        for(int i = 0; i < numlen-1; i++){
            ans *= nums[i];
            answer[i+1] = ans;
        }
        ans = 1;
        for(int i = numlen-1; i > 0; i--){
            ans *= nums[i];
            answer[i-1] *= ans;
        }
        return answer;
    }
};