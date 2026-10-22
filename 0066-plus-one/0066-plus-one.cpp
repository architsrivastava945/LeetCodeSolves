class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int LenD = digits.size();
        int i = LenD-1;
        digits[i]++;
        int carry = digits[i]/10;
        digits[i--] %= 10;
        while(carry && i >=0){
            digits[i] += carry;
            carry = digits[i]/10;
            digits[i--] %= 10;
        }
        if(carry){
            std::vector<int> result(++LenD);
            result[0] = carry;
            for(i = 1;i < LenD; i++) result[i] = digits[i-1];
            return result;
        }
        return digits;
    } 
};