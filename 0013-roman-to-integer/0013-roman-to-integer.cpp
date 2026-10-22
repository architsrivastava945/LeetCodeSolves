class Solution {
public:
    int romanToInt(string s) {
        std::unordered_map<char, int> roman = {
            {'I',1},
            {'V',5},
            {'X',10},
            {'L',50},
            {'C',100},
            {'D',500},
            {'M',1000}
        };
        int len = s.length();
        int *nums;
        nums = new int[len];
        int sum = 0;
        nums[0] = roman[s.at(0)];
        int i = 1;
        for(; i < len; i++){
            nums[i] = roman[s.at(i)];
            if(nums[i-1] < nums[i]){
                nums[i-1] = -nums[i-1];
            }
            sum = sum + nums[i-1];
        }
        sum = sum + nums[len-1];
        return sum;
    }
};