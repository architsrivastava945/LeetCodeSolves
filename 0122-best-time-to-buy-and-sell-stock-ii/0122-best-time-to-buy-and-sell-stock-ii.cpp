class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxProfit = 0;
        int localProfit = 0;
        int minPrice = prices[0];
        for(int i = 1; i < prices.size(); i++){
            if(minPrice > prices[i]) minPrice = prices[i];
            localProfit += prices[i] - minPrice;
            if(maxProfit < localProfit) maxProfit = localProfit;
            if(minPrice < prices[i]) minPrice = prices[i];
        }
        return maxProfit;
    }
};