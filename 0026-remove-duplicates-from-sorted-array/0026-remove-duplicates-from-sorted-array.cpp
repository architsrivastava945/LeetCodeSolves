class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int temp;
        int count = nums.size();
        int i=0,j=1;
        while(j < count){
            if(nums[i]==nums[j]){
                for(int k=j,l=j+1; l < count; l++,k++){
                    temp = nums[k];
                    nums[k] = nums[l];
                    nums[l] = temp;
                }
                count--;
            }else{
                i++;
                j++;
            }
        }
        return count;
    }
};