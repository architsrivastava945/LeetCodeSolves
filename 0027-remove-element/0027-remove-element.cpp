class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int j = nums.size() - 1;
        int temp;
        for(int i = 0; i <= j; i++){
            if(i == j && nums[i] == val){
                j--;
                break;
            }
            if(nums[i]==val){
                while(j>=0 && nums[j]==val){
                    j--;
                }
                if(j>i){
                temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
                }
            }
        }
        return ++j;
    }
};